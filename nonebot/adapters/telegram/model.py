from typing import List, Tuple, Union, Literal, Optional

from pydantic import Field, BaseModel


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    is_premium: Optional[Literal[True]] = None
    added_to_attachment_menu: Optional[Literal[True]] = None
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None


class ChatPhoto(BaseModel):
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


class ReactionTypeEmoji(BaseModel):
    type: Literal["emoji"] = "emoji"
    emoji: str


class ReactionTypeCustomEmoji(BaseModel):
    type: Literal["custom_emoji"] = "custom_emoji"
    custom_emoji_id: str


ReactionType = Union[ReactionTypeEmoji, ReactionTypeCustomEmoji]


class ChatPermissions(BaseModel):
    can_send_messages: Optional[bool] = None
    can_send_audios: Optional[bool] = None
    can_send_documents: Optional[bool] = None
    can_send_photos: Optional[bool] = None
    can_send_videos: Optional[bool] = None
    can_send_video_notes: Optional[bool] = None
    can_send_voice_notes: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_manage_topics: Optional[bool] = None


class Location(BaseModel):
    longitude: float
    latitude: float
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None


class ChatLocation(BaseModel):
    location: Location
    address: str


class Chat(BaseModel):
    id: int
    type: Literal["private", "group", "supergroup", "channel"]
    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_forum: Optional[Literal[True]] = None
    photo: Optional[ChatPhoto] = None
    active_usernames: Optional[List[str]] = None
    available_reactions: Optional[List[ReactionType]] = None
    accent_color_id: Optional[int] = None
    background_custom_emoji_id: Optional[str] = None
    profile_accent_color_id: Optional[int] = None
    profile_background_custom_emoji_id: Optional[str] = None
    emoji_status_custom_emoji_id: Optional[str] = None
    emoji_status_expiration_date: Optional[int] = None
    bio: Optional[str] = None
    has_private_forwards: Optional[Literal[True]] = None
    has_restricted_voice_and_video_messages: Optional[Literal[True]] = None
    join_to_send_messages: Optional[Literal[True]] = None
    join_by_request: Optional[Literal[True]] = None
    description: Optional[str] = None
    invite_link: Optional[str] = None
    pinned_message: Optional["Message"] = None
    permissions: Optional[ChatPermissions] = None
    slow_mode_delay: Optional[int] = None
    message_auto_delete_time: Optional[int] = None
    has_aggressive_anti_spam_enabled: Optional[Literal[True]] = None
    has_hidden_members: Optional[Literal[True]] = None
    has_protected_content: Optional[Literal[True]] = None
    has_visible_history: Optional[Literal[True]] = None
    sticker_set_name: Optional[str] = None
    can_set_sticker_set: Optional[Literal[True]] = None
    linked_chat_id: Optional[int] = None
    location: Optional[ChatLocation] = None


class MessageOriginUser(BaseModel):
    type: Literal["user"] = "user"
    date: int
    sender_user: User


class MessageOriginHiddenUser(BaseModel):
    type: Literal["hidden_user"] = "hidden_user"
    date: int
    sender_user_name: str


class MessageOriginChat(BaseModel):
    type: Literal["chat"] = "chat"
    date: int
    sender_chat: Chat
    author_signature: Optional[str] = None


class MessageOriginChannel(BaseModel):
    type: Literal["channel"] = "channel"
    date: int
    chat: Chat
    message_id: int
    author_signature: Optional[str] = None


MessageOrigin = Union[
    MessageOriginUser, MessageOriginHiddenUser, MessageOriginChat, MessageOriginChannel
]


class LinkPreviewOptions(BaseModel):
    is_disabled: Optional[bool] = None
    url: Optional[str] = None
    prefer_small_media: Optional[bool] = None
    prefer_large_media: Optional[bool] = None
    show_above_text: Optional[bool] = None


class PhotoSize(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int] = None


class Animation(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class Audio(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    performer: Optional[str] = None
    title: Optional[str] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None
    thumbnail: Optional[PhotoSize] = None


class Document(BaseModel):
    file_id: str
    file_unique_id: str
    thumbnail: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class File(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: Optional[int] = None
    file_path: Optional[str] = None


class MaskPosition(BaseModel):
    point: Literal["forehead", "eyes", "mouth", "chin"]
    x_shift: float
    y_shift: float
    scale: float


class Sticker(BaseModel):
    file_id: str
    file_unique_id: str
    type: Literal["regular", "mask", "custom_emoji"]
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumbnail: Optional[PhotoSize] = None
    emoji: Optional[str] = None
    set_name: Optional[str] = None
    premium_animation: Optional[File] = None
    mask_position: Optional[MaskPosition] = None
    custom_emoji_id: Optional[str] = None
    needs_repainting: Optional[Literal[True]] = None
    file_size: Optional[int] = None


class Story(BaseModel):
    pass


class Video(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class VideoNote(BaseModel):
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumbnail: Optional[PhotoSize] = None
    file_size: Optional[int] = None


class Voice(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class Contact(BaseModel):
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    user_id: Optional[int] = None
    vcard: Optional[str] = None


class Dice(BaseModel):
    emoji: Literal["🎲", "🎯", "🏀", "⚽", "🎳", "🎰"]
    value: int


class MessageEntity(BaseModel):
    type: Literal[
        "mention",
        "hashtag",
        "cashtag",
        "bot_command",
        "url",
        "email",
        "phone_number",
        "bold",
        "italic",
        "underline",
        "strikethrough",
        "spoiler",
        "blockquote",
        "code",
        "pre",
        "text_link",
        "text_mention",
        "custom_emoji",
    ]
    offset: int
    length: int
    url: Optional[str] = None
    user: Optional[User] = None
    language: Optional[str] = None
    custom_emoji_id: Optional[str] = None


class Game(BaseModel):
    title: str
    description: str
    photo: List[PhotoSize]
    text: Optional[str] = None
    text_entities: Optional[List[MessageEntity]] = None
    animation: Optional[Animation] = None


class Giveaway(BaseModel):
    chats: List[Chat]
    winners_selection_date: int
    winner_count: int
    only_new_members: Optional[Literal[True]] = None
    has_public_winners: Optional[Literal[True]] = None
    prize_description: Optional[str] = None
    country_codes: Optional[List[str]] = None
    premium_subscription_month_count: Optional[int] = None


class GiveawayWinners(BaseModel):
    chat: Chat
    giveaway_message_id: int
    winners_selection_date: int
    winner_count: int
    winners: List[User]
    additional_chat_count: Optional[int] = None
    premium_subscription_month_count: Optional[int] = None
    unclaimed_prize_count: Optional[int] = None
    only_new_members: Optional[Literal[True]] = None
    was_refunded: Optional[Literal[True]] = None
    prize_description: Optional[str] = None


class Invoice(BaseModel):
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


class PollOption(BaseModel):
    text: str
    voter_count: int


class Poll(BaseModel):
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: Literal["regular", "quiz"]
    allows_multiple_answers: bool
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None
    explanation_entities: Optional[List[MessageEntity]] = None
    open_period: Optional[int] = None
    close_date: Optional[int] = None


class Venue(BaseModel):
    location: Location
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None


class ExternalReplyInfo(BaseModel):
    origin: MessageOrigin
    chat: Optional[Chat] = None
    message_id: Optional[int] = None
    link_preview_options: Optional[LinkPreviewOptions] = None
    animation: Optional[Animation] = None
    audio: Optional[Audio] = None
    document: Optional[Document] = None
    photo: Optional[List[PhotoSize]] = None
    sticker: Optional[Sticker] = None
    story: Optional[Story] = None
    video: Optional[Video] = None
    video_note: Optional[VideoNote] = None
    voice: Optional[Voice] = None
    has_media_spoiler: Optional[Literal[True]] = None
    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    giveaway: Optional[Giveaway] = None
    giveaway_winners: Optional[GiveawayWinners] = None
    invoice: Optional[Invoice] = None
    location: Optional[Location] = None
    poll: Optional[Poll] = None
    venue: Optional[Venue] = None


class TextQuote(BaseModel):
    text: str
    entities: Optional[List[MessageEntity]] = None
    position: int
    is_manual: Optional[Literal[True]] = None


class MessageAutoDeleteTimerChanged(BaseModel):
    message_auto_delete_time: int


class InaccessibleMessage(BaseModel):
    chat: Chat
    message_id: int
    date: int


MaybeInaccessibleMessage = Union["Message", InaccessibleMessage]


class ShippingAddress(BaseModel):
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


class OrderInfo(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    shipping_address: Optional[ShippingAddress] = None


class SuccessfulPayment(BaseModel):
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None
    telegram_payment_charge_id: str
    provider_payment_charge_id: str


class UsersShared(BaseModel):
    request_id: int
    user_ids: List[int]


class ChatShared(BaseModel):
    request_id: int
    chat_id: int


class WriteAccessAllowed(BaseModel):
    from_request: Optional[bool] = None
    web_app_name: Optional[str] = None
    from_attachment_menu: Optional[bool] = None


class PassportFile(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


class EncryptedPassportElement(BaseModel):
    type: Literal[
        "personal_details",
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "address",
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
        "phone_number",
        "email",
    ]
    data: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    files: Optional[List[PassportFile]] = None
    front_side: Optional[PassportFile] = None
    reverse_side: Optional[PassportFile] = None
    selfie: Optional[PassportFile] = None
    translation: Optional[List[PassportFile]] = None
    hash: str


class EncryptedCredentials(BaseModel):
    data: str
    hash: str
    secret: str


class PassportData(BaseModel):
    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials


class ProximityAlertTriggered(BaseModel):
    traveler: User
    watcher: User
    distance: int


class ForumTopicCreated(BaseModel):
    name: str
    icon_color: int
    icon_custom_emoji_id: Optional[str] = None


class ForumTopicEdited(BaseModel):
    name: Optional[str] = None
    icon_custom_emoji_id: Optional[str] = None


class ForumTopicClosed(BaseModel):
    pass


class ForumTopicReopened(BaseModel):
    pass


class GeneralForumTopicHidden(BaseModel):
    pass


class GeneralForumTopicUnhidden(BaseModel):
    pass


class GiveawayCreated(BaseModel):
    pass


class GiveawayCompleted(BaseModel):
    winner_count: int
    unclaimed_prize_count: Optional[int] = None
    giveaway_message: Optional["Message"] = None


class VideoChatScheduled(BaseModel):
    start_date: int


class VideoChatStarted(BaseModel):
    pass


class VideoChatEnded(BaseModel):
    duration: int


class VideoChatParticipantsInvited(BaseModel):
    users: List[User]


class WebAppData(BaseModel):
    data: str
    button_text: str


class WebAppInfo(BaseModel):
    url: str


class LoginUrl(BaseModel):
    url: str
    forward_text: Optional[str] = None
    bot_username: Optional[str] = None
    request_write_access: Optional[bool] = None


class SwitchInlineQueryChosenChat(BaseModel):
    query: Optional[str] = None
    allow_user_chats: Optional[bool] = None
    allow_bot_chats: Optional[bool] = None
    allow_group_chats: Optional[bool] = None
    allow_channel_chats: Optional[bool] = None


class CallbackGame(BaseModel):
    pass


class InlineKeyboardButton(BaseModel):
    text: str
    url: Optional[str] = None
    callback_data: Optional[str] = None
    web_app: Optional[WebAppInfo] = None
    login_url: Optional[LoginUrl] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None
    callback_game: Optional[CallbackGame] = None
    pay: Optional[bool] = None


class InlineKeyboardMarkup(BaseModel):
    inline_keyboard: List[List[InlineKeyboardButton]]


class Message(BaseModel):
    message_id: int
    message_thread_id: Optional[int] = None
    from_: Optional[User] = Field(default=None, alias="from")
    sender_chat: Optional[Chat] = None
    date: int
    chat: Chat
    forward_origin: Optional[MessageOrigin] = None
    is_topic_message: Optional[Literal[True]] = None
    is_automatic_forward: Optional[Literal[True]] = None
    reply_to_message: Optional["Message"] = None
    external_reply: Optional[ExternalReplyInfo] = None
    quote: Optional[TextQuote] = None
    via_bot: Optional[User] = None
    edit_date: Optional[int] = None
    has_protected_content: Optional[Literal[True]] = None
    media_group_id: Optional[str] = None
    author_signature: Optional[str] = None
    text: Optional[str] = None
    entities: Optional[List[MessageEntity]] = None
    link_preview_options: Optional[LinkPreviewOptions] = None
    animation: Optional[Animation] = None
    audio: Optional[Audio] = None
    document: Optional[Document] = None
    photo: Optional[List[PhotoSize]] = None
    sticker: Optional[Sticker] = None
    story: Optional[Story] = None
    video: Optional[Video] = None
    video_note: Optional[VideoNote] = None
    voice: Optional[Voice] = None
    caption: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    has_media_spoiler: Optional[Literal[True]] = None
    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    poll: Optional[Poll] = None
    venue: Optional[Venue] = None
    location: Optional[Location] = None
    new_chat_members: Optional[List[User]] = None
    left_chat_member: Optional[User] = None
    new_chat_title: Optional[str] = None
    new_chat_photo: Optional[List[PhotoSize]] = None
    delete_chat_photo: Optional[Literal[True]] = None
    group_chat_created: Optional[Literal[True]] = None
    supergroup_chat_created: Optional[Literal[True]] = None
    channel_chat_created: Optional[Literal[True]] = None
    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None
    migrate_to_chat_id: Optional[int] = None
    migrate_from_chat_id: Optional[int] = None
    pinned_message: Optional[MaybeInaccessibleMessage] = None
    invoice: Optional[Invoice] = None
    successful_payment: Optional[SuccessfulPayment] = None
    users_shared: Optional[UsersShared] = None
    chat_shared: Optional[ChatShared] = None
    connected_website: Optional[str] = None
    write_access_allowed: Optional[WriteAccessAllowed] = None
    passport_data: Optional[PassportData] = None
    proximity_alert_triggered: Optional[ProximityAlertTriggered] = None
    forum_topic_created: Optional[ForumTopicCreated] = None
    forum_topic_edited: Optional[ForumTopicEdited] = None
    forum_topic_closed: Optional[ForumTopicClosed] = None
    forum_topic_reopened: Optional[ForumTopicReopened] = None
    general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = None
    general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = None
    giveaway_created: Optional[GiveawayCreated] = None
    giveaway: Optional[Giveaway] = None
    giveaway_winners: Optional[GiveawayWinners] = None
    giveaway_completed: Optional[GiveawayCompleted] = None
    video_chat_scheduled: Optional[VideoChatScheduled] = None
    video_chat_started: Optional[VideoChatStarted] = None
    video_chat_ended: Optional[VideoChatEnded] = None
    video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = None
    web_app_data: Optional[WebAppData] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


class MessageReactionUpdated(BaseModel):
    chat: Chat
    message_id: int
    user: Optional[User] = None
    actor_chat: Optional[Chat] = None
    date: int
    old_reaction: List[ReactionType]
    new_reaction: List[ReactionType]


class ReactionCount(BaseModel):
    type: ReactionType
    total_count: int


class MessageReactionCountUpdated(BaseModel):
    chat: Chat
    message_id: int
    date: int
    reactions: List[ReactionCount]


class InlineQuery(BaseModel):
    id: str
    from_: User = Field(alias="from")
    query: str
    offset: str
    chat_type: Optional[
        Literal["sender", "private", "group", "supergroup", "channel"]
    ] = None
    location: Optional[Location] = None


class ChosenInlineResult(BaseModel):
    result_id: str
    from_: User = Field(alias="from")
    location: Optional[Location] = None
    inline_message_id: Optional[str] = None
    query: str


class CallbackQuery(BaseModel):
    id: str
    from_: User = Field(alias="from")
    message: Optional[MaybeInaccessibleMessage] = None
    inline_message_id: Optional[str] = None
    chat_instance: str
    data: Optional[str] = None
    game_short_name: Optional[str] = None


class ShippingQuery(BaseModel):
    id: str
    from_: User = Field(alias="from")
    invoice_payload: str
    shipping_address: ShippingAddress


class PreCheckoutQuery(BaseModel):
    id: str
    from_: User = Field(alias="from")
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None


class PollAnswer(BaseModel):
    poll_id: str
    voter_chat: Optional[Chat] = None
    user: Optional[User] = None
    option_ids: List[int]


class ChatMemberOwner(BaseModel):
    status: Literal["creator"] = "creator"
    user: User
    is_anonymous: bool
    custom_title: Optional[str] = None


class ChatMemberAdministrator(BaseModel):
    status: Literal["administrator"] = "administrator"
    user: User
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_post_stories: Optional[bool] = None
    can_edit_stories: Optional[bool] = None
    can_delete_stories: Optional[bool] = None
    can_manage_topics: Optional[bool] = None
    custom_title: Optional[str] = None


class ChatMemberMember(BaseModel):
    status: Literal["member"] = "member"
    user: User


class ChatMemberRestricted(BaseModel):
    status: Literal["restricted"] = "restricted"
    user: User
    is_member: bool
    can_send_messages: bool
    can_send_audios: bool
    can_send_documents: bool
    can_send_photos: bool
    can_send_videos: bool
    can_send_video_notes: bool
    can_send_voice_notes: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool
    until_date: int


class ChatMemberLeft(BaseModel):
    status: Literal["left"] = "left"
    user: User


class ChatMemberBanned(BaseModel):
    status: Literal["kicked"] = "kicked"
    user: User
    until_date: int


ChatMember = Union[
    ChatMemberOwner,
    ChatMemberAdministrator,
    ChatMemberMember,
    ChatMemberRestricted,
    ChatMemberLeft,
    ChatMemberBanned,
]


class ChatInviteLink(BaseModel):
    invite_link: str
    creator: User
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: Optional[str] = None
    expire_date: Optional[int] = None
    member_limit: Optional[int] = None
    pending_join_request_count: Optional[int] = None


class ChatMemberUpdated(BaseModel):
    chat: Chat
    from_: User = Field(alias="from")
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: Optional[ChatInviteLink] = None
    via_chat_folder_invite_link: Optional[bool] = None


class ChatJoinRequest(BaseModel):
    chat: Chat
    from_: User = Field(alias="from")
    user_chat_id: int
    date: int
    bio: Optional[str] = None
    invite_link: Optional[ChatInviteLink] = None


class ChatBoostSourcePremium(BaseModel):
    source: Literal["premium"] = "premium"
    user: User


class ChatBoostSourceGiftCode(BaseModel):
    source: Literal["gift_code"] = "gift_code"
    user: User


class ChatBoostSourceGiveaway(BaseModel):
    source: Literal["giveaway"] = "giveaway"
    giveaway_message_id: int
    user: Optional[User] = None
    is_unclaimed: Optional[Literal[True]] = None


ChatBoostSource = Union[
    ChatBoostSourcePremium, ChatBoostSourceGiftCode, ChatBoostSourceGiveaway
]


class ChatBoost(BaseModel):
    boost_id: str
    add_date: int
    expiration_date: int
    source: ChatBoostSource


class ChatBoostUpdated(BaseModel):
    chat: Chat
    boost: ChatBoost


class ChatBoostRemoved(BaseModel):
    chat: Chat
    boost_id: str
    remove_date: int
    source: ChatBoostSource


class Update(BaseModel):
    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
    message_reaction: Optional[MessageReactionUpdated] = None
    message_reaction_count: Optional[MessageReactionCountUpdated] = None
    inline_query: Optional[InlineQuery] = None
    chosen_inline_result: Optional[ChosenInlineResult] = None
    callback_query: Optional[CallbackQuery] = None
    shipping_query: Optional[ShippingQuery] = None
    pre_checkout_query: Optional[PreCheckoutQuery] = None
    poll: Optional[Poll] = None
    poll_answer: Optional[PollAnswer] = None
    my_chat_member: Optional[ChatMemberUpdated] = None
    chat_member: Optional[ChatMemberUpdated] = None
    chat_join_request: Optional[ChatJoinRequest] = None
    chat_boost: Optional[ChatBoostUpdated] = None
    removed_chat_boost: Optional[ChatBoostRemoved] = None


class WebhookInfo(BaseModel):
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: Optional[str] = None
    last_error_date: Optional[int] = None
    last_error_message: Optional[str] = None
    last_synchronization_error_date: Optional[int] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[str]] = None


class MessageId(BaseModel):
    message_id: int


class ReplyParameters(BaseModel):
    message_id: int
    chat_id: Optional[Union[int, str]] = None
    allow_sending_without_reply: Optional[bool] = None
    quote: Optional[str] = None
    quote_parse_mode: Optional[Literal["MarkdownV2", "HTML"]] = None
    quote_entities: Optional[List[MessageEntity]] = None
    quote_position: Optional[int] = None


class UserProfilePhotos(BaseModel):
    total_count: int
    photos: List[List[PhotoSize]]


class KeyboardButtonRequestUsers(BaseModel):
    request_id: int
    user_is_bot: Optional[bool] = None
    user_is_premium: Optional[bool] = None
    max_quantity: Optional[int] = None


class ChatAdministratorRights(BaseModel):
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_post_stories: Optional[bool] = None
    can_edit_stories: Optional[bool] = None
    can_delete_stories: Optional[bool] = None
    can_manage_topics: Optional[bool] = None


class KeyboardButtonRequestChat(BaseModel):
    request_id: int
    chat_is_channel: bool
    chat_is_forum: Optional[bool] = None
    chat_has_username: Optional[bool] = None
    chat_is_created: Optional[bool] = None
    user_administrator_rights: Optional[ChatAdministratorRights] = None
    bot_administrator_rights: Optional[ChatAdministratorRights] = None
    bot_is_member: Optional[bool] = None


class KeyboardButtonPollType(BaseModel):
    type: Optional[str] = None


class KeyboardButton(BaseModel):
    text: str
    request_users: Optional[KeyboardButtonRequestUsers] = None
    request_chat: Optional[KeyboardButtonRequestChat] = None
    request_contact: Optional[bool] = None
    request_location: Optional[bool] = None
    request_poll: Optional[KeyboardButtonPollType] = None
    web_app: Optional[WebAppInfo] = None


class ReplyKeyboardMarkup(BaseModel):
    keyboard: List[List[KeyboardButton]]
    is_persistent: Optional[bool] = None
    resize_keyboard: Optional[bool] = None
    one_time_keyboard: Optional[bool] = None
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None


class ReplyKeyboardRemove(BaseModel):
    remove_keyboard: Literal[True]
    selective: Optional[bool] = None


class ForceReply(BaseModel):
    force_reply: Literal[True]
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None


class ForumTopic(BaseModel):
    message_thread_id: int
    name: str
    icon_color: int
    icon_custom_emoji_id: Optional[str] = None


class BotCommand(BaseModel):
    command: str
    description: str


class BotCommandScopeDefault(BaseModel):
    type: Literal["default"] = "default"


class BotCommandScopeAllPrivateChats(BaseModel):
    type: Literal["all_private_chats"] = "all_private_chats"


class BotCommandScopeAllGroupChats(BaseModel):
    type: Literal["all_group_chats"] = "all_group_chats"


class BotCommandScopeAllChatAdministrators(BaseModel):
    type: Literal["all_chat_administrators"] = "all_chat_administrators"


class BotCommandScopeChat(BaseModel):
    type: Literal["chat"] = "chat"
    chat_id: Union[int, str]


class BotCommandScopeChatAdministrators(BaseModel):
    type: Literal["chat_administrators"] = "chat_administrators"
    chat_id: Union[int, str]


class BotCommandScopeChatMember(BaseModel):
    type: Literal["chat_member"] = "chat_member"
    chat_id: Union[int, str]
    user_id: int


BotCommandScope = Union[
    BotCommandScopeDefault,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
]


class BotName(BaseModel):
    name: str


class BotDescription(BaseModel):
    description: str


class BotShortDescription(BaseModel):
    short_description: str


class MenuButtonCommands(BaseModel):
    type: Literal["commands"] = "commands"


class MenuButtonWebApp(BaseModel):
    type: Literal["web_app"] = "web_app"
    text: str
    web_app: WebAppInfo


class MenuButtonDefault(BaseModel):
    type: Literal["default"] = "default"


MenuButton = Union[MenuButtonCommands, MenuButtonWebApp, MenuButtonDefault]


class UserChatBoosts(BaseModel):
    boosts: List[ChatBoost]


class ResponseParameters(BaseModel):
    migrate_to_chat_id: Optional[int] = None
    retry_after: Optional[int] = None


InputFile = Union[bytes, Tuple[str, bytes]]


class InputMediaAnimation(BaseModel):
    type: Literal["animation"] = "animation"
    media: str
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    has_spoiler: Optional[bool] = None


class InputMediaDocument(BaseModel):
    type: Literal["document"] = "document"
    media: str
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    disable_content_type_detection: Optional[bool] = None


class InputMediaAudio(BaseModel):
    type: Literal["audio"] = "audio"
    media: str
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    duration: Optional[int] = None
    performer: Optional[str] = None
    title: Optional[str] = None


class InputMediaPhoto(BaseModel):
    type: Literal["photo"] = "photo"
    media: str
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    has_spoiler: Optional[bool] = None


class InputMediaVideo(BaseModel):
    type: Literal["video"] = "video"
    media: str
    thumbnail: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    supports_streaming: Optional[bool] = None
    has_spoiler: Optional[bool] = None


InputMedia = Union[
    InputMediaAnimation,
    InputMediaDocument,
    InputMediaAudio,
    InputMediaPhoto,
    InputMediaVideo,
]


class StickerSet(BaseModel):
    name: str
    title: str
    sticker_type: str
    is_animated: bool
    is_video: bool
    stickers: List[Sticker]
    thumbnail: Optional[PhotoSize] = None


class InputSticker(BaseModel):
    sticker: Union[InputFile, str]
    emoji_list: List[str]
    mask_position: Optional[MaskPosition] = None
    keywords: Optional[List[str]] = None


class InlineQueryResultsButton(BaseModel):
    text: str
    web_app: Optional[WebAppInfo] = None
    start_parameter: Optional[str] = None


class InputTextMessageContent(BaseModel):
    message_text: str
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    entities: Optional[List[MessageEntity]] = None
    link_preview_options: Optional[LinkPreviewOptions] = None


class InputLocationMessageContent(BaseModel):
    latitude: float
    longitude: float
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None


class InputVenueMessageContent(BaseModel):
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None


class InputContactMessageContent(BaseModel):
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None


class LabeledPrice(BaseModel):
    label: str
    amount: int


class InputInvoiceMessageContent(BaseModel):
    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: List[LabeledPrice]
    max_tip_amount: Optional[int] = None
    suggested_tip_amounts: Optional[List[int]] = None
    provider_data: Optional[str] = None
    photo_url: Optional[str] = None
    photo_size: Optional[int] = None
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    need_name: Optional[bool] = None
    need_phone_number: Optional[bool] = None
    need_email: Optional[bool] = None
    need_shipping_address: Optional[bool] = None
    send_phone_number_to_provider: Optional[bool] = None
    send_email_to_provider: Optional[bool] = None
    is_flexible: Optional[bool] = None


InputMessageContent = Union[
    InputTextMessageContent,
    InputLocationMessageContent,
    InputVenueMessageContent,
    InputContactMessageContent,
    InputInvoiceMessageContent,
]


class InlineQueryResultCachedAudio(BaseModel):
    type: Literal["audio"] = "audio"
    id: str
    audio_file_id: str
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultCachedDocument(BaseModel):
    type: Literal["document"] = "document"
    id: str
    title: str
    document_file_id: str
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultCachedGif(BaseModel):
    type: Literal["gif"] = "gif"
    id: str
    gif_file_id: str
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultCachedMpeg4Gif(BaseModel):
    type: Literal["mpeg4_gif"] = "mpeg4_gif"
    id: str
    mpeg4_file_id: str
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultCachedPhoto(BaseModel):
    type: Literal["photo"] = "photo"
    id: str
    photo_file_id: str
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultCachedSticker(BaseModel):
    type: Literal["sticker"] = "sticker"
    id: str
    sticker_file_id: str
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultCachedVideo(BaseModel):
    type: Literal["video"] = "video"
    id: str
    video_file_id: str
    title: str
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultCachedVoice(BaseModel):
    type: Literal["voice"] = "voice"
    id: str
    voice_file_id: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultArticle(BaseModel):
    type: Literal["article"] = "article"
    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: Optional[InlineKeyboardMarkup] = None
    url: Optional[str] = None
    hide_url: Optional[bool] = None
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


class InlineQueryResultAudio(BaseModel):
    type: Literal["audio"] = "audio"
    id: str
    audio_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    performer: Optional[str] = None
    audio_duration: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultContact(BaseModel):
    type: Literal["contact"] = "contact"
    id: str
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


class InlineQueryResultGame(BaseModel):
    type: Literal["game"] = "game"
    id: str
    game_short_name: str
    reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultDocument(BaseModel):
    type: Literal["document"] = "document"
    id: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    document_url: str
    mime_type: str
    description: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


class InlineQueryResultGif(BaseModel):
    type: Literal["gif"] = "gif"
    id: str
    gif_url: str
    gif_width: Optional[int] = None
    gif_height: Optional[int] = None
    gif_duration: Optional[int] = None
    thumbnail_url: str
    thumbnail_mime_type: Optional[str] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultLocation(BaseModel):
    type: Literal["location"] = "location"
    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


class InlineQueryResultMpeg4Gif(BaseModel):
    type: Literal["mpeg4_gif"] = "mpeg4_gif"
    id: str
    mpeg4_url: str
    mpeg4_width: Optional[int] = None
    mpeg4_height: Optional[int] = None
    mpeg4_duration: Optional[int] = None
    thumbnail_url: str
    thumbnail_mime_type: Optional[str] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultPhoto(BaseModel):
    type: Literal["photo"] = "photo"
    id: str
    photo_url: str
    thumbnail_url: str
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultVenue(BaseModel):
    type: Literal["venue"] = "venue"
    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


class InlineQueryResultVideo(BaseModel):
    type: Literal["video"] = "video"
    id: str
    video_url: str
    mime_type: str
    thumbnail_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    video_width: Optional[int] = None
    video_height: Optional[int] = None
    video_duration: Optional[int] = None
    description: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultVoice(BaseModel):
    type: Literal["voice"] = "voice"
    id: str
    voice_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[Literal["MarkdownV2", "Markdown" "HTML"]] = None
    caption_entities: Optional[List[MessageEntity]] = None
    voice_duration: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


InlineQueryResult = Union[
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultContact,
    InlineQueryResultGame,
    InlineQueryResultDocument,
    InlineQueryResultGif,
    InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoice,
]


class SentWebAppMessage(BaseModel):
    inline_message_id: Optional[str] = None


class ShippingOption(BaseModel):
    id: str
    title: str
    prices: List[LabeledPrice]


class PassportElementErrorDataField(BaseModel):
    source: Literal["data"] = "data"
    type: str
    field_name: str
    data_hash: str
    message: str


class PassportElementErrorFrontSide(BaseModel):
    source: Literal["front_side"] = "front_side"
    type: str
    file_hash: str
    message: str


class PassportElementErrorReverseSide(BaseModel):
    source: Literal["reverse_side"] = "reverse_side"
    type: str
    file_hash: str
    message: str


class PassportElementErrorSelfie(BaseModel):
    source: Literal["selfie"] = "selfie"
    type: str
    file_hash: str
    message: str


class PassportElementErrorFile(BaseModel):
    source: Literal["file"] = "file"
    type: str
    file_hash: str
    message: str


class PassportElementErrorFiles(BaseModel):
    source: Literal["files"] = "files"
    type: str
    file_hashes: List[str]
    message: str


class PassportElementErrorTranslationFile(BaseModel):
    source: Literal["translation_file"] = "translation_file"
    type: str
    file_hash: str
    message: str


class PassportElementErrorTranslationFiles(BaseModel):
    source: Literal["translation_files"] = "translation_files"
    type: str
    file_hashes: List[str]
    message: str


class PassportElementErrorUnspecified(BaseModel):
    source: Literal["unspecified"] = "unspecified"
    type: str
    element_hash: str
    message: str


PassportElementError = Union[
    PassportElementErrorDataField,
    PassportElementErrorFrontSide,
    PassportElementErrorReverseSide,
    PassportElementErrorSelfie,
    PassportElementErrorFile,
    PassportElementErrorFiles,
    PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified,
]


class GameHighScore(BaseModel):
    position: int
    user: User
    score: int
