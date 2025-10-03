# SNMP MIB module (CM-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:03 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(TrapAlarmSeverity,
 fsp150cm) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "TrapAlarmSeverity",
    "fsp150cm")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortIndex,
 cmEthernetNetPortIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cmAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6)
)
if mibBuilder.loadTexts:
    cmAlarmMIB.setRevisions(
        ("2020-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmServiceEffect(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("nonServiceAffecting", 1),
          ("serviceAffecting", 2))
    )



class CmLocation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("both", 1),
          ("farEnd", 2),
          ("nearEnd", 3),
          ("notApplicable", 4))
    )



class CmDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("bidirectional", 1),
          ("bothDirections", 2),
          ("notApplicable", 3),
          ("receiveDirectionOnly", 4),
          ("transmitDirectionOnly", 5),
          ("uniDirectional", 6))
    )



class CmConditionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420,
              421,
              422)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("acoopr", 1),
          ("hwinitedsysboot", 2),
          ("userinitednemireboot", 3),
          ("userinitedsysboot", 4),
          ("userinitedsysbootdefaultdb", 5),
          ("userinitedsysbootdbrestore", 6),
          ("userinitedsysrebootswact", 7),
          ("sysrecoveryfailed", 8),
          ("primntpsvrFailed", 9),
          ("bckupntpsvrFailed", 10),
          ("swdl-ftip", 11),
          ("swdl-ftfail", 12),
          ("swdl-ftpass", 13),
          ("swdl-instip", 14),
          ("swdl-instfail", 15),
          ("swdl-instpass", 16),
          ("swdl-actip", 17),
          ("swdl-actfail", 18),
          ("swdl-actpass", 19),
          ("swdl-valip", 20),
          ("swdl-valfail", 21),
          ("swdl-valpass", 22),
          ("db-ftip", 23),
          ("db-ftfail", 24),
          ("db-ftpass", 25),
          ("ctneqpt", 26),
          ("eqptflt", 27),
          ("forced", 28),
          ("lockout", 29),
          ("manualswitch", 30),
          ("wkswtopr", 31),
          ("wkswbk", 32),
          ("mismatch", 33),
          ("psu1fail", 34),
          ("psu2fail", 35),
          ("eqptremoved", 36),
          ("autonegunknown", 37),
          ("dyinggasp", 38),
          ("efmfail", 39),
          ("efmrce", 40),
          ("efmrld", 41),
          ("efmrls", 42),
          ("lnkdeactivated", 43),
          ("lnkdownunisolated", 44),
          ("lnkdowncablefault", 45),
          ("lnkdowncableremoved", 46),
          ("lnkdownautonegfailed", 47),
          ("lnkdownlpbkfault", 48),
          ("lnkdowncabletestfault", 49),
          ("lnkdown", 50),
          ("rfi", 51),
          ("rxjabber", 52),
          ("sfpmismatch", 53),
          ("sfpremoved", 54),
          ("sfptxfault", 55),
          ("sfpinserted", 56),
          ("fan-a", 57),
          ("fan-b", 58),
          ("overtemp", 59),
          ("undertemp", 60),
          ("overvoltage", 61),
          ("undervoltage", 62),
          ("shelfrmvd", 63),
          ("rmtefmlpbkfail", 64),
          ("inpwrflt", 65),
          ("crossconnectccm", 66),
          ("erroneousccm", 67),
          ("someremotemepccm", 68),
          ("somemacstatus", 69),
          ("somerdi", 70),
          ("ais", 71),
          ("syncref", 72),
          ("esmcfail", 73),
          ("qlmismatch", 74),
          ("freqoff", 75),
          ("los", 76),
          ("lof", 77),
          ("qlsqlch", 78),
          ("frngsync", 79),
          ("fstsync", 80),
          ("hldovrsync", 81),
          ("losloc", 82),
          ("wtr", 83),
          ("allsyncref", 84),
          ("qlinvalid", 85),
          ("snmpdghostunresolved", 86),
          ("snmpdghostresourcesbusy", 87),
          ("bwexceedednegspeed", 88),
          ("shaperbtd", 89),
          ("sfpnonqualified", 90),
          ("avghldovrfrqnotrdy", 91),
          ("lnkdownmasterslavecfg", 92),
          ("pwrnoinputunitfault", 93),
          ("ipaddrconflict", 94),
          ("nomoreresources", 95),
          ("syncreflck", 96),
          ("syncreffrc", 97),
          ("syncrefman", 98),
          ("syncrefwtr", 99),
          ("syncrefsw", 100),
          ("lcpfail", 101),
          ("lcploopback", 102),
          ("authservernotreachable", 103),
          ("excessiveinterrupts", 104),
          ("dbdowngradeip", 105),
          ("testalarm", 106),
          ("gen-filexfer-ip", 107),
          ("gen-filexfer-fail", 108),
          ("gen-filexfer-pass", 109),
          ("gen-oper-ip", 110),
          ("gen-oper-fail", 111),
          ("gen-oper-pass", 112),
          ("trafficfail", 113),
          ("clockfail", 114),
          ("rdncyswitchover", 115),
          ("rdncyswvermismatch", 116),
          ("rdncyoutofsync", 117),
          ("rdncylockout", 118),
          ("rdncymaintenance", 119),
          ("xfptxfault", 120),
          ("xfpmismatch", 121),
          ("xfpnonqualified", 122),
          ("xfpremoved", 123),
          ("xfpinserted", 124),
          ("lagmbrfail", 125),
          ("swdl-proip", 126),
          ("swdl-propass", 127),
          ("swdl-profail", 128),
          ("db-proip", 129),
          ("db-propass", 130),
          ("db-profail", 131),
          ("swdl-rvtip", 132),
          ("swdl-rvtpass", 133),
          ("swdl-rvtfail", 134),
          ("db-corruption", 135),
          ("bpmismatch", 136),
          ("popr-oovar", 137),
          ("popr-oorange", 138),
          ("popr-genfail", 139),
          ("popr-sfpnqual", 140),
          ("popr-rta", 141),
          ("modemmea", 142),
          ("modemnonqualified", 143),
          ("modemremoved", 144),
          ("nosimcard", 145),
          ("env-genfail", 146),
          ("env-misc", 147),
          ("env-batterydischarge", 148),
          ("env-batteryfail", 149),
          ("env-coolingfanfail", 150),
          ("env-enginefail", 151),
          ("env-fusefail", 152),
          ("env-hightemp", 153),
          ("env-intrusion", 154),
          ("env-lowbatteryvoltage", 155),
          ("env-lowtemp", 156),
          ("env-opendoor", 157),
          ("env-powerfail", 158),
          ("intctneqpt", 159),
          ("syncnotready", 160),
          ("vcgfail", 161),
          ("loa", 162),
          ("plct", 163),
          ("tlct", 164),
          ("plcr", 165),
          ("tlcr", 166),
          ("sqnc", 167),
          ("ais-l", 168),
          ("rfi-l", 169),
          ("rei-l", 170),
          ("exc-l", 171),
          ("deg-l", 172),
          ("tim-s", 173),
          ("ais-p", 174),
          ("lop-p", 175),
          ("tim-p", 176),
          ("uneq-p", 177),
          ("plm-p", 178),
          ("lom-p", 179),
          ("exc-p", 180),
          ("deg-p", 181),
          ("rei-p", 182),
          ("rfi-p", 183),
          ("lcascrc", 184),
          ("sqm", 185),
          ("lom", 186),
          ("gidmismatch", 187),
          ("mnd", 188),
          ("ais-v", 189),
          ("lop-v", 190),
          ("tim-v", 191),
          ("uneq-v", 192),
          ("plm-v", 193),
          ("exc-v", 194),
          ("deg-v", 195),
          ("rei-v", 196),
          ("rfi-v", 197),
          ("rmtinitlpbk", 198),
          ("rai", 199),
          ("rei", 200),
          ("idle", 201),
          ("csf", 202),
          ("gfplfd", 203),
          ("gfpuplmismatch", 204),
          ("gfpexhmismatch", 205),
          ("vcat-lom", 206),
          ("fragileecc", 207),
          ("elmi-seqnummismatch", 208),
          ("elmi-notoper", 209),
          ("pw-rlofs", 210),
          ("pw-lof", 211),
          ("pw-latefrm", 212),
          ("pw-jbovrn", 213),
          ("allsoocsfailed", 214),
          ("tsholdoverfrqnotready", 215),
          ("tsfreerun", 216),
          ("tsholdover", 217),
          ("ptsflossofsync", 218),
          ("ptsflossofannounce", 219),
          ("ptsfunusable", 220),
          ("unresolvedsatop", 221),
          ("rdi-v", 222),
          ("autonegBypass", 223),
          ("forcedOffline", 224),
          ("hwcfginconsistent", 225),
          ("sjmtiemaskcross", 226),
          ("sjoffsetfail", 227),
          ("sjnotimelock", 228),
          ("sjnofreqlock", 229),
          ("sjmtiemargincross", 230),
          ("sjtestreferencefail", 231),
          ("sjtestsourcefail", 232),
          ("sjtestnotimestamp", 233),
          ("sjtestnomessages", 234),
          ("gpsantennafail", 235),
          ("ampNoPeer", 236),
          ("ampProvFail", 237),
          ("ampCfgFail", 238),
          ("ltpFailure", 239),
          ("ltpInprogress", 240),
          ("pse-power-threshold-exceeded", 241),
          ("pse-power-fail", 242),
          ("pse-poweroff-overcurrent", 243),
          ("pse-poweroff-overvoltage", 244),
          ("pse-poweroff-overload", 245),
          ("pse-poweroff-overtemp", 246),
          ("pse-poweroff-short", 247),
          ("erpFoPPM", 248),
          ("erpFoPTO", 249),
          ("erpBlockPort0RPL", 250),
          ("erpBlockPort0SF", 251),
          ("erpBlockPort0MS", 252),
          ("erpBlockPort0FS", 253),
          ("erpBlockPort0WTR", 254),
          ("erpBlockPort1RPL", 255),
          ("erpBlockPort1SF", 256),
          ("erpBlockPort1MS", 257),
          ("erpBlockPort1FS", 258),
          ("erpBlockPort1WTR", 259),
          ("ipv6addr-conflict", 260),
          ("macAddrlearntblFull", 261),
          ("timeClockNotLocked", 262),
          ("timeNotTraceAble", 263),
          ("timeFreqNotTraceAble", 264),
          ("timeHoldOver", 265),
          ("timeFreqLock", 266),
          ("timeRefLock", 267),
          ("timeRefUnavailable", 268),
          ("timeRefDegraded", 269),
          ("timeRefFrc", 270),
          ("tsTimeFrun", 271),
          ("tsTimeHoldOver", 272),
          ("timeRefUnavailableWTR", 273),
          ("timeRefDegradedWTR", 274),
          ("rmtInitSat", 275),
          ("lldpRemoteTblChg", 276),
          ("soocLck", 277),
          ("ampProvSuccess", 278),
          ("ampCfgSuccess", 279),
          ("soocSW", 280),
          ("soocWTR", 281),
          ("sjtealert", 282),
          ("dataExportFtpFail", 283),
          ("xfpWaveLengthMismatch", 284),
          ("cpmrUpgrading", 285),
          ("beaconLightFailure", 286),
          ("manualSwitchClear", 287),
          ("loopbackActive", 288),
          ("loopbackRequest", 289),
          ("trafficResourceLimitExceeded", 290),
          ("oduAis", 291),
          ("opuAis", 292),
          ("otuAis", 293),
          ("otnProtMsmtch", 294),
          ("otnProtPrtclFail", 295),
          ("oduBdi", 296),
          ("otuBdi", 297),
          ("lossCharSync", 298),
          ("berHigh", 299),
          ("laserFail", 300),
          ("laserCurrentAbnormal", 301),
          ("oduLock", 302),
          ("autoShutdown", 303),
          ("localFault", 304),
          ("otuLof", 305),
          ("otuLom", 306),
          ("oduOci", 307),
          ("opuPlm", 308),
          ("oduSd", 309),
          ("otuSd", 310),
          ("opuSf", 311),
          ("optPowerHighRx", 312),
          ("optPowerLowRx", 313),
          ("optPowerHighTx", 314),
          ("optPowerLowTx", 315),
          ("oduTim", 316),
          ("otuTim", 317),
          ("sjConstTeThrshld", 318),
          ("sjInstTeThrshld", 319),
          ("timeRefSW", 320),
          ("aadcfailed", 321),
          ("ptpfreqfrun", 322),
          ("ptptimefrun", 323),
          ("ptpfreqhldovr", 324),
          ("ptptimehldovr", 325),
          ("ptptimenottraceable", 326),
          ("ptpfreqnottraceable", 327),
          ("synctimeout", 328),
          ("announcetimeout", 329),
          ("delayresptimeout", 330),
          ("multiplepeers", 331),
          ("wrongdomain", 332),
          ("nosatellitercv", 333),
          ("trafficipifoutage", 334),
          ("ptpportstatechanged", 335),
          ("physicalSelfLpbk", 336),
          ("cfCardRWFail", 337),
          ("maxexpectedslaves", 338),
          ("external-alarm", 339),
          ("maskcrossed", 340),
          ("oof", 341),
          ("signalfail", 342),
          ("timenottai", 343),
          ("perffuncfailure", 344),
          ("ptpportnotoper", 345),
          ("leapsecondexpected", 346),
          ("keyExchangeFail", 347),
          ("keyExchangeAuthPasswordMissing", 348),
          ("secureRamCleared", 349),
          ("noRouteResources", 350),
          ("tamperSwitchOpen", 351),
          ("bfdSessionDown", 352),
          ("destinationUnresolved", 353),
          ("sjmaxtethrshld", 354),
          ("trafficArpTableFull", 355),
          ("erpRingSegmentation", 356),
          ("gpsrcvrfail", 357),
          ("noActiveRoute", 358),
          ("vxlanDMac2DIPTableFull", 359),
          ("bwExceedLagMemberPortSpeed", 360),
          ("greRemoteUnreachable", 361),
          ("bweexceedsportspeed", 362),
          ("servicediscarded", 363),
          ("bmcaError", 364),
          ("freeze", 365),
          ("gpsFwUpgrade", 366),
          ("storageWearout", 367),
          ("pps-not-generated", 368),
          ("min-sat-1-thrshld-crossed", 369),
          ("min-sat-2-thrshld-crossed", 370),
          ("gatewayNotReachable", 371),
          ("pdop-mask-cross", 372),
          ("nc-initInProgress", 373),
          ("primaryNtpSvr-auth-failed", 374),
          ("backupNtpSvr-auth-failed", 375),
          ("clock-class-mismatch", 376),
          ("hpg-switch-force", 377),
          ("hpg-switch-lockout", 378),
          ("hpg-switch-to-3gpp-path", 379),
          ("hpg-switch-to-fixed-path", 380),
          ("bgp-linkdown", 381),
          ("ospf-neighbour-lost", 382),
          ("traffic-ndptable-full", 383),
          ("dup-link-local-address", 384),
          ("dup-unicast-address", 385),
          ("ztp-failed", 386),
          ("ztp-in-progress", 387),
          ("nc-runningConfigLocked", 388),
          ("pwrnoinput2", 389),
          ("keyExchangeStopped", 390),
          ("security-error", 391),
          ("pppoe-connection-failed", 392),
          ("no-ipv6route-resource", 393),
          ("sfp-firmware-revision-mismatch", 394),
          ("vrrp-new-master", 395),
          ("nontpkeys", 396),
          ("timesrcunavailable", 397),
          ("syncsrcunavailable", 398),
          ("local-cooling-fail", 399),
          ("jamming", 400),
          ("spoofing", 401),
          ("httpsSslCertExpiryPending", 402),
          ("httpsSslCertExpired", 403),
          ("srgb-collision", 404),
          ("sid-collision", 405),
          ("sr-index-out-of-range", 406),
          ("novalidsymkeybroadcast", 407),
          ("patch-panel-mismatch", 408),
          ("fan-fail", 409),
          ("invalidsymkeypeering", 410),
          ("auto-asymmetry-delay-fail", 411),
          ("no-certificate", 412),
          ("certificate-expired-soon", 413),
          ("bpvc", 414),
          ("crcf", 415),
          ("oofc", 416),
          ("psuinputfail1", 417),
          ("psuinputfail2", 418),
          ("time-clock-degraded-system-time", 419),
          ("spoofing-pps", 420),
          ("spoofing-loc", 421),
          ("invalid-syscfg", 422))
    )



class CmConditionDescr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class CmAlarmEntityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("hubshelf", 2),
          ("cpmrshelf", 3),
          ("eth-10-100-1000-ntucard", 4),
          ("eth-cpmr-card", 5),
          ("nemi-card", 6),
          ("scu-card", 7),
          ("fan", 8),
          ("powersupply", 9),
          ("accessport", 10),
          ("networkport", 11),
          ("oneru-ge101-shelf", 12),
          ("oneru-ge206-shelf", 13),
          ("eth-ge-101-card", 14),
          ("eth-ge-206-card", 15),
          ("cfmmep", 16),
          ("sync", 17),
          ("bitsinport", 18),
          ("bitsoutport", 19),
          ("cfmqosshaper", 20),
          ("dcnport", 21),
          ("oneru-ge201-shelf", 22),
          ("eth-ge-201-card", 23),
          ("oneru-ge201se-shelf", 24),
          ("eth-ge-201se-card", 25),
          ("oneru-ge206f-shelf", 26),
          ("eth-ge-206f-card", 27),
          ("lag", 28),
          ("eth-1-10gcard", 29),
          ("redundancygroup", 30),
          ("protectiongroup", 31),
          ("stucard", 32),
          ("ethertrafficport", 33),
          ("eth-10-gecard", 34),
          ("swf-140gcard", 35),
          ("aggregationshelf", 36),
          ("sticard", 37),
          ("amicard", 38),
          ("usb3gmodem", 39),
          ("oneru-ge112-shelf", 40),
          ("eth-ge-112-card", 41),
          ("oneru-ge114-shelf", 42),
          ("eth-ge-114-card", 43),
          ("oneru-ge206v-shelf", 44),
          ("eth-ge-206v-card", 45),
          ("ge-4e-cc", 46),
          ("ge-4s-cc", 47),
          ("oneru-xg210-shelf", 48),
          ("eth-xg-210-card", 49),
          ("xg-1x-cc", 50),
          ("xg-1s-cc", 51),
          ("scu-t-card", 52),
          ("eth-10-100-1000-ntecard", 53),
          ("slot", 54),
          ("ocnstmport", 55),
          ("e1t1port", 56),
          ("stsvcpath", 57),
          ("vtvcpath", 58),
          ("vcg", 59),
          ("e3t3port", 60),
          ("vc4", 61),
          ("vc3", 62),
          ("vc12", 63),
          ("sts3c", 64),
          ("sts1", 65),
          ("vt15", 66),
          ("t3", 67),
          ("e3", 68),
          ("t1", 69),
          ("e1", 70),
          ("stm1-4-et", 71),
          ("eotdmtrafficport", 72),
          ("pwe3-ocnstm-card", 73),
          ("pwe3-e1t1-card", 74),
          ("satop", 75),
          ("telecom-slave", 76),
          ("sooc", 77),
          ("eth-1-10ghcard", 78),
          ("eth-10-gehcard", 79),
          ("port-10mhz", 80),
          ("ppsport", 81),
          ("timeofdayport", 82),
          ("oneru-t1804-shelf", 83),
          ("eth-t1804-card", 84),
          ("oneru-t3204-shelf", 85),
          ("eth-t3204-card", 86),
          ("eotdmnetworkport", 87),
          ("oneru-syncprobe-shelf", 88),
          ("eth-ge-syncprobe-card", 89),
          ("sj-clockprobe", 90),
          ("sj-ptpclockprobe", 91),
          ("sj-ptpnetworkprobe", 92),
          ("gps-receiverport", 93),
          ("ampConfig", 94),
          ("ge-8s-cc", 95),
          ("oneru-ge114h-shelf", 96),
          ("eth-ge-114h-card", 97),
          ("oneru-ge114ph-shelf", 98),
          ("eth-ge-114ph-card", 99),
          ("psegroup", 100),
          ("pseport", 101),
          ("erpGroup", 102),
          ("eth-fe-36e-card", 103),
          ("mpflow", 104),
          ("oneru-ge114sh-shelf", 105),
          ("eth-ge-114sh-card", 106),
          ("oneru-ge114s-shelf", 107),
          ("eth-ge-114s-card", 108),
          ("timeclock", 109),
          ("satResponderSession", 110),
          ("stu-h-card", 111),
          ("sti-h-card", 112),
          ("ge-8e-cc", 113),
          ("oneru-otn210-shelf", 114),
          ("eth-otn-210-card", 115),
          ("ptpclock", 116),
          ("ptpport", 117),
          ("oneru-osa5411-shelf", 118),
          ("eth-osa5411-card", 119),
          ("oneru-ge112pro-shelf", 120),
          ("eth-ge-112pro-card", 121),
          ("oneru-ge112pro-m-shelf", 122),
          ("eth-ge-112pro-m-card", 123),
          ("oneru-ge114pro-shelf", 124),
          ("eth-ge-114pro-card", 125),
          ("oneru-ge114pro-c-shelf", 126),
          ("eth-ge-114pro-c-card", 127),
          ("oneru-ge114pro-sh-shelf", 128),
          ("eth-ge-114pro-sh-card", 129),
          ("oneru-ge114pro-csh-shelf", 130),
          ("eth-ge-114pro-csh-card", 131),
          ("connectGuardFlow", 132),
          ("trafficIpIF", 133),
          ("vrf", 134),
          ("oneru-ge114pro-he-shelf", 135),
          ("eth-ge-114pro-he-card", 136),
          ("oneru-ge112pro-h-shelf", 137),
          ("eth-ge-112pro-h-card", 138),
          ("dhcpRelayAgent", 139),
          ("oneru-xg210c-shelf", 140),
          ("eth-xg-210c-card", 141),
          ("ge-8sc-cc", 142),
          ("oneru-osa5420-shelf", 143),
          ("eth-osa5420-card", 144),
          ("oneru-osa5421-shelf", 145),
          ("eth-osa5421-card", 146),
          ("mci", 147),
          ("bits-x16", 148),
          ("bfdSession", 149),
          ("eomplsPw", 150),
          ("oneru-ge114g-shelf", 151),
          ("eth-ge-114g-card", 152),
          ("wifidongleport", 153),
          ("oneru-ge114proVm-h-shelf", 154),
          ("eth-ge-114proVm-h-card", 155),
          ("oneru-ge114proVm-ch-shelf", 156),
          ("eth-ge-114proVm-ch-card", 157),
          ("oneru-ge114proVm-csh-shelf", 158),
          ("eth-ge-114proVm-csh-card", 159),
          ("server-card", 160),
          ("oneru-xg116pro-shelf", 161),
          ("eth-xg-116pro-card", 162),
          ("oneru-xg120pro-shelf", 163),
          ("eth-xg-120pro-card", 164),
          ("pps-x16", 165),
          ("clk-x16", 166),
          ("todandpps-x16", 167),
          ("vxlanSegment", 168),
          ("vtep", 169),
          ("ge101pro-shelf", 170),
          ("eth-ge-101pro-card", 171),
          ("greTunnel", 172),
          ("go102pro-s-shelf", 173),
          ("go102pro-sp-shelf", 174),
          ("onru-cx101pro-30a-shelf", 175),
          ("onru-cx102pro-30a-shelf", 176),
          ("eth-go102pro-s-card", 177),
          ("eth-go102pro-sp-card", 178),
          ("eth-cx101pro-30a-card", 179),
          ("eth-cx102pro-30a-card", 180),
          ("osa-ge-4s", 181),
          ("elpgroup", 182),
          ("oneru-ge112proVm-shelf", 183),
          ("eth-ge-112proVm-card", 184),
          ("hybrid-path-group", 191),
          ("ge102pro-h-shelf", 192),
          ("eth-ge-102pro-h-card", 193),
          ("ge102pro-efmh-shelf", 194),
          ("eth-ge-102pro-efmh-card", 195),
          ("traffic-bgprouter-peer", 196),
          ("traffic-ipv6-interface", 197),
          ("oneru-xg116pro-h-shelf", 198),
          ("eth-xg-116pro-h-card", 199),
          ("go102pro-sm-shelf", 200),
          ("eth-go102pro-sm-card", 201),
          ("vrrp-router", 202),
          ("ru1-osa5430-shelf", 203),
          ("eth-csm-osa-card", 204),
          ("ru3-osa5440-shelf", 205),
          ("eth-osa5440-card", 206),
          ("aux-osa", 207),
          ("bits-x16-enhanced", 208),
          ("osa-ge-4s-protected", 209),
          ("syncprotectiongroup", 210),
          ("timeclockprotectiongroup", 211),
          ("mciprotectiongroup", 212),
          ("oneru-xg118pro-sh-shelf", 213),
          ("eth-xg-118pro-sh-card", 214),
          ("ntp-clock", 215),
          ("oneru-xg118proac-sh-shelf", 216),
          ("eth-xg-118proac-sh-card", 217),
          ("oneru-ge114proVm-sh-shelf", 218),
          ("eth-ge-114proVm-sh-card", 219),
          ("oneru-ge104-shelf", 220),
          ("eth-ge-104-card", 221),
          ("segment-routing", 222),
          ("oneru-xg120pro-sh-shelf", 223),
          ("eth-xg-120pro-sh-card", 224),
          ("irig-card", 225),
          ("irig-port-group", 226),
          ("nci", 227),
          ("ru1-osa5422-shelf", 228),
          ("ru1-softsync-shelf", 229),
          ("eth-osa5422-card", 230),
          ("eth-softsync-card", 231),
          ("mb-gnss-card", 232),
          ("composite-clock-card", 233),
          ("l3ptpport", 234))
    )



class CmCondEffectType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sc", 1),
          ("tc", 2),
          ("cl", 3))
    )



class TestAlarmAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("raise", 1),
          ("clear", 2))
    )



class EnvAlarmInputMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("alarmopen", 2),
          ("alarmclosed", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AlarmObjects_ObjectIdentity = ObjectIdentity
alarmObjects = _AlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1)
)
_CmAlarmScalars_ObjectIdentity = ObjectIdentity
cmAlarmScalars = _CmAlarmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 1)
)
_CmAlmLastChange_Type = TimeStamp
_CmAlmLastChange_Object = MibScalar
cmAlmLastChange = _CmAlmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 1, 1),
    _CmAlmLastChange_Type()
)
cmAlmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlmLastChange.setStatus("current")


class _CmAlmIndex_Type(Integer32):
    """Custom type cmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmAlmIndex_Type.__name__ = "Integer32"
_CmAlmIndex_Object = MibScalar
cmAlmIndex = _CmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 1, 2),
    _CmAlmIndex_Type()
)
cmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlmIndex.setStatus("current")
_CmAlmTestAlarmEntity_Type = VariablePointer
_CmAlmTestAlarmEntity_Object = MibScalar
cmAlmTestAlarmEntity = _CmAlmTestAlarmEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 1, 3),
    _CmAlmTestAlarmEntity_Type()
)
cmAlmTestAlarmEntity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlmTestAlarmEntity.setStatus("current")
_CmAlmTestAlarmAction_Type = TestAlarmAction
_CmAlmTestAlarmAction_Object = MibScalar
cmAlmTestAlarmAction = _CmAlmTestAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 1, 4),
    _CmAlmTestAlarmAction_Type()
)
cmAlmTestAlarmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlmTestAlarmAction.setStatus("current")
_CmSysAlmTable_Object = MibTable
cmSysAlmTable = _CmSysAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2)
)
if mibBuilder.loadTexts:
    cmSysAlmTable.setStatus("current")
_CmSysAlmEntry_Object = MibTableRow
cmSysAlmEntry = _CmSysAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1)
)
cmSysAlmEntry.setIndexNames(
    (0, "CM-ALARM-MIB", "cmAlmIndex"),
)
if mibBuilder.loadTexts:
    cmSysAlmEntry.setStatus("current")
_CmSysAlmNotifCode_Type = TrapAlarmSeverity
_CmSysAlmNotifCode_Object = MibTableColumn
cmSysAlmNotifCode = _CmSysAlmNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 1),
    _CmSysAlmNotifCode_Type()
)
cmSysAlmNotifCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmNotifCode.setStatus("current")
_CmSysAlmType_Type = CmConditionType
_CmSysAlmType_Object = MibTableColumn
cmSysAlmType = _CmSysAlmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 2),
    _CmSysAlmType_Type()
)
cmSysAlmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmType.setStatus("current")
_CmSysAlmSrvEff_Type = CmServiceEffect
_CmSysAlmSrvEff_Object = MibTableColumn
cmSysAlmSrvEff = _CmSysAlmSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 3),
    _CmSysAlmSrvEff_Type()
)
cmSysAlmSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmSrvEff.setStatus("current")
_CmSysAlmTime_Type = DateAndTime
_CmSysAlmTime_Object = MibTableColumn
cmSysAlmTime = _CmSysAlmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 4),
    _CmSysAlmTime_Type()
)
cmSysAlmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmTime.setStatus("current")
_CmSysAlmLocation_Type = CmLocation
_CmSysAlmLocation_Object = MibTableColumn
cmSysAlmLocation = _CmSysAlmLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 5),
    _CmSysAlmLocation_Type()
)
cmSysAlmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmLocation.setStatus("current")
_CmSysAlmDirection_Type = CmDirection
_CmSysAlmDirection_Object = MibTableColumn
cmSysAlmDirection = _CmSysAlmDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 6),
    _CmSysAlmDirection_Type()
)
cmSysAlmDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmDirection.setStatus("current")
_CmSysAlmDescr_Type = CmConditionDescr
_CmSysAlmDescr_Object = MibTableColumn
cmSysAlmDescr = _CmSysAlmDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 7),
    _CmSysAlmDescr_Type()
)
cmSysAlmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmDescr.setStatus("current")
_CmSysAlmObject_Type = VariablePointer
_CmSysAlmObject_Object = MibTableColumn
cmSysAlmObject = _CmSysAlmObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 8),
    _CmSysAlmObject_Type()
)
cmSysAlmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmObject.setStatus("current")
_CmSysAlmObjectName_Type = DisplayString
_CmSysAlmObjectName_Object = MibTableColumn
cmSysAlmObjectName = _CmSysAlmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 9),
    _CmSysAlmObjectName_Type()
)
cmSysAlmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmObjectName.setStatus("current")
_CmSysAlmAdditionalInfoObject_Type = VariablePointer
_CmSysAlmAdditionalInfoObject_Object = MibTableColumn
cmSysAlmAdditionalInfoObject = _CmSysAlmAdditionalInfoObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 10),
    _CmSysAlmAdditionalInfoObject_Type()
)
cmSysAlmAdditionalInfoObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmAdditionalInfoObject.setStatus("current")


class _CmSysAlmAdditionalInfoName_Type(DisplayString):
    """Custom type cmSysAlmAdditionalInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSysAlmAdditionalInfoName_Type.__name__ = "DisplayString"
_CmSysAlmAdditionalInfoName_Object = MibTableColumn
cmSysAlmAdditionalInfoName = _CmSysAlmAdditionalInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 2, 1, 11),
    _CmSysAlmAdditionalInfoName_Type()
)
cmSysAlmAdditionalInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysAlmAdditionalInfoName.setStatus("current")
_CmSysCondTable_Object = MibTable
cmSysCondTable = _CmSysCondTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3)
)
if mibBuilder.loadTexts:
    cmSysCondTable.setStatus("current")
_CmSysCondEntry_Object = MibTableRow
cmSysCondEntry = _CmSysCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1)
)
cmSysCondEntry.setIndexNames(
    (0, "CM-ALARM-MIB", "cmSysCondIndex"),
)
if mibBuilder.loadTexts:
    cmSysCondEntry.setStatus("current")


class _CmSysCondIndex_Type(Integer32):
    """Custom type cmSysCondIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmSysCondIndex_Type.__name__ = "Integer32"
_CmSysCondIndex_Object = MibTableColumn
cmSysCondIndex = _CmSysCondIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 1),
    _CmSysCondIndex_Type()
)
cmSysCondIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondIndex.setStatus("current")
_CmSysCondNotifCode_Type = TrapAlarmSeverity
_CmSysCondNotifCode_Object = MibTableColumn
cmSysCondNotifCode = _CmSysCondNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 2),
    _CmSysCondNotifCode_Type()
)
cmSysCondNotifCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondNotifCode.setStatus("current")
_CmSysCondType_Type = CmConditionType
_CmSysCondType_Object = MibTableColumn
cmSysCondType = _CmSysCondType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 3),
    _CmSysCondType_Type()
)
cmSysCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondType.setStatus("current")
_CmSysCondSrvEff_Type = CmServiceEffect
_CmSysCondSrvEff_Object = MibTableColumn
cmSysCondSrvEff = _CmSysCondSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 4),
    _CmSysCondSrvEff_Type()
)
cmSysCondSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondSrvEff.setStatus("current")
_CmSysCondTime_Type = DateAndTime
_CmSysCondTime_Object = MibTableColumn
cmSysCondTime = _CmSysCondTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 5),
    _CmSysCondTime_Type()
)
cmSysCondTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondTime.setStatus("current")
_CmSysCondLocation_Type = CmLocation
_CmSysCondLocation_Object = MibTableColumn
cmSysCondLocation = _CmSysCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 6),
    _CmSysCondLocation_Type()
)
cmSysCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondLocation.setStatus("current")
_CmSysCondDirection_Type = CmDirection
_CmSysCondDirection_Object = MibTableColumn
cmSysCondDirection = _CmSysCondDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 7),
    _CmSysCondDirection_Type()
)
cmSysCondDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondDirection.setStatus("current")
_CmSysCondDescr_Type = CmConditionDescr
_CmSysCondDescr_Object = MibTableColumn
cmSysCondDescr = _CmSysCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 8),
    _CmSysCondDescr_Type()
)
cmSysCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondDescr.setStatus("current")
_CmSysCondEffType_Type = CmCondEffectType
_CmSysCondEffType_Object = MibTableColumn
cmSysCondEffType = _CmSysCondEffType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 9),
    _CmSysCondEffType_Type()
)
cmSysCondEffType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondEffType.setStatus("current")
_CmSysCondObject_Type = VariablePointer
_CmSysCondObject_Object = MibTableColumn
cmSysCondObject = _CmSysCondObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 10),
    _CmSysCondObject_Type()
)
cmSysCondObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondObject.setStatus("current")
_CmSysCondObjectName_Type = DisplayString
_CmSysCondObjectName_Object = MibTableColumn
cmSysCondObjectName = _CmSysCondObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 11),
    _CmSysCondObjectName_Type()
)
cmSysCondObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondObjectName.setStatus("current")
_CmSysCondAdditionalInfoObject_Type = VariablePointer
_CmSysCondAdditionalInfoObject_Object = MibTableColumn
cmSysCondAdditionalInfoObject = _CmSysCondAdditionalInfoObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 12),
    _CmSysCondAdditionalInfoObject_Type()
)
cmSysCondAdditionalInfoObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondAdditionalInfoObject.setStatus("current")


class _CmSysCondAdditionalInfoName_Type(DisplayString):
    """Custom type cmSysCondAdditionalInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CmSysCondAdditionalInfoName_Type.__name__ = "DisplayString"
_CmSysCondAdditionalInfoName_Object = MibTableColumn
cmSysCondAdditionalInfoName = _CmSysCondAdditionalInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 3, 1, 13),
    _CmSysCondAdditionalInfoName_Type()
)
cmSysCondAdditionalInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCondAdditionalInfoName.setStatus("current")
_CmNetworkElementAlmTable_Object = MibTable
cmNetworkElementAlmTable = _CmNetworkElementAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4)
)
if mibBuilder.loadTexts:
    cmNetworkElementAlmTable.setStatus("current")
_CmNetworkElementAlmEntry_Object = MibTableRow
cmNetworkElementAlmEntry = _CmNetworkElementAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1)
)
cmNetworkElementAlmEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ALARM-MIB", "cmAlmIndex"),
)
if mibBuilder.loadTexts:
    cmNetworkElementAlmEntry.setStatus("current")
_CmNetworkElementAlmNotifCode_Type = TrapAlarmSeverity
_CmNetworkElementAlmNotifCode_Object = MibTableColumn
cmNetworkElementAlmNotifCode = _CmNetworkElementAlmNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 1),
    _CmNetworkElementAlmNotifCode_Type()
)
cmNetworkElementAlmNotifCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmNotifCode.setStatus("current")
_CmNetworkElementAlmType_Type = CmConditionType
_CmNetworkElementAlmType_Object = MibTableColumn
cmNetworkElementAlmType = _CmNetworkElementAlmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 2),
    _CmNetworkElementAlmType_Type()
)
cmNetworkElementAlmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmType.setStatus("current")
_CmNetworkElementAlmSrvEff_Type = CmServiceEffect
_CmNetworkElementAlmSrvEff_Object = MibTableColumn
cmNetworkElementAlmSrvEff = _CmNetworkElementAlmSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 3),
    _CmNetworkElementAlmSrvEff_Type()
)
cmNetworkElementAlmSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmSrvEff.setStatus("current")
_CmNetworkElementAlmTime_Type = DateAndTime
_CmNetworkElementAlmTime_Object = MibTableColumn
cmNetworkElementAlmTime = _CmNetworkElementAlmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 4),
    _CmNetworkElementAlmTime_Type()
)
cmNetworkElementAlmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmTime.setStatus("current")
_CmNetworkElementAlmLocation_Type = CmLocation
_CmNetworkElementAlmLocation_Object = MibTableColumn
cmNetworkElementAlmLocation = _CmNetworkElementAlmLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 5),
    _CmNetworkElementAlmLocation_Type()
)
cmNetworkElementAlmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmLocation.setStatus("current")
_CmNetworkElementAlmDirection_Type = CmDirection
_CmNetworkElementAlmDirection_Object = MibTableColumn
cmNetworkElementAlmDirection = _CmNetworkElementAlmDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 6),
    _CmNetworkElementAlmDirection_Type()
)
cmNetworkElementAlmDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmDirection.setStatus("current")
_CmNetworkElementAlmDescr_Type = CmConditionDescr
_CmNetworkElementAlmDescr_Object = MibTableColumn
cmNetworkElementAlmDescr = _CmNetworkElementAlmDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 7),
    _CmNetworkElementAlmDescr_Type()
)
cmNetworkElementAlmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmDescr.setStatus("current")
_CmNetworkElementAlmObject_Type = VariablePointer
_CmNetworkElementAlmObject_Object = MibTableColumn
cmNetworkElementAlmObject = _CmNetworkElementAlmObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 8),
    _CmNetworkElementAlmObject_Type()
)
cmNetworkElementAlmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmObject.setStatus("current")
_CmNetworkElementAlmObjectName_Type = DisplayString
_CmNetworkElementAlmObjectName_Object = MibTableColumn
cmNetworkElementAlmObjectName = _CmNetworkElementAlmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 9),
    _CmNetworkElementAlmObjectName_Type()
)
cmNetworkElementAlmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmObjectName.setStatus("current")
_CmNetworkElementAlmAdditionalInfoObject_Type = VariablePointer
_CmNetworkElementAlmAdditionalInfoObject_Object = MibTableColumn
cmNetworkElementAlmAdditionalInfoObject = _CmNetworkElementAlmAdditionalInfoObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 10),
    _CmNetworkElementAlmAdditionalInfoObject_Type()
)
cmNetworkElementAlmAdditionalInfoObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmAdditionalInfoObject.setStatus("current")


class _CmNetworkElementAlmAdditionalInfoName_Type(DisplayString):
    """Custom type cmNetworkElementAlmAdditionalInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmNetworkElementAlmAdditionalInfoName_Type.__name__ = "DisplayString"
_CmNetworkElementAlmAdditionalInfoName_Object = MibTableColumn
cmNetworkElementAlmAdditionalInfoName = _CmNetworkElementAlmAdditionalInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 4, 1, 11),
    _CmNetworkElementAlmAdditionalInfoName_Type()
)
cmNetworkElementAlmAdditionalInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementAlmAdditionalInfoName.setStatus("current")
_CmNetworkElementCondTable_Object = MibTable
cmNetworkElementCondTable = _CmNetworkElementCondTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5)
)
if mibBuilder.loadTexts:
    cmNetworkElementCondTable.setStatus("current")
_CmNetworkElementCondEntry_Object = MibTableRow
cmNetworkElementCondEntry = _CmNetworkElementCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1)
)
cmNetworkElementCondEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ALARM-MIB", "cmNetworkElementCondIndex"),
)
if mibBuilder.loadTexts:
    cmNetworkElementCondEntry.setStatus("current")


class _CmNetworkElementCondIndex_Type(Integer32):
    """Custom type cmNetworkElementCondIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmNetworkElementCondIndex_Type.__name__ = "Integer32"
_CmNetworkElementCondIndex_Object = MibTableColumn
cmNetworkElementCondIndex = _CmNetworkElementCondIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 1),
    _CmNetworkElementCondIndex_Type()
)
cmNetworkElementCondIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondIndex.setStatus("current")
_CmNetworkElementCondNotifCode_Type = TrapAlarmSeverity
_CmNetworkElementCondNotifCode_Object = MibTableColumn
cmNetworkElementCondNotifCode = _CmNetworkElementCondNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 2),
    _CmNetworkElementCondNotifCode_Type()
)
cmNetworkElementCondNotifCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondNotifCode.setStatus("current")
_CmNetworkElementCondType_Type = CmConditionType
_CmNetworkElementCondType_Object = MibTableColumn
cmNetworkElementCondType = _CmNetworkElementCondType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 3),
    _CmNetworkElementCondType_Type()
)
cmNetworkElementCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondType.setStatus("current")
_CmNetworkElementCondSrvEff_Type = CmServiceEffect
_CmNetworkElementCondSrvEff_Object = MibTableColumn
cmNetworkElementCondSrvEff = _CmNetworkElementCondSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 4),
    _CmNetworkElementCondSrvEff_Type()
)
cmNetworkElementCondSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondSrvEff.setStatus("current")
_CmNetworkElementCondTime_Type = DateAndTime
_CmNetworkElementCondTime_Object = MibTableColumn
cmNetworkElementCondTime = _CmNetworkElementCondTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 5),
    _CmNetworkElementCondTime_Type()
)
cmNetworkElementCondTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondTime.setStatus("current")
_CmNetworkElementCondLocation_Type = CmLocation
_CmNetworkElementCondLocation_Object = MibTableColumn
cmNetworkElementCondLocation = _CmNetworkElementCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 6),
    _CmNetworkElementCondLocation_Type()
)
cmNetworkElementCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondLocation.setStatus("current")
_CmNetworkElementCondDirection_Type = CmDirection
_CmNetworkElementCondDirection_Object = MibTableColumn
cmNetworkElementCondDirection = _CmNetworkElementCondDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 7),
    _CmNetworkElementCondDirection_Type()
)
cmNetworkElementCondDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondDirection.setStatus("current")
_CmNetworkElementCondDescr_Type = CmConditionDescr
_CmNetworkElementCondDescr_Object = MibTableColumn
cmNetworkElementCondDescr = _CmNetworkElementCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 8),
    _CmNetworkElementCondDescr_Type()
)
cmNetworkElementCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondDescr.setStatus("current")
_CmNetworkElementCondObject_Type = VariablePointer
_CmNetworkElementCondObject_Object = MibTableColumn
cmNetworkElementCondObject = _CmNetworkElementCondObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 9),
    _CmNetworkElementCondObject_Type()
)
cmNetworkElementCondObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondObject.setStatus("current")
_CmNetworkElementCondObjectName_Type = DisplayString
_CmNetworkElementCondObjectName_Object = MibTableColumn
cmNetworkElementCondObjectName = _CmNetworkElementCondObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 10),
    _CmNetworkElementCondObjectName_Type()
)
cmNetworkElementCondObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondObjectName.setStatus("current")
_CmNetworkElementCondEffType_Type = CmCondEffectType
_CmNetworkElementCondEffType_Object = MibTableColumn
cmNetworkElementCondEffType = _CmNetworkElementCondEffType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 11),
    _CmNetworkElementCondEffType_Type()
)
cmNetworkElementCondEffType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondEffType.setStatus("current")
_CmNetworkElementCondAdditionalInfoObject_Type = VariablePointer
_CmNetworkElementCondAdditionalInfoObject_Object = MibTableColumn
cmNetworkElementCondAdditionalInfoObject = _CmNetworkElementCondAdditionalInfoObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 12),
    _CmNetworkElementCondAdditionalInfoObject_Type()
)
cmNetworkElementCondAdditionalInfoObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondAdditionalInfoObject.setStatus("current")


class _CmNetworkElementCondAdditionalInfoName_Type(DisplayString):
    """Custom type cmNetworkElementCondAdditionalInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmNetworkElementCondAdditionalInfoName_Type.__name__ = "DisplayString"
_CmNetworkElementCondAdditionalInfoName_Object = MibTableColumn
cmNetworkElementCondAdditionalInfoName = _CmNetworkElementCondAdditionalInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 5, 1, 13),
    _CmNetworkElementCondAdditionalInfoName_Type()
)
cmNetworkElementCondAdditionalInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNetworkElementCondAdditionalInfoName.setStatus("current")
_CmAlarmSeverityAssignmentTable_Object = MibTable
cmAlarmSeverityAssignmentTable = _CmAlarmSeverityAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6)
)
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentTable.setStatus("current")
_CmAlarmSeverityAssignmentEntry_Object = MibTableRow
cmAlarmSeverityAssignmentEntry = _CmAlarmSeverityAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6, 1)
)
cmAlarmSeverityAssignmentEntry.setIndexNames(
    (0, "CM-ALARM-MIB", "cmAlarmSeverityAssignmentEntityType"),
    (0, "CM-ALARM-MIB", "cmAlarmSeverityAssignmentCondType"),
    (0, "CM-ALARM-MIB", "cmAlarmSeverityAssignmentSrvEff"),
)
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentEntry.setStatus("current")
_CmAlarmSeverityAssignmentEntityType_Type = CmAlarmEntityType
_CmAlarmSeverityAssignmentEntityType_Object = MibTableColumn
cmAlarmSeverityAssignmentEntityType = _CmAlarmSeverityAssignmentEntityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6, 1, 1),
    _CmAlarmSeverityAssignmentEntityType_Type()
)
cmAlarmSeverityAssignmentEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentEntityType.setStatus("current")
_CmAlarmSeverityAssignmentCondType_Type = CmConditionType
_CmAlarmSeverityAssignmentCondType_Object = MibTableColumn
cmAlarmSeverityAssignmentCondType = _CmAlarmSeverityAssignmentCondType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6, 1, 2),
    _CmAlarmSeverityAssignmentCondType_Type()
)
cmAlarmSeverityAssignmentCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentCondType.setStatus("current")
_CmAlarmSeverityAssignmentSrvEff_Type = CmServiceEffect
_CmAlarmSeverityAssignmentSrvEff_Object = MibTableColumn
cmAlarmSeverityAssignmentSrvEff = _CmAlarmSeverityAssignmentSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6, 1, 3),
    _CmAlarmSeverityAssignmentSrvEff_Type()
)
cmAlarmSeverityAssignmentSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentSrvEff.setStatus("current")
_CmAlarmSeverityAssignmentLocation_Type = CmLocation
_CmAlarmSeverityAssignmentLocation_Object = MibTableColumn
cmAlarmSeverityAssignmentLocation = _CmAlarmSeverityAssignmentLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6, 1, 4),
    _CmAlarmSeverityAssignmentLocation_Type()
)
cmAlarmSeverityAssignmentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentLocation.setStatus("current")
_CmAlarmSeverityAssignmentNotifCode_Type = TrapAlarmSeverity
_CmAlarmSeverityAssignmentNotifCode_Object = MibTableColumn
cmAlarmSeverityAssignmentNotifCode = _CmAlarmSeverityAssignmentNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6, 1, 5),
    _CmAlarmSeverityAssignmentNotifCode_Type()
)
cmAlarmSeverityAssignmentNotifCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentNotifCode.setStatus("current")
_CmAlarmSeverityAssignmentDirection_Type = CmDirection
_CmAlarmSeverityAssignmentDirection_Object = MibTableColumn
cmAlarmSeverityAssignmentDirection = _CmAlarmSeverityAssignmentDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 6, 1, 6),
    _CmAlarmSeverityAssignmentDirection_Type()
)
cmAlarmSeverityAssignmentDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmSeverityAssignmentDirection.setStatus("current")
_F3EnvAlarmInputTable_Object = MibTable
f3EnvAlarmInputTable = _F3EnvAlarmInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7)
)
if mibBuilder.loadTexts:
    f3EnvAlarmInputTable.setStatus("current")
_F3EnvAlarmInputEntry_Object = MibTableRow
f3EnvAlarmInputEntry = _F3EnvAlarmInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7, 1)
)
f3EnvAlarmInputEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ALARM-MIB", "f3EnvAlarmInputIndex"),
)
if mibBuilder.loadTexts:
    f3EnvAlarmInputEntry.setStatus("current")
_F3EnvAlarmInputIndex_Type = Integer32
_F3EnvAlarmInputIndex_Object = MibTableColumn
f3EnvAlarmInputIndex = _F3EnvAlarmInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7, 1, 1),
    _F3EnvAlarmInputIndex_Type()
)
f3EnvAlarmInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3EnvAlarmInputIndex.setStatus("current")


class _F3EnvAlarmInputDescr_Type(DisplayString):
    """Custom type f3EnvAlarmInputDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3EnvAlarmInputDescr_Type.__name__ = "DisplayString"
_F3EnvAlarmInputDescr_Object = MibTableColumn
f3EnvAlarmInputDescr = _F3EnvAlarmInputDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7, 1, 2),
    _F3EnvAlarmInputDescr_Type()
)
f3EnvAlarmInputDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EnvAlarmInputDescr.setStatus("current")
_F3EnvAlarmInputCondType_Type = CmConditionType
_F3EnvAlarmInputCondType_Object = MibTableColumn
f3EnvAlarmInputCondType = _F3EnvAlarmInputCondType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7, 1, 3),
    _F3EnvAlarmInputCondType_Type()
)
f3EnvAlarmInputCondType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EnvAlarmInputCondType.setStatus("current")
_F3EnvAlarmInputNotifCode_Type = TrapAlarmSeverity
_F3EnvAlarmInputNotifCode_Object = MibTableColumn
f3EnvAlarmInputNotifCode = _F3EnvAlarmInputNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7, 1, 4),
    _F3EnvAlarmInputNotifCode_Type()
)
f3EnvAlarmInputNotifCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EnvAlarmInputNotifCode.setStatus("current")
_F3EnvAlarmInputMode_Type = EnvAlarmInputMode
_F3EnvAlarmInputMode_Object = MibTableColumn
f3EnvAlarmInputMode = _F3EnvAlarmInputMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7, 1, 5),
    _F3EnvAlarmInputMode_Type()
)
f3EnvAlarmInputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EnvAlarmInputMode.setStatus("current")
_F3EnvAlarmInputAlmHoldOffEnabled_Type = TruthValue
_F3EnvAlarmInputAlmHoldOffEnabled_Object = MibTableColumn
f3EnvAlarmInputAlmHoldOffEnabled = _F3EnvAlarmInputAlmHoldOffEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 1, 7, 1, 6),
    _F3EnvAlarmInputAlmHoldOffEnabled_Type()
)
f3EnvAlarmInputAlmHoldOffEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EnvAlarmInputAlmHoldOffEnabled.setStatus("current")
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 2)
)
_AlarmConformance_ObjectIdentity = ObjectIdentity
alarmConformance = _AlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 3)
)
_CmAlmCompliances_ObjectIdentity = ObjectIdentity
cmAlmCompliances = _CmAlmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 3, 1)
)
_CmAlmGroups_ObjectIdentity = ObjectIdentity
cmAlmGroups = _CmAlmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 3, 2)
)

# Managed Objects groups

cmAlmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 3, 2, 1)
)
cmAlmObjectGroup.setObjects(
      *(("CM-ALARM-MIB", "cmAlmLastChange"),
        ("CM-ALARM-MIB", "cmAlmIndex"),
        ("CM-ALARM-MIB", "cmAlmTestAlarmEntity"),
        ("CM-ALARM-MIB", "cmAlmTestAlarmAction"),
        ("CM-ALARM-MIB", "cmSysAlmNotifCode"),
        ("CM-ALARM-MIB", "cmSysAlmType"),
        ("CM-ALARM-MIB", "cmSysAlmSrvEff"),
        ("CM-ALARM-MIB", "cmSysAlmTime"),
        ("CM-ALARM-MIB", "cmSysAlmLocation"),
        ("CM-ALARM-MIB", "cmSysAlmDirection"),
        ("CM-ALARM-MIB", "cmSysAlmDescr"),
        ("CM-ALARM-MIB", "cmSysAlmObject"),
        ("CM-ALARM-MIB", "cmSysAlmObjectName"),
        ("CM-ALARM-MIB", "cmSysAlmAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmSysAlmAdditionalInfoName"),
        ("CM-ALARM-MIB", "cmSysCondIndex"),
        ("CM-ALARM-MIB", "cmSysCondNotifCode"),
        ("CM-ALARM-MIB", "cmSysCondType"),
        ("CM-ALARM-MIB", "cmSysCondSrvEff"),
        ("CM-ALARM-MIB", "cmSysCondTime"),
        ("CM-ALARM-MIB", "cmSysCondLocation"),
        ("CM-ALARM-MIB", "cmSysCondDirection"),
        ("CM-ALARM-MIB", "cmSysCondDescr"),
        ("CM-ALARM-MIB", "cmSysCondEffType"),
        ("CM-ALARM-MIB", "cmSysCondObject"),
        ("CM-ALARM-MIB", "cmSysCondObjectName"),
        ("CM-ALARM-MIB", "cmSysCondAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmSysCondAdditionalInfoName"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmNotifCode"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmType"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmSrvEff"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmTime"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmLocation"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmDirection"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmDescr"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmObject"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmObjectName"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmAdditionalInfoName"),
        ("CM-ALARM-MIB", "cmNetworkElementCondIndex"),
        ("CM-ALARM-MIB", "cmNetworkElementCondNotifCode"),
        ("CM-ALARM-MIB", "cmNetworkElementCondType"),
        ("CM-ALARM-MIB", "cmNetworkElementCondSrvEff"),
        ("CM-ALARM-MIB", "cmNetworkElementCondTime"),
        ("CM-ALARM-MIB", "cmNetworkElementCondLocation"),
        ("CM-ALARM-MIB", "cmNetworkElementCondDirection"),
        ("CM-ALARM-MIB", "cmNetworkElementCondDescr"),
        ("CM-ALARM-MIB", "cmNetworkElementCondObject"),
        ("CM-ALARM-MIB", "cmNetworkElementCondObjectName"),
        ("CM-ALARM-MIB", "cmNetworkElementCondEffType"),
        ("CM-ALARM-MIB", "cmNetworkElementCondAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmNetworkElementCondAdditionalInfoName"),
        ("CM-ALARM-MIB", "cmAlarmSeverityAssignmentEntityType"),
        ("CM-ALARM-MIB", "cmAlarmSeverityAssignmentCondType"),
        ("CM-ALARM-MIB", "cmAlarmSeverityAssignmentSrvEff"),
        ("CM-ALARM-MIB", "cmAlarmSeverityAssignmentLocation"),
        ("CM-ALARM-MIB", "cmAlarmSeverityAssignmentNotifCode"),
        ("CM-ALARM-MIB", "cmAlarmSeverityAssignmentDirection"))
)
if mibBuilder.loadTexts:
    cmAlmObjectGroup.setStatus("current")

f3EnvAlarmInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 3, 2, 3)
)
f3EnvAlarmInputGroup.setObjects(
      *(("CM-ALARM-MIB", "f3EnvAlarmInputIndex"),
        ("CM-ALARM-MIB", "f3EnvAlarmInputDescr"),
        ("CM-ALARM-MIB", "f3EnvAlarmInputCondType"),
        ("CM-ALARM-MIB", "f3EnvAlarmInputNotifCode"),
        ("CM-ALARM-MIB", "f3EnvAlarmInputMode"),
        ("CM-ALARM-MIB", "f3EnvAlarmInputAlmHoldOffEnabled"))
)
if mibBuilder.loadTexts:
    f3EnvAlarmInputGroup.setStatus("current")


# Notification objects

cmSysAlmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 2, 1)
)
cmSysAlmTrap.setObjects(
      *(("CM-ALARM-MIB", "cmAlmIndex"),
        ("CM-ALARM-MIB", "cmSysAlmNotifCode"),
        ("CM-ALARM-MIB", "cmSysAlmType"),
        ("CM-ALARM-MIB", "cmSysAlmSrvEff"),
        ("CM-ALARM-MIB", "cmSysAlmTime"),
        ("CM-ALARM-MIB", "cmSysAlmLocation"),
        ("CM-ALARM-MIB", "cmSysAlmDirection"),
        ("CM-ALARM-MIB", "cmSysAlmDescr"),
        ("CM-ALARM-MIB", "cmSysAlmObject"),
        ("CM-ALARM-MIB", "cmSysAlmObjectName"),
        ("CM-ALARM-MIB", "cmSysAlmAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmSysAlmAdditionalInfoName"))
)
if mibBuilder.loadTexts:
    cmSysAlmTrap.setStatus(
        "current"
    )

cmNetworkElementAlmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 2, 2)
)
cmNetworkElementAlmTrap.setObjects(
      *(("CM-ALARM-MIB", "cmAlmIndex"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmNotifCode"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmType"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmSrvEff"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmTime"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmLocation"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmDirection"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmDescr"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmObject"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmObjectName"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmAdditionalInfoName"))
)
if mibBuilder.loadTexts:
    cmNetworkElementAlmTrap.setStatus(
        "current"
    )

cmSysEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 2, 3)
)
cmSysEvent.setObjects(
      *(("CM-ALARM-MIB", "cmAlmIndex"),
        ("CM-ALARM-MIB", "cmSysCondType"),
        ("CM-ALARM-MIB", "cmSysCondTime"),
        ("CM-ALARM-MIB", "cmSysCondLocation"),
        ("CM-ALARM-MIB", "cmSysCondDirection"),
        ("CM-ALARM-MIB", "cmSysCondDescr"),
        ("CM-ALARM-MIB", "cmSysCondEffType"),
        ("CM-ALARM-MIB", "cmSysCondObject"),
        ("CM-ALARM-MIB", "cmSysCondObjectName"),
        ("CM-ALARM-MIB", "cmSysCondAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmSysCondAdditionalInfoName"))
)
if mibBuilder.loadTexts:
    cmSysEvent.setStatus(
        "current"
    )

cmNetworkElementEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 2, 4)
)
cmNetworkElementEvent.setObjects(
      *(("CM-ALARM-MIB", "cmAlmIndex"),
        ("CM-ALARM-MIB", "cmNetworkElementCondType"),
        ("CM-ALARM-MIB", "cmNetworkElementCondTime"),
        ("CM-ALARM-MIB", "cmNetworkElementCondLocation"),
        ("CM-ALARM-MIB", "cmNetworkElementCondDirection"),
        ("CM-ALARM-MIB", "cmNetworkElementCondDescr"),
        ("CM-ALARM-MIB", "cmNetworkElementCondObject"),
        ("CM-ALARM-MIB", "cmNetworkElementCondObjectName"),
        ("CM-ALARM-MIB", "cmNetworkElementCondEffType"),
        ("CM-ALARM-MIB", "cmNetworkElementCondAdditionalInfoObject"),
        ("CM-ALARM-MIB", "cmNetworkElementCondAdditionalInfoName"))
)
if mibBuilder.loadTexts:
    cmNetworkElementEvent.setStatus(
        "current"
    )


# Notifications groups

cmAlmNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 3, 2, 2)
)
cmAlmNotifGroup.setObjects(
      *(("CM-ALARM-MIB", "cmSysAlmTrap"),
        ("CM-ALARM-MIB", "cmNetworkElementAlmTrap"),
        ("CM-ALARM-MIB", "cmSysEvent"),
        ("CM-ALARM-MIB", "cmNetworkElementEvent"))
)
if mibBuilder.loadTexts:
    cmAlmNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmAlmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 6, 3, 1, 1)
)
cmAlmCompliance.setObjects(
      *(("CM-ALARM-MIB", "cmAlmObjectGroup"),
        ("CM-ALARM-MIB", "cmAlmNotifGroup"),
        ("CM-ALARM-MIB", "f3EnvAlarmInputGroup"))
)
if mibBuilder.loadTexts:
    cmAlmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-ALARM-MIB",
    **{"CmServiceEffect": CmServiceEffect,
       "CmLocation": CmLocation,
       "CmDirection": CmDirection,
       "CmConditionType": CmConditionType,
       "CmConditionDescr": CmConditionDescr,
       "CmAlarmEntityType": CmAlarmEntityType,
       "CmCondEffectType": CmCondEffectType,
       "TestAlarmAction": TestAlarmAction,
       "EnvAlarmInputMode": EnvAlarmInputMode,
       "cmAlarmMIB": cmAlarmMIB,
       "alarmObjects": alarmObjects,
       "cmAlarmScalars": cmAlarmScalars,
       "cmAlmLastChange": cmAlmLastChange,
       "cmAlmIndex": cmAlmIndex,
       "cmAlmTestAlarmEntity": cmAlmTestAlarmEntity,
       "cmAlmTestAlarmAction": cmAlmTestAlarmAction,
       "cmSysAlmTable": cmSysAlmTable,
       "cmSysAlmEntry": cmSysAlmEntry,
       "cmSysAlmNotifCode": cmSysAlmNotifCode,
       "cmSysAlmType": cmSysAlmType,
       "cmSysAlmSrvEff": cmSysAlmSrvEff,
       "cmSysAlmTime": cmSysAlmTime,
       "cmSysAlmLocation": cmSysAlmLocation,
       "cmSysAlmDirection": cmSysAlmDirection,
       "cmSysAlmDescr": cmSysAlmDescr,
       "cmSysAlmObject": cmSysAlmObject,
       "cmSysAlmObjectName": cmSysAlmObjectName,
       "cmSysAlmAdditionalInfoObject": cmSysAlmAdditionalInfoObject,
       "cmSysAlmAdditionalInfoName": cmSysAlmAdditionalInfoName,
       "cmSysCondTable": cmSysCondTable,
       "cmSysCondEntry": cmSysCondEntry,
       "cmSysCondIndex": cmSysCondIndex,
       "cmSysCondNotifCode": cmSysCondNotifCode,
       "cmSysCondType": cmSysCondType,
       "cmSysCondSrvEff": cmSysCondSrvEff,
       "cmSysCondTime": cmSysCondTime,
       "cmSysCondLocation": cmSysCondLocation,
       "cmSysCondDirection": cmSysCondDirection,
       "cmSysCondDescr": cmSysCondDescr,
       "cmSysCondEffType": cmSysCondEffType,
       "cmSysCondObject": cmSysCondObject,
       "cmSysCondObjectName": cmSysCondObjectName,
       "cmSysCondAdditionalInfoObject": cmSysCondAdditionalInfoObject,
       "cmSysCondAdditionalInfoName": cmSysCondAdditionalInfoName,
       "cmNetworkElementAlmTable": cmNetworkElementAlmTable,
       "cmNetworkElementAlmEntry": cmNetworkElementAlmEntry,
       "cmNetworkElementAlmNotifCode": cmNetworkElementAlmNotifCode,
       "cmNetworkElementAlmType": cmNetworkElementAlmType,
       "cmNetworkElementAlmSrvEff": cmNetworkElementAlmSrvEff,
       "cmNetworkElementAlmTime": cmNetworkElementAlmTime,
       "cmNetworkElementAlmLocation": cmNetworkElementAlmLocation,
       "cmNetworkElementAlmDirection": cmNetworkElementAlmDirection,
       "cmNetworkElementAlmDescr": cmNetworkElementAlmDescr,
       "cmNetworkElementAlmObject": cmNetworkElementAlmObject,
       "cmNetworkElementAlmObjectName": cmNetworkElementAlmObjectName,
       "cmNetworkElementAlmAdditionalInfoObject": cmNetworkElementAlmAdditionalInfoObject,
       "cmNetworkElementAlmAdditionalInfoName": cmNetworkElementAlmAdditionalInfoName,
       "cmNetworkElementCondTable": cmNetworkElementCondTable,
       "cmNetworkElementCondEntry": cmNetworkElementCondEntry,
       "cmNetworkElementCondIndex": cmNetworkElementCondIndex,
       "cmNetworkElementCondNotifCode": cmNetworkElementCondNotifCode,
       "cmNetworkElementCondType": cmNetworkElementCondType,
       "cmNetworkElementCondSrvEff": cmNetworkElementCondSrvEff,
       "cmNetworkElementCondTime": cmNetworkElementCondTime,
       "cmNetworkElementCondLocation": cmNetworkElementCondLocation,
       "cmNetworkElementCondDirection": cmNetworkElementCondDirection,
       "cmNetworkElementCondDescr": cmNetworkElementCondDescr,
       "cmNetworkElementCondObject": cmNetworkElementCondObject,
       "cmNetworkElementCondObjectName": cmNetworkElementCondObjectName,
       "cmNetworkElementCondEffType": cmNetworkElementCondEffType,
       "cmNetworkElementCondAdditionalInfoObject": cmNetworkElementCondAdditionalInfoObject,
       "cmNetworkElementCondAdditionalInfoName": cmNetworkElementCondAdditionalInfoName,
       "cmAlarmSeverityAssignmentTable": cmAlarmSeverityAssignmentTable,
       "cmAlarmSeverityAssignmentEntry": cmAlarmSeverityAssignmentEntry,
       "cmAlarmSeverityAssignmentEntityType": cmAlarmSeverityAssignmentEntityType,
       "cmAlarmSeverityAssignmentCondType": cmAlarmSeverityAssignmentCondType,
       "cmAlarmSeverityAssignmentSrvEff": cmAlarmSeverityAssignmentSrvEff,
       "cmAlarmSeverityAssignmentLocation": cmAlarmSeverityAssignmentLocation,
       "cmAlarmSeverityAssignmentNotifCode": cmAlarmSeverityAssignmentNotifCode,
       "cmAlarmSeverityAssignmentDirection": cmAlarmSeverityAssignmentDirection,
       "f3EnvAlarmInputTable": f3EnvAlarmInputTable,
       "f3EnvAlarmInputEntry": f3EnvAlarmInputEntry,
       "f3EnvAlarmInputIndex": f3EnvAlarmInputIndex,
       "f3EnvAlarmInputDescr": f3EnvAlarmInputDescr,
       "f3EnvAlarmInputCondType": f3EnvAlarmInputCondType,
       "f3EnvAlarmInputNotifCode": f3EnvAlarmInputNotifCode,
       "f3EnvAlarmInputMode": f3EnvAlarmInputMode,
       "f3EnvAlarmInputAlmHoldOffEnabled": f3EnvAlarmInputAlmHoldOffEnabled,
       "alarmNotifications": alarmNotifications,
       "cmSysAlmTrap": cmSysAlmTrap,
       "cmNetworkElementAlmTrap": cmNetworkElementAlmTrap,
       "cmSysEvent": cmSysEvent,
       "cmNetworkElementEvent": cmNetworkElementEvent,
       "alarmConformance": alarmConformance,
       "cmAlmCompliances": cmAlmCompliances,
       "cmAlmCompliance": cmAlmCompliance,
       "cmAlmGroups": cmAlmGroups,
       "cmAlmObjectGroup": cmAlmObjectGroup,
       "cmAlmNotifGroup": cmAlmNotifGroup,
       "f3EnvAlarmInputGroup": f3EnvAlarmInputGroup}
)
