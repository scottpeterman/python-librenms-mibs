# SNMP MIB module (CORIANT-GROOVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\infinera\CORIANT-GROOVE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:31 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

groove = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2)
)
if mibBuilder.loadTexts:
    groove.setRevisions(
        ("2018-07-10 07:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CoriantCommonOtnEncryStatusEnum(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("handshake", 1),
          ("keyInitializing", 2),
          ("keyInSync", 3),
          ("unreachable", 4),
          ("mismatch", 5),
          ("connectFailed", 6),
          ("disabled", 7),
          ("encryptFail", 8),
          ("encryptNormal", 9),
          ("authenticationFailed", 10),
          ("trafficSquelched", 11))
    )


class CoriantCommonOtnKeySyncSession(TextualConvention, OctetString):
    status = "current"


class CoriantCommonpmThresholdValue(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CoriantCommonpmUnitOfValue(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("dbm", 1),
          ("microseconds", 2),
          ("ps", 3),
          ("psNm", 4),
          ("db", 5),
          ("seconds", 6),
          ("packets", 7),
          ("events", 8),
          ("octets", 9),
          ("bits", 10),
          ("bitsS", 11),
          ("blocks", 12),
          ("times", 13),
          ("percentage", 14),
          ("bitRatio", 15),
          ("mhz", 16),
          ("degreec", 17),
          ("frames", 18))
    )



class CoriantFileSwTypesDeviceFwVersion(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CoriantFileSwTypesDeviceName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CoriantFileSwTypesSwVersion(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class CoriantFileSwTypesSwloadProduct(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CoriantFileSwTypesSwloadVendor(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CoriantFmtypesConditionType(TextualConvention, Integer32):
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
              10001,
              10002,
              10003,
              10004,
              10005,
              10006,
              10007,
              10008,
              10009,
              10010,
              10011,
              10012,
              10013,
              10014,
              10015,
              10016,
              10017,
              10018,
              10019,
              10020,
              10021,
              10022,
              10023,
              10024,
              10025,
              10026,
              10027,
              10028,
              10029,
              10030,
              10031,
              10032,
              10033,
              10034,
              10035,
              10036,
              10037,
              10038,
              10039,
              10040,
              10041,
              10042,
              10043,
              10044,
              10045,
              10046,
              10047,
              10048,
              10049,
              10050,
              10051,
              10052,
              10053,
              10054,
              10055,
              10056,
              10057,
              10058,
              10059,
              10060,
              10061,
              10062,
              10063,
              10064,
              10065,
              10066,
              11001,
              11002,
              11003,
              11004,
              11005,
              11006,
              11007,
              11008,
              11009,
              11010,
              11011,
              11012,
              11013,
              11014,
              11015,
              11016,
              11017,
              11018,
              11019,
              11020,
              11021,
              11022,
              11023,
              11024,
              11025,
              11026,
              11027,
              11028,
              11029,
              11030,
              11031,
              11032,
              11033,
              11034)
        )
    )
    namedValues = NamedValues(
        *(("idp", 1),
          ("rupDeg", 2),
          ("rupFail", 3),
          ("meaHwvm", 4),
          ("mea", 5),
          ("pwra", 6),
          ("pwrb", 7),
          ("rupMiss", 8),
          ("sbanr", 9),
          ("sdf", 10),
          ("thermal", 11),
          ("sdcardmiss", 12),
          ("sdcardfail", 13),
          ("mgmtrst", 14),
          ("progflt", 15),
          ("ntppu", 16),
          ("linkdown", 17),
          ("los", 18),
          ("lol", 19),
          ("lofOtu", 20),
          ("lomOtu", 21),
          ("timOtu", 22),
          ("bdiOtu", 23),
          ("bersdOtu", 24),
          ("aisOtu", 25),
          ("bersdOdu", 26),
          ("lckOdu", 27),
          ("ociOdu", 28),
          ("aisOdu", 29),
          ("bdiOdu", 30),
          ("timOdu", 31),
          ("plmOdu", 32),
          ("loomfi", 33),
          ("msim", 34),
          ("loflom", 35),
          ("csfOpu", 36),
          ("losync", 37),
          ("lf", 38),
          ("rf", 39),
          ("csfLosGfp", 40),
          ("csfLosyncGfp", 41),
          ("csfFdiGfp", 42),
          ("csfRdiGfp", 43),
          ("lofdGfp", 44),
          ("plmGfp", 45),
          ("lpbkfacility", 46),
          ("lpbkfterm", 47),
          ("contcom", 48),
          ("latchOpen", 49),
          ("lof", 50),
          ("aisL", 51),
          ("msAis", 52),
          ("timR", 53),
          ("rsTim", 54),
          ("rfiL", 55),
          ("msRfi", 56),
          ("cabs", 99),
          ("oog", 100),
          ("connectFail", 101),
          ("encryptFail", 102),
          ("keyexFail", 103),
          ("bdi", 104),
          ("bdiO", 105),
          ("autoshutoff", 106),
          ("fibrconnMiss", 107),
          ("bdiP", 108),
          ("losMsa", 109),
          ("protna", 110),
          ("switchThres", 111),
          ("losyncCd", 112),
          ("updatePskFail", 113),
          ("encTrafficSquelch", 114),
          ("tSe", 10001),
          ("tDropevents", 10002),
          ("tOctets", 10003),
          ("tPkts", 10004),
          ("tBroadcastpkts", 10005),
          ("tMulticastpkts", 10006),
          ("tCrcalignerrors", 10007),
          ("tUndersizepkts", 10008),
          ("tOversizepkts", 10009),
          ("tFragments", 10010),
          ("tJabbers", 10011),
          ("tPkts64octets", 10012),
          ("tPkts65to127octets", 10013),
          ("tPkts128to255octets", 10014),
          ("tPkts256to511octets", 10015),
          ("tPkts512to1023octets", 10016),
          ("tPkts1024to1518octets", 10017),
          ("tUtilHt", 10018),
          ("tBeFec", 10019),
          ("tUbeFec", 10020),
          ("tBerFecHt", 10021),
          ("tEbOtu", 10022),
          ("tEsOtu", 10023),
          ("tSesOtu", 10024),
          ("tUasOtu", 10025),
          ("tEbOdu", 10026),
          ("tEsOdu", 10027),
          ("tSesOdu", 10028),
          ("tUasOdu", 10029),
          ("tDelayOduHt", 10030),
          ("tDelayOduLt", 10031),
          ("tDgdHt", 10032),
          ("tCdLt", 10033),
          ("tCdHt", 10034),
          ("tOsnrLt", 10035),
          ("tLoss", 10036),
          ("tOprHt", 10037),
          ("tOprLt", 10038),
          ("tQfactorLt", 10039),
          ("tOptHt", 10040),
          ("tOptLt", 10041),
          ("tPdlHt", 10042),
          ("tOftHt", 10043),
          ("tOftLt", 10044),
          ("tOfrHt", 10045),
          ("tOfrLt", 10046),
          ("tCvS", 10047),
          ("tEsS", 10048),
          ("tSesS", 10049),
          ("tUasS", 10050),
          ("tSefs", 10051),
          ("tBbeRs", 10052),
          ("tEsRs", 10053),
          ("tSesRs", 10054),
          ("tUasRs", 10055),
          ("tOfs", 10056),
          ("tOprLaneHt", 10057),
          ("tOprLaneLt", 10058),
          ("tOprTotalHt", 10059),
          ("tOprTotalLt", 10060),
          ("tOptLaneHt", 10061),
          ("tOptLaneLt", 10062),
          ("tOptTotalHt", 10063),
          ("tOptTotalLt", 10064),
          ("tLossTx", 10065),
          ("tLossRx", 10066),
          ("init", 11001),
          ("swupgCompld", 11002),
          ("swupgFail", 11003),
          ("swupgRollback", 11004),
          ("upgCompld", 11005),
          ("upgFail", 11006),
          ("intrusion", 11007),
          ("userlock", 11008),
          ("swupgIp", 11009),
          ("ztcFail", 11010),
          ("ztcComplete", 11011),
          ("dbactFail", 11012),
          ("inactive", 11013),
          ("restart", 11014),
          ("fstoprot", 11015),
          ("fstowkg", 11016),
          ("lockout", 11017),
          ("mantoprot", 11018),
          ("mantowkg", 11019),
          ("noreq", 11020),
          ("sdonprot", 11021),
          ("sdonwkg", 11022),
          ("sfonprot", 11023),
          ("sfonwkg", 11024),
          ("wkswpr", 11025),
          ("prswwk", 11026),
          ("wtr", 11027),
          ("dnr", 11028),
          ("authnFailed", 11029),
          ("loginFailed", 11030),
          ("candidatePskMismatch", 11031),
          ("updatePskCompld", 11032),
          ("candidatePskAuthenticated", 11033),
          ("updatePskReqRcv", 11034))
    )



class CoriantFmtypesEntityTypeFm(TextualConvention, Integer32):
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
              72)
        )
    )
    namedValues = NamedValues(
        *(("t10gbe", 1),
          ("t40gbe", 2),
          ("t100gbe", 3),
          ("ochOs", 4),
          ("otu4", 5),
          ("otuc2", 6),
          ("otuc3", 7),
          ("oduc2", 8),
          ("oduc3", 9),
          ("odu4", 10),
          ("odu3", 11),
          ("odu2e", 12),
          ("odu2", 13),
          ("shelf", 14),
          ("slot", 15),
          ("port", 16),
          ("fan", 17),
          ("chm1", 18),
          ("chm2", 19),
          ("bfm", 20),
          ("mgteth", 21),
          ("ntppeer", 22),
          ("db", 23),
          ("sw", 24),
          ("log", 25),
          ("security", 26),
          ("psu", 27),
          ("cfp2", 28),
          ("qsfp", 29),
          ("time", 30),
          ("user", 31),
          ("ztc", 32),
          ("ppp", 33),
          ("fc8g", 34),
          ("fc16g", 35),
          ("oduflex", 36),
          ("otu2", 37),
          ("otu2e", 38),
          ("oc192", 39),
          ("stm64", 40),
          ("oms", 41),
          ("gopt", 42),
          ("paoscofp2", 43),
          ("pabaofp2", 44),
          ("pairofp2", 45),
          ("palrofp2", 46),
          ("paerofp2", 47),
          ("bahofp2", 48),
          ("subslot", 50),
          ("occ2", 51),
          ("omd96", 52),
          ("amplifier", 53),
          ("omd48S", 54),
          ("omd48O", 55),
          ("chm1g", 56),
          ("tdcmofp2", 57),
          ("bauofp2", 58),
          ("paulrofp2", 59),
          ("osc", 60),
          ("ots", 61),
          ("sfpplus", 62),
          ("xtm2", 63),
          ("omd8b1ofp2", 64),
          ("omd8b2ofp2", 65),
          ("opsofp2", 66),
          ("ops", 67),
          ("chm1lh", 68),
          ("chm2lh", 69),
          ("t10gwanSonet", 70),
          ("t10gwanSdh", 71),
          ("otdrofp2", 72))
    )



class CoriantFmtypesServiceAffectFm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sa", 1),
          ("nsa", 2))
    )



class CoriantFmtypesSeverityLevel(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("notAlarmed", 4),
          ("notReported", 5),
          ("cleared", 6))
    )



class CoriantPmtypesPmParameter(TextualConvention, Integer32):
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
              102)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("eb", 1),
          ("es", 2),
          ("ses", 3),
          ("uas", 4),
          ("delay", 5),
          ("delayMax", 6),
          ("delayMin", 7),
          ("dgd", 8),
          ("dgdMax", 9),
          ("dgdMin", 10),
          ("cd", 11),
          ("cdMax", 12),
          ("cdMin", 13),
          ("osnr", 14),
          ("osnrMax", 15),
          ("osnrMin", 16),
          ("qFactor", 17),
          ("qFactorMax", 18),
          ("qFactorMin", 19),
          ("opr", 20),
          ("oprMax", 21),
          ("oprMin", 22),
          ("loss", 23),
          ("se", 24),
          ("dropevents", 25),
          ("octets", 26),
          ("pkts", 27),
          ("broadcastpkts", 28),
          ("multicastpkts", 29),
          ("crcalignerrors", 30),
          ("undersizepkts", 31),
          ("oversizepkts", 32),
          ("fragments", 33),
          ("jabbers", 34),
          ("pkts64octets", 35),
          ("pkts65to127octets", 36),
          ("pkts128to255octets", 37),
          ("pkts256to511octets", 38),
          ("pkts512to1023octets", 39),
          ("pkts1024to1518octets", 40),
          ("utilization", 41),
          ("utilizationMax", 42),
          ("utilizationMin", 43),
          ("beFec", 44),
          ("ubeFec", 45),
          ("berFec", 46),
          ("berFecMax", 47),
          ("berFecMin", 48),
          ("opt", 49),
          ("optMax", 50),
          ("optMin", 51),
          ("pdl", 52),
          ("pdlMax", 53),
          ("pdlMin", 54),
          ("oft", 55),
          ("oftMax", 56),
          ("oftMin", 57),
          ("ofr", 58),
          ("ofrMax", 59),
          ("ofrMin", 60),
          ("bbe", 61),
          ("ofs", 65),
          ("cv", 66),
          ("sefs", 67),
          ("oprLaneHigh", 68),
          ("oprLaneHighMax", 69),
          ("oprLaneHighMin", 70),
          ("oprLaneLow", 71),
          ("oprLaneLowMax", 72),
          ("oprLaneLowMin", 73),
          ("oprTotal", 74),
          ("oprTotalMax", 75),
          ("oprTotalMin", 76),
          ("optLaneHigh", 77),
          ("optLaneHighMax", 78),
          ("optLaneHighMin", 79),
          ("optLaneLow", 80),
          ("optLaneLowMax", 81),
          ("optLaneLowMin", 82),
          ("optTotal", 83),
          ("optTotalMax", 84),
          ("optTotalMin", 85),
          ("tmodule", 86),
          ("tinlet", 87),
          ("toutlet", 88),
          ("tmoduleMax", 89),
          ("tmoduleMin", 90),
          ("tinletMax", 91),
          ("tinletMin", 92),
          ("toutletMax", 93),
          ("toutletMin", 94),
          ("berPostFec", 95),
          ("berPostFecMax", 96),
          ("berPostFecMin", 97),
          ("psd", 98),
          ("psc", 99),
          ("lossTx", 100),
          ("lossRx", 101),
          ("encryptionFailRx", 102))
    )



class CoriantPmtypesPmpType(TextualConvention, Integer32):
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("oduNendEgress", 1),
          ("oduNendIngress", 2),
          ("otuNendIngress", 3),
          ("delayMeasurementOdu", 4),
          ("coherentOpticalInterface", 5),
          ("opticalPower", 6),
          ("loss", 7),
          ("ethernetNendIngress", 8),
          ("ethernetNendEgress", 9),
          ("fec", 10),
          ("fcNendIngress", 11),
          ("sonetSNendIngress", 12),
          ("sdhRsNendIngress", 13),
          ("sonetSNendEgress", 14),
          ("sdhRsNendEgress", 15),
          ("shelfTemperature", 16),
          ("equipmentTemperature", 17),
          ("opticalPowerLane", 18),
          ("protectionSwitch", 19),
          ("lossTxrx", 20),
          ("opticalPowerIngress", 21),
          ("opticalPowerEgress", 22),
          ("oduEncryption", 23),
          ("all", 100))
    )



class CoriantPmtypesValidityType(TextualConvention, Integer32):
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
        *(("complete", 1),
          ("partial", 2),
          ("notAvailable", 3))
    )



class CoriantRpcConfigurableLedTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ledTest", 1),
          ("locationLed", 2))
    )



class CoriantTypesCardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117)
        )
    )
    namedValues = NamedValues(
        *(("fan", 11),
          ("psu", 12),
          ("chm1", 13),
          ("chm2", 14),
          ("xtm2", 16),
          ("chm1g", 17),
          ("chm1lh", 18),
          ("chm2lh", 19),
          ("occ2", 100),
          ("omd96", 101),
          ("paoscofp2", 102),
          ("pabaofp2", 103),
          ("pairofp2", 104),
          ("palrofp2", 105),
          ("paerofp2", 106),
          ("bahofp2", 107),
          ("omd48S", 109),
          ("omd48O", 110),
          ("tdcmofp2", 111),
          ("bauofp2", 112),
          ("paulrofp2", 113),
          ("omd8b1ofp2", 114),
          ("omd8b2ofp2", 115),
          ("opsofp2", 116),
          ("otdrofp2", 117))
    )



class CoriantTypesCreationscope(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("systemCreated", 0),
          ("userCreated", 1))
    )



class CoriantTypesDBPrecision1(TextualConvention, OctetString):
    status = "current"


class CoriantTypesDate(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )



class CoriantTypesDecimalFract1(TextualConvention, OctetString):
    status = "current"


class CoriantTypesDuplexMode(TextualConvention, Integer32):
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
        *(("na", 0),
          ("full", 1),
          ("half", 2))
    )



class CoriantTypesEnableSwitch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class CoriantTypesEquipmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              21,
              22,
              23,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("filled", 1),
          ("reserved", 2),
          ("unrecognized", 3),
          ("fan", 11),
          ("psu", 12),
          ("chm1", 13),
          ("chm2", 14),
          ("bfm", 15),
          ("xtm2", 16),
          ("chm1g", 17),
          ("chm1lh", 18),
          ("chm2lh", 19),
          ("qsfp", 21),
          ("cfp2", 22),
          ("sfpplus", 23),
          ("occ2", 100),
          ("omd96", 101),
          ("paoscofp2", 102),
          ("pabaofp2", 103),
          ("pairofp2", 104),
          ("palrofp2", 105),
          ("paerofp2", 106),
          ("bahofp2", 107),
          ("omd48S", 109),
          ("omd48O", 110),
          ("tdcmofp2", 111),
          ("bauofp2", 112),
          ("paulrofp2", 113),
          ("omd8b1ofp2", 114),
          ("omd8b2ofp2", 115),
          ("opsofp2", 116),
          ("otdrofp2", 117))
    )



class CoriantTypesEthFec(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("auto", 3))
    )



class CoriantTypesEthernetRate(TextualConvention, Integer32):
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
        *(("na", 0),
          ("t10", 1),
          ("t100", 2),
          ("t1000", 3),
          ("maxRate", 4))
    )



class CoriantTypesFilename(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class CoriantTypesFlowControl(TextualConvention, Integer32):
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
        *(("na", 0),
          ("off", 1),
          ("txRx", 2),
          ("tx", 3),
          ("rx", 4))
    )



class CoriantTypesFreq(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(191300000, 196111250),
    )



class CoriantTypesFtpPath(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )



class CoriantTypesManagementDirection(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("ingress", 1),
          ("egress", 2))
    )



class CoriantTypesManagementLocation(TextualConvention, Integer32):
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
        *(("nearEnd", 1),
          ("farEnd", 2),
          ("notApplicable", 3))
    )



class CoriantTypesManagementTimePeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("t15min", 1),
          ("t24h", 2),
          ("all", 4),
          ("t1min", 5),
          ("t1h", 6))
    )



class CoriantTypesNameIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CoriantTypesNumberList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CoriantTypesOduType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("odu0", 1),
          ("odu1", 2),
          ("odu2", 3),
          ("odu2e", 4),
          ("odu3", 5),
          ("odu3e", 6),
          ("odu4", 7),
          ("oduflex", 8),
          ("oduc2", 9),
          ("oduc3", 10))
    )



class CoriantTypesOnOff(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class CoriantTypesOpticalDB(TextualConvention, OctetString):
    status = "current"


class CoriantTypesOpticalPower(TextualConvention, OctetString):
    status = "current"


class CoriantTypesOtukFec(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sdfec15", 1),
          ("sdfec25", 2),
          ("g709", 3),
          ("i4", 4),
          ("i7", 5),
          ("nofec", 6),
          ("staircase7", 7),
          ("sdfec15nd", 8))
    )



class CoriantTypesPassword(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )



class CoriantTypesPercentage(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CoriantTypesPluggableFormFactor(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("unrecognized", 1),
          ("qsfpplus", 2),
          ("qsfp28", 3),
          ("cfp2Aco", 4),
          ("sfpplus", 5),
          ("sfp", 6),
          ("xfp", 7))
    )



class CoriantTypesPluggableType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("qsfp", 21),
          ("cfp2", 22),
          ("sfpplus", 23))
    )



class CoriantTypesPortId(TextualConvention, Unsigned32):
    status = "current"


class CoriantTypesPortMode(TextualConvention, Integer32):
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("t10gbe", 1),
          ("t40gbe", 2),
          ("t100gbe", 3),
          ("subport", 4),
          ("qpsk100g", 5),
          ("t8qam300g", 6),
          ("t16qam200g", 7),
          ("fc16g", 8),
          ("fc8g", 9),
          ("otu4", 10),
          ("otu2", 12),
          ("otu2e", 13),
          ("oc192", 14),
          ("stm64", 15),
          ("ochosOtu2", 16),
          ("ochosOtu2e", 17),
          ("t8qam200g", 18),
          ("t10gwanSonet", 19),
          ("t10gwanSdh", 20))
    )



class CoriantTypesPower(TextualConvention, OctetString):
    status = "current"


class CoriantTypesRtpType(TextualConvention, Integer32):
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
        *(("direct", 1),
          ("static", 2),
          ("ospfv2", 3))
    )



class CoriantTypesSessionId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )



class CoriantTypesShelfId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CoriantTypesSlotId(TextualConvention, Unsigned32):
    status = "current"


class CoriantTypesSnmpString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CoriantTypesSourceProtocol(TextualConvention, Integer32):
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
        *(("direct", 1),
          ("static", 2),
          ("ospfv2", 3))
    )



class CoriantTypesSubslotId(TextualConvention, Unsigned32):
    status = "current"


class CoriantTypesTemperature(TextualConvention, OctetString):
    status = "current"


class CoriantTypesTemperaturePrecision3(TextualConvention, OctetString):
    status = "current"


class CoriantTypesTestSignalConfig(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rxtx", 3))
    )



class CoriantTypesTestSignalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prbs", 1),
          ("idle", 3))
    )



class CoriantTypesTimMode(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sapi", 1),
          ("dapi", 2),
          ("oper", 3),
          ("sapiDapi", 4),
          ("sapiOper", 5),
          ("dapiOper", 6),
          ("sapiDapiOper", 7))
    )



class CoriantTypesTimePeriod(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class CoriantTypesTypeOfDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("tx", 2),
          ("rx", 3),
          ("rxtx", 4))
    )



class CoriantTypesUserName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class CoriantTypesYesNo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )



class IetfInetTypesAsNumber(TextualConvention, Unsigned32):
    status = "current"


class IetfInetTypesDomainName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )



class IetfInetTypesDscp(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class IetfInetTypesHost(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpAddress(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpAddressNoZone(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpPrefix(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpVersion(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )



class IetfInetTypesIpv4Address(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpv4AddressNoZone(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpv4Prefix(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpv6Address(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpv6AddressNoZone(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesIpv6FlowLabel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class IetfInetTypesIpv6Prefix(TextualConvention, OctetString):
    status = "current"


class IetfInetTypesPortNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IetfInetTypesUri(TextualConvention, OctetString):
    status = "current"


class IetfNetconfAcmAccessOperationsType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("create", 0),
          ("read", 1),
          ("update", 2),
          ("delete", 3),
          ("exec", 4))
    )


class IetfNetconfAcmActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )



class IetfNetconfAcmGroupNameType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )



class IetfNetconfAcmMatchallStringType(TextualConvention, OctetString):
    status = "current"


class IetfNetconfAcmNodeInstanceIdentifier(TextualConvention, OctetString):
    status = "current"


class IetfNetconfAcmUserNameType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )



class IetfNetconfEditOperationType(TextualConvention, Integer32):
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
        *(("merge", 0),
          ("replace", 1),
          ("create", 2),
          ("delete", 3),
          ("remove", 4))
    )



class IetfNetconfErrorSeverityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("warning", 1))
    )



class IetfNetconfErrorTagType(TextualConvention, Integer32):
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 0),
          ("invalidValue", 1),
          ("tooBig", 2),
          ("missingAttribute", 3),
          ("badAttribute", 4),
          ("unknownAttribute", 5),
          ("missingElement", 6),
          ("badElement", 7),
          ("unknownElement", 8),
          ("unknownNamespace", 9),
          ("accessDenied", 10),
          ("lockDenied", 11),
          ("resourceDenied", 12),
          ("rollbackFailed", 13),
          ("dataExists", 14),
          ("dataMissing", 15),
          ("operationNotSupported", 16),
          ("operationFailed", 17),
          ("partialOperation", 18),
          ("malformedMessage", 19))
    )



class IetfNetconfSessionIdOrZeroType(TextualConvention, Unsigned32):
    status = "current"


class IetfNetconfSessionIdType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IetfNetconfWithDefaultsWithDefaultsMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reportAll", 0),
          ("reportAllTagged", 1),
          ("trim", 2),
          ("explicit", 3))
    )



class IetfYangTypesCounter32(TextualConvention, Unsigned32):
    status = "current"


class IetfYangTypesCounter64(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesDateAndTime(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesDottedQuad(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesGauge32(TextualConvention, Unsigned32):
    status = "current"


class IetfYangTypesGauge64(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesHexString(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesMacAddress(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesObjectIdentifier(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesObjectIdentifier128(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesPhysAddress(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesTimestamp(TextualConvention, Unsigned32):
    status = "current"


class IetfYangTypesTimeticks(TextualConvention, Unsigned32):
    status = "current"


class IetfYangTypesUuid(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesXpath10(TextualConvention, OctetString):
    status = "current"


class IetfYangTypesYangIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )



class IetfYangTypesZeroBasedCounter32(TextualConvention, Unsigned32):
    status = "current"


class IetfYangTypesZeroBasedCounter64(TextualConvention, OctetString):
    status = "current"


class KeySyncSessionCertificateRef(TextualConvention, OctetString):
    status = "current"


class KeySyncSessionInterfaceRef(TextualConvention, OctetString):
    status = "current"


class LldpLldpSysCap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("other", 0),
          ("repeater", 1),
          ("bridge", 2),
          ("wlanaccesspoint", 3),
          ("router", 4),
          ("telephone", 5),
          ("docsiscabledevice", 6),
          ("stationonly", 7),
          ("cvlancomponent", 8),
          ("svlancomponent", 9),
          ("twoportmacrelay", 10))
    )


class OpticalCommonSupportingPort(TextualConvention, OctetString):
    status = "current"


class OtdrOtdrIor(TextualConvention, OctetString):
    status = "current"


class OtdrOtdrPulseWidth(TextualConvention, OctetString):
    status = "current"


class OtdrOtdrRange(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Coriant_ObjectIdentity = ObjectIdentity
coriant = _Coriant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1)
)
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1)
)
_NotificationInfo_ObjectIdentity = ObjectIdentity
notificationInfo = _NotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1)
)
_NotificationObject_ObjectIdentity = ObjectIdentity
notificationObject = _NotificationObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1)
)
_NotificationFmEntity_Type = DisplayString
_NotificationFmEntity_Object = MibScalar
notificationFmEntity = _NotificationFmEntity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 1),
    _NotificationFmEntity_Type()
)
notificationFmEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationFmEntity.setStatus("current")
_NotificationConditionType_Type = CoriantFmtypesConditionType
_NotificationConditionType_Object = MibScalar
notificationConditionType = _NotificationConditionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 2),
    _NotificationConditionType_Type()
)
notificationConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationConditionType.setStatus("current")
_NotificationLocation_Type = CoriantTypesManagementLocation
_NotificationLocation_Object = MibScalar
notificationLocation = _NotificationLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 3),
    _NotificationLocation_Type()
)
notificationLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationLocation.setStatus("current")
_NotificationDirection_Type = CoriantTypesManagementDirection
_NotificationDirection_Object = MibScalar
notificationDirection = _NotificationDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 4),
    _NotificationDirection_Type()
)
notificationDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationDirection.setStatus("current")
_NotificationTimePeriod_Type = CoriantTypesManagementTimePeriod
_NotificationTimePeriod_Object = MibScalar
notificationTimePeriod = _NotificationTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 5),
    _NotificationTimePeriod_Type()
)
notificationTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationTimePeriod.setStatus("current")
_NotificationServiceAffect_Type = CoriantFmtypesServiceAffectFm
_NotificationServiceAffect_Object = MibScalar
notificationServiceAffect = _NotificationServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 6),
    _NotificationServiceAffect_Type()
)
notificationServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationServiceAffect.setStatus("current")
_NotificationSeverityLevel_Type = CoriantFmtypesSeverityLevel
_NotificationSeverityLevel_Object = MibScalar
notificationSeverityLevel = _NotificationSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 7),
    _NotificationSeverityLevel_Type()
)
notificationSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationSeverityLevel.setStatus("current")
_NotificationOccurrenceDateTime_Type = IetfYangTypesDateAndTime
_NotificationOccurrenceDateTime_Object = MibScalar
notificationOccurrenceDateTime = _NotificationOccurrenceDateTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 8),
    _NotificationOccurrenceDateTime_Type()
)
notificationOccurrenceDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationOccurrenceDateTime.setStatus("current")


class _NotificationConditionDescription_Type(OctetString):
    """Custom type notificationConditionDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotificationConditionDescription_Type.__name__ = "OctetString"
_NotificationConditionDescription_Object = MibScalar
notificationConditionDescription = _NotificationConditionDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 9),
    _NotificationConditionDescription_Type()
)
notificationConditionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationConditionDescription.setStatus("current")


class _NotificationAlarmConditionType_Type(Integer32):
    """Custom type notificationAlarmConditionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standing", 1),
          ("transient", 2))
    )


_NotificationAlarmConditionType_Type.__name__ = "Integer32"
_NotificationAlarmConditionType_Object = MibScalar
notificationAlarmConditionType = _NotificationAlarmConditionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 10),
    _NotificationAlarmConditionType_Type()
)
notificationAlarmConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationAlarmConditionType.setStatus("current")
_NotificationLastSeverityLevel_Type = CoriantFmtypesSeverityLevel
_NotificationLastSeverityLevel_Object = MibScalar
notificationLastSeverityLevel = _NotificationLastSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 11),
    _NotificationLastSeverityLevel_Type()
)
notificationLastSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationLastSeverityLevel.setStatus("current")


class _NotificationExtensionDescription_Type(OctetString):
    """Custom type notificationExtensionDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotificationExtensionDescription_Type.__name__ = "OctetString"
_NotificationExtensionDescription_Object = MibScalar
notificationExtensionDescription = _NotificationExtensionDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 12),
    _NotificationExtensionDescription_Type()
)
notificationExtensionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationExtensionDescription.setStatus("current")
_NotificationFmEntityType_Type = CoriantFmtypesEntityTypeFm
_NotificationFmEntityType_Object = MibScalar
notificationFmEntityType = _NotificationFmEntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 1, 1, 13),
    _NotificationFmEntityType_Type()
)
notificationFmEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationFmEntityType.setStatus("current")
_NotificationTrap_ObjectIdentity = ObjectIdentity
notificationTrap = _NotificationTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 2)
)
_AlarmProfile_ObjectIdentity = ObjectIdentity
alarmProfile = _AlarmProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 4)
)
_AlarmProfileTable_Object = MibTable
alarmProfileTable = _AlarmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alarmProfileTable.setStatus("current")
_AlarmProfileEntry_Object = MibTableRow
alarmProfileEntry = _AlarmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 4, 1, 1)
)
alarmProfileEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "alarmProfileId"),
)
if mibBuilder.loadTexts:
    alarmProfileEntry.setStatus("current")


class _AlarmProfileId_Type(Unsigned32):
    """Custom type alarmProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlarmProfileId_Type.__name__ = "Unsigned32"
_AlarmProfileId_Object = MibTableColumn
alarmProfileId = _AlarmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 4, 1, 1, 1),
    _AlarmProfileId_Type()
)
alarmProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProfileId.setStatus("current")
_AlarmProfileENTR_ObjectIdentity = ObjectIdentity
alarmProfileENTR = _AlarmProfileENTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5)
)
_AlarmProfileENTRTable_Object = MibTable
alarmProfileENTRTable = _AlarmProfileENTRTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alarmProfileENTRTable.setStatus("current")
_AlarmProfileENTREntry_Object = MibTableRow
alarmProfileENTREntry = _AlarmProfileENTREntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5, 1, 1)
)
alarmProfileENTREntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "alarmProfileId"),
    (0, "CORIANT-GROOVE-MIB", "alarmProfileENTRConditionType"),
    (0, "CORIANT-GROOVE-MIB", "alarmProfileENTRFmEntityType"),
    (0, "CORIANT-GROOVE-MIB", "alarmProfileENTRTimePeriod"),
)
if mibBuilder.loadTexts:
    alarmProfileENTREntry.setStatus("current")
_AlarmProfileENTRConditionType_Type = CoriantFmtypesConditionType
_AlarmProfileENTRConditionType_Object = MibTableColumn
alarmProfileENTRConditionType = _AlarmProfileENTRConditionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5, 1, 1, 1),
    _AlarmProfileENTRConditionType_Type()
)
alarmProfileENTRConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProfileENTRConditionType.setStatus("current")
_AlarmProfileENTRFmEntityType_Type = CoriantFmtypesEntityTypeFm
_AlarmProfileENTRFmEntityType_Object = MibTableColumn
alarmProfileENTRFmEntityType = _AlarmProfileENTRFmEntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5, 1, 1, 2),
    _AlarmProfileENTRFmEntityType_Type()
)
alarmProfileENTRFmEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProfileENTRFmEntityType.setStatus("current")
_AlarmProfileENTRTimePeriod_Type = CoriantTypesManagementTimePeriod
_AlarmProfileENTRTimePeriod_Object = MibTableColumn
alarmProfileENTRTimePeriod = _AlarmProfileENTRTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5, 1, 1, 3),
    _AlarmProfileENTRTimePeriod_Type()
)
alarmProfileENTRTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProfileENTRTimePeriod.setStatus("current")
_AlarmProfileENTRSeverityLevelSa_Type = CoriantFmtypesSeverityLevel
_AlarmProfileENTRSeverityLevelSa_Object = MibTableColumn
alarmProfileENTRSeverityLevelSa = _AlarmProfileENTRSeverityLevelSa_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5, 1, 1, 4),
    _AlarmProfileENTRSeverityLevelSa_Type()
)
alarmProfileENTRSeverityLevelSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProfileENTRSeverityLevelSa.setStatus("current")
_AlarmProfileENTRSeverityLevelNsa_Type = CoriantFmtypesSeverityLevel
_AlarmProfileENTRSeverityLevelNsa_Object = MibTableColumn
alarmProfileENTRSeverityLevelNsa = _AlarmProfileENTRSeverityLevelNsa_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 5, 1, 1, 5),
    _AlarmProfileENTRSeverityLevelNsa_Type()
)
alarmProfileENTRSeverityLevelNsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProfileENTRSeverityLevelNsa.setStatus("current")
_StandingCondition_ObjectIdentity = ObjectIdentity
standingCondition = _StandingCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6)
)
_StandingConditionTable_Object = MibTable
standingConditionTable = _StandingConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    standingConditionTable.setStatus("current")
_StandingConditionEntry_Object = MibTableRow
standingConditionEntry = _StandingConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1)
)
standingConditionEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "standingConditionFmEntity"),
    (0, "CORIANT-GROOVE-MIB", "standingConditionConditionType"),
    (0, "CORIANT-GROOVE-MIB", "standingConditionLocation"),
    (0, "CORIANT-GROOVE-MIB", "standingConditionDirection"),
    (0, "CORIANT-GROOVE-MIB", "standingConditionTimePeriod"),
)
if mibBuilder.loadTexts:
    standingConditionEntry.setStatus("current")
_StandingConditionFmEntity_Type = RowPointer
_StandingConditionFmEntity_Object = MibTableColumn
standingConditionFmEntity = _StandingConditionFmEntity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 1),
    _StandingConditionFmEntity_Type()
)
standingConditionFmEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionFmEntity.setStatus("current")
_StandingConditionConditionType_Type = CoriantFmtypesConditionType
_StandingConditionConditionType_Object = MibTableColumn
standingConditionConditionType = _StandingConditionConditionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 2),
    _StandingConditionConditionType_Type()
)
standingConditionConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionConditionType.setStatus("current")
_StandingConditionLocation_Type = CoriantTypesManagementLocation
_StandingConditionLocation_Object = MibTableColumn
standingConditionLocation = _StandingConditionLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 3),
    _StandingConditionLocation_Type()
)
standingConditionLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionLocation.setStatus("current")
_StandingConditionDirection_Type = CoriantTypesManagementDirection
_StandingConditionDirection_Object = MibTableColumn
standingConditionDirection = _StandingConditionDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 4),
    _StandingConditionDirection_Type()
)
standingConditionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionDirection.setStatus("current")
_StandingConditionTimePeriod_Type = CoriantTypesManagementTimePeriod
_StandingConditionTimePeriod_Object = MibTableColumn
standingConditionTimePeriod = _StandingConditionTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 5),
    _StandingConditionTimePeriod_Type()
)
standingConditionTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionTimePeriod.setStatus("current")
_StandingConditionServiceAffect_Type = CoriantFmtypesServiceAffectFm
_StandingConditionServiceAffect_Object = MibTableColumn
standingConditionServiceAffect = _StandingConditionServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 6),
    _StandingConditionServiceAffect_Type()
)
standingConditionServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionServiceAffect.setStatus("current")
_StandingConditionSeverityLevel_Type = CoriantFmtypesSeverityLevel
_StandingConditionSeverityLevel_Object = MibTableColumn
standingConditionSeverityLevel = _StandingConditionSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 7),
    _StandingConditionSeverityLevel_Type()
)
standingConditionSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionSeverityLevel.setStatus("current")
_StandingConditionOccurrenceDateTime_Type = IetfYangTypesDateAndTime
_StandingConditionOccurrenceDateTime_Object = MibTableColumn
standingConditionOccurrenceDateTime = _StandingConditionOccurrenceDateTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 8),
    _StandingConditionOccurrenceDateTime_Type()
)
standingConditionOccurrenceDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionOccurrenceDateTime.setStatus("current")


class _StandingConditionConditionDescription_Type(OctetString):
    """Custom type standingConditionConditionDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StandingConditionConditionDescription_Type.__name__ = "OctetString"
_StandingConditionConditionDescription_Object = MibTableColumn
standingConditionConditionDescription = _StandingConditionConditionDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 9),
    _StandingConditionConditionDescription_Type()
)
standingConditionConditionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionConditionDescription.setStatus("current")
_StandingConditionFmEntityType_Type = CoriantFmtypesEntityTypeFm
_StandingConditionFmEntityType_Object = MibTableColumn
standingConditionFmEntityType = _StandingConditionFmEntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 6, 1, 1, 10),
    _StandingConditionFmEntityType_Type()
)
standingConditionFmEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standingConditionFmEntityType.setStatus("current")
_Ne_ObjectIdentity = ObjectIdentity
ne = _Ne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2)
)
_NeInfo_ObjectIdentity = ObjectIdentity
neInfo = _NeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1)
)


class _NeId_Type(OctetString):
    """Custom type neId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NeId_Type.__name__ = "OctetString"
_NeId_Object = MibScalar
neId = _NeId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 1),
    _NeId_Type()
)
neId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neId.setStatus("current")


class _NeName_Type(OctetString):
    """Custom type neName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NeName_Type.__name__ = "OctetString"
_NeName_Object = MibScalar
neName = _NeName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 2),
    _NeName_Type()
)
neName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neName.setStatus("current")
_NeType_Type = OctetString
_NeType_Object = MibScalar
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 3),
    _NeType_Type()
)
neType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neType.setStatus("current")


class _NeLocation_Type(OctetString):
    """Custom type neLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NeLocation_Type.__name__ = "OctetString"
_NeLocation_Object = MibScalar
neLocation = _NeLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 4),
    _NeLocation_Type()
)
neLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLocation.setStatus("current")


class _NeSite_Type(OctetString):
    """Custom type neSite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NeSite_Type.__name__ = "OctetString"
_NeSite_Object = MibScalar
neSite = _NeSite_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 5),
    _NeSite_Type()
)
neSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neSite.setStatus("current")
_NeAltitude_Type = Integer32
_NeAltitude_Object = MibScalar
neAltitude = _NeAltitude_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 6),
    _NeAltitude_Type()
)
neAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAltitude.setStatus("current")
_NeVendor_Type = OctetString
_NeVendor_Object = MibScalar
neVendor = _NeVendor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 7),
    _NeVendor_Type()
)
neVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neVendor.setStatus("current")
_NeTemperature_Type = CoriantTypesTemperature
_NeTemperature_Object = MibScalar
neTemperature = _NeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 1, 8),
    _NeTemperature_Type()
)
neTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTemperature.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 2)
)
_SystemUnknownPluggableReport_Type = CoriantTypesEnableSwitch
_SystemUnknownPluggableReport_Object = MibScalar
systemUnknownPluggableReport = _SystemUnknownPluggableReport_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 2, 1),
    _SystemUnknownPluggableReport_Type()
)
systemUnknownPluggableReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUnknownPluggableReport.setStatus("current")
_SystemPowerConsumptionCurrent_Type = CoriantTypesPower
_SystemPowerConsumptionCurrent_Object = MibScalar
systemPowerConsumptionCurrent = _SystemPowerConsumptionCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 2, 2),
    _SystemPowerConsumptionCurrent_Type()
)
systemPowerConsumptionCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerConsumptionCurrent.setStatus("current")
_SystemPowerConsumptionEstimatedMax_Type = CoriantTypesPower
_SystemPowerConsumptionEstimatedMax_Object = MibScalar
systemPowerConsumptionEstimatedMax = _SystemPowerConsumptionEstimatedMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 2, 3),
    _SystemPowerConsumptionEstimatedMax_Type()
)
systemPowerConsumptionEstimatedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerConsumptionEstimatedMax.setStatus("current")
_SystemFactoryResetButton_Type = CoriantTypesEnableSwitch
_SystemFactoryResetButton_Object = MibScalar
systemFactoryResetButton = _SystemFactoryResetButton_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 2, 4),
    _SystemFactoryResetButton_Type()
)
systemFactoryResetButton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFactoryResetButton.setStatus("current")
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 3)
)


class _ConsoleBaudRate_Type(Integer32):
    """Custom type consoleBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("t9600", 6),
          ("t19200", 7),
          ("t38400", 8),
          ("t57600", 11),
          ("t115200", 12))
    )


_ConsoleBaudRate_Type.__name__ = "Integer32"
_ConsoleBaudRate_Object = MibScalar
consoleBaudRate = _ConsoleBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 2, 3, 1),
    _ConsoleBaudRate_Type()
)
consoleBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleBaudRate.setStatus("current")
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3)
)
_Shelf_ObjectIdentity = ObjectIdentity
shelf = _Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1)
)
_ShelfTable_Object = MibTable
shelfTable = _ShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    shelfTable.setStatus("current")
_ShelfEntry_Object = MibTableRow
shelfEntry = _ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1)
)
shelfEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
)
if mibBuilder.loadTexts:
    shelfEntry.setStatus("current")
_ShelfId_Type = CoriantTypesShelfId
_ShelfId_Object = MibTableColumn
shelfId = _ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 1),
    _ShelfId_Type()
)
shelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfId.setStatus("current")


class _ShelfLocation_Type(OctetString):
    """Custom type shelfLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ShelfLocation_Type.__name__ = "OctetString"
_ShelfLocation_Object = MibTableColumn
shelfLocation = _ShelfLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 2),
    _ShelfLocation_Type()
)
shelfLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfLocation.setStatus("current")
_ShelfInletTemperature_Type = CoriantTypesTemperature
_ShelfInletTemperature_Object = MibTableColumn
shelfInletTemperature = _ShelfInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 3),
    _ShelfInletTemperature_Type()
)
shelfInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfInletTemperature.setStatus("current")
_ShelfOutletTemperature_Type = CoriantTypesTemperature
_ShelfOutletTemperature_Object = MibTableColumn
shelfOutletTemperature = _ShelfOutletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 4),
    _ShelfOutletTemperature_Type()
)
shelfOutletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfOutletTemperature.setStatus("current")


class _ShelfAdminStatus_Type(Integer32):
    """Custom type shelfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ShelfAdminStatus_Type.__name__ = "Integer32"
_ShelfAdminStatus_Object = MibTableColumn
shelfAdminStatus = _ShelfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 5),
    _ShelfAdminStatus_Type()
)
shelfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfAdminStatus.setStatus("current")


class _ShelfOperStatus_Type(Integer32):
    """Custom type shelfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ShelfOperStatus_Type.__name__ = "Integer32"
_ShelfOperStatus_Object = MibTableColumn
shelfOperStatus = _ShelfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 6),
    _ShelfOperStatus_Type()
)
shelfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfOperStatus.setStatus("current")


class _ShelfAvailStatus_Type(Bits):
    """Custom type shelfAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_ShelfAvailStatus_Type.__name__ = "Bits"
_ShelfAvailStatus_Object = MibTableColumn
shelfAvailStatus = _ShelfAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 7),
    _ShelfAvailStatus_Type()
)
shelfAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfAvailStatus.setStatus("current")


class _ShelfAliasName_Type(OctetString):
    """Custom type shelfAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ShelfAliasName_Type.__name__ = "OctetString"
_ShelfAliasName_Object = MibTableColumn
shelfAliasName = _ShelfAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 1, 1, 1, 8),
    _ShelfAliasName_Type()
)
shelfAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfAliasName.setStatus("current")
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("current")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1)
)
slotEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("current")
_SlotId_Type = CoriantTypesSlotId
_SlotId_Object = MibTableColumn
slotId = _SlotId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1, 1),
    _SlotId_Type()
)
slotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotId.setStatus("current")
_SlotActualCardType_Type = CoriantTypesEquipmentType
_SlotActualCardType_Object = MibTableColumn
slotActualCardType = _SlotActualCardType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1, 2),
    _SlotActualCardType_Type()
)
slotActualCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotActualCardType.setStatus("current")
_SlotPossibleCardTypes_Type = OctetString
_SlotPossibleCardTypes_Object = MibTableColumn
slotPossibleCardTypes = _SlotPossibleCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1, 3),
    _SlotPossibleCardTypes_Type()
)
slotPossibleCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPossibleCardTypes.setStatus("current")


class _SlotAdminStatus_Type(Integer32):
    """Custom type slotAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SlotAdminStatus_Type.__name__ = "Integer32"
_SlotAdminStatus_Object = MibTableColumn
slotAdminStatus = _SlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1, 4),
    _SlotAdminStatus_Type()
)
slotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAdminStatus.setStatus("current")


class _SlotOperStatus_Type(Integer32):
    """Custom type slotOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SlotOperStatus_Type.__name__ = "Integer32"
_SlotOperStatus_Object = MibTableColumn
slotOperStatus = _SlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1, 5),
    _SlotOperStatus_Type()
)
slotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotOperStatus.setStatus("current")


class _SlotAvailStatus_Type(Bits):
    """Custom type slotAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_SlotAvailStatus_Type.__name__ = "Bits"
_SlotAvailStatus_Object = MibTableColumn
slotAvailStatus = _SlotAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1, 6),
    _SlotAvailStatus_Type()
)
slotAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAvailStatus.setStatus("current")


class _SlotAliasName_Type(OctetString):
    """Custom type slotAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlotAliasName_Type.__name__ = "OctetString"
_SlotAliasName_Object = MibTableColumn
slotAliasName = _SlotAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 2, 1, 1, 7),
    _SlotAliasName_Type()
)
slotAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAliasName.setStatus("current")
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3)
)
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("current")
_CardEntry_Object = MibTableRow
cardEntry = _CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1)
)
cardEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
)
if mibBuilder.loadTexts:
    cardEntry.setStatus("current")
_CardRequiredType_Type = CoriantTypesCardType
_CardRequiredType_Object = MibTableColumn
cardRequiredType = _CardRequiredType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 1),
    _CardRequiredType_Type()
)
cardRequiredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRequiredType.setStatus("current")


class _CardEquipmentName_Type(OctetString):
    """Custom type cardEquipmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardEquipmentName_Type.__name__ = "OctetString"
_CardEquipmentName_Object = MibTableColumn
cardEquipmentName = _CardEquipmentName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 2),
    _CardEquipmentName_Type()
)
cardEquipmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardEquipmentName.setStatus("current")


class _CardAdminStatus_Type(Integer32):
    """Custom type cardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_CardAdminStatus_Type.__name__ = "Integer32"
_CardAdminStatus_Object = MibTableColumn
cardAdminStatus = _CardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 3),
    _CardAdminStatus_Type()
)
cardAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAdminStatus.setStatus("current")


class _CardOperStatus_Type(Integer32):
    """Custom type cardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_CardOperStatus_Type.__name__ = "Integer32"
_CardOperStatus_Object = MibTableColumn
cardOperStatus = _CardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 4),
    _CardOperStatus_Type()
)
cardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperStatus.setStatus("current")


class _CardAvailStatus_Type(Bits):
    """Custom type cardAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_CardAvailStatus_Type.__name__ = "Bits"
_CardAvailStatus_Object = MibTableColumn
cardAvailStatus = _CardAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 5),
    _CardAvailStatus_Type()
)
cardAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAvailStatus.setStatus("current")


class _CardAliasName_Type(OctetString):
    """Custom type cardAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CardAliasName_Type.__name__ = "OctetString"
_CardAliasName_Object = MibTableColumn
cardAliasName = _CardAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 6),
    _CardAliasName_Type()
)
cardAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAliasName.setStatus("current")
_CardFanSpeedRate_Type = CoriantTypesPercentage
_CardFanSpeedRate_Object = MibTableColumn
cardFanSpeedRate = _CardFanSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 7),
    _CardFanSpeedRate_Type()
)
cardFanSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFanSpeedRate.setStatus("current")


class _CardSwitchingType_Type(Integer32):
    """Custom type cardSwitchingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("otn", 0),
          ("tdm", 1),
          ("optical", 2),
          ("packet", 3))
    )


_CardSwitchingType_Type.__name__ = "Integer32"
_CardSwitchingType_Object = MibTableColumn
cardSwitchingType = _CardSwitchingType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 8),
    _CardSwitchingType_Type()
)
cardSwitchingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwitchingType.setStatus("current")
_CardTemperature_Type = CoriantTypesTemperature
_CardTemperature_Object = MibTableColumn
cardTemperature = _CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 9),
    _CardTemperature_Type()
)
cardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTemperature.setStatus("current")


class _CardMode_Type(Integer32):
    """Custom type cardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("normal", 1),
          ("regen", 2))
    )


_CardMode_Type.__name__ = "Integer32"
_CardMode_Object = MibTableColumn
cardMode = _CardMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 3, 1, 1, 10),
    _CardMode_Type()
)
cardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMode.setStatus("current")
_Subslot_ObjectIdentity = ObjectIdentity
subslot = _Subslot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4)
)
_SubslotTable_Object = MibTable
subslotTable = _SubslotTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    subslotTable.setStatus("current")
_SubslotEntry_Object = MibTableRow
subslotEntry = _SubslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1)
)
subslotEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
)
if mibBuilder.loadTexts:
    subslotEntry.setStatus("current")
_SubslotId_Type = CoriantTypesSlotId
_SubslotId_Object = MibTableColumn
subslotId = _SubslotId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1, 1),
    _SubslotId_Type()
)
subslotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subslotId.setStatus("current")
_SubslotActualCardType_Type = CoriantTypesEquipmentType
_SubslotActualCardType_Object = MibTableColumn
subslotActualCardType = _SubslotActualCardType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1, 2),
    _SubslotActualCardType_Type()
)
subslotActualCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subslotActualCardType.setStatus("current")
_SubslotPossibleCardTypes_Type = OctetString
_SubslotPossibleCardTypes_Object = MibTableColumn
subslotPossibleCardTypes = _SubslotPossibleCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1, 3),
    _SubslotPossibleCardTypes_Type()
)
subslotPossibleCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subslotPossibleCardTypes.setStatus("current")


class _SubslotAdminStatus_Type(Integer32):
    """Custom type subslotAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SubslotAdminStatus_Type.__name__ = "Integer32"
_SubslotAdminStatus_Object = MibTableColumn
subslotAdminStatus = _SubslotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1, 4),
    _SubslotAdminStatus_Type()
)
subslotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subslotAdminStatus.setStatus("current")


class _SubslotOperStatus_Type(Integer32):
    """Custom type subslotOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SubslotOperStatus_Type.__name__ = "Integer32"
_SubslotOperStatus_Object = MibTableColumn
subslotOperStatus = _SubslotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1, 5),
    _SubslotOperStatus_Type()
)
subslotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subslotOperStatus.setStatus("current")


class _SubslotAvailStatus_Type(Bits):
    """Custom type subslotAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_SubslotAvailStatus_Type.__name__ = "Bits"
_SubslotAvailStatus_Object = MibTableColumn
subslotAvailStatus = _SubslotAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1, 6),
    _SubslotAvailStatus_Type()
)
subslotAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subslotAvailStatus.setStatus("current")


class _SubslotAliasName_Type(OctetString):
    """Custom type subslotAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SubslotAliasName_Type.__name__ = "OctetString"
_SubslotAliasName_Object = MibTableColumn
subslotAliasName = _SubslotAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 4, 1, 1, 7),
    _SubslotAliasName_Type()
)
subslotAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subslotAliasName.setStatus("current")
_Subcard_ObjectIdentity = ObjectIdentity
subcard = _Subcard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5)
)
_SubcardTable_Object = MibTable
subcardTable = _SubcardTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    subcardTable.setStatus("current")
_SubcardEntry_Object = MibTableRow
subcardEntry = _SubcardEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1)
)
subcardEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
)
if mibBuilder.loadTexts:
    subcardEntry.setStatus("current")
_SubcardRequiredType_Type = CoriantTypesCardType
_SubcardRequiredType_Object = MibTableColumn
subcardRequiredType = _SubcardRequiredType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1, 1),
    _SubcardRequiredType_Type()
)
subcardRequiredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardRequiredType.setStatus("current")


class _SubcardEquipmentName_Type(OctetString):
    """Custom type subcardEquipmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SubcardEquipmentName_Type.__name__ = "OctetString"
_SubcardEquipmentName_Object = MibTableColumn
subcardEquipmentName = _SubcardEquipmentName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1, 2),
    _SubcardEquipmentName_Type()
)
subcardEquipmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardEquipmentName.setStatus("current")


class _SubcardAdminStatus_Type(Integer32):
    """Custom type subcardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SubcardAdminStatus_Type.__name__ = "Integer32"
_SubcardAdminStatus_Object = MibTableColumn
subcardAdminStatus = _SubcardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1, 3),
    _SubcardAdminStatus_Type()
)
subcardAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardAdminStatus.setStatus("current")


class _SubcardOperStatus_Type(Integer32):
    """Custom type subcardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SubcardOperStatus_Type.__name__ = "Integer32"
_SubcardOperStatus_Object = MibTableColumn
subcardOperStatus = _SubcardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1, 4),
    _SubcardOperStatus_Type()
)
subcardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardOperStatus.setStatus("current")


class _SubcardAvailStatus_Type(Bits):
    """Custom type subcardAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_SubcardAvailStatus_Type.__name__ = "Bits"
_SubcardAvailStatus_Object = MibTableColumn
subcardAvailStatus = _SubcardAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1, 5),
    _SubcardAvailStatus_Type()
)
subcardAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardAvailStatus.setStatus("current")


class _SubcardAliasName_Type(OctetString):
    """Custom type subcardAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SubcardAliasName_Type.__name__ = "OctetString"
_SubcardAliasName_Object = MibTableColumn
subcardAliasName = _SubcardAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1, 6),
    _SubcardAliasName_Type()
)
subcardAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardAliasName.setStatus("current")
_SubcardTemperature_Type = CoriantTypesTemperature
_SubcardTemperature_Object = MibTableColumn
subcardTemperature = _SubcardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 5, 1, 1, 7),
    _SubcardTemperature_Type()
)
subcardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardTemperature.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1)
)
portEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortId_Type = CoriantTypesPortId
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 1),
    _PortId_Type()
)
portId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portId.setStatus("current")
_PortPossiblePluggableTypes_Type = OctetString
_PortPossiblePluggableTypes_Object = MibTableColumn
portPossiblePluggableTypes = _PortPossiblePluggableTypes_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 2),
    _PortPossiblePluggableTypes_Type()
)
portPossiblePluggableTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPossiblePluggableTypes.setStatus("current")
_PortActualPluggableType_Type = CoriantTypesEquipmentType
_PortActualPluggableType_Object = MibTableColumn
portActualPluggableType = _PortActualPluggableType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 3),
    _PortActualPluggableType_Type()
)
portActualPluggableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portActualPluggableType.setStatus("current")
_PortRxOpticalPower_Type = CoriantTypesOpticalPower
_PortRxOpticalPower_Object = MibTableColumn
portRxOpticalPower = _PortRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 4),
    _PortRxOpticalPower_Type()
)
portRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxOpticalPower.setStatus("current")
_PortTxOpticalPower_Type = CoriantTypesOpticalPower
_PortTxOpticalPower_Object = MibTableColumn
portTxOpticalPower = _PortTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 5),
    _PortTxOpticalPower_Type()
)
portTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTxOpticalPower.setStatus("current")
_PortRxOpticalPowerSelectedChannel_Type = CoriantTypesOpticalPower
_PortRxOpticalPowerSelectedChannel_Object = MibTableColumn
portRxOpticalPowerSelectedChannel = _PortRxOpticalPowerSelectedChannel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 6),
    _PortRxOpticalPowerSelectedChannel_Type()
)
portRxOpticalPowerSelectedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxOpticalPowerSelectedChannel.setStatus("current")
_PortRxOpticalPowerLane1_Type = CoriantTypesOpticalPower
_PortRxOpticalPowerLane1_Object = MibTableColumn
portRxOpticalPowerLane1 = _PortRxOpticalPowerLane1_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 7),
    _PortRxOpticalPowerLane1_Type()
)
portRxOpticalPowerLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxOpticalPowerLane1.setStatus("current")
_PortRxOpticalPowerLane2_Type = CoriantTypesOpticalPower
_PortRxOpticalPowerLane2_Object = MibTableColumn
portRxOpticalPowerLane2 = _PortRxOpticalPowerLane2_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 8),
    _PortRxOpticalPowerLane2_Type()
)
portRxOpticalPowerLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxOpticalPowerLane2.setStatus("current")
_PortRxOpticalPowerLane3_Type = CoriantTypesOpticalPower
_PortRxOpticalPowerLane3_Object = MibTableColumn
portRxOpticalPowerLane3 = _PortRxOpticalPowerLane3_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 9),
    _PortRxOpticalPowerLane3_Type()
)
portRxOpticalPowerLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxOpticalPowerLane3.setStatus("current")
_PortRxOpticalPowerLane4_Type = CoriantTypesOpticalPower
_PortRxOpticalPowerLane4_Object = MibTableColumn
portRxOpticalPowerLane4 = _PortRxOpticalPowerLane4_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 10),
    _PortRxOpticalPowerLane4_Type()
)
portRxOpticalPowerLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxOpticalPowerLane4.setStatus("current")
_PortTxOpticalPowerLane1_Type = CoriantTypesOpticalPower
_PortTxOpticalPowerLane1_Object = MibTableColumn
portTxOpticalPowerLane1 = _PortTxOpticalPowerLane1_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 11),
    _PortTxOpticalPowerLane1_Type()
)
portTxOpticalPowerLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTxOpticalPowerLane1.setStatus("current")
_PortTxOpticalPowerLane2_Type = CoriantTypesOpticalPower
_PortTxOpticalPowerLane2_Object = MibTableColumn
portTxOpticalPowerLane2 = _PortTxOpticalPowerLane2_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 12),
    _PortTxOpticalPowerLane2_Type()
)
portTxOpticalPowerLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTxOpticalPowerLane2.setStatus("current")
_PortTxOpticalPowerLane3_Type = CoriantTypesOpticalPower
_PortTxOpticalPowerLane3_Object = MibTableColumn
portTxOpticalPowerLane3 = _PortTxOpticalPowerLane3_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 13),
    _PortTxOpticalPowerLane3_Type()
)
portTxOpticalPowerLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTxOpticalPowerLane3.setStatus("current")
_PortTxOpticalPowerLane4_Type = CoriantTypesOpticalPower
_PortTxOpticalPowerLane4_Object = MibTableColumn
portTxOpticalPowerLane4 = _PortTxOpticalPowerLane4_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 14),
    _PortTxOpticalPowerLane4_Type()
)
portTxOpticalPowerLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTxOpticalPowerLane4.setStatus("current")
_PortDirectionType_Type = CoriantTypesTypeOfDirection
_PortDirectionType_Object = MibTableColumn
portDirectionType = _PortDirectionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 15),
    _PortDirectionType_Type()
)
portDirectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDirectionType.setStatus("current")
_PortName_Type = CoriantTypesNameIdentifier
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 16),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("line", 2),
          ("clientSubport", 3),
          ("optical", 4),
          ("otdr", 5),
          ("opticalNomon", 6))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 17),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")
_PortMode_Type = CoriantTypesPortMode
_PortMode_Object = MibTableColumn
portMode = _PortMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 18),
    _PortMode_Type()
)
portMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMode.setStatus("current")


class _PortAdminStatus_Type(Integer32):
    """Custom type portAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PortAdminStatus_Type.__name__ = "Integer32"
_PortAdminStatus_Object = MibTableColumn
portAdminStatus = _PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 19),
    _PortAdminStatus_Type()
)
portAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAdminStatus.setStatus("current")


class _PortOperStatus_Type(Integer32):
    """Custom type portOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PortOperStatus_Type.__name__ = "Integer32"
_PortOperStatus_Object = MibTableColumn
portOperStatus = _PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 20),
    _PortOperStatus_Type()
)
portOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperStatus.setStatus("current")


class _PortAvailStatus_Type(Bits):
    """Custom type portAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_PortAvailStatus_Type.__name__ = "Bits"
_PortAvailStatus_Object = MibTableColumn
portAvailStatus = _PortAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 21),
    _PortAvailStatus_Type()
)
portAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAvailStatus.setStatus("current")


class _PortAliasName_Type(OctetString):
    """Custom type portAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortAliasName_Type.__name__ = "OctetString"
_PortAliasName_Object = MibTableColumn
portAliasName = _PortAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 22),
    _PortAliasName_Type()
)
portAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAliasName.setStatus("current")


class _PortServiceLabel_Type(OctetString):
    """Custom type portServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortServiceLabel_Type.__name__ = "OctetString"
_PortServiceLabel_Object = MibTableColumn
portServiceLabel = _PortServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 23),
    _PortServiceLabel_Type()
)
portServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portServiceLabel.setStatus("current")


class _PortConnectedTo_Type(OctetString):
    """Custom type portConnectedTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortConnectedTo_Type.__name__ = "OctetString"
_PortConnectedTo_Object = MibTableColumn
portConnectedTo = _PortConnectedTo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 24),
    _PortConnectedTo_Type()
)
portConnectedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConnectedTo.setStatus("current")


class _PortArcConfig_Type(Integer32):
    """Custom type portArcConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alm", 1),
          ("nalmQi", 2),
          ("nalm", 3))
    )


_PortArcConfig_Type.__name__ = "Integer32"
_PortArcConfig_Object = MibTableColumn
portArcConfig = _PortArcConfig_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 25),
    _PortArcConfig_Type()
)
portArcConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portArcConfig.setStatus("current")


class _PortArcState_Type(Integer32):
    """Custom type portArcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alm", 1),
          ("nalmQi", 2),
          ("nalm", 3))
    )


_PortArcState_Type.__name__ = "Integer32"
_PortArcState_Object = MibTableColumn
portArcState = _PortArcState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 26),
    _PortArcState_Type()
)
portArcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portArcState.setStatus("current")


class _PortArcSubState_Type(Integer32):
    """Custom type portArcSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nalmCd", 1),
          ("nalmNr", 2))
    )


_PortArcSubState_Type.__name__ = "Integer32"
_PortArcSubState_Object = MibTableColumn
portArcSubState = _PortArcSubState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 27),
    _PortArcSubState_Type()
)
portArcSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portArcSubState.setStatus("current")


class _PortArcTimer_Type(Unsigned32):
    """Custom type portArcTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_PortArcTimer_Type.__name__ = "Unsigned32"
_PortArcTimer_Object = MibTableColumn
portArcTimer = _PortArcTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 28),
    _PortArcTimer_Type()
)
portArcTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portArcTimer.setStatus("current")
_PortArcRemainingTime_Type = OctetString
_PortArcRemainingTime_Object = MibTableColumn
portArcRemainingTime = _PortArcRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 29),
    _PortArcRemainingTime_Type()
)
portArcRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portArcRemainingTime.setStatus("current")
_PortExternalConnectivity_Type = CoriantTypesYesNo
_PortExternalConnectivity_Object = MibTableColumn
portExternalConnectivity = _PortExternalConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 6, 1, 1, 30),
    _PortExternalConnectivity_Type()
)
portExternalConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portExternalConnectivity.setStatus("current")
_Subport_ObjectIdentity = ObjectIdentity
subport = _Subport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7)
)
_SubportTable_Object = MibTable
subportTable = _SubportTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    subportTable.setStatus("current")
_SubportEntry_Object = MibTableRow
subportEntry = _SubportEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1)
)
subportEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    subportEntry.setStatus("current")
_SubportId_Type = CoriantTypesPortId
_SubportId_Object = MibTableColumn
subportId = _SubportId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 1),
    _SubportId_Type()
)
subportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportId.setStatus("current")
_SubportPortName_Type = CoriantTypesNameIdentifier
_SubportPortName_Object = MibTableColumn
subportPortName = _SubportPortName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 2),
    _SubportPortName_Type()
)
subportPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportPortName.setStatus("current")


class _SubportPortType_Type(Integer32):
    """Custom type subportPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("line", 2),
          ("clientSubport", 3),
          ("optical", 4),
          ("otdr", 5),
          ("opticalNomon", 6))
    )


_SubportPortType_Type.__name__ = "Integer32"
_SubportPortType_Object = MibTableColumn
subportPortType = _SubportPortType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 3),
    _SubportPortType_Type()
)
subportPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportPortType.setStatus("current")
_SubportPortMode_Type = CoriantTypesPortMode
_SubportPortMode_Object = MibTableColumn
subportPortMode = _SubportPortMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 4),
    _SubportPortMode_Type()
)
subportPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportPortMode.setStatus("current")


class _SubportAdminStatus_Type(Integer32):
    """Custom type subportAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SubportAdminStatus_Type.__name__ = "Integer32"
_SubportAdminStatus_Object = MibTableColumn
subportAdminStatus = _SubportAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 5),
    _SubportAdminStatus_Type()
)
subportAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportAdminStatus.setStatus("current")


class _SubportOperStatus_Type(Integer32):
    """Custom type subportOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SubportOperStatus_Type.__name__ = "Integer32"
_SubportOperStatus_Object = MibTableColumn
subportOperStatus = _SubportOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 6),
    _SubportOperStatus_Type()
)
subportOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportOperStatus.setStatus("current")


class _SubportAvailStatus_Type(Bits):
    """Custom type subportAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_SubportAvailStatus_Type.__name__ = "Bits"
_SubportAvailStatus_Object = MibTableColumn
subportAvailStatus = _SubportAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 7),
    _SubportAvailStatus_Type()
)
subportAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportAvailStatus.setStatus("current")


class _SubportAliasName_Type(OctetString):
    """Custom type subportAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SubportAliasName_Type.__name__ = "OctetString"
_SubportAliasName_Object = MibTableColumn
subportAliasName = _SubportAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 8),
    _SubportAliasName_Type()
)
subportAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportAliasName.setStatus("current")


class _SubportServiceLabel_Type(OctetString):
    """Custom type subportServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SubportServiceLabel_Type.__name__ = "OctetString"
_SubportServiceLabel_Object = MibTableColumn
subportServiceLabel = _SubportServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 9),
    _SubportServiceLabel_Type()
)
subportServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportServiceLabel.setStatus("current")


class _SubportConnectedTo_Type(OctetString):
    """Custom type subportConnectedTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SubportConnectedTo_Type.__name__ = "OctetString"
_SubportConnectedTo_Object = MibTableColumn
subportConnectedTo = _SubportConnectedTo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 10),
    _SubportConnectedTo_Type()
)
subportConnectedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportConnectedTo.setStatus("current")


class _SubportArcConfig_Type(Integer32):
    """Custom type subportArcConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alm", 1),
          ("nalmQi", 2),
          ("nalm", 3))
    )


_SubportArcConfig_Type.__name__ = "Integer32"
_SubportArcConfig_Object = MibTableColumn
subportArcConfig = _SubportArcConfig_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 11),
    _SubportArcConfig_Type()
)
subportArcConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportArcConfig.setStatus("current")


class _SubportArcState_Type(Integer32):
    """Custom type subportArcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alm", 1),
          ("nalmQi", 2),
          ("nalm", 3))
    )


_SubportArcState_Type.__name__ = "Integer32"
_SubportArcState_Object = MibTableColumn
subportArcState = _SubportArcState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 12),
    _SubportArcState_Type()
)
subportArcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportArcState.setStatus("current")


class _SubportArcSubState_Type(Integer32):
    """Custom type subportArcSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nalmCd", 1),
          ("nalmNr", 2))
    )


_SubportArcSubState_Type.__name__ = "Integer32"
_SubportArcSubState_Object = MibTableColumn
subportArcSubState = _SubportArcSubState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 13),
    _SubportArcSubState_Type()
)
subportArcSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportArcSubState.setStatus("current")


class _SubportArcTimer_Type(Unsigned32):
    """Custom type subportArcTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_SubportArcTimer_Type.__name__ = "Unsigned32"
_SubportArcTimer_Object = MibTableColumn
subportArcTimer = _SubportArcTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 14),
    _SubportArcTimer_Type()
)
subportArcTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportArcTimer.setStatus("current")
_SubportArcRemainingTime_Type = OctetString
_SubportArcRemainingTime_Object = MibTableColumn
subportArcRemainingTime = _SubportArcRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 15),
    _SubportArcRemainingTime_Type()
)
subportArcRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportArcRemainingTime.setStatus("current")
_SubportRxOpticalPower_Type = CoriantTypesOpticalPower
_SubportRxOpticalPower_Object = MibTableColumn
subportRxOpticalPower = _SubportRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 16),
    _SubportRxOpticalPower_Type()
)
subportRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportRxOpticalPower.setStatus("current")
_SubportTxOpticalPower_Type = CoriantTypesOpticalPower
_SubportTxOpticalPower_Object = MibTableColumn
subportTxOpticalPower = _SubportTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 17),
    _SubportTxOpticalPower_Type()
)
subportTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportTxOpticalPower.setStatus("current")
_SubportExternalConnectivity_Type = CoriantTypesYesNo
_SubportExternalConnectivity_Object = MibTableColumn
subportExternalConnectivity = _SubportExternalConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 7, 1, 1, 18),
    _SubportExternalConnectivity_Type()
)
subportExternalConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportExternalConnectivity.setStatus("current")
_Pluggable_ObjectIdentity = ObjectIdentity
pluggable = _Pluggable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8)
)
_PluggableTable_Object = MibTable
pluggableTable = _PluggableTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    pluggableTable.setStatus("current")
_PluggableEntry_Object = MibTableRow
pluggableEntry = _PluggableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1)
)
pluggableEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    pluggableEntry.setStatus("current")
_PluggableRequiredType_Type = CoriantTypesPluggableType
_PluggableRequiredType_Object = MibTableColumn
pluggableRequiredType = _PluggableRequiredType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 1),
    _PluggableRequiredType_Type()
)
pluggableRequiredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableRequiredType.setStatus("current")
_PluggableFormFactor_Type = CoriantTypesPluggableFormFactor
_PluggableFormFactor_Object = MibTableColumn
pluggableFormFactor = _PluggableFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 2),
    _PluggableFormFactor_Type()
)
pluggableFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableFormFactor.setStatus("current")


class _PluggableInterfaceType_Type(OctetString):
    """Custom type pluggableInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PluggableInterfaceType_Type.__name__ = "OctetString"
_PluggableInterfaceType_Object = MibTableColumn
pluggableInterfaceType = _PluggableInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 3),
    _PluggableInterfaceType_Type()
)
pluggableInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableInterfaceType.setStatus("current")


class _PluggableLaserSource_Type(Integer32):
    """Custom type pluggableLaserSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txLoShared", 1),
          ("txLoIndependent", 2),
          ("notAvailable", 3))
    )


_PluggableLaserSource_Type.__name__ = "Integer32"
_PluggableLaserSource_Object = MibTableColumn
pluggableLaserSource = _PluggableLaserSource_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 4),
    _PluggableLaserSource_Type()
)
pluggableLaserSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableLaserSource.setStatus("current")


class _PluggableHwVersion_Type(OctetString):
    """Custom type pluggableHwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PluggableHwVersion_Type.__name__ = "OctetString"
_PluggableHwVersion_Object = MibTableColumn
pluggableHwVersion = _PluggableHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 5),
    _PluggableHwVersion_Type()
)
pluggableHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableHwVersion.setStatus("current")


class _PluggableVendor_Type(OctetString):
    """Custom type pluggableVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PluggableVendor_Type.__name__ = "OctetString"
_PluggableVendor_Object = MibTableColumn
pluggableVendor = _PluggableVendor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 6),
    _PluggableVendor_Type()
)
pluggableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableVendor.setStatus("current")


class _PluggableSerialNumber_Type(OctetString):
    """Custom type pluggableSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_PluggableSerialNumber_Type.__name__ = "OctetString"
_PluggableSerialNumber_Object = MibTableColumn
pluggableSerialNumber = _PluggableSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 7),
    _PluggableSerialNumber_Type()
)
pluggableSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableSerialNumber.setStatus("current")


class _PluggableFwVersion_Type(OctetString):
    """Custom type pluggableFwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PluggableFwVersion_Type.__name__ = "OctetString"
_PluggableFwVersion_Object = MibTableColumn
pluggableFwVersion = _PluggableFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 8),
    _PluggableFwVersion_Type()
)
pluggableFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableFwVersion.setStatus("current")


class _PluggablePartNumber_Type(OctetString):
    """Custom type pluggablePartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_PluggablePartNumber_Type.__name__ = "OctetString"
_PluggablePartNumber_Object = MibTableColumn
pluggablePartNumber = _PluggablePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 9),
    _PluggablePartNumber_Type()
)
pluggablePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggablePartNumber.setStatus("current")


class _PluggableClei_Type(OctetString):
    """Custom type pluggableClei based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_PluggableClei_Type.__name__ = "OctetString"
_PluggableClei_Object = MibTableColumn
pluggableClei = _PluggableClei_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 10),
    _PluggableClei_Type()
)
pluggableClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableClei.setStatus("current")


class _PluggableEquipmentName_Type(OctetString):
    """Custom type pluggableEquipmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PluggableEquipmentName_Type.__name__ = "OctetString"
_PluggableEquipmentName_Object = MibTableColumn
pluggableEquipmentName = _PluggableEquipmentName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 11),
    _PluggableEquipmentName_Type()
)
pluggableEquipmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableEquipmentName.setStatus("current")


class _PluggableAdminStatus_Type(Integer32):
    """Custom type pluggableAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PluggableAdminStatus_Type.__name__ = "Integer32"
_PluggableAdminStatus_Object = MibTableColumn
pluggableAdminStatus = _PluggableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 12),
    _PluggableAdminStatus_Type()
)
pluggableAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableAdminStatus.setStatus("current")


class _PluggableOperStatus_Type(Integer32):
    """Custom type pluggableOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PluggableOperStatus_Type.__name__ = "Integer32"
_PluggableOperStatus_Object = MibTableColumn
pluggableOperStatus = _PluggableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 13),
    _PluggableOperStatus_Type()
)
pluggableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableOperStatus.setStatus("current")


class _PluggableAvailStatus_Type(Bits):
    """Custom type pluggableAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_PluggableAvailStatus_Type.__name__ = "Bits"
_PluggableAvailStatus_Object = MibTableColumn
pluggableAvailStatus = _PluggableAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 14),
    _PluggableAvailStatus_Type()
)
pluggableAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableAvailStatus.setStatus("current")


class _PluggableAliasName_Type(OctetString):
    """Custom type pluggableAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PluggableAliasName_Type.__name__ = "OctetString"
_PluggableAliasName_Object = MibTableColumn
pluggableAliasName = _PluggableAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 15),
    _PluggableAliasName_Type()
)
pluggableAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableAliasName.setStatus("current")
_PluggableTemperature_Type = CoriantTypesTemperature
_PluggableTemperature_Object = MibTableColumn
pluggableTemperature = _PluggableTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 8, 1, 1, 16),
    _PluggableTemperature_Type()
)
pluggableTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pluggableTemperature.setStatus("current")
_Amplifier_ObjectIdentity = ObjectIdentity
amplifier = _Amplifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9)
)
_AmplifierTable_Object = MibTable
amplifierTable = _AmplifierTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    amplifierTable.setStatus("current")
_AmplifierEntry_Object = MibTableRow
amplifierEntry = _AmplifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1)
)
amplifierEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "amplifierName"),
)
if mibBuilder.loadTexts:
    amplifierEntry.setStatus("current")
_AmplifierName_Type = CoriantTypesNameIdentifier
_AmplifierName_Object = MibTableColumn
amplifierName = _AmplifierName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 1),
    _AmplifierName_Type()
)
amplifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierName.setStatus("current")
_AmplifierSupportingInputPort_Type = RowPointer
_AmplifierSupportingInputPort_Object = MibTableColumn
amplifierSupportingInputPort = _AmplifierSupportingInputPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 2),
    _AmplifierSupportingInputPort_Type()
)
amplifierSupportingInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierSupportingInputPort.setStatus("current")
_AmplifierSupportingOutputPort_Type = RowPointer
_AmplifierSupportingOutputPort_Object = MibTableColumn
amplifierSupportingOutputPort = _AmplifierSupportingOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 3),
    _AmplifierSupportingOutputPort_Type()
)
amplifierSupportingOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierSupportingOutputPort.setStatus("current")


class _AmplifierAdminStatus_Type(Integer32):
    """Custom type amplifierAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AmplifierAdminStatus_Type.__name__ = "Integer32"
_AmplifierAdminStatus_Object = MibTableColumn
amplifierAdminStatus = _AmplifierAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 4),
    _AmplifierAdminStatus_Type()
)
amplifierAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierAdminStatus.setStatus("current")


class _AmplifierOperStatus_Type(Integer32):
    """Custom type amplifierOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AmplifierOperStatus_Type.__name__ = "Integer32"
_AmplifierOperStatus_Object = MibTableColumn
amplifierOperStatus = _AmplifierOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 5),
    _AmplifierOperStatus_Type()
)
amplifierOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierOperStatus.setStatus("current")


class _AmplifierAvailStatus_Type(Bits):
    """Custom type amplifierAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_AmplifierAvailStatus_Type.__name__ = "Bits"
_AmplifierAvailStatus_Object = MibTableColumn
amplifierAvailStatus = _AmplifierAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 6),
    _AmplifierAvailStatus_Type()
)
amplifierAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierAvailStatus.setStatus("current")


class _AmplifierAliasName_Type(OctetString):
    """Custom type amplifierAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AmplifierAliasName_Type.__name__ = "OctetString"
_AmplifierAliasName_Object = MibTableColumn
amplifierAliasName = _AmplifierAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 7),
    _AmplifierAliasName_Type()
)
amplifierAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierAliasName.setStatus("current")
_AmplifierEnable_Type = CoriantTypesEnableSwitch
_AmplifierEnable_Object = MibTableColumn
amplifierEnable = _AmplifierEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 8),
    _AmplifierEnable_Type()
)
amplifierEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierEnable.setStatus("current")
_AmplifierInputLosShutdown_Type = CoriantTypesEnableSwitch
_AmplifierInputLosShutdown_Object = MibTableColumn
amplifierInputLosShutdown = _AmplifierInputLosShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 9),
    _AmplifierInputLosShutdown_Type()
)
amplifierInputLosShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierInputLosShutdown.setStatus("current")


class _AmplifierControlMode_Type(Integer32):
    """Custom type amplifierControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )


_AmplifierControlMode_Type.__name__ = "Integer32"
_AmplifierControlMode_Object = MibTableColumn
amplifierControlMode = _AmplifierControlMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 10),
    _AmplifierControlMode_Type()
)
amplifierControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierControlMode.setStatus("current")


class _AmplifierMode_Type(Integer32):
    """Custom type amplifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constantPower", 1),
          ("constantGain", 2))
    )


_AmplifierMode_Type.__name__ = "Integer32"
_AmplifierMode_Object = MibTableColumn
amplifierMode = _AmplifierMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 11),
    _AmplifierMode_Type()
)
amplifierMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierMode.setStatus("current")


class _AmplifierType_Type(Integer32):
    """Custom type amplifierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixedGainEdfa", 1),
          ("variableGainEdfa", 2))
    )


_AmplifierType_Type.__name__ = "Integer32"
_AmplifierType_Object = MibTableColumn
amplifierType = _AmplifierType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 12),
    _AmplifierType_Type()
)
amplifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierType.setStatus("current")
_AmplifierTargetGain_Type = CoriantTypesOpticalDB
_AmplifierTargetGain_Object = MibTableColumn
amplifierTargetGain = _AmplifierTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 13),
    _AmplifierTargetGain_Type()
)
amplifierTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierTargetGain.setStatus("current")
_AmplifierOperatingGain_Type = CoriantTypesOpticalDB
_AmplifierOperatingGain_Object = MibTableColumn
amplifierOperatingGain = _AmplifierOperatingGain_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 14),
    _AmplifierOperatingGain_Type()
)
amplifierOperatingGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierOperatingGain.setStatus("current")
_AmplifierGainAdjustment_Type = CoriantTypesOpticalDB
_AmplifierGainAdjustment_Object = MibTableColumn
amplifierGainAdjustment = _AmplifierGainAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 15),
    _AmplifierGainAdjustment_Type()
)
amplifierGainAdjustment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierGainAdjustment.setStatus("current")
_AmplifierGainRangeMin_Type = CoriantTypesOpticalDB
_AmplifierGainRangeMin_Object = MibTableColumn
amplifierGainRangeMin = _AmplifierGainRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 16),
    _AmplifierGainRangeMin_Type()
)
amplifierGainRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierGainRangeMin.setStatus("current")
_AmplifierGainRangeMax_Type = CoriantTypesOpticalPower
_AmplifierGainRangeMax_Object = MibTableColumn
amplifierGainRangeMax = _AmplifierGainRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 17),
    _AmplifierGainRangeMax_Type()
)
amplifierGainRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierGainRangeMax.setStatus("current")
_AmplifierOutputPowerMon_Type = CoriantTypesOpticalPower
_AmplifierOutputPowerMon_Object = MibTableColumn
amplifierOutputPowerMon = _AmplifierOutputPowerMon_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 18),
    _AmplifierOutputPowerMon_Type()
)
amplifierOutputPowerMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierOutputPowerMon.setStatus("current")
_AmplifierOutputPowerMonWithAse_Type = CoriantTypesOpticalPower
_AmplifierOutputPowerMonWithAse_Object = MibTableColumn
amplifierOutputPowerMonWithAse = _AmplifierOutputPowerMonWithAse_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 19),
    _AmplifierOutputPowerMonWithAse_Type()
)
amplifierOutputPowerMonWithAse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierOutputPowerMonWithAse.setStatus("current")
_AmplifierInputPowerMon_Type = CoriantTypesOpticalPower
_AmplifierInputPowerMon_Object = MibTableColumn
amplifierInputPowerMon = _AmplifierInputPowerMon_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 20),
    _AmplifierInputPowerMon_Type()
)
amplifierInputPowerMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierInputPowerMon.setStatus("current")
_AmplifierOutputVoa_Type = CoriantTypesOpticalDB
_AmplifierOutputVoa_Object = MibTableColumn
amplifierOutputVoa = _AmplifierOutputVoa_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 21),
    _AmplifierOutputVoa_Type()
)
amplifierOutputVoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierOutputVoa.setStatus("current")
_AmplifierPowerBeforeOutputVoa_Type = CoriantTypesOpticalPower
_AmplifierPowerBeforeOutputVoa_Object = MibTableColumn
amplifierPowerBeforeOutputVoa = _AmplifierPowerBeforeOutputVoa_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 9, 1, 1, 22),
    _AmplifierPowerBeforeOutputVoa_Type()
)
amplifierPowerBeforeOutputVoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifierPowerBeforeOutputVoa.setStatus("current")
_Tdc_ObjectIdentity = ObjectIdentity
tdc = _Tdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10)
)
_TdcTable_Object = MibTable
tdcTable = _TdcTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1)
)
if mibBuilder.loadTexts:
    tdcTable.setStatus("current")
_TdcEntry_Object = MibTableRow
tdcEntry = _TdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1)
)
tdcEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "tdcName"),
)
if mibBuilder.loadTexts:
    tdcEntry.setStatus("current")
_TdcName_Type = CoriantTypesNameIdentifier
_TdcName_Object = MibTableColumn
tdcName = _TdcName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 1),
    _TdcName_Type()
)
tdcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcName.setStatus("current")
_TdcSupportingInputPort_Type = RowPointer
_TdcSupportingInputPort_Object = MibTableColumn
tdcSupportingInputPort = _TdcSupportingInputPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 2),
    _TdcSupportingInputPort_Type()
)
tdcSupportingInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcSupportingInputPort.setStatus("current")
_TdcSupportingOutputPort_Type = RowPointer
_TdcSupportingOutputPort_Object = MibTableColumn
tdcSupportingOutputPort = _TdcSupportingOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 3),
    _TdcSupportingOutputPort_Type()
)
tdcSupportingOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcSupportingOutputPort.setStatus("current")


class _TdcAdminStatus_Type(Integer32):
    """Custom type tdcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TdcAdminStatus_Type.__name__ = "Integer32"
_TdcAdminStatus_Object = MibTableColumn
tdcAdminStatus = _TdcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 4),
    _TdcAdminStatus_Type()
)
tdcAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcAdminStatus.setStatus("current")


class _TdcOperStatus_Type(Integer32):
    """Custom type tdcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TdcOperStatus_Type.__name__ = "Integer32"
_TdcOperStatus_Object = MibTableColumn
tdcOperStatus = _TdcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 5),
    _TdcOperStatus_Type()
)
tdcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcOperStatus.setStatus("current")


class _TdcAvailStatus_Type(Bits):
    """Custom type tdcAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_TdcAvailStatus_Type.__name__ = "Bits"
_TdcAvailStatus_Object = MibTableColumn
tdcAvailStatus = _TdcAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 6),
    _TdcAvailStatus_Type()
)
tdcAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcAvailStatus.setStatus("current")


class _TdcAliasName_Type(OctetString):
    """Custom type tdcAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TdcAliasName_Type.__name__ = "OctetString"
_TdcAliasName_Object = MibTableColumn
tdcAliasName = _TdcAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 7),
    _TdcAliasName_Type()
)
tdcAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcAliasName.setStatus("current")


class _TdcMode_Type(Integer32):
    """Custom type tdcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )


_TdcMode_Type.__name__ = "Integer32"
_TdcMode_Object = MibTableColumn
tdcMode = _TdcMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 8),
    _TdcMode_Type()
)
tdcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcMode.setStatus("current")
_TdcReferenceFrequency_Type = CoriantTypesFreq
_TdcReferenceFrequency_Object = MibTableColumn
tdcReferenceFrequency = _TdcReferenceFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 9),
    _TdcReferenceFrequency_Type()
)
tdcReferenceFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcReferenceFrequency.setStatus("current")
_TdcActualReferenceFrequency_Type = Unsigned32
_TdcActualReferenceFrequency_Object = MibTableColumn
tdcActualReferenceFrequency = _TdcActualReferenceFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 10),
    _TdcActualReferenceFrequency_Type()
)
tdcActualReferenceFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcActualReferenceFrequency.setStatus("current")
_TdcFrequencyRangeMin_Type = Unsigned32
_TdcFrequencyRangeMin_Object = MibTableColumn
tdcFrequencyRangeMin = _TdcFrequencyRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 11),
    _TdcFrequencyRangeMin_Type()
)
tdcFrequencyRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcFrequencyRangeMin.setStatus("current")
_TdcFrequencyRangeMax_Type = Unsigned32
_TdcFrequencyRangeMax_Object = MibTableColumn
tdcFrequencyRangeMax = _TdcFrequencyRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 12),
    _TdcFrequencyRangeMax_Type()
)
tdcFrequencyRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcFrequencyRangeMax.setStatus("current")
_TdcChromaticDispersion_Type = Integer32
_TdcChromaticDispersion_Object = MibTableColumn
tdcChromaticDispersion = _TdcChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 13),
    _TdcChromaticDispersion_Type()
)
tdcChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcChromaticDispersion.setStatus("current")
_TdcChromaticDispersionAdjustment_Type = Integer32
_TdcChromaticDispersionAdjustment_Object = MibTableColumn
tdcChromaticDispersionAdjustment = _TdcChromaticDispersionAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 14),
    _TdcChromaticDispersionAdjustment_Type()
)
tdcChromaticDispersionAdjustment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcChromaticDispersionAdjustment.setStatus("current")
_TdcActualChromaticDispersion_Type = Integer32
_TdcActualChromaticDispersion_Object = MibTableColumn
tdcActualChromaticDispersion = _TdcActualChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 15),
    _TdcActualChromaticDispersion_Type()
)
tdcActualChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcActualChromaticDispersion.setStatus("current")
_TdcCdRangeMin_Type = Integer32
_TdcCdRangeMin_Object = MibTableColumn
tdcCdRangeMin = _TdcCdRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 16),
    _TdcCdRangeMin_Type()
)
tdcCdRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcCdRangeMin.setStatus("current")
_TdcCdRangeMax_Type = Integer32
_TdcCdRangeMax_Object = MibTableColumn
tdcCdRangeMax = _TdcCdRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 10, 1, 1, 17),
    _TdcCdRangeMax_Type()
)
tdcCdRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdcCdRangeMax.setStatus("current")
_Inventory_ObjectIdentity = ObjectIdentity
inventory = _Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12)
)
_InventoryTable_Object = MibTable
inventoryTable = _InventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1)
)
if mibBuilder.loadTexts:
    inventoryTable.setStatus("current")
_InventoryEntry_Object = MibTableRow
inventoryEntry = _InventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1)
)
inventoryEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "inventoryEquipmentType"),
    (0, "CORIANT-GROOVE-MIB", "inventoryShelfId"),
    (0, "CORIANT-GROOVE-MIB", "inventorySlotId"),
    (0, "CORIANT-GROOVE-MIB", "inventorySubslotId"),
    (0, "CORIANT-GROOVE-MIB", "inventoryPortId"),
)
if mibBuilder.loadTexts:
    inventoryEntry.setStatus("current")


class _InventoryEquipmentType_Type(Integer32):
    """Custom type inventoryEquipmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("shelf", 1),
          ("slot", 2),
          ("card", 3),
          ("port", 4),
          ("pluggable", 5),
          ("subslot", 6),
          ("subcard", 7))
    )


_InventoryEquipmentType_Type.__name__ = "Integer32"
_InventoryEquipmentType_Object = MibTableColumn
inventoryEquipmentType = _InventoryEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 1),
    _InventoryEquipmentType_Type()
)
inventoryEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryEquipmentType.setStatus("current")
_InventoryShelfId_Type = CoriantTypesShelfId
_InventoryShelfId_Object = MibTableColumn
inventoryShelfId = _InventoryShelfId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 2),
    _InventoryShelfId_Type()
)
inventoryShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryShelfId.setStatus("current")
_InventorySlotId_Type = CoriantTypesSlotId
_InventorySlotId_Object = MibTableColumn
inventorySlotId = _InventorySlotId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 3),
    _InventorySlotId_Type()
)
inventorySlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySlotId.setStatus("current")
_InventorySubslotId_Type = CoriantTypesSlotId
_InventorySubslotId_Object = MibTableColumn
inventorySubslotId = _InventorySubslotId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 4),
    _InventorySubslotId_Type()
)
inventorySubslotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySubslotId.setStatus("current")
_InventoryPortId_Type = CoriantTypesPortId
_InventoryPortId_Object = MibTableColumn
inventoryPortId = _InventoryPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 5),
    _InventoryPortId_Type()
)
inventoryPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryPortId.setStatus("current")


class _InventoryEquipmentVersion_Type(OctetString):
    """Custom type inventoryEquipmentVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InventoryEquipmentVersion_Type.__name__ = "OctetString"
_InventoryEquipmentVersion_Object = MibTableColumn
inventoryEquipmentVersion = _InventoryEquipmentVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 6),
    _InventoryEquipmentVersion_Type()
)
inventoryEquipmentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryEquipmentVersion.setStatus("current")


class _InventoryModuleType_Type(OctetString):
    """Custom type inventoryModuleType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_InventoryModuleType_Type.__name__ = "OctetString"
_InventoryModuleType_Object = MibTableColumn
inventoryModuleType = _InventoryModuleType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 7),
    _InventoryModuleType_Type()
)
inventoryModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryModuleType.setStatus("current")


class _InventoryVendor_Type(OctetString):
    """Custom type inventoryVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_InventoryVendor_Type.__name__ = "OctetString"
_InventoryVendor_Object = MibTableColumn
inventoryVendor = _InventoryVendor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 8),
    _InventoryVendor_Type()
)
inventoryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryVendor.setStatus("current")


class _InventorySerialNumber_Type(OctetString):
    """Custom type inventorySerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InventorySerialNumber_Type.__name__ = "OctetString"
_InventorySerialNumber_Object = MibTableColumn
inventorySerialNumber = _InventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 9),
    _InventorySerialNumber_Type()
)
inventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySerialNumber.setStatus("current")


class _InventoryFwVersion_Type(OctetString):
    """Custom type inventoryFwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InventoryFwVersion_Type.__name__ = "OctetString"
_InventoryFwVersion_Object = MibTableColumn
inventoryFwVersion = _InventoryFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 10),
    _InventoryFwVersion_Type()
)
inventoryFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryFwVersion.setStatus("current")


class _InventoryPartNumber_Type(OctetString):
    """Custom type inventoryPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_InventoryPartNumber_Type.__name__ = "OctetString"
_InventoryPartNumber_Object = MibTableColumn
inventoryPartNumber = _InventoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 11),
    _InventoryPartNumber_Type()
)
inventoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryPartNumber.setStatus("current")


class _InventoryClei_Type(OctetString):
    """Custom type inventoryClei based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_InventoryClei_Type.__name__ = "OctetString"
_InventoryClei_Object = MibTableColumn
inventoryClei = _InventoryClei_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 12),
    _InventoryClei_Type()
)
inventoryClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryClei.setStatus("current")


class _InventoryInterfaceType_Type(OctetString):
    """Custom type inventoryInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_InventoryInterfaceType_Type.__name__ = "OctetString"
_InventoryInterfaceType_Object = MibTableColumn
inventoryInterfaceType = _InventoryInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 13),
    _InventoryInterfaceType_Type()
)
inventoryInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryInterfaceType.setStatus("current")
_InventoryManufactureDate_Type = OctetString
_InventoryManufactureDate_Object = MibTableColumn
inventoryManufactureDate = _InventoryManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 14),
    _InventoryManufactureDate_Type()
)
inventoryManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryManufactureDate.setStatus("current")


class _InventoryManufacturerNumber_Type(OctetString):
    """Custom type inventoryManufacturerNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_InventoryManufacturerNumber_Type.__name__ = "OctetString"
_InventoryManufacturerNumber_Object = MibTableColumn
inventoryManufacturerNumber = _InventoryManufacturerNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 12, 1, 1, 16),
    _InventoryManufacturerNumber_Type()
)
inventoryManufacturerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryManufacturerNumber.setStatus("current")
_Led_ObjectIdentity = ObjectIdentity
led = _Led_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14)
)
_LedTable_Object = MibTable
ledTable = _LedTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1)
)
if mibBuilder.loadTexts:
    ledTable.setStatus("current")
_LedEntry_Object = MibTableRow
ledEntry = _LedEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1, 1)
)
ledEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "ledEquipmentType"),
    (0, "CORIANT-GROOVE-MIB", "ledShelfId"),
    (0, "CORIANT-GROOVE-MIB", "ledSlotId"),
    (0, "CORIANT-GROOVE-MIB", "ledSubslotId"),
    (0, "CORIANT-GROOVE-MIB", "ledName"),
)
if mibBuilder.loadTexts:
    ledEntry.setStatus("current")


class _LedEquipmentType_Type(OctetString):
    """Custom type ledEquipmentType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LedEquipmentType_Type.__name__ = "OctetString"
_LedEquipmentType_Object = MibTableColumn
ledEquipmentType = _LedEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1, 1, 1),
    _LedEquipmentType_Type()
)
ledEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledEquipmentType.setStatus("current")
_LedShelfId_Type = CoriantTypesShelfId
_LedShelfId_Object = MibTableColumn
ledShelfId = _LedShelfId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1, 1, 2),
    _LedShelfId_Type()
)
ledShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledShelfId.setStatus("current")
_LedSlotId_Type = CoriantTypesSlotId
_LedSlotId_Object = MibTableColumn
ledSlotId = _LedSlotId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1, 1, 3),
    _LedSlotId_Type()
)
ledSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledSlotId.setStatus("current")


class _LedName_Type(OctetString):
    """Custom type ledName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LedName_Type.__name__ = "OctetString"
_LedName_Object = MibTableColumn
ledName = _LedName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1, 1, 4),
    _LedName_Type()
)
ledName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledName.setStatus("current")


class _LedStatus_Type(Integer32):
    """Custom type ledStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("off", 2),
          ("blink", 3),
          ("red", 4),
          ("redBlink", 5),
          ("green", 6),
          ("greenBlink", 7),
          ("amber", 8),
          ("amberBlink", 9))
    )


_LedStatus_Type.__name__ = "Integer32"
_LedStatus_Object = MibTableColumn
ledStatus = _LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1, 1, 5),
    _LedStatus_Type()
)
ledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledStatus.setStatus("current")
_LedSubslotId_Type = CoriantTypesSubslotId
_LedSubslotId_Object = MibTableColumn
ledSubslotId = _LedSubslotId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 14, 1, 1, 6),
    _LedSubslotId_Type()
)
ledSubslotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledSubslotId.setStatus("current")
_TemperatureDetails_ObjectIdentity = ObjectIdentity
temperatureDetails = _TemperatureDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 15)
)
_TemperatureDetailsTable_Object = MibTable
temperatureDetailsTable = _TemperatureDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 15, 1)
)
if mibBuilder.loadTexts:
    temperatureDetailsTable.setStatus("current")
_TemperatureDetailsEntry_Object = MibTableRow
temperatureDetailsEntry = _TemperatureDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 15, 1, 1)
)
temperatureDetailsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "temperatureDetailsMonitoringPoint"),
)
if mibBuilder.loadTexts:
    temperatureDetailsEntry.setStatus("current")


class _TemperatureDetailsMonitoringPoint_Type(OctetString):
    """Custom type temperatureDetailsMonitoringPoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TemperatureDetailsMonitoringPoint_Type.__name__ = "OctetString"
_TemperatureDetailsMonitoringPoint_Object = MibTableColumn
temperatureDetailsMonitoringPoint = _TemperatureDetailsMonitoringPoint_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 15, 1, 1, 1),
    _TemperatureDetailsMonitoringPoint_Type()
)
temperatureDetailsMonitoringPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDetailsMonitoringPoint.setStatus("current")
_TemperatureDetailsTemperature_Type = CoriantTypesTemperature
_TemperatureDetailsTemperature_Object = MibTableColumn
temperatureDetailsTemperature = _TemperatureDetailsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 15, 1, 1, 2),
    _TemperatureDetailsTemperature_Type()
)
temperatureDetailsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDetailsTemperature.setStatus("current")
_TemperatureDetailsTemperatureRangeLow_Type = CoriantTypesTemperature
_TemperatureDetailsTemperatureRangeLow_Object = MibTableColumn
temperatureDetailsTemperatureRangeLow = _TemperatureDetailsTemperatureRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 15, 1, 1, 3),
    _TemperatureDetailsTemperatureRangeLow_Type()
)
temperatureDetailsTemperatureRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDetailsTemperatureRangeLow.setStatus("current")
_TemperatureDetailsTemperatureRangeHigh_Type = CoriantTypesTemperature
_TemperatureDetailsTemperatureRangeHigh_Object = MibTableColumn
temperatureDetailsTemperatureRangeHigh = _TemperatureDetailsTemperatureRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 15, 1, 1, 4),
    _TemperatureDetailsTemperatureRangeHigh_Type()
)
temperatureDetailsTemperatureRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDetailsTemperatureRangeHigh.setStatus("current")
_Otdr_ObjectIdentity = ObjectIdentity
otdr = _Otdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16)
)
_OtdrTable_Object = MibTable
otdrTable = _OtdrTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16, 1)
)
if mibBuilder.loadTexts:
    otdrTable.setStatus("current")
_OtdrEntry_Object = MibTableRow
otdrEntry = _OtdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16, 1, 1)
)
otdrEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
)
if mibBuilder.loadTexts:
    otdrEntry.setStatus("current")


class _OtdrState_Type(Integer32):
    """Custom type otdrState based on Integer32"""
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
        *(("notAvailable", 0),
          ("idle", 1),
          ("measuring", 2),
          ("finished", 3),
          ("fail", 4))
    )


_OtdrState_Type.__name__ = "Integer32"
_OtdrState_Object = MibTableColumn
otdrState = _OtdrState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16, 1, 1, 1),
    _OtdrState_Type()
)
otdrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrState.setStatus("current")
_OtdrMeasurementTime_Type = Unsigned32
_OtdrMeasurementTime_Object = MibTableColumn
otdrMeasurementTime = _OtdrMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16, 1, 1, 2),
    _OtdrMeasurementTime_Type()
)
otdrMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrMeasurementTime.setStatus("current")


class _OtdrError_Type(OctetString):
    """Custom type otdrError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OtdrError_Type.__name__ = "OctetString"
_OtdrError_Object = MibTableColumn
otdrError = _OtdrError_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16, 1, 1, 3),
    _OtdrError_Type()
)
otdrError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrError.setStatus("current")


class _OtdrLaserStatus_Type(Integer32):
    """Custom type otdrLaserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_OtdrLaserStatus_Type.__name__ = "Integer32"
_OtdrLaserStatus_Object = MibTableColumn
otdrLaserStatus = _OtdrLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16, 1, 1, 4),
    _OtdrLaserStatus_Type()
)
otdrLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrLaserStatus.setStatus("current")
_OtdrMeasurementPort_Type = Unsigned32
_OtdrMeasurementPort_Object = MibTableColumn
otdrMeasurementPort = _OtdrMeasurementPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 16, 1, 1, 5),
    _OtdrMeasurementPort_Type()
)
otdrMeasurementPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrMeasurementPort.setStatus("current")
_OtdrPort_ObjectIdentity = ObjectIdentity
otdrPort = _OtdrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18)
)
_OtdrPortTable_Object = MibTable
otdrPortTable = _OtdrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1)
)
if mibBuilder.loadTexts:
    otdrPortTable.setStatus("current")
_OtdrPortEntry_Object = MibTableRow
otdrPortEntry = _OtdrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1)
)
otdrPortEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    otdrPortEntry.setStatus("current")
_OtdrPortOtdrRange_Type = OtdrOtdrRange
_OtdrPortOtdrRange_Object = MibTableColumn
otdrPortOtdrRange = _OtdrPortOtdrRange_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1, 1),
    _OtdrPortOtdrRange_Type()
)
otdrPortOtdrRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrPortOtdrRange.setStatus("current")
_OtdrPortOtdrPulseWidth_Type = OtdrOtdrPulseWidth
_OtdrPortOtdrPulseWidth_Object = MibTableColumn
otdrPortOtdrPulseWidth = _OtdrPortOtdrPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1, 2),
    _OtdrPortOtdrPulseWidth_Type()
)
otdrPortOtdrPulseWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrPortOtdrPulseWidth.setStatus("current")


class _OtdrPortOtdrMeasurementSpeed_Type(Integer32):
    """Custom type otdrPortOtdrMeasurementSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("medium", 3),
          ("slow", 4),
          ("precision", 5),
          ("auto", 6))
    )


_OtdrPortOtdrMeasurementSpeed_Type.__name__ = "Integer32"
_OtdrPortOtdrMeasurementSpeed_Object = MibTableColumn
otdrPortOtdrMeasurementSpeed = _OtdrPortOtdrMeasurementSpeed_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1, 3),
    _OtdrPortOtdrMeasurementSpeed_Type()
)
otdrPortOtdrMeasurementSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrPortOtdrMeasurementSpeed.setStatus("current")
_OtdrPortOtdrIor_Type = OtdrOtdrIor
_OtdrPortOtdrIor_Object = MibTableColumn
otdrPortOtdrIor = _OtdrPortOtdrIor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1, 4),
    _OtdrPortOtdrIor_Type()
)
otdrPortOtdrIor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrPortOtdrIor.setStatus("current")


class _OtdrPortOtdrFiberType_Type(Integer32):
    """Custom type otdrPortOtdrFiberType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ssmf", 1),
          ("leaf", 2),
          ("twrs", 3),
          ("twc", 4),
          ("allwave", 5),
          ("dsf", 6),
          ("ls", 7),
          ("puresilica", 8),
          ("twreach", 9),
          ("vistacor", 10),
          ("teralight", 11),
          ("drakall", 12),
          ("twplus", 13),
          ("twminus", 14),
          ("pslc", 15),
          ("auto", 16))
    )


_OtdrPortOtdrFiberType_Type.__name__ = "Integer32"
_OtdrPortOtdrFiberType_Object = MibTableColumn
otdrPortOtdrFiberType = _OtdrPortOtdrFiberType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1, 5),
    _OtdrPortOtdrFiberType_Type()
)
otdrPortOtdrFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrPortOtdrFiberType.setStatus("current")
_OtdrPortOtdrLastMeasurement_Type = IetfYangTypesDateAndTime
_OtdrPortOtdrLastMeasurement_Object = MibTableColumn
otdrPortOtdrLastMeasurement = _OtdrPortOtdrLastMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1, 6),
    _OtdrPortOtdrLastMeasurement_Type()
)
otdrPortOtdrLastMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrPortOtdrLastMeasurement.setStatus("current")
_OtdrPortOtdrResolution_Type = OctetString
_OtdrPortOtdrResolution_Object = MibTableColumn
otdrPortOtdrResolution = _OtdrPortOtdrResolution_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 18, 1, 1, 7),
    _OtdrPortOtdrResolution_Type()
)
otdrPortOtdrResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrPortOtdrResolution.setStatus("current")
_Ops_ObjectIdentity = ObjectIdentity
ops = _Ops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20)
)
_OpsTable_Object = MibTable
opsTable = _OpsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1)
)
if mibBuilder.loadTexts:
    opsTable.setStatus("current")
_OpsEntry_Object = MibTableRow
opsEntry = _OpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1)
)
opsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "opsName"),
)
if mibBuilder.loadTexts:
    opsEntry.setStatus("current")
_OpsName_Type = CoriantTypesNameIdentifier
_OpsName_Object = MibTableColumn
opsName = _OpsName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 1),
    _OpsName_Type()
)
opsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsName.setStatus("current")
_OpsWorkingEntity_Type = RowPointer
_OpsWorkingEntity_Object = MibTableColumn
opsWorkingEntity = _OpsWorkingEntity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 2),
    _OpsWorkingEntity_Type()
)
opsWorkingEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsWorkingEntity.setStatus("current")
_OpsProtectionEntity_Type = RowPointer
_OpsProtectionEntity_Object = MibTableColumn
opsProtectionEntity = _OpsProtectionEntity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 3),
    _OpsProtectionEntity_Type()
)
opsProtectionEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsProtectionEntity.setStatus("current")


class _OpsAdminStatus_Type(Integer32):
    """Custom type opsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OpsAdminStatus_Type.__name__ = "Integer32"
_OpsAdminStatus_Object = MibTableColumn
opsAdminStatus = _OpsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 4),
    _OpsAdminStatus_Type()
)
opsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsAdminStatus.setStatus("current")


class _OpsOperStatus_Type(Integer32):
    """Custom type opsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OpsOperStatus_Type.__name__ = "Integer32"
_OpsOperStatus_Object = MibTableColumn
opsOperStatus = _OpsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 5),
    _OpsOperStatus_Type()
)
opsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsOperStatus.setStatus("current")


class _OpsAvailStatus_Type(Bits):
    """Custom type opsAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_OpsAvailStatus_Type.__name__ = "Bits"
_OpsAvailStatus_Object = MibTableColumn
opsAvailStatus = _OpsAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 6),
    _OpsAvailStatus_Type()
)
opsAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsAvailStatus.setStatus("current")


class _OpsAliasName_Type(OctetString):
    """Custom type opsAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OpsAliasName_Type.__name__ = "OctetString"
_OpsAliasName_Object = MibTableColumn
opsAliasName = _OpsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 7),
    _OpsAliasName_Type()
)
opsAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsAliasName.setStatus("current")


class _OpsProtectionStatus_Type(Integer32):
    """Custom type opsProtectionStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("manualSwitchToProtection", 1),
          ("manualSwitchToWorking", 2),
          ("forceSwitchToProtection", 3),
          ("forceSwitchToWorking", 4),
          ("lockoutOfProtection", 5),
          ("signalFailureOnWorking", 6),
          ("signalFailureOnProtection", 7),
          ("signalDegradeOnWorking", 8),
          ("signalDegradeOnProtection", 9),
          ("doNotRevert", 10),
          ("noRequest", 11),
          ("waitToRestore", 12))
    )


_OpsProtectionStatus_Type.__name__ = "Integer32"
_OpsProtectionStatus_Object = MibTableColumn
opsProtectionStatus = _OpsProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 8),
    _OpsProtectionStatus_Type()
)
opsProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsProtectionStatus.setStatus("current")


class _OpsActivePath_Type(Integer32):
    """Custom type opsActivePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protection", 2),
          ("unknown", 3))
    )


_OpsActivePath_Type.__name__ = "Integer32"
_OpsActivePath_Object = MibTableColumn
opsActivePath = _OpsActivePath_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 9),
    _OpsActivePath_Type()
)
opsActivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsActivePath.setStatus("current")
_OpsRevertive_Type = CoriantTypesYesNo
_OpsRevertive_Object = MibTableColumn
opsRevertive = _OpsRevertive_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 10),
    _OpsRevertive_Type()
)
opsRevertive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsRevertive.setStatus("current")


class _OpsWaitToRestore_Type(Unsigned32):
    """Custom type opsWaitToRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OpsWaitToRestore_Type.__name__ = "Unsigned32"
_OpsWaitToRestore_Object = MibTableColumn
opsWaitToRestore = _OpsWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 11),
    _OpsWaitToRestore_Type()
)
opsWaitToRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsWaitToRestore.setStatus("current")
_OpsWorkingSwitchThreshold_Type = CoriantTypesOpticalPower
_OpsWorkingSwitchThreshold_Object = MibTableColumn
opsWorkingSwitchThreshold = _OpsWorkingSwitchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 12),
    _OpsWorkingSwitchThreshold_Type()
)
opsWorkingSwitchThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsWorkingSwitchThreshold.setStatus("current")
_OpsProtectionSwitchThreshold_Type = CoriantTypesOpticalPower
_OpsProtectionSwitchThreshold_Object = MibTableColumn
opsProtectionSwitchThreshold = _OpsProtectionSwitchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 13),
    _OpsProtectionSwitchThreshold_Type()
)
opsProtectionSwitchThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsProtectionSwitchThreshold.setStatus("current")
_OpsWorkingLosThreshold_Type = CoriantTypesOpticalPower
_OpsWorkingLosThreshold_Object = MibTableColumn
opsWorkingLosThreshold = _OpsWorkingLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 14),
    _OpsWorkingLosThreshold_Type()
)
opsWorkingLosThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsWorkingLosThreshold.setStatus("current")
_OpsProtectionLosThreshold_Type = CoriantTypesOpticalPower
_OpsProtectionLosThreshold_Object = MibTableColumn
opsProtectionLosThreshold = _OpsProtectionLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 15),
    _OpsProtectionLosThreshold_Type()
)
opsProtectionLosThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsProtectionLosThreshold.setStatus("current")


class _OpsHoldoffTimer_Type(Unsigned32):
    """Custom type opsHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_OpsHoldoffTimer_Type.__name__ = "Unsigned32"
_OpsHoldoffTimer_Object = MibTableColumn
opsHoldoffTimer = _OpsHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 16),
    _OpsHoldoffTimer_Type()
)
opsHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsHoldoffTimer.setStatus("current")


class _OpsWavelengthBand_Type(Integer32):
    """Custom type opsWavelengthBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1550", 1),
          ("t1310", 2))
    )


_OpsWavelengthBand_Type.__name__ = "Integer32"
_OpsWavelengthBand_Object = MibTableColumn
opsWavelengthBand = _OpsWavelengthBand_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 20, 1, 1, 17),
    _OpsWavelengthBand_Type()
)
opsWavelengthBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsWavelengthBand.setStatus("current")
_SubportStatistics_ObjectIdentity = ObjectIdentity
subportStatistics = _SubportStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 25)
)
_SubportStatisticsTable_Object = MibTable
subportStatisticsTable = _SubportStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 25, 1)
)
if mibBuilder.loadTexts:
    subportStatisticsTable.setStatus("current")
_SubportStatisticsEntry_Object = MibTableRow
subportStatisticsEntry = _SubportStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 25, 1, 1)
)
subportStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    subportStatisticsEntry.setStatus("current")
_SubportStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_SubportStatisticsEntryLastClear_Object = MibTableColumn
subportStatisticsEntryLastClear = _SubportStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 25, 1, 1, 1),
    _SubportStatisticsEntryLastClear_Type()
)
subportStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subportStatisticsEntryLastClear.setStatus("current")
_PortStatistics_ObjectIdentity = ObjectIdentity
portStatistics = _PortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 26)
)
_PortStatisticsTable_Object = MibTable
portStatisticsTable = _PortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 26, 1)
)
if mibBuilder.loadTexts:
    portStatisticsTable.setStatus("current")
_PortStatisticsEntry_Object = MibTableRow
portStatisticsEntry = _PortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 26, 1, 1)
)
portStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portStatisticsEntry.setStatus("current")
_PortStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_PortStatisticsEntryLastClear_Object = MibTableColumn
portStatisticsEntryLastClear = _PortStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 26, 1, 1, 1),
    _PortStatisticsEntryLastClear_Type()
)
portStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatisticsEntryLastClear.setStatus("current")
_SubcardStatistics_ObjectIdentity = ObjectIdentity
subcardStatistics = _SubcardStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 27)
)
_SubcardStatisticsTable_Object = MibTable
subcardStatisticsTable = _SubcardStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 27, 1)
)
if mibBuilder.loadTexts:
    subcardStatisticsTable.setStatus("current")
_SubcardStatisticsEntry_Object = MibTableRow
subcardStatisticsEntry = _SubcardStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 27, 1, 1)
)
subcardStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
)
if mibBuilder.loadTexts:
    subcardStatisticsEntry.setStatus("current")
_SubcardStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_SubcardStatisticsEntryLastClear_Object = MibTableColumn
subcardStatisticsEntryLastClear = _SubcardStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 27, 1, 1, 1),
    _SubcardStatisticsEntryLastClear_Type()
)
subcardStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subcardStatisticsEntryLastClear.setStatus("current")
_CardStatistics_ObjectIdentity = ObjectIdentity
cardStatistics = _CardStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 28)
)
_CardStatisticsTable_Object = MibTable
cardStatisticsTable = _CardStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 28, 1)
)
if mibBuilder.loadTexts:
    cardStatisticsTable.setStatus("current")
_CardStatisticsEntry_Object = MibTableRow
cardStatisticsEntry = _CardStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 28, 1, 1)
)
cardStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
)
if mibBuilder.loadTexts:
    cardStatisticsEntry.setStatus("current")
_CardStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_CardStatisticsEntryLastClear_Object = MibTableColumn
cardStatisticsEntryLastClear = _CardStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 28, 1, 1, 1),
    _CardStatisticsEntryLastClear_Type()
)
cardStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatisticsEntryLastClear.setStatus("current")
_ShelfStatistics_ObjectIdentity = ObjectIdentity
shelfStatistics = _ShelfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 29)
)
_ShelfStatisticsTable_Object = MibTable
shelfStatisticsTable = _ShelfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 29, 1)
)
if mibBuilder.loadTexts:
    shelfStatisticsTable.setStatus("current")
_ShelfStatisticsEntry_Object = MibTableRow
shelfStatisticsEntry = _ShelfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 29, 1, 1)
)
shelfStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
)
if mibBuilder.loadTexts:
    shelfStatisticsEntry.setStatus("current")
_ShelfStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_ShelfStatisticsEntryLastClear_Object = MibTableColumn
shelfStatisticsEntryLastClear = _ShelfStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 3, 29, 1, 1, 1),
    _ShelfStatisticsEntryLastClear_Type()
)
shelfStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfStatisticsEntryLastClear.setStatus("current")
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4)
)
_Otn_ObjectIdentity = ObjectIdentity
otn = _Otn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1)
)
_Eth10g_ObjectIdentity = ObjectIdentity
eth10g = _Eth10g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1)
)
_Eth10gTable_Object = MibTable
eth10gTable = _Eth10gTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eth10gTable.setStatus("current")
_Eth10gEntry_Object = MibTableRow
eth10gEntry = _Eth10gEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1)
)
eth10gEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    eth10gEntry.setStatus("current")
_Eth10gEthFecType_Type = CoriantTypesEthFec
_Eth10gEthFecType_Object = MibTableColumn
eth10gEthFecType = _Eth10gEthFecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 1),
    _Eth10gEthFecType_Type()
)
eth10gEthFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gEthFecType.setStatus("current")
_Eth10gEthFecTypeState_Type = CoriantTypesEthFec
_Eth10gEthFecTypeState_Object = MibTableColumn
eth10gEthFecTypeState = _Eth10gEthFecTypeState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 2),
    _Eth10gEthFecTypeState_Type()
)
eth10gEthFecTypeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gEthFecTypeState.setStatus("current")


class _Eth10gTransmitInterpacketgap_Type(Unsigned32):
    """Custom type eth10gTransmitInterpacketgap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 12),
    )


_Eth10gTransmitInterpacketgap_Type.__name__ = "Unsigned32"
_Eth10gTransmitInterpacketgap_Object = MibTableColumn
eth10gTransmitInterpacketgap = _Eth10gTransmitInterpacketgap_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 3),
    _Eth10gTransmitInterpacketgap_Type()
)
eth10gTransmitInterpacketgap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gTransmitInterpacketgap.setStatus("current")
_Eth10gGfpPayloadFcs_Type = CoriantTypesEnableSwitch
_Eth10gGfpPayloadFcs_Object = MibTableColumn
eth10gGfpPayloadFcs = _Eth10gGfpPayloadFcs_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 4),
    _Eth10gGfpPayloadFcs_Type()
)
eth10gGfpPayloadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gGfpPayloadFcs.setStatus("current")


class _Eth10gMappingMode_Type(Integer32):
    """Custom type eth10gMappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Eth10gMappingMode_Type.__name__ = "Integer32"
_Eth10gMappingMode_Object = MibTableColumn
eth10gMappingMode = _Eth10gMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 5),
    _Eth10gMappingMode_Type()
)
eth10gMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gMappingMode.setStatus("current")


class _Eth10gAdminStatus_Type(Integer32):
    """Custom type eth10gAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Eth10gAdminStatus_Type.__name__ = "Integer32"
_Eth10gAdminStatus_Object = MibTableColumn
eth10gAdminStatus = _Eth10gAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 6),
    _Eth10gAdminStatus_Type()
)
eth10gAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gAdminStatus.setStatus("current")


class _Eth10gOperStatus_Type(Integer32):
    """Custom type eth10gOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Eth10gOperStatus_Type.__name__ = "Integer32"
_Eth10gOperStatus_Object = MibTableColumn
eth10gOperStatus = _Eth10gOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 7),
    _Eth10gOperStatus_Type()
)
eth10gOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gOperStatus.setStatus("current")


class _Eth10gAvailStatus_Type(Bits):
    """Custom type eth10gAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Eth10gAvailStatus_Type.__name__ = "Bits"
_Eth10gAvailStatus_Object = MibTableColumn
eth10gAvailStatus = _Eth10gAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 8),
    _Eth10gAvailStatus_Type()
)
eth10gAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gAvailStatus.setStatus("current")


class _Eth10gAliasName_Type(OctetString):
    """Custom type eth10gAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Eth10gAliasName_Type.__name__ = "OctetString"
_Eth10gAliasName_Object = MibTableColumn
eth10gAliasName = _Eth10gAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 9),
    _Eth10gAliasName_Type()
)
eth10gAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gAliasName.setStatus("current")
_Eth10gClientShutdown_Type = CoriantTypesYesNo
_Eth10gClientShutdown_Object = MibTableColumn
eth10gClientShutdown = _Eth10gClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 10),
    _Eth10gClientShutdown_Type()
)
eth10gClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gClientShutdown.setStatus("current")


class _Eth10gClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type eth10gClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Eth10gClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Eth10gClientShutdownHoldoffTimer_Object = MibTableColumn
eth10gClientShutdownHoldoffTimer = _Eth10gClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 11),
    _Eth10gClientShutdownHoldoffTimer_Type()
)
eth10gClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gClientShutdownHoldoffTimer.setStatus("current")
_Eth10gNearEndAls_Type = CoriantTypesYesNo
_Eth10gNearEndAls_Object = MibTableColumn
eth10gNearEndAls = _Eth10gNearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 12),
    _Eth10gNearEndAls_Type()
)
eth10gNearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gNearEndAls.setStatus("current")
_Eth10gAlsDegradeMode_Type = CoriantTypesEnableSwitch
_Eth10gAlsDegradeMode_Object = MibTableColumn
eth10gAlsDegradeMode = _Eth10gAlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 13),
    _Eth10gAlsDegradeMode_Type()
)
eth10gAlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gAlsDegradeMode.setStatus("current")
_Eth10gLoopbackEnable_Type = CoriantTypesEnableSwitch
_Eth10gLoopbackEnable_Object = MibTableColumn
eth10gLoopbackEnable = _Eth10gLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 14),
    _Eth10gLoopbackEnable_Type()
)
eth10gLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gLoopbackEnable.setStatus("current")


class _Eth10gLoopbackType_Type(Integer32):
    """Custom type eth10gLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Eth10gLoopbackType_Type.__name__ = "Integer32"
_Eth10gLoopbackType_Object = MibTableColumn
eth10gLoopbackType = _Eth10gLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 15),
    _Eth10gLoopbackType_Type()
)
eth10gLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gLoopbackType.setStatus("current")
_Eth10gTestSignalType_Type = CoriantTypesTestSignalType
_Eth10gTestSignalType_Object = MibTableColumn
eth10gTestSignalType = _Eth10gTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 16),
    _Eth10gTestSignalType_Type()
)
eth10gTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gTestSignalType.setStatus("current")
_Eth10gTestSignalEnable_Type = CoriantTypesTestSignalConfig
_Eth10gTestSignalEnable_Object = MibTableColumn
eth10gTestSignalEnable = _Eth10gTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 17),
    _Eth10gTestSignalEnable_Type()
)
eth10gTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gTestSignalEnable.setStatus("current")


class _Eth10gServiceLabel_Type(OctetString):
    """Custom type eth10gServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eth10gServiceLabel_Type.__name__ = "OctetString"
_Eth10gServiceLabel_Object = MibTableColumn
eth10gServiceLabel = _Eth10gServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 18),
    _Eth10gServiceLabel_Type()
)
eth10gServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gServiceLabel.setStatus("current")


class _Eth10gLldpStatusIf_Type(Integer32):
    """Custom type eth10gLldpStatusIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("rxonly", 2),
          ("disabled", 4))
    )


_Eth10gLldpStatusIf_Type.__name__ = "Integer32"
_Eth10gLldpStatusIf_Object = MibTableColumn
eth10gLldpStatusIf = _Eth10gLldpStatusIf_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 19),
    _Eth10gLldpStatusIf_Type()
)
eth10gLldpStatusIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gLldpStatusIf.setStatus("current")


class _Eth10gUpiValue_Type(Integer32):
    """Custom type eth10gUpiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("g709", 1),
          ("gsupp43", 2))
    )


_Eth10gUpiValue_Type.__name__ = "Integer32"
_Eth10gUpiValue_Object = MibTableColumn
eth10gUpiValue = _Eth10gUpiValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 20),
    _Eth10gUpiValue_Type()
)
eth10gUpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gUpiValue.setStatus("current")
_Eth10gHoldoffSignal_Type = CoriantTypesYesNo
_Eth10gHoldoffSignal_Object = MibTableColumn
eth10gHoldoffSignal = _Eth10gHoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 1, 1, 1, 21),
    _Eth10gHoldoffSignal_Type()
)
eth10gHoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gHoldoffSignal.setStatus("current")
_TestSignalFacilityStatus_ObjectIdentity = ObjectIdentity
testSignalFacilityStatus = _TestSignalFacilityStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 2)
)
_TestSignalFacilityStatusTable_Object = MibTable
testSignalFacilityStatusTable = _TestSignalFacilityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    testSignalFacilityStatusTable.setStatus("current")
_TestSignalFacilityStatusEntry_Object = MibTableRow
testSignalFacilityStatusEntry = _TestSignalFacilityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 2, 1, 1)
)
testSignalFacilityStatusEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    testSignalFacilityStatusEntry.setStatus("current")


class _TestSignalFacilityStatusPrbsSync_Type(Integer32):
    """Custom type testSignalFacilityStatusPrbsSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("inSync", 1),
          ("outSync", 2),
          ("errSync", 3))
    )


_TestSignalFacilityStatusPrbsSync_Type.__name__ = "Integer32"
_TestSignalFacilityStatusPrbsSync_Object = MibTableColumn
testSignalFacilityStatusPrbsSync = _TestSignalFacilityStatusPrbsSync_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 2, 1, 1, 1),
    _TestSignalFacilityStatusPrbsSync_Type()
)
testSignalFacilityStatusPrbsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testSignalFacilityStatusPrbsSync.setStatus("current")
_TestSignalFacilityStatusTestTimeDuration_Type = Unsigned32
_TestSignalFacilityStatusTestTimeDuration_Object = MibTableColumn
testSignalFacilityStatusTestTimeDuration = _TestSignalFacilityStatusTestTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 2, 1, 1, 2),
    _TestSignalFacilityStatusTestTimeDuration_Type()
)
testSignalFacilityStatusTestTimeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testSignalFacilityStatusTestTimeDuration.setStatus("current")
_TestSignalFacilityStatusPrbsBitErrorCount_Type = IetfYangTypesGauge64
_TestSignalFacilityStatusPrbsBitErrorCount_Object = MibTableColumn
testSignalFacilityStatusPrbsBitErrorCount = _TestSignalFacilityStatusPrbsBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 2, 1, 1, 3),
    _TestSignalFacilityStatusPrbsBitErrorCount_Type()
)
testSignalFacilityStatusPrbsBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testSignalFacilityStatusPrbsBitErrorCount.setStatus("current")
_LldpRemoteSystem_ObjectIdentity = ObjectIdentity
lldpRemoteSystem = _LldpRemoteSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3)
)
_LldpRemoteSystemTable_Object = MibTable
lldpRemoteSystemTable = _LldpRemoteSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpRemoteSystemTable.setStatus("current")
_LldpRemoteSystemEntry_Object = MibTableRow
lldpRemoteSystemEntry = _LldpRemoteSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1)
)
lldpRemoteSystemEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "lldpRemoteSystemLldpRemoteIndex"),
)
if mibBuilder.loadTexts:
    lldpRemoteSystemEntry.setStatus("current")
_LldpRemoteSystemLldpRemoteIndex_Type = Unsigned32
_LldpRemoteSystemLldpRemoteIndex_Object = MibTableColumn
lldpRemoteSystemLldpRemoteIndex = _LldpRemoteSystemLldpRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 1),
    _LldpRemoteSystemLldpRemoteIndex_Type()
)
lldpRemoteSystemLldpRemoteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemLldpRemoteIndex.setStatus("current")


class _LldpRemoteSystemRemoteChassisIdSubtype_Type(Integer32):
    """Custom type lldpRemoteSystemRemoteChassisIdSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassiscomponent", 1),
          ("interfacealias", 2),
          ("portcomponent", 3),
          ("macaddress", 4),
          ("networkaddress", 5),
          ("interfacename", 6),
          ("local", 7))
    )


_LldpRemoteSystemRemoteChassisIdSubtype_Type.__name__ = "Integer32"
_LldpRemoteSystemRemoteChassisIdSubtype_Object = MibTableColumn
lldpRemoteSystemRemoteChassisIdSubtype = _LldpRemoteSystemRemoteChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 2),
    _LldpRemoteSystemRemoteChassisIdSubtype_Type()
)
lldpRemoteSystemRemoteChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemoteChassisIdSubtype.setStatus("current")


class _LldpRemoteSystemRemoteChassisId_Type(OctetString):
    """Custom type lldpRemoteSystemRemoteChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemoteSystemRemoteChassisId_Type.__name__ = "OctetString"
_LldpRemoteSystemRemoteChassisId_Object = MibTableColumn
lldpRemoteSystemRemoteChassisId = _LldpRemoteSystemRemoteChassisId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 3),
    _LldpRemoteSystemRemoteChassisId_Type()
)
lldpRemoteSystemRemoteChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemoteChassisId.setStatus("current")


class _LldpRemoteSystemRemotePortIdSubtype_Type(Integer32):
    """Custom type lldpRemoteSystemRemotePortIdSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("interfacealias", 1),
          ("portcomponent", 2),
          ("macaddress", 3),
          ("networkaddress", 4),
          ("interfacename", 5),
          ("agentcircuitid", 6),
          ("local", 7))
    )


_LldpRemoteSystemRemotePortIdSubtype_Type.__name__ = "Integer32"
_LldpRemoteSystemRemotePortIdSubtype_Object = MibTableColumn
lldpRemoteSystemRemotePortIdSubtype = _LldpRemoteSystemRemotePortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 4),
    _LldpRemoteSystemRemotePortIdSubtype_Type()
)
lldpRemoteSystemRemotePortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemotePortIdSubtype.setStatus("current")


class _LldpRemoteSystemRemotePortId_Type(OctetString):
    """Custom type lldpRemoteSystemRemotePortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemoteSystemRemotePortId_Type.__name__ = "OctetString"
_LldpRemoteSystemRemotePortId_Object = MibTableColumn
lldpRemoteSystemRemotePortId = _LldpRemoteSystemRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 5),
    _LldpRemoteSystemRemotePortId_Type()
)
lldpRemoteSystemRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemotePortId.setStatus("current")


class _LldpRemoteSystemRemotePortDesc_Type(OctetString):
    """Custom type lldpRemoteSystemRemotePortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemoteSystemRemotePortDesc_Type.__name__ = "OctetString"
_LldpRemoteSystemRemotePortDesc_Object = MibTableColumn
lldpRemoteSystemRemotePortDesc = _LldpRemoteSystemRemotePortDesc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 6),
    _LldpRemoteSystemRemotePortDesc_Type()
)
lldpRemoteSystemRemotePortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemotePortDesc.setStatus("current")


class _LldpRemoteSystemRemoteSysName_Type(OctetString):
    """Custom type lldpRemoteSystemRemoteSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemoteSystemRemoteSysName_Type.__name__ = "OctetString"
_LldpRemoteSystemRemoteSysName_Object = MibTableColumn
lldpRemoteSystemRemoteSysName = _LldpRemoteSystemRemoteSysName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 7),
    _LldpRemoteSystemRemoteSysName_Type()
)
lldpRemoteSystemRemoteSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemoteSysName.setStatus("current")


class _LldpRemoteSystemRemoteSysDesc_Type(OctetString):
    """Custom type lldpRemoteSystemRemoteSysDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemoteSystemRemoteSysDesc_Type.__name__ = "OctetString"
_LldpRemoteSystemRemoteSysDesc_Object = MibTableColumn
lldpRemoteSystemRemoteSysDesc = _LldpRemoteSystemRemoteSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 8),
    _LldpRemoteSystemRemoteSysDesc_Type()
)
lldpRemoteSystemRemoteSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemoteSysDesc.setStatus("current")
_LldpRemoteSystemRemoteSysCapSupported_Type = LldpLldpSysCap
_LldpRemoteSystemRemoteSysCapSupported_Object = MibTableColumn
lldpRemoteSystemRemoteSysCapSupported = _LldpRemoteSystemRemoteSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 9),
    _LldpRemoteSystemRemoteSysCapSupported_Type()
)
lldpRemoteSystemRemoteSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemoteSysCapSupported.setStatus("current")
_LldpRemoteSystemRemoteSysCapEnabled_Type = LldpLldpSysCap
_LldpRemoteSystemRemoteSysCapEnabled_Object = MibTableColumn
lldpRemoteSystemRemoteSysCapEnabled = _LldpRemoteSystemRemoteSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 3, 1, 1, 10),
    _LldpRemoteSystemRemoteSysCapEnabled_Type()
)
lldpRemoteSystemRemoteSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSystemRemoteSysCapEnabled.setStatus("current")
_RemoteManAddresses_ObjectIdentity = ObjectIdentity
remoteManAddresses = _RemoteManAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4)
)
_RemoteManAddressesTable_Object = MibTable
remoteManAddressesTable = _RemoteManAddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    remoteManAddressesTable.setStatus("current")
_RemoteManAddressesEntry_Object = MibTableRow
remoteManAddressesEntry = _RemoteManAddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4, 1, 1)
)
remoteManAddressesEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "lldpRemoteSystemLldpRemoteIndex"),
    (0, "CORIANT-GROOVE-MIB", "remoteManAddressesRemoteManAddrSubtype"),
    (0, "CORIANT-GROOVE-MIB", "remoteManAddressesRemoteManAddr"),
)
if mibBuilder.loadTexts:
    remoteManAddressesEntry.setStatus("current")
_RemoteManAddressesRemoteManAddrSubtype_Type = Unsigned32
_RemoteManAddressesRemoteManAddrSubtype_Object = MibTableColumn
remoteManAddressesRemoteManAddrSubtype = _RemoteManAddressesRemoteManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4, 1, 1, 1),
    _RemoteManAddressesRemoteManAddrSubtype_Type()
)
remoteManAddressesRemoteManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteManAddressesRemoteManAddrSubtype.setStatus("current")


class _RemoteManAddressesRemoteManAddr_Type(OctetString):
    """Custom type remoteManAddressesRemoteManAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_RemoteManAddressesRemoteManAddr_Type.__name__ = "OctetString"
_RemoteManAddressesRemoteManAddr_Object = MibTableColumn
remoteManAddressesRemoteManAddr = _RemoteManAddressesRemoteManAddr_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4, 1, 1, 2),
    _RemoteManAddressesRemoteManAddr_Type()
)
remoteManAddressesRemoteManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteManAddressesRemoteManAddr.setStatus("current")
_RemoteManAddressesRemoteManAddrIfSubtype_Type = Unsigned32
_RemoteManAddressesRemoteManAddrIfSubtype_Object = MibTableColumn
remoteManAddressesRemoteManAddrIfSubtype = _RemoteManAddressesRemoteManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4, 1, 1, 3),
    _RemoteManAddressesRemoteManAddrIfSubtype_Type()
)
remoteManAddressesRemoteManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteManAddressesRemoteManAddrIfSubtype.setStatus("current")
_RemoteManAddressesRemoteManAddrIfId_Type = Unsigned32
_RemoteManAddressesRemoteManAddrIfId_Object = MibTableColumn
remoteManAddressesRemoteManAddrIfId = _RemoteManAddressesRemoteManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4, 1, 1, 4),
    _RemoteManAddressesRemoteManAddrIfId_Type()
)
remoteManAddressesRemoteManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteManAddressesRemoteManAddrIfId.setStatus("current")


class _RemoteManAddressesRemoteManAddrOid_Type(OctetString):
    """Custom type remoteManAddressesRemoteManAddrOid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RemoteManAddressesRemoteManAddrOid_Type.__name__ = "OctetString"
_RemoteManAddressesRemoteManAddrOid_Object = MibTableColumn
remoteManAddressesRemoteManAddrOid = _RemoteManAddressesRemoteManAddrOid_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 4, 1, 1, 5),
    _RemoteManAddressesRemoteManAddrOid_Type()
)
remoteManAddressesRemoteManAddrOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteManAddressesRemoteManAddrOid.setStatus("current")
_Odu_ObjectIdentity = ObjectIdentity
odu = _Odu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5)
)
_OduTable_Object = MibTable
oduTable = _OduTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    oduTable.setStatus("current")
_OduEntry_Object = MibTableRow
oduEntry = _OduEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1)
)
oduEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL1"),
    (0, "CORIANT-GROOVE-MIB", "oduidL1"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL2"),
    (0, "CORIANT-GROOVE-MIB", "oduidL2"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL3"),
    (0, "CORIANT-GROOVE-MIB", "oduidL3"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL4"),
    (0, "CORIANT-GROOVE-MIB", "oduidL4"),
)
if mibBuilder.loadTexts:
    oduEntry.setStatus("current")
_OdutypeL1_Type = CoriantTypesOduType
_OdutypeL1_Object = MibTableColumn
odutypeL1 = _OdutypeL1_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 1),
    _OdutypeL1_Type()
)
odutypeL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    odutypeL1.setStatus("current")
_OduidL1_Type = Unsigned32
_OduidL1_Object = MibTableColumn
oduidL1 = _OduidL1_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 2),
    _OduidL1_Type()
)
oduidL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduidL1.setStatus("current")
_OdutypeL2_Type = CoriantTypesOduType
_OdutypeL2_Object = MibTableColumn
odutypeL2 = _OdutypeL2_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 3),
    _OdutypeL2_Type()
)
odutypeL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    odutypeL2.setStatus("current")
_OduidL2_Type = Unsigned32
_OduidL2_Object = MibTableColumn
oduidL2 = _OduidL2_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 4),
    _OduidL2_Type()
)
oduidL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduidL2.setStatus("current")
_OdutypeL3_Type = CoriantTypesOduType
_OdutypeL3_Object = MibTableColumn
odutypeL3 = _OdutypeL3_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 5),
    _OdutypeL3_Type()
)
odutypeL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    odutypeL3.setStatus("current")
_OduidL3_Type = Unsigned32
_OduidL3_Object = MibTableColumn
oduidL3 = _OduidL3_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 6),
    _OduidL3_Type()
)
oduidL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduidL3.setStatus("current")
_OdutypeL4_Type = CoriantTypesOduType
_OdutypeL4_Object = MibTableColumn
odutypeL4 = _OdutypeL4_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 7),
    _OdutypeL4_Type()
)
odutypeL4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    odutypeL4.setStatus("current")
_OduidL4_Type = Unsigned32
_OduidL4_Object = MibTableColumn
oduidL4 = _OduidL4_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 8),
    _OduidL4_Type()
)
oduidL4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduidL4.setStatus("current")


class _OduAdminStatus_Type(Integer32):
    """Custom type oduAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OduAdminStatus_Type.__name__ = "Integer32"
_OduAdminStatus_Object = MibTableColumn
oduAdminStatus = _OduAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 9),
    _OduAdminStatus_Type()
)
oduAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduAdminStatus.setStatus("current")


class _OduOperStatus_Type(Integer32):
    """Custom type oduOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OduOperStatus_Type.__name__ = "Integer32"
_OduOperStatus_Object = MibTableColumn
oduOperStatus = _OduOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 10),
    _OduOperStatus_Type()
)
oduOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduOperStatus.setStatus("current")


class _OduAvailStatus_Type(Bits):
    """Custom type oduAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_OduAvailStatus_Type.__name__ = "Bits"
_OduAvailStatus_Object = MibTableColumn
oduAvailStatus = _OduAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 11),
    _OduAvailStatus_Type()
)
oduAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduAvailStatus.setStatus("current")


class _OduAliasName_Type(OctetString):
    """Custom type oduAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OduAliasName_Type.__name__ = "OctetString"
_OduAliasName_Object = MibTableColumn
oduAliasName = _OduAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 12),
    _OduAliasName_Type()
)
oduAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduAliasName.setStatus("current")


class _OduServiceLabel_Type(OctetString):
    """Custom type oduServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OduServiceLabel_Type.__name__ = "OctetString"
_OduServiceLabel_Object = MibTableColumn
oduServiceLabel = _OduServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 13),
    _OduServiceLabel_Type()
)
oduServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduServiceLabel.setStatus("current")
_OduTribSlot_Type = CoriantTypesNumberList
_OduTribSlot_Object = MibTableColumn
oduTribSlot = _OduTribSlot_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 14),
    _OduTribSlot_Type()
)
oduTribSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTribSlot.setStatus("current")


class _OduRxPayloadType_Type(OctetString):
    """Custom type oduRxPayloadType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_OduRxPayloadType_Type.__name__ = "OctetString"
_OduRxPayloadType_Object = MibTableColumn
oduRxPayloadType = _OduRxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 15),
    _OduRxPayloadType_Type()
)
oduRxPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduRxPayloadType.setStatus("current")


class _OduTxPayloadType_Type(OctetString):
    """Custom type oduTxPayloadType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_OduTxPayloadType_Type.__name__ = "OctetString"
_OduTxPayloadType_Object = MibTableColumn
oduTxPayloadType = _OduTxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 16),
    _OduTxPayloadType_Type()
)
oduTxPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTxPayloadType.setStatus("current")
_OduNimEnable_Type = CoriantTypesEnableSwitch
_OduNimEnable_Object = MibTableColumn
oduNimEnable = _OduNimEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 17),
    _OduNimEnable_Type()
)
oduNimEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduNimEnable.setStatus("current")
_OduDelayMeasurementEnable_Type = CoriantTypesEnableSwitch
_OduDelayMeasurementEnable_Object = MibTableColumn
oduDelayMeasurementEnable = _OduDelayMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 18),
    _OduDelayMeasurementEnable_Type()
)
oduDelayMeasurementEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduDelayMeasurementEnable.setStatus("current")


class _OduOpuConfigActual_Type(Integer32):
    """Custom type oduOpuConfigActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("intact", 1),
          ("client", 2),
          ("mux", 3))
    )


_OduOpuConfigActual_Type.__name__ = "Integer32"
_OduOpuConfigActual_Object = MibTableColumn
oduOpuConfigActual = _OduOpuConfigActual_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 19),
    _OduOpuConfigActual_Type()
)
oduOpuConfigActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduOpuConfigActual.setStatus("current")


class _OduClientSignalType_Type(Integer32):
    """Custom type oduClientSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("fc8g", 1),
          ("fc16g", 2))
    )


_OduClientSignalType_Type.__name__ = "Integer32"
_OduClientSignalType_Object = MibTableColumn
oduClientSignalType = _OduClientSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 20),
    _OduClientSignalType_Type()
)
oduClientSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientSignalType.setStatus("current")


class _OduExpSapi_Type(OctetString):
    """Custom type oduExpSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduExpSapi_Type.__name__ = "OctetString"
_OduExpSapi_Object = MibTableColumn
oduExpSapi = _OduExpSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 21),
    _OduExpSapi_Type()
)
oduExpSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduExpSapi.setStatus("current")


class _OduExpDapi_Type(OctetString):
    """Custom type oduExpDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduExpDapi_Type.__name__ = "OctetString"
_OduExpDapi_Object = MibTableColumn
oduExpDapi = _OduExpDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 22),
    _OduExpDapi_Type()
)
oduExpDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduExpDapi.setStatus("current")


class _OduExpOperator_Type(OctetString):
    """Custom type oduExpOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduExpOperator_Type.__name__ = "OctetString"
_OduExpOperator_Object = MibTableColumn
oduExpOperator = _OduExpOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 23),
    _OduExpOperator_Type()
)
oduExpOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduExpOperator.setStatus("current")


class _OduTxSapi_Type(OctetString):
    """Custom type oduTxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTxSapi_Type.__name__ = "OctetString"
_OduTxSapi_Object = MibTableColumn
oduTxSapi = _OduTxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 24),
    _OduTxSapi_Type()
)
oduTxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTxSapi.setStatus("current")


class _OduTxDapi_Type(OctetString):
    """Custom type oduTxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTxDapi_Type.__name__ = "OctetString"
_OduTxDapi_Object = MibTableColumn
oduTxDapi = _OduTxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 25),
    _OduTxDapi_Type()
)
oduTxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTxDapi.setStatus("current")


class _OduTxOperator_Type(OctetString):
    """Custom type oduTxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduTxOperator_Type.__name__ = "OctetString"
_OduTxOperator_Object = MibTableColumn
oduTxOperator = _OduTxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 26),
    _OduTxOperator_Type()
)
oduTxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTxOperator.setStatus("current")
_OduTimDefectMode_Type = CoriantTypesTimMode
_OduTimDefectMode_Object = MibTableColumn
oduTimDefectMode = _OduTimDefectMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 27),
    _OduTimDefectMode_Type()
)
oduTimDefectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTimDefectMode.setStatus("current")
_OduTimAct_Type = CoriantTypesEnableSwitch
_OduTimAct_Object = MibTableColumn
oduTimAct = _OduTimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 28),
    _OduTimAct_Type()
)
oduTimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTimAct.setStatus("current")


class _OduRxSapi_Type(OctetString):
    """Custom type oduRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduRxSapi_Type.__name__ = "OctetString"
_OduRxSapi_Object = MibTableColumn
oduRxSapi = _OduRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 29),
    _OduRxSapi_Type()
)
oduRxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduRxSapi.setStatus("current")


class _OduRxDapi_Type(OctetString):
    """Custom type oduRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduRxDapi_Type.__name__ = "OctetString"
_OduRxDapi_Object = MibTableColumn
oduRxDapi = _OduRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 30),
    _OduRxDapi_Type()
)
oduRxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduRxDapi.setStatus("current")


class _OduRxOperator_Type(OctetString):
    """Custom type oduRxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduRxOperator_Type.__name__ = "OctetString"
_OduRxOperator_Object = MibTableColumn
oduRxOperator = _OduRxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 31),
    _OduRxOperator_Type()
)
oduRxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduRxOperator.setStatus("current")


class _OduDegradeInterval_Type(Unsigned32):
    """Custom type oduDegradeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduDegradeInterval_Type.__name__ = "Unsigned32"
_OduDegradeInterval_Object = MibTableColumn
oduDegradeInterval = _OduDegradeInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 32),
    _OduDegradeInterval_Type()
)
oduDegradeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduDegradeInterval.setStatus("current")


class _OduDegradeThreshold_Type(Unsigned32):
    """Custom type oduDegradeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2590845),
    )


_OduDegradeThreshold_Type.__name__ = "Unsigned32"
_OduDegradeThreshold_Object = MibTableColumn
oduDegradeThreshold = _OduDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 33),
    _OduDegradeThreshold_Type()
)
oduDegradeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduDegradeThreshold.setStatus("current")
_OduTestSignalType_Type = CoriantTypesTestSignalType
_OduTestSignalType_Object = MibTableColumn
oduTestSignalType = _OduTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 34),
    _OduTestSignalType_Type()
)
oduTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTestSignalType.setStatus("current")
_OduTestSignalEnable_Type = CoriantTypesTestSignalConfig
_OduTestSignalEnable_Object = MibTableColumn
oduTestSignalEnable = _OduTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 35),
    _OduTestSignalEnable_Type()
)
oduTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTestSignalEnable.setStatus("current")


class _OduTerminationMode_Type(Integer32):
    """Custom type oduTerminationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("terminated", 0),
          ("nonTerminated", 1))
    )


_OduTerminationMode_Type.__name__ = "Integer32"
_OduTerminationMode_Object = MibTableColumn
oduTerminationMode = _OduTerminationMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 5, 1, 1, 36),
    _OduTerminationMode_Type()
)
oduTerminationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTerminationMode.setStatus("current")
_OduEncryption_ObjectIdentity = ObjectIdentity
oduEncryption = _OduEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6)
)
_OduEncryptionTable_Object = MibTable
oduEncryptionTable = _OduEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    oduEncryptionTable.setStatus("current")
_OduEncryptionEntry_Object = MibTableRow
oduEncryptionEntry = _OduEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1)
)
oduEncryptionEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL1"),
    (0, "CORIANT-GROOVE-MIB", "oduidL1"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL2"),
    (0, "CORIANT-GROOVE-MIB", "oduidL2"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL3"),
    (0, "CORIANT-GROOVE-MIB", "oduidL3"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL4"),
    (0, "CORIANT-GROOVE-MIB", "oduidL4"),
)
if mibBuilder.loadTexts:
    oduEncryptionEntry.setStatus("current")


class _OduEncryptionEncryptionEnable_Type(Integer32):
    """Custom type oduEncryptionEncryptionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("enabledNonRevertive", 3))
    )


_OduEncryptionEncryptionEnable_Type.__name__ = "Integer32"
_OduEncryptionEncryptionEnable_Object = MibTableColumn
oduEncryptionEncryptionEnable = _OduEncryptionEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 1),
    _OduEncryptionEncryptionEnable_Type()
)
oduEncryptionEncryptionEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionEncryptionEnable.setStatus("current")


class _OduEncryptionBlockCipherMode_Type(Integer32):
    """Custom type oduEncryptionBlockCipherMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctr", 1),
          ("gcm", 2))
    )


_OduEncryptionBlockCipherMode_Type.__name__ = "Integer32"
_OduEncryptionBlockCipherMode_Object = MibTableColumn
oduEncryptionBlockCipherMode = _OduEncryptionBlockCipherMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 2),
    _OduEncryptionBlockCipherMode_Type()
)
oduEncryptionBlockCipherMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionBlockCipherMode.setStatus("current")


class _OduEncryptionEncryptionInterval_Type(Unsigned32):
    """Custom type oduEncryptionEncryptionInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_OduEncryptionEncryptionInterval_Type.__name__ = "Unsigned32"
_OduEncryptionEncryptionInterval_Object = MibTableColumn
oduEncryptionEncryptionInterval = _OduEncryptionEncryptionInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 3),
    _OduEncryptionEncryptionInterval_Type()
)
oduEncryptionEncryptionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionEncryptionInterval.setStatus("current")
_OduEncryptionEncryptionTxStatus_Type = CoriantCommonOtnEncryStatusEnum
_OduEncryptionEncryptionTxStatus_Object = MibTableColumn
oduEncryptionEncryptionTxStatus = _OduEncryptionEncryptionTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 4),
    _OduEncryptionEncryptionTxStatus_Type()
)
oduEncryptionEncryptionTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionEncryptionTxStatus.setStatus("current")
_OduEncryptionEncryptionRxStatus_Type = CoriantCommonOtnEncryStatusEnum
_OduEncryptionEncryptionRxStatus_Object = MibTableColumn
oduEncryptionEncryptionRxStatus = _OduEncryptionEncryptionRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 5),
    _OduEncryptionEncryptionRxStatus_Type()
)
oduEncryptionEncryptionRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionEncryptionRxStatus.setStatus("current")
_OduEncryptionOduKeySyncSession_Type = CoriantCommonOtnKeySyncSession
_OduEncryptionOduKeySyncSession_Object = MibTableColumn
oduEncryptionOduKeySyncSession = _OduEncryptionOduKeySyncSession_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 6),
    _OduEncryptionOduKeySyncSession_Type()
)
oduEncryptionOduKeySyncSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionOduKeySyncSession.setStatus("current")


class _OduEncryptionEncryptionTxChannelId_Type(OctetString):
    """Custom type oduEncryptionEncryptionTxChannelId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduEncryptionEncryptionTxChannelId_Type.__name__ = "OctetString"
_OduEncryptionEncryptionTxChannelId_Object = MibTableColumn
oduEncryptionEncryptionTxChannelId = _OduEncryptionEncryptionTxChannelId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 7),
    _OduEncryptionEncryptionTxChannelId_Type()
)
oduEncryptionEncryptionTxChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionEncryptionTxChannelId.setStatus("current")
_OduEncryptionTimeToNextKey_Type = Unsigned32
_OduEncryptionTimeToNextKey_Object = MibTableColumn
oduEncryptionTimeToNextKey = _OduEncryptionTimeToNextKey_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 6, 1, 1, 8),
    _OduEncryptionTimeToNextKey_Type()
)
oduEncryptionTimeToNextKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduEncryptionTimeToNextKey.setStatus("current")
_TestSignalStatus_ObjectIdentity = ObjectIdentity
testSignalStatus = _TestSignalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 7)
)
_TestSignalStatusTable_Object = MibTable
testSignalStatusTable = _TestSignalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    testSignalStatusTable.setStatus("current")
_TestSignalStatusEntry_Object = MibTableRow
testSignalStatusEntry = _TestSignalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 7, 1, 1)
)
testSignalStatusEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL1"),
    (0, "CORIANT-GROOVE-MIB", "oduidL1"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL2"),
    (0, "CORIANT-GROOVE-MIB", "oduidL2"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL3"),
    (0, "CORIANT-GROOVE-MIB", "oduidL3"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL4"),
    (0, "CORIANT-GROOVE-MIB", "oduidL4"),
)
if mibBuilder.loadTexts:
    testSignalStatusEntry.setStatus("current")


class _TestSignalStatusPrbsSync_Type(Integer32):
    """Custom type testSignalStatusPrbsSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("inSync", 1),
          ("outSync", 2),
          ("errSync", 3))
    )


_TestSignalStatusPrbsSync_Type.__name__ = "Integer32"
_TestSignalStatusPrbsSync_Object = MibTableColumn
testSignalStatusPrbsSync = _TestSignalStatusPrbsSync_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 7, 1, 1, 1),
    _TestSignalStatusPrbsSync_Type()
)
testSignalStatusPrbsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testSignalStatusPrbsSync.setStatus("current")
_TestSignalStatusTestTimeDuration_Type = Unsigned32
_TestSignalStatusTestTimeDuration_Object = MibTableColumn
testSignalStatusTestTimeDuration = _TestSignalStatusTestTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 7, 1, 1, 2),
    _TestSignalStatusTestTimeDuration_Type()
)
testSignalStatusTestTimeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testSignalStatusTestTimeDuration.setStatus("current")
_TestSignalStatusPrbsBitErrorCount_Type = IetfYangTypesGauge64
_TestSignalStatusPrbsBitErrorCount_Object = MibTableColumn
testSignalStatusPrbsBitErrorCount = _TestSignalStatusPrbsBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 7, 1, 1, 3),
    _TestSignalStatusPrbsBitErrorCount_Type()
)
testSignalStatusPrbsBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testSignalStatusPrbsBitErrorCount.setStatus("current")
_Eth40g_ObjectIdentity = ObjectIdentity
eth40g = _Eth40g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8)
)
_Eth40gTable_Object = MibTable
eth40gTable = _Eth40gTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    eth40gTable.setStatus("current")
_Eth40gEntry_Object = MibTableRow
eth40gEntry = _Eth40gEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1)
)
eth40gEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    eth40gEntry.setStatus("current")
_Eth40gEthFecType_Type = CoriantTypesEthFec
_Eth40gEthFecType_Object = MibTableColumn
eth40gEthFecType = _Eth40gEthFecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 1),
    _Eth40gEthFecType_Type()
)
eth40gEthFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gEthFecType.setStatus("current")
_Eth40gEthFecTypeState_Type = CoriantTypesEthFec
_Eth40gEthFecTypeState_Object = MibTableColumn
eth40gEthFecTypeState = _Eth40gEthFecTypeState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 2),
    _Eth40gEthFecTypeState_Type()
)
eth40gEthFecTypeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gEthFecTypeState.setStatus("current")


class _Eth40gTransmitInterpacketgap_Type(Unsigned32):
    """Custom type eth40gTransmitInterpacketgap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 12),
    )


_Eth40gTransmitInterpacketgap_Type.__name__ = "Unsigned32"
_Eth40gTransmitInterpacketgap_Object = MibTableColumn
eth40gTransmitInterpacketgap = _Eth40gTransmitInterpacketgap_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 3),
    _Eth40gTransmitInterpacketgap_Type()
)
eth40gTransmitInterpacketgap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gTransmitInterpacketgap.setStatus("current")
_Eth40gGfpPayloadFcs_Type = CoriantTypesEnableSwitch
_Eth40gGfpPayloadFcs_Object = MibTableColumn
eth40gGfpPayloadFcs = _Eth40gGfpPayloadFcs_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 4),
    _Eth40gGfpPayloadFcs_Type()
)
eth40gGfpPayloadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gGfpPayloadFcs.setStatus("current")


class _Eth40gMappingMode_Type(Integer32):
    """Custom type eth40gMappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Eth40gMappingMode_Type.__name__ = "Integer32"
_Eth40gMappingMode_Object = MibTableColumn
eth40gMappingMode = _Eth40gMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 5),
    _Eth40gMappingMode_Type()
)
eth40gMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gMappingMode.setStatus("current")


class _Eth40gAdminStatus_Type(Integer32):
    """Custom type eth40gAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Eth40gAdminStatus_Type.__name__ = "Integer32"
_Eth40gAdminStatus_Object = MibTableColumn
eth40gAdminStatus = _Eth40gAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 6),
    _Eth40gAdminStatus_Type()
)
eth40gAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gAdminStatus.setStatus("current")


class _Eth40gOperStatus_Type(Integer32):
    """Custom type eth40gOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Eth40gOperStatus_Type.__name__ = "Integer32"
_Eth40gOperStatus_Object = MibTableColumn
eth40gOperStatus = _Eth40gOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 7),
    _Eth40gOperStatus_Type()
)
eth40gOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gOperStatus.setStatus("current")


class _Eth40gAvailStatus_Type(Bits):
    """Custom type eth40gAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Eth40gAvailStatus_Type.__name__ = "Bits"
_Eth40gAvailStatus_Object = MibTableColumn
eth40gAvailStatus = _Eth40gAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 8),
    _Eth40gAvailStatus_Type()
)
eth40gAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gAvailStatus.setStatus("current")


class _Eth40gAliasName_Type(OctetString):
    """Custom type eth40gAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Eth40gAliasName_Type.__name__ = "OctetString"
_Eth40gAliasName_Object = MibTableColumn
eth40gAliasName = _Eth40gAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 9),
    _Eth40gAliasName_Type()
)
eth40gAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gAliasName.setStatus("current")
_Eth40gClientShutdown_Type = CoriantTypesYesNo
_Eth40gClientShutdown_Object = MibTableColumn
eth40gClientShutdown = _Eth40gClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 10),
    _Eth40gClientShutdown_Type()
)
eth40gClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gClientShutdown.setStatus("current")


class _Eth40gClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type eth40gClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Eth40gClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Eth40gClientShutdownHoldoffTimer_Object = MibTableColumn
eth40gClientShutdownHoldoffTimer = _Eth40gClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 11),
    _Eth40gClientShutdownHoldoffTimer_Type()
)
eth40gClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gClientShutdownHoldoffTimer.setStatus("current")
_Eth40gNearEndAls_Type = CoriantTypesYesNo
_Eth40gNearEndAls_Object = MibTableColumn
eth40gNearEndAls = _Eth40gNearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 12),
    _Eth40gNearEndAls_Type()
)
eth40gNearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gNearEndAls.setStatus("current")
_Eth40gAlsDegradeMode_Type = CoriantTypesEnableSwitch
_Eth40gAlsDegradeMode_Object = MibTableColumn
eth40gAlsDegradeMode = _Eth40gAlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 13),
    _Eth40gAlsDegradeMode_Type()
)
eth40gAlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gAlsDegradeMode.setStatus("current")
_Eth40gLoopbackEnable_Type = CoriantTypesEnableSwitch
_Eth40gLoopbackEnable_Object = MibTableColumn
eth40gLoopbackEnable = _Eth40gLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 14),
    _Eth40gLoopbackEnable_Type()
)
eth40gLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gLoopbackEnable.setStatus("current")


class _Eth40gLoopbackType_Type(Integer32):
    """Custom type eth40gLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Eth40gLoopbackType_Type.__name__ = "Integer32"
_Eth40gLoopbackType_Object = MibTableColumn
eth40gLoopbackType = _Eth40gLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 15),
    _Eth40gLoopbackType_Type()
)
eth40gLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gLoopbackType.setStatus("current")
_Eth40gTestSignalType_Type = CoriantTypesTestSignalType
_Eth40gTestSignalType_Object = MibTableColumn
eth40gTestSignalType = _Eth40gTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 16),
    _Eth40gTestSignalType_Type()
)
eth40gTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gTestSignalType.setStatus("current")
_Eth40gTestSignalEnable_Type = CoriantTypesTestSignalConfig
_Eth40gTestSignalEnable_Object = MibTableColumn
eth40gTestSignalEnable = _Eth40gTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 17),
    _Eth40gTestSignalEnable_Type()
)
eth40gTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gTestSignalEnable.setStatus("current")


class _Eth40gServiceLabel_Type(OctetString):
    """Custom type eth40gServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eth40gServiceLabel_Type.__name__ = "OctetString"
_Eth40gServiceLabel_Object = MibTableColumn
eth40gServiceLabel = _Eth40gServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 18),
    _Eth40gServiceLabel_Type()
)
eth40gServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gServiceLabel.setStatus("current")


class _Eth40gLldpStatusIf_Type(Integer32):
    """Custom type eth40gLldpStatusIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("rxonly", 2),
          ("disabled", 4))
    )


_Eth40gLldpStatusIf_Type.__name__ = "Integer32"
_Eth40gLldpStatusIf_Object = MibTableColumn
eth40gLldpStatusIf = _Eth40gLldpStatusIf_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 19),
    _Eth40gLldpStatusIf_Type()
)
eth40gLldpStatusIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gLldpStatusIf.setStatus("current")
_Eth40gHoldoffSignal_Type = CoriantTypesYesNo
_Eth40gHoldoffSignal_Object = MibTableColumn
eth40gHoldoffSignal = _Eth40gHoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 8, 1, 1, 20),
    _Eth40gHoldoffSignal_Type()
)
eth40gHoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gHoldoffSignal.setStatus("current")
_Eth100g_ObjectIdentity = ObjectIdentity
eth100g = _Eth100g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9)
)
_Eth100gTable_Object = MibTable
eth100gTable = _Eth100gTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    eth100gTable.setStatus("current")
_Eth100gEntry_Object = MibTableRow
eth100gEntry = _Eth100gEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1)
)
eth100gEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    eth100gEntry.setStatus("current")
_Eth100gEthFecType_Type = CoriantTypesEthFec
_Eth100gEthFecType_Object = MibTableColumn
eth100gEthFecType = _Eth100gEthFecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 1),
    _Eth100gEthFecType_Type()
)
eth100gEthFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gEthFecType.setStatus("current")
_Eth100gEthFecTypeState_Type = CoriantTypesEthFec
_Eth100gEthFecTypeState_Object = MibTableColumn
eth100gEthFecTypeState = _Eth100gEthFecTypeState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 2),
    _Eth100gEthFecTypeState_Type()
)
eth100gEthFecTypeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gEthFecTypeState.setStatus("current")


class _Eth100gTransmitInterpacketgap_Type(Unsigned32):
    """Custom type eth100gTransmitInterpacketgap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 12),
    )


_Eth100gTransmitInterpacketgap_Type.__name__ = "Unsigned32"
_Eth100gTransmitInterpacketgap_Object = MibTableColumn
eth100gTransmitInterpacketgap = _Eth100gTransmitInterpacketgap_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 3),
    _Eth100gTransmitInterpacketgap_Type()
)
eth100gTransmitInterpacketgap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gTransmitInterpacketgap.setStatus("current")
_Eth100gGfpPayloadFcs_Type = CoriantTypesEnableSwitch
_Eth100gGfpPayloadFcs_Object = MibTableColumn
eth100gGfpPayloadFcs = _Eth100gGfpPayloadFcs_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 4),
    _Eth100gGfpPayloadFcs_Type()
)
eth100gGfpPayloadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gGfpPayloadFcs.setStatus("current")


class _Eth100gMappingMode_Type(Integer32):
    """Custom type eth100gMappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Eth100gMappingMode_Type.__name__ = "Integer32"
_Eth100gMappingMode_Object = MibTableColumn
eth100gMappingMode = _Eth100gMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 5),
    _Eth100gMappingMode_Type()
)
eth100gMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gMappingMode.setStatus("current")


class _Eth100gAdminStatus_Type(Integer32):
    """Custom type eth100gAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Eth100gAdminStatus_Type.__name__ = "Integer32"
_Eth100gAdminStatus_Object = MibTableColumn
eth100gAdminStatus = _Eth100gAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 6),
    _Eth100gAdminStatus_Type()
)
eth100gAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gAdminStatus.setStatus("current")


class _Eth100gOperStatus_Type(Integer32):
    """Custom type eth100gOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Eth100gOperStatus_Type.__name__ = "Integer32"
_Eth100gOperStatus_Object = MibTableColumn
eth100gOperStatus = _Eth100gOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 7),
    _Eth100gOperStatus_Type()
)
eth100gOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gOperStatus.setStatus("current")


class _Eth100gAvailStatus_Type(Bits):
    """Custom type eth100gAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Eth100gAvailStatus_Type.__name__ = "Bits"
_Eth100gAvailStatus_Object = MibTableColumn
eth100gAvailStatus = _Eth100gAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 8),
    _Eth100gAvailStatus_Type()
)
eth100gAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gAvailStatus.setStatus("current")


class _Eth100gAliasName_Type(OctetString):
    """Custom type eth100gAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Eth100gAliasName_Type.__name__ = "OctetString"
_Eth100gAliasName_Object = MibTableColumn
eth100gAliasName = _Eth100gAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 9),
    _Eth100gAliasName_Type()
)
eth100gAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gAliasName.setStatus("current")
_Eth100gClientShutdown_Type = CoriantTypesYesNo
_Eth100gClientShutdown_Object = MibTableColumn
eth100gClientShutdown = _Eth100gClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 10),
    _Eth100gClientShutdown_Type()
)
eth100gClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gClientShutdown.setStatus("current")


class _Eth100gClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type eth100gClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Eth100gClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Eth100gClientShutdownHoldoffTimer_Object = MibTableColumn
eth100gClientShutdownHoldoffTimer = _Eth100gClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 11),
    _Eth100gClientShutdownHoldoffTimer_Type()
)
eth100gClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gClientShutdownHoldoffTimer.setStatus("current")
_Eth100gNearEndAls_Type = CoriantTypesYesNo
_Eth100gNearEndAls_Object = MibTableColumn
eth100gNearEndAls = _Eth100gNearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 12),
    _Eth100gNearEndAls_Type()
)
eth100gNearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gNearEndAls.setStatus("current")
_Eth100gAlsDegradeMode_Type = CoriantTypesEnableSwitch
_Eth100gAlsDegradeMode_Object = MibTableColumn
eth100gAlsDegradeMode = _Eth100gAlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 13),
    _Eth100gAlsDegradeMode_Type()
)
eth100gAlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gAlsDegradeMode.setStatus("current")
_Eth100gLoopbackEnable_Type = CoriantTypesEnableSwitch
_Eth100gLoopbackEnable_Object = MibTableColumn
eth100gLoopbackEnable = _Eth100gLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 14),
    _Eth100gLoopbackEnable_Type()
)
eth100gLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gLoopbackEnable.setStatus("current")


class _Eth100gLoopbackType_Type(Integer32):
    """Custom type eth100gLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Eth100gLoopbackType_Type.__name__ = "Integer32"
_Eth100gLoopbackType_Object = MibTableColumn
eth100gLoopbackType = _Eth100gLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 15),
    _Eth100gLoopbackType_Type()
)
eth100gLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gLoopbackType.setStatus("current")
_Eth100gTestSignalType_Type = CoriantTypesTestSignalType
_Eth100gTestSignalType_Object = MibTableColumn
eth100gTestSignalType = _Eth100gTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 16),
    _Eth100gTestSignalType_Type()
)
eth100gTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gTestSignalType.setStatus("current")
_Eth100gTestSignalEnable_Type = CoriantTypesTestSignalConfig
_Eth100gTestSignalEnable_Object = MibTableColumn
eth100gTestSignalEnable = _Eth100gTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 17),
    _Eth100gTestSignalEnable_Type()
)
eth100gTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gTestSignalEnable.setStatus("current")


class _Eth100gServiceLabel_Type(OctetString):
    """Custom type eth100gServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eth100gServiceLabel_Type.__name__ = "OctetString"
_Eth100gServiceLabel_Object = MibTableColumn
eth100gServiceLabel = _Eth100gServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 18),
    _Eth100gServiceLabel_Type()
)
eth100gServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gServiceLabel.setStatus("current")


class _Eth100gLldpStatusIf_Type(Integer32):
    """Custom type eth100gLldpStatusIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("rxonly", 2),
          ("disabled", 4))
    )


_Eth100gLldpStatusIf_Type.__name__ = "Integer32"
_Eth100gLldpStatusIf_Object = MibTableColumn
eth100gLldpStatusIf = _Eth100gLldpStatusIf_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 19),
    _Eth100gLldpStatusIf_Type()
)
eth100gLldpStatusIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gLldpStatusIf.setStatus("current")
_Eth100gHoldoffSignal_Type = CoriantTypesYesNo
_Eth100gHoldoffSignal_Object = MibTableColumn
eth100gHoldoffSignal = _Eth100gHoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 9, 1, 1, 20),
    _Eth100gHoldoffSignal_Type()
)
eth100gHoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gHoldoffSignal.setStatus("current")
_Otu4_ObjectIdentity = ObjectIdentity
otu4 = _Otu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10)
)
_Otu4Table_Object = MibTable
otu4Table = _Otu4Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    otu4Table.setStatus("current")
_Otu4Entry_Object = MibTableRow
otu4Entry = _Otu4Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1)
)
otu4Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otu4Entry.setStatus("current")
_Otu4FecType_Type = CoriantTypesOtukFec
_Otu4FecType_Object = MibTableColumn
otu4FecType = _Otu4FecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 1),
    _Otu4FecType_Type()
)
otu4FecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4FecType.setStatus("current")


class _Otu4AdminStatus_Type(Integer32):
    """Custom type otu4AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otu4AdminStatus_Type.__name__ = "Integer32"
_Otu4AdminStatus_Object = MibTableColumn
otu4AdminStatus = _Otu4AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 2),
    _Otu4AdminStatus_Type()
)
otu4AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4AdminStatus.setStatus("current")


class _Otu4OperStatus_Type(Integer32):
    """Custom type otu4OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otu4OperStatus_Type.__name__ = "Integer32"
_Otu4OperStatus_Object = MibTableColumn
otu4OperStatus = _Otu4OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 3),
    _Otu4OperStatus_Type()
)
otu4OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4OperStatus.setStatus("current")


class _Otu4AvailStatus_Type(Bits):
    """Custom type otu4AvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Otu4AvailStatus_Type.__name__ = "Bits"
_Otu4AvailStatus_Object = MibTableColumn
otu4AvailStatus = _Otu4AvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 4),
    _Otu4AvailStatus_Type()
)
otu4AvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4AvailStatus.setStatus("current")


class _Otu4AliasName_Type(OctetString):
    """Custom type otu4AliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Otu4AliasName_Type.__name__ = "OctetString"
_Otu4AliasName_Object = MibTableColumn
otu4AliasName = _Otu4AliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 5),
    _Otu4AliasName_Type()
)
otu4AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4AliasName.setStatus("current")


class _Otu4ServiceLabel_Type(OctetString):
    """Custom type otu4ServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Otu4ServiceLabel_Type.__name__ = "OctetString"
_Otu4ServiceLabel_Object = MibTableColumn
otu4ServiceLabel = _Otu4ServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 6),
    _Otu4ServiceLabel_Type()
)
otu4ServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4ServiceLabel.setStatus("current")


class _Otu4ExpSapi_Type(OctetString):
    """Custom type otu4ExpSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu4ExpSapi_Type.__name__ = "OctetString"
_Otu4ExpSapi_Object = MibTableColumn
otu4ExpSapi = _Otu4ExpSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 7),
    _Otu4ExpSapi_Type()
)
otu4ExpSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4ExpSapi.setStatus("current")


class _Otu4ExpDapi_Type(OctetString):
    """Custom type otu4ExpDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu4ExpDapi_Type.__name__ = "OctetString"
_Otu4ExpDapi_Object = MibTableColumn
otu4ExpDapi = _Otu4ExpDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 8),
    _Otu4ExpDapi_Type()
)
otu4ExpDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4ExpDapi.setStatus("current")


class _Otu4ExpOperator_Type(OctetString):
    """Custom type otu4ExpOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu4ExpOperator_Type.__name__ = "OctetString"
_Otu4ExpOperator_Object = MibTableColumn
otu4ExpOperator = _Otu4ExpOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 9),
    _Otu4ExpOperator_Type()
)
otu4ExpOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4ExpOperator.setStatus("current")


class _Otu4TxSapi_Type(OctetString):
    """Custom type otu4TxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu4TxSapi_Type.__name__ = "OctetString"
_Otu4TxSapi_Object = MibTableColumn
otu4TxSapi = _Otu4TxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 10),
    _Otu4TxSapi_Type()
)
otu4TxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4TxSapi.setStatus("current")


class _Otu4TxDapi_Type(OctetString):
    """Custom type otu4TxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu4TxDapi_Type.__name__ = "OctetString"
_Otu4TxDapi_Object = MibTableColumn
otu4TxDapi = _Otu4TxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 11),
    _Otu4TxDapi_Type()
)
otu4TxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4TxDapi.setStatus("current")


class _Otu4TxOperator_Type(OctetString):
    """Custom type otu4TxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu4TxOperator_Type.__name__ = "OctetString"
_Otu4TxOperator_Object = MibTableColumn
otu4TxOperator = _Otu4TxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 12),
    _Otu4TxOperator_Type()
)
otu4TxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4TxOperator.setStatus("current")
_Otu4TimDefectMode_Type = CoriantTypesTimMode
_Otu4TimDefectMode_Object = MibTableColumn
otu4TimDefectMode = _Otu4TimDefectMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 13),
    _Otu4TimDefectMode_Type()
)
otu4TimDefectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4TimDefectMode.setStatus("current")
_Otu4TimAct_Type = CoriantTypesEnableSwitch
_Otu4TimAct_Object = MibTableColumn
otu4TimAct = _Otu4TimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 14),
    _Otu4TimAct_Type()
)
otu4TimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4TimAct.setStatus("current")


class _Otu4RxSapi_Type(OctetString):
    """Custom type otu4RxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu4RxSapi_Type.__name__ = "OctetString"
_Otu4RxSapi_Object = MibTableColumn
otu4RxSapi = _Otu4RxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 15),
    _Otu4RxSapi_Type()
)
otu4RxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4RxSapi.setStatus("current")


class _Otu4RxDapi_Type(OctetString):
    """Custom type otu4RxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu4RxDapi_Type.__name__ = "OctetString"
_Otu4RxDapi_Object = MibTableColumn
otu4RxDapi = _Otu4RxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 16),
    _Otu4RxDapi_Type()
)
otu4RxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4RxDapi.setStatus("current")


class _Otu4RxOperator_Type(OctetString):
    """Custom type otu4RxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu4RxOperator_Type.__name__ = "OctetString"
_Otu4RxOperator_Object = MibTableColumn
otu4RxOperator = _Otu4RxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 17),
    _Otu4RxOperator_Type()
)
otu4RxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4RxOperator.setStatus("current")


class _Otu4DegradeInterval_Type(Unsigned32):
    """Custom type otu4DegradeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Otu4DegradeInterval_Type.__name__ = "Unsigned32"
_Otu4DegradeInterval_Object = MibTableColumn
otu4DegradeInterval = _Otu4DegradeInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 18),
    _Otu4DegradeInterval_Type()
)
otu4DegradeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4DegradeInterval.setStatus("current")


class _Otu4DegradeThreshold_Type(Unsigned32):
    """Custom type otu4DegradeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2590845),
    )


_Otu4DegradeThreshold_Type.__name__ = "Unsigned32"
_Otu4DegradeThreshold_Object = MibTableColumn
otu4DegradeThreshold = _Otu4DegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 19),
    _Otu4DegradeThreshold_Type()
)
otu4DegradeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4DegradeThreshold.setStatus("current")
_Otu4LoopbackEnable_Type = CoriantTypesEnableSwitch
_Otu4LoopbackEnable_Object = MibTableColumn
otu4LoopbackEnable = _Otu4LoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 20),
    _Otu4LoopbackEnable_Type()
)
otu4LoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4LoopbackEnable.setStatus("current")


class _Otu4LoopbackType_Type(Integer32):
    """Custom type otu4LoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Otu4LoopbackType_Type.__name__ = "Integer32"
_Otu4LoopbackType_Object = MibTableColumn
otu4LoopbackType = _Otu4LoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 21),
    _Otu4LoopbackType_Type()
)
otu4LoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4LoopbackType.setStatus("current")
_Otu4ClientShutdown_Type = CoriantTypesYesNo
_Otu4ClientShutdown_Object = MibTableColumn
otu4ClientShutdown = _Otu4ClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 22),
    _Otu4ClientShutdown_Type()
)
otu4ClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4ClientShutdown.setStatus("current")


class _Otu4ClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type otu4ClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Otu4ClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Otu4ClientShutdownHoldoffTimer_Object = MibTableColumn
otu4ClientShutdownHoldoffTimer = _Otu4ClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 23),
    _Otu4ClientShutdownHoldoffTimer_Type()
)
otu4ClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4ClientShutdownHoldoffTimer.setStatus("current")
_Otu4HoldoffSignal_Type = CoriantTypesYesNo
_Otu4HoldoffSignal_Object = MibTableColumn
otu4HoldoffSignal = _Otu4HoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 24),
    _Otu4HoldoffSignal_Type()
)
otu4HoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4HoldoffSignal.setStatus("current")
_Otu4NearEndAls_Type = CoriantTypesYesNo
_Otu4NearEndAls_Object = MibTableColumn
otu4NearEndAls = _Otu4NearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 25),
    _Otu4NearEndAls_Type()
)
otu4NearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4NearEndAls.setStatus("current")
_Otu4AlsDegradeMode_Type = CoriantTypesEnableSwitch
_Otu4AlsDegradeMode_Object = MibTableColumn
otu4AlsDegradeMode = _Otu4AlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 10, 1, 1, 26),
    _Otu4AlsDegradeMode_Type()
)
otu4AlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4AlsDegradeMode.setStatus("current")
_Otu2_ObjectIdentity = ObjectIdentity
otu2 = _Otu2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11)
)
_Otu2Table_Object = MibTable
otu2Table = _Otu2Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    otu2Table.setStatus("current")
_Otu2Entry_Object = MibTableRow
otu2Entry = _Otu2Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1)
)
otu2Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otu2Entry.setStatus("current")
_Otu2FecType_Type = CoriantTypesOtukFec
_Otu2FecType_Object = MibTableColumn
otu2FecType = _Otu2FecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 1),
    _Otu2FecType_Type()
)
otu2FecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2FecType.setStatus("current")


class _Otu2AdminStatus_Type(Integer32):
    """Custom type otu2AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otu2AdminStatus_Type.__name__ = "Integer32"
_Otu2AdminStatus_Object = MibTableColumn
otu2AdminStatus = _Otu2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 2),
    _Otu2AdminStatus_Type()
)
otu2AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2AdminStatus.setStatus("current")


class _Otu2OperStatus_Type(Integer32):
    """Custom type otu2OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otu2OperStatus_Type.__name__ = "Integer32"
_Otu2OperStatus_Object = MibTableColumn
otu2OperStatus = _Otu2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 3),
    _Otu2OperStatus_Type()
)
otu2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2OperStatus.setStatus("current")


class _Otu2AvailStatus_Type(Bits):
    """Custom type otu2AvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Otu2AvailStatus_Type.__name__ = "Bits"
_Otu2AvailStatus_Object = MibTableColumn
otu2AvailStatus = _Otu2AvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 4),
    _Otu2AvailStatus_Type()
)
otu2AvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2AvailStatus.setStatus("current")


class _Otu2AliasName_Type(OctetString):
    """Custom type otu2AliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Otu2AliasName_Type.__name__ = "OctetString"
_Otu2AliasName_Object = MibTableColumn
otu2AliasName = _Otu2AliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 5),
    _Otu2AliasName_Type()
)
otu2AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2AliasName.setStatus("current")


class _Otu2ServiceLabel_Type(OctetString):
    """Custom type otu2ServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Otu2ServiceLabel_Type.__name__ = "OctetString"
_Otu2ServiceLabel_Object = MibTableColumn
otu2ServiceLabel = _Otu2ServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 6),
    _Otu2ServiceLabel_Type()
)
otu2ServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2ServiceLabel.setStatus("current")


class _Otu2ExpSapi_Type(OctetString):
    """Custom type otu2ExpSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2ExpSapi_Type.__name__ = "OctetString"
_Otu2ExpSapi_Object = MibTableColumn
otu2ExpSapi = _Otu2ExpSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 7),
    _Otu2ExpSapi_Type()
)
otu2ExpSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2ExpSapi.setStatus("current")


class _Otu2ExpDapi_Type(OctetString):
    """Custom type otu2ExpDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2ExpDapi_Type.__name__ = "OctetString"
_Otu2ExpDapi_Object = MibTableColumn
otu2ExpDapi = _Otu2ExpDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 8),
    _Otu2ExpDapi_Type()
)
otu2ExpDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2ExpDapi.setStatus("current")


class _Otu2ExpOperator_Type(OctetString):
    """Custom type otu2ExpOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu2ExpOperator_Type.__name__ = "OctetString"
_Otu2ExpOperator_Object = MibTableColumn
otu2ExpOperator = _Otu2ExpOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 9),
    _Otu2ExpOperator_Type()
)
otu2ExpOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2ExpOperator.setStatus("current")


class _Otu2TxSapi_Type(OctetString):
    """Custom type otu2TxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2TxSapi_Type.__name__ = "OctetString"
_Otu2TxSapi_Object = MibTableColumn
otu2TxSapi = _Otu2TxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 10),
    _Otu2TxSapi_Type()
)
otu2TxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2TxSapi.setStatus("current")


class _Otu2TxDapi_Type(OctetString):
    """Custom type otu2TxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2TxDapi_Type.__name__ = "OctetString"
_Otu2TxDapi_Object = MibTableColumn
otu2TxDapi = _Otu2TxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 11),
    _Otu2TxDapi_Type()
)
otu2TxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2TxDapi.setStatus("current")


class _Otu2TxOperator_Type(OctetString):
    """Custom type otu2TxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu2TxOperator_Type.__name__ = "OctetString"
_Otu2TxOperator_Object = MibTableColumn
otu2TxOperator = _Otu2TxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 12),
    _Otu2TxOperator_Type()
)
otu2TxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2TxOperator.setStatus("current")
_Otu2TimDefectMode_Type = CoriantTypesTimMode
_Otu2TimDefectMode_Object = MibTableColumn
otu2TimDefectMode = _Otu2TimDefectMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 13),
    _Otu2TimDefectMode_Type()
)
otu2TimDefectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2TimDefectMode.setStatus("current")
_Otu2TimAct_Type = CoriantTypesEnableSwitch
_Otu2TimAct_Object = MibTableColumn
otu2TimAct = _Otu2TimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 14),
    _Otu2TimAct_Type()
)
otu2TimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2TimAct.setStatus("current")


class _Otu2RxSapi_Type(OctetString):
    """Custom type otu2RxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2RxSapi_Type.__name__ = "OctetString"
_Otu2RxSapi_Object = MibTableColumn
otu2RxSapi = _Otu2RxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 15),
    _Otu2RxSapi_Type()
)
otu2RxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2RxSapi.setStatus("current")


class _Otu2RxDapi_Type(OctetString):
    """Custom type otu2RxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2RxDapi_Type.__name__ = "OctetString"
_Otu2RxDapi_Object = MibTableColumn
otu2RxDapi = _Otu2RxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 16),
    _Otu2RxDapi_Type()
)
otu2RxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2RxDapi.setStatus("current")


class _Otu2RxOperator_Type(OctetString):
    """Custom type otu2RxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu2RxOperator_Type.__name__ = "OctetString"
_Otu2RxOperator_Object = MibTableColumn
otu2RxOperator = _Otu2RxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 17),
    _Otu2RxOperator_Type()
)
otu2RxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2RxOperator.setStatus("current")


class _Otu2DegradeInterval_Type(Unsigned32):
    """Custom type otu2DegradeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Otu2DegradeInterval_Type.__name__ = "Unsigned32"
_Otu2DegradeInterval_Object = MibTableColumn
otu2DegradeInterval = _Otu2DegradeInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 18),
    _Otu2DegradeInterval_Type()
)
otu2DegradeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2DegradeInterval.setStatus("current")


class _Otu2DegradeThreshold_Type(Unsigned32):
    """Custom type otu2DegradeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2590845),
    )


_Otu2DegradeThreshold_Type.__name__ = "Unsigned32"
_Otu2DegradeThreshold_Object = MibTableColumn
otu2DegradeThreshold = _Otu2DegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 19),
    _Otu2DegradeThreshold_Type()
)
otu2DegradeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2DegradeThreshold.setStatus("current")
_Otu2LoopbackEnable_Type = CoriantTypesEnableSwitch
_Otu2LoopbackEnable_Object = MibTableColumn
otu2LoopbackEnable = _Otu2LoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 20),
    _Otu2LoopbackEnable_Type()
)
otu2LoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2LoopbackEnable.setStatus("current")


class _Otu2LoopbackType_Type(Integer32):
    """Custom type otu2LoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Otu2LoopbackType_Type.__name__ = "Integer32"
_Otu2LoopbackType_Object = MibTableColumn
otu2LoopbackType = _Otu2LoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 11, 1, 1, 21),
    _Otu2LoopbackType_Type()
)
otu2LoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2LoopbackType.setStatus("current")
_Otu2e_ObjectIdentity = ObjectIdentity
otu2e = _Otu2e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12)
)
_Otu2eTable_Object = MibTable
otu2eTable = _Otu2eTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1)
)
if mibBuilder.loadTexts:
    otu2eTable.setStatus("current")
_Otu2eEntry_Object = MibTableRow
otu2eEntry = _Otu2eEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1)
)
otu2eEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otu2eEntry.setStatus("current")
_Otu2eFecType_Type = CoriantTypesOtukFec
_Otu2eFecType_Object = MibTableColumn
otu2eFecType = _Otu2eFecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 1),
    _Otu2eFecType_Type()
)
otu2eFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eFecType.setStatus("current")


class _Otu2eAdminStatus_Type(Integer32):
    """Custom type otu2eAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otu2eAdminStatus_Type.__name__ = "Integer32"
_Otu2eAdminStatus_Object = MibTableColumn
otu2eAdminStatus = _Otu2eAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 2),
    _Otu2eAdminStatus_Type()
)
otu2eAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eAdminStatus.setStatus("current")


class _Otu2eOperStatus_Type(Integer32):
    """Custom type otu2eOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otu2eOperStatus_Type.__name__ = "Integer32"
_Otu2eOperStatus_Object = MibTableColumn
otu2eOperStatus = _Otu2eOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 3),
    _Otu2eOperStatus_Type()
)
otu2eOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eOperStatus.setStatus("current")


class _Otu2eAvailStatus_Type(Bits):
    """Custom type otu2eAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Otu2eAvailStatus_Type.__name__ = "Bits"
_Otu2eAvailStatus_Object = MibTableColumn
otu2eAvailStatus = _Otu2eAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 4),
    _Otu2eAvailStatus_Type()
)
otu2eAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eAvailStatus.setStatus("current")


class _Otu2eAliasName_Type(OctetString):
    """Custom type otu2eAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Otu2eAliasName_Type.__name__ = "OctetString"
_Otu2eAliasName_Object = MibTableColumn
otu2eAliasName = _Otu2eAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 5),
    _Otu2eAliasName_Type()
)
otu2eAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eAliasName.setStatus("current")


class _Otu2eServiceLabel_Type(OctetString):
    """Custom type otu2eServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Otu2eServiceLabel_Type.__name__ = "OctetString"
_Otu2eServiceLabel_Object = MibTableColumn
otu2eServiceLabel = _Otu2eServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 6),
    _Otu2eServiceLabel_Type()
)
otu2eServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eServiceLabel.setStatus("current")


class _Otu2eExpSapi_Type(OctetString):
    """Custom type otu2eExpSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2eExpSapi_Type.__name__ = "OctetString"
_Otu2eExpSapi_Object = MibTableColumn
otu2eExpSapi = _Otu2eExpSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 7),
    _Otu2eExpSapi_Type()
)
otu2eExpSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eExpSapi.setStatus("current")


class _Otu2eExpDapi_Type(OctetString):
    """Custom type otu2eExpDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2eExpDapi_Type.__name__ = "OctetString"
_Otu2eExpDapi_Object = MibTableColumn
otu2eExpDapi = _Otu2eExpDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 8),
    _Otu2eExpDapi_Type()
)
otu2eExpDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eExpDapi.setStatus("current")


class _Otu2eExpOperator_Type(OctetString):
    """Custom type otu2eExpOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu2eExpOperator_Type.__name__ = "OctetString"
_Otu2eExpOperator_Object = MibTableColumn
otu2eExpOperator = _Otu2eExpOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 9),
    _Otu2eExpOperator_Type()
)
otu2eExpOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eExpOperator.setStatus("current")


class _Otu2eTxSapi_Type(OctetString):
    """Custom type otu2eTxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2eTxSapi_Type.__name__ = "OctetString"
_Otu2eTxSapi_Object = MibTableColumn
otu2eTxSapi = _Otu2eTxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 10),
    _Otu2eTxSapi_Type()
)
otu2eTxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eTxSapi.setStatus("current")


class _Otu2eTxDapi_Type(OctetString):
    """Custom type otu2eTxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2eTxDapi_Type.__name__ = "OctetString"
_Otu2eTxDapi_Object = MibTableColumn
otu2eTxDapi = _Otu2eTxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 11),
    _Otu2eTxDapi_Type()
)
otu2eTxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eTxDapi.setStatus("current")


class _Otu2eTxOperator_Type(OctetString):
    """Custom type otu2eTxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu2eTxOperator_Type.__name__ = "OctetString"
_Otu2eTxOperator_Object = MibTableColumn
otu2eTxOperator = _Otu2eTxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 12),
    _Otu2eTxOperator_Type()
)
otu2eTxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eTxOperator.setStatus("current")
_Otu2eTimDefectMode_Type = CoriantTypesTimMode
_Otu2eTimDefectMode_Object = MibTableColumn
otu2eTimDefectMode = _Otu2eTimDefectMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 13),
    _Otu2eTimDefectMode_Type()
)
otu2eTimDefectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eTimDefectMode.setStatus("current")
_Otu2eTimAct_Type = CoriantTypesEnableSwitch
_Otu2eTimAct_Object = MibTableColumn
otu2eTimAct = _Otu2eTimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 14),
    _Otu2eTimAct_Type()
)
otu2eTimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eTimAct.setStatus("current")


class _Otu2eRxSapi_Type(OctetString):
    """Custom type otu2eRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2eRxSapi_Type.__name__ = "OctetString"
_Otu2eRxSapi_Object = MibTableColumn
otu2eRxSapi = _Otu2eRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 15),
    _Otu2eRxSapi_Type()
)
otu2eRxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eRxSapi.setStatus("current")


class _Otu2eRxDapi_Type(OctetString):
    """Custom type otu2eRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otu2eRxDapi_Type.__name__ = "OctetString"
_Otu2eRxDapi_Object = MibTableColumn
otu2eRxDapi = _Otu2eRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 16),
    _Otu2eRxDapi_Type()
)
otu2eRxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eRxDapi.setStatus("current")


class _Otu2eRxOperator_Type(OctetString):
    """Custom type otu2eRxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otu2eRxOperator_Type.__name__ = "OctetString"
_Otu2eRxOperator_Object = MibTableColumn
otu2eRxOperator = _Otu2eRxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 17),
    _Otu2eRxOperator_Type()
)
otu2eRxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eRxOperator.setStatus("current")


class _Otu2eDegradeInterval_Type(Unsigned32):
    """Custom type otu2eDegradeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Otu2eDegradeInterval_Type.__name__ = "Unsigned32"
_Otu2eDegradeInterval_Object = MibTableColumn
otu2eDegradeInterval = _Otu2eDegradeInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 18),
    _Otu2eDegradeInterval_Type()
)
otu2eDegradeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eDegradeInterval.setStatus("current")


class _Otu2eDegradeThreshold_Type(Unsigned32):
    """Custom type otu2eDegradeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2590845),
    )


_Otu2eDegradeThreshold_Type.__name__ = "Unsigned32"
_Otu2eDegradeThreshold_Object = MibTableColumn
otu2eDegradeThreshold = _Otu2eDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 19),
    _Otu2eDegradeThreshold_Type()
)
otu2eDegradeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eDegradeThreshold.setStatus("current")
_Otu2eLoopbackEnable_Type = CoriantTypesEnableSwitch
_Otu2eLoopbackEnable_Object = MibTableColumn
otu2eLoopbackEnable = _Otu2eLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 20),
    _Otu2eLoopbackEnable_Type()
)
otu2eLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eLoopbackEnable.setStatus("current")


class _Otu2eLoopbackType_Type(Integer32):
    """Custom type otu2eLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Otu2eLoopbackType_Type.__name__ = "Integer32"
_Otu2eLoopbackType_Object = MibTableColumn
otu2eLoopbackType = _Otu2eLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 12, 1, 1, 21),
    _Otu2eLoopbackType_Type()
)
otu2eLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eLoopbackType.setStatus("current")
_Fc8g_ObjectIdentity = ObjectIdentity
fc8g = _Fc8g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13)
)
_Fc8gTable_Object = MibTable
fc8gTable = _Fc8gTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    fc8gTable.setStatus("current")
_Fc8gEntry_Object = MibTableRow
fc8gEntry = _Fc8gEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1)
)
fc8gEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    fc8gEntry.setStatus("current")


class _Fc8gMappingMode_Type(Integer32):
    """Custom type fc8gMappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Fc8gMappingMode_Type.__name__ = "Integer32"
_Fc8gMappingMode_Object = MibTableColumn
fc8gMappingMode = _Fc8gMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 1),
    _Fc8gMappingMode_Type()
)
fc8gMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gMappingMode.setStatus("current")


class _Fc8gAdminStatus_Type(Integer32):
    """Custom type fc8gAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Fc8gAdminStatus_Type.__name__ = "Integer32"
_Fc8gAdminStatus_Object = MibTableColumn
fc8gAdminStatus = _Fc8gAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 2),
    _Fc8gAdminStatus_Type()
)
fc8gAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gAdminStatus.setStatus("current")


class _Fc8gOperStatus_Type(Integer32):
    """Custom type fc8gOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Fc8gOperStatus_Type.__name__ = "Integer32"
_Fc8gOperStatus_Object = MibTableColumn
fc8gOperStatus = _Fc8gOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 3),
    _Fc8gOperStatus_Type()
)
fc8gOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gOperStatus.setStatus("current")


class _Fc8gAvailStatus_Type(Bits):
    """Custom type fc8gAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Fc8gAvailStatus_Type.__name__ = "Bits"
_Fc8gAvailStatus_Object = MibTableColumn
fc8gAvailStatus = _Fc8gAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 4),
    _Fc8gAvailStatus_Type()
)
fc8gAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gAvailStatus.setStatus("current")


class _Fc8gAliasName_Type(OctetString):
    """Custom type fc8gAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Fc8gAliasName_Type.__name__ = "OctetString"
_Fc8gAliasName_Object = MibTableColumn
fc8gAliasName = _Fc8gAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 5),
    _Fc8gAliasName_Type()
)
fc8gAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gAliasName.setStatus("current")
_Fc8gClientShutdown_Type = CoriantTypesYesNo
_Fc8gClientShutdown_Object = MibTableColumn
fc8gClientShutdown = _Fc8gClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 6),
    _Fc8gClientShutdown_Type()
)
fc8gClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gClientShutdown.setStatus("current")


class _Fc8gClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type fc8gClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Fc8gClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Fc8gClientShutdownHoldoffTimer_Object = MibTableColumn
fc8gClientShutdownHoldoffTimer = _Fc8gClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 7),
    _Fc8gClientShutdownHoldoffTimer_Type()
)
fc8gClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gClientShutdownHoldoffTimer.setStatus("current")
_Fc8gNearEndAls_Type = CoriantTypesYesNo
_Fc8gNearEndAls_Object = MibTableColumn
fc8gNearEndAls = _Fc8gNearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 8),
    _Fc8gNearEndAls_Type()
)
fc8gNearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gNearEndAls.setStatus("current")
_Fc8gAlsDegradeMode_Type = CoriantTypesEnableSwitch
_Fc8gAlsDegradeMode_Object = MibTableColumn
fc8gAlsDegradeMode = _Fc8gAlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 9),
    _Fc8gAlsDegradeMode_Type()
)
fc8gAlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gAlsDegradeMode.setStatus("current")
_Fc8gLoopbackEnable_Type = CoriantTypesEnableSwitch
_Fc8gLoopbackEnable_Object = MibTableColumn
fc8gLoopbackEnable = _Fc8gLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 10),
    _Fc8gLoopbackEnable_Type()
)
fc8gLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gLoopbackEnable.setStatus("current")


class _Fc8gLoopbackType_Type(Integer32):
    """Custom type fc8gLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Fc8gLoopbackType_Type.__name__ = "Integer32"
_Fc8gLoopbackType_Object = MibTableColumn
fc8gLoopbackType = _Fc8gLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 11),
    _Fc8gLoopbackType_Type()
)
fc8gLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gLoopbackType.setStatus("current")
_Fc8gTestSignalType_Type = CoriantTypesTestSignalType
_Fc8gTestSignalType_Object = MibTableColumn
fc8gTestSignalType = _Fc8gTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 12),
    _Fc8gTestSignalType_Type()
)
fc8gTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gTestSignalType.setStatus("current")
_Fc8gTestSignalEnable_Type = CoriantTypesTestSignalConfig
_Fc8gTestSignalEnable_Object = MibTableColumn
fc8gTestSignalEnable = _Fc8gTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 13),
    _Fc8gTestSignalEnable_Type()
)
fc8gTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gTestSignalEnable.setStatus("current")


class _Fc8gServiceLabel_Type(OctetString):
    """Custom type fc8gServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Fc8gServiceLabel_Type.__name__ = "OctetString"
_Fc8gServiceLabel_Object = MibTableColumn
fc8gServiceLabel = _Fc8gServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 14),
    _Fc8gServiceLabel_Type()
)
fc8gServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gServiceLabel.setStatus("current")
_Fc8gHoldoffSignal_Type = CoriantTypesYesNo
_Fc8gHoldoffSignal_Object = MibTableColumn
fc8gHoldoffSignal = _Fc8gHoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 13, 1, 1, 15),
    _Fc8gHoldoffSignal_Type()
)
fc8gHoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gHoldoffSignal.setStatus("current")
_Fc16g_ObjectIdentity = ObjectIdentity
fc16g = _Fc16g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14)
)
_Fc16gTable_Object = MibTable
fc16gTable = _Fc16gTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1)
)
if mibBuilder.loadTexts:
    fc16gTable.setStatus("current")
_Fc16gEntry_Object = MibTableRow
fc16gEntry = _Fc16gEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1)
)
fc16gEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    fc16gEntry.setStatus("current")


class _Fc16gMappingMode_Type(Integer32):
    """Custom type fc16gMappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Fc16gMappingMode_Type.__name__ = "Integer32"
_Fc16gMappingMode_Object = MibTableColumn
fc16gMappingMode = _Fc16gMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 1),
    _Fc16gMappingMode_Type()
)
fc16gMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gMappingMode.setStatus("current")


class _Fc16gAdminStatus_Type(Integer32):
    """Custom type fc16gAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Fc16gAdminStatus_Type.__name__ = "Integer32"
_Fc16gAdminStatus_Object = MibTableColumn
fc16gAdminStatus = _Fc16gAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 2),
    _Fc16gAdminStatus_Type()
)
fc16gAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gAdminStatus.setStatus("current")


class _Fc16gOperStatus_Type(Integer32):
    """Custom type fc16gOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Fc16gOperStatus_Type.__name__ = "Integer32"
_Fc16gOperStatus_Object = MibTableColumn
fc16gOperStatus = _Fc16gOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 3),
    _Fc16gOperStatus_Type()
)
fc16gOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gOperStatus.setStatus("current")


class _Fc16gAvailStatus_Type(Bits):
    """Custom type fc16gAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Fc16gAvailStatus_Type.__name__ = "Bits"
_Fc16gAvailStatus_Object = MibTableColumn
fc16gAvailStatus = _Fc16gAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 4),
    _Fc16gAvailStatus_Type()
)
fc16gAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gAvailStatus.setStatus("current")


class _Fc16gAliasName_Type(OctetString):
    """Custom type fc16gAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Fc16gAliasName_Type.__name__ = "OctetString"
_Fc16gAliasName_Object = MibTableColumn
fc16gAliasName = _Fc16gAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 5),
    _Fc16gAliasName_Type()
)
fc16gAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gAliasName.setStatus("current")
_Fc16gClientShutdown_Type = CoriantTypesYesNo
_Fc16gClientShutdown_Object = MibTableColumn
fc16gClientShutdown = _Fc16gClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 6),
    _Fc16gClientShutdown_Type()
)
fc16gClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gClientShutdown.setStatus("current")


class _Fc16gClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type fc16gClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Fc16gClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Fc16gClientShutdownHoldoffTimer_Object = MibTableColumn
fc16gClientShutdownHoldoffTimer = _Fc16gClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 7),
    _Fc16gClientShutdownHoldoffTimer_Type()
)
fc16gClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gClientShutdownHoldoffTimer.setStatus("current")
_Fc16gNearEndAls_Type = CoriantTypesYesNo
_Fc16gNearEndAls_Object = MibTableColumn
fc16gNearEndAls = _Fc16gNearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 8),
    _Fc16gNearEndAls_Type()
)
fc16gNearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gNearEndAls.setStatus("current")
_Fc16gAlsDegradeMode_Type = CoriantTypesEnableSwitch
_Fc16gAlsDegradeMode_Object = MibTableColumn
fc16gAlsDegradeMode = _Fc16gAlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 9),
    _Fc16gAlsDegradeMode_Type()
)
fc16gAlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gAlsDegradeMode.setStatus("current")
_Fc16gLoopbackEnable_Type = CoriantTypesEnableSwitch
_Fc16gLoopbackEnable_Object = MibTableColumn
fc16gLoopbackEnable = _Fc16gLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 10),
    _Fc16gLoopbackEnable_Type()
)
fc16gLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gLoopbackEnable.setStatus("current")


class _Fc16gLoopbackType_Type(Integer32):
    """Custom type fc16gLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Fc16gLoopbackType_Type.__name__ = "Integer32"
_Fc16gLoopbackType_Object = MibTableColumn
fc16gLoopbackType = _Fc16gLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 11),
    _Fc16gLoopbackType_Type()
)
fc16gLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gLoopbackType.setStatus("current")
_Fc16gTestSignalType_Type = CoriantTypesTestSignalType
_Fc16gTestSignalType_Object = MibTableColumn
fc16gTestSignalType = _Fc16gTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 12),
    _Fc16gTestSignalType_Type()
)
fc16gTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gTestSignalType.setStatus("current")
_Fc16gTestSignalEnable_Type = CoriantTypesTestSignalConfig
_Fc16gTestSignalEnable_Object = MibTableColumn
fc16gTestSignalEnable = _Fc16gTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 13),
    _Fc16gTestSignalEnable_Type()
)
fc16gTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gTestSignalEnable.setStatus("current")


class _Fc16gServiceLabel_Type(OctetString):
    """Custom type fc16gServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Fc16gServiceLabel_Type.__name__ = "OctetString"
_Fc16gServiceLabel_Object = MibTableColumn
fc16gServiceLabel = _Fc16gServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 14),
    _Fc16gServiceLabel_Type()
)
fc16gServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gServiceLabel.setStatus("current")
_Fc16gHoldoffSignal_Type = CoriantTypesYesNo
_Fc16gHoldoffSignal_Object = MibTableColumn
fc16gHoldoffSignal = _Fc16gHoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 14, 1, 1, 15),
    _Fc16gHoldoffSignal_Type()
)
fc16gHoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gHoldoffSignal.setStatus("current")
_Oc192_ObjectIdentity = ObjectIdentity
oc192 = _Oc192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15)
)
_Oc192Table_Object = MibTable
oc192Table = _Oc192Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    oc192Table.setStatus("current")
_Oc192Entry_Object = MibTableRow
oc192Entry = _Oc192Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1)
)
oc192Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    oc192Entry.setStatus("current")


class _Oc192MappingMode_Type(Integer32):
    """Custom type oc192MappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Oc192MappingMode_Type.__name__ = "Integer32"
_Oc192MappingMode_Object = MibTableColumn
oc192MappingMode = _Oc192MappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 1),
    _Oc192MappingMode_Type()
)
oc192MappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192MappingMode.setStatus("current")


class _Oc192AdminStatus_Type(Integer32):
    """Custom type oc192AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Oc192AdminStatus_Type.__name__ = "Integer32"
_Oc192AdminStatus_Object = MibTableColumn
oc192AdminStatus = _Oc192AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 2),
    _Oc192AdminStatus_Type()
)
oc192AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192AdminStatus.setStatus("current")


class _Oc192OperStatus_Type(Integer32):
    """Custom type oc192OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Oc192OperStatus_Type.__name__ = "Integer32"
_Oc192OperStatus_Object = MibTableColumn
oc192OperStatus = _Oc192OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 3),
    _Oc192OperStatus_Type()
)
oc192OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192OperStatus.setStatus("current")


class _Oc192AvailStatus_Type(Bits):
    """Custom type oc192AvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Oc192AvailStatus_Type.__name__ = "Bits"
_Oc192AvailStatus_Object = MibTableColumn
oc192AvailStatus = _Oc192AvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 4),
    _Oc192AvailStatus_Type()
)
oc192AvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192AvailStatus.setStatus("current")


class _Oc192AliasName_Type(OctetString):
    """Custom type oc192AliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Oc192AliasName_Type.__name__ = "OctetString"
_Oc192AliasName_Object = MibTableColumn
oc192AliasName = _Oc192AliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 5),
    _Oc192AliasName_Type()
)
oc192AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192AliasName.setStatus("current")
_Oc192ClientShutdown_Type = CoriantTypesYesNo
_Oc192ClientShutdown_Object = MibTableColumn
oc192ClientShutdown = _Oc192ClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 6),
    _Oc192ClientShutdown_Type()
)
oc192ClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192ClientShutdown.setStatus("current")


class _Oc192ClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type oc192ClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Oc192ClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Oc192ClientShutdownHoldoffTimer_Object = MibTableColumn
oc192ClientShutdownHoldoffTimer = _Oc192ClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 7),
    _Oc192ClientShutdownHoldoffTimer_Type()
)
oc192ClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192ClientShutdownHoldoffTimer.setStatus("current")
_Oc192NearEndAls_Type = CoriantTypesYesNo
_Oc192NearEndAls_Object = MibTableColumn
oc192NearEndAls = _Oc192NearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 8),
    _Oc192NearEndAls_Type()
)
oc192NearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192NearEndAls.setStatus("current")
_Oc192AlsDegradeMode_Type = CoriantTypesEnableSwitch
_Oc192AlsDegradeMode_Object = MibTableColumn
oc192AlsDegradeMode = _Oc192AlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 9),
    _Oc192AlsDegradeMode_Type()
)
oc192AlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192AlsDegradeMode.setStatus("current")
_Oc192LoopbackEnable_Type = CoriantTypesEnableSwitch
_Oc192LoopbackEnable_Object = MibTableColumn
oc192LoopbackEnable = _Oc192LoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 10),
    _Oc192LoopbackEnable_Type()
)
oc192LoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192LoopbackEnable.setStatus("current")


class _Oc192LoopbackType_Type(Integer32):
    """Custom type oc192LoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Oc192LoopbackType_Type.__name__ = "Integer32"
_Oc192LoopbackType_Object = MibTableColumn
oc192LoopbackType = _Oc192LoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 11),
    _Oc192LoopbackType_Type()
)
oc192LoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192LoopbackType.setStatus("current")
_Oc192TestSignalType_Type = CoriantTypesTestSignalType
_Oc192TestSignalType_Object = MibTableColumn
oc192TestSignalType = _Oc192TestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 12),
    _Oc192TestSignalType_Type()
)
oc192TestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192TestSignalType.setStatus("current")
_Oc192TestSignalEnable_Type = CoriantTypesTestSignalConfig
_Oc192TestSignalEnable_Object = MibTableColumn
oc192TestSignalEnable = _Oc192TestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 13),
    _Oc192TestSignalEnable_Type()
)
oc192TestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192TestSignalEnable.setStatus("current")


class _Oc192ServiceLabel_Type(OctetString):
    """Custom type oc192ServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Oc192ServiceLabel_Type.__name__ = "OctetString"
_Oc192ServiceLabel_Object = MibTableColumn
oc192ServiceLabel = _Oc192ServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 14),
    _Oc192ServiceLabel_Type()
)
oc192ServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192ServiceLabel.setStatus("current")


class _Oc192ExpTrc_Type(OctetString):
    """Custom type oc192ExpTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Oc192ExpTrc_Type.__name__ = "OctetString"
_Oc192ExpTrc_Object = MibTableColumn
oc192ExpTrc = _Oc192ExpTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 15),
    _Oc192ExpTrc_Type()
)
oc192ExpTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192ExpTrc.setStatus("current")


class _Oc192TxTrc_Type(OctetString):
    """Custom type oc192TxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Oc192TxTrc_Type.__name__ = "OctetString"
_Oc192TxTrc_Object = MibTableColumn
oc192TxTrc = _Oc192TxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 16),
    _Oc192TxTrc_Type()
)
oc192TxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192TxTrc.setStatus("current")


class _Oc192RxTrc_Type(OctetString):
    """Custom type oc192RxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Oc192RxTrc_Type.__name__ = "OctetString"
_Oc192RxTrc_Object = MibTableColumn
oc192RxTrc = _Oc192RxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 17),
    _Oc192RxTrc_Type()
)
oc192RxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192RxTrc.setStatus("current")
_Oc192TimAct_Type = CoriantTypesEnableSwitch
_Oc192TimAct_Object = MibTableColumn
oc192TimAct = _Oc192TimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 18),
    _Oc192TimAct_Type()
)
oc192TimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192TimAct.setStatus("current")
_Oc192TimMonitor_Type = CoriantTypesEnableSwitch
_Oc192TimMonitor_Object = MibTableColumn
oc192TimMonitor = _Oc192TimMonitor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 19),
    _Oc192TimMonitor_Type()
)
oc192TimMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192TimMonitor.setStatus("current")


class _Oc192AisType_Type(Integer32):
    """Custom type oc192AisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("genericAis", 0),
          ("msAis", 1),
          ("aisL", 2))
    )


_Oc192AisType_Type.__name__ = "Integer32"
_Oc192AisType_Object = MibTableColumn
oc192AisType = _Oc192AisType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 20),
    _Oc192AisType_Type()
)
oc192AisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192AisType.setStatus("current")
_Oc192HoldoffSignal_Type = CoriantTypesYesNo
_Oc192HoldoffSignal_Object = MibTableColumn
oc192HoldoffSignal = _Oc192HoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 15, 1, 1, 21),
    _Oc192HoldoffSignal_Type()
)
oc192HoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192HoldoffSignal.setStatus("current")
_Stm64_ObjectIdentity = ObjectIdentity
stm64 = _Stm64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16)
)
_Stm64Table_Object = MibTable
stm64Table = _Stm64Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    stm64Table.setStatus("current")
_Stm64Entry_Object = MibTableRow
stm64Entry = _Stm64Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1)
)
stm64Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    stm64Entry.setStatus("current")


class _Stm64MappingMode_Type(Integer32):
    """Custom type stm64MappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Stm64MappingMode_Type.__name__ = "Integer32"
_Stm64MappingMode_Object = MibTableColumn
stm64MappingMode = _Stm64MappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 1),
    _Stm64MappingMode_Type()
)
stm64MappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64MappingMode.setStatus("current")


class _Stm64AdminStatus_Type(Integer32):
    """Custom type stm64AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Stm64AdminStatus_Type.__name__ = "Integer32"
_Stm64AdminStatus_Object = MibTableColumn
stm64AdminStatus = _Stm64AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 2),
    _Stm64AdminStatus_Type()
)
stm64AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64AdminStatus.setStatus("current")


class _Stm64OperStatus_Type(Integer32):
    """Custom type stm64OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Stm64OperStatus_Type.__name__ = "Integer32"
_Stm64OperStatus_Object = MibTableColumn
stm64OperStatus = _Stm64OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 3),
    _Stm64OperStatus_Type()
)
stm64OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64OperStatus.setStatus("current")


class _Stm64AvailStatus_Type(Bits):
    """Custom type stm64AvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Stm64AvailStatus_Type.__name__ = "Bits"
_Stm64AvailStatus_Object = MibTableColumn
stm64AvailStatus = _Stm64AvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 4),
    _Stm64AvailStatus_Type()
)
stm64AvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64AvailStatus.setStatus("current")


class _Stm64AliasName_Type(OctetString):
    """Custom type stm64AliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Stm64AliasName_Type.__name__ = "OctetString"
_Stm64AliasName_Object = MibTableColumn
stm64AliasName = _Stm64AliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 5),
    _Stm64AliasName_Type()
)
stm64AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64AliasName.setStatus("current")
_Stm64ClientShutdown_Type = CoriantTypesYesNo
_Stm64ClientShutdown_Object = MibTableColumn
stm64ClientShutdown = _Stm64ClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 6),
    _Stm64ClientShutdown_Type()
)
stm64ClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64ClientShutdown.setStatus("current")


class _Stm64ClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type stm64ClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Stm64ClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Stm64ClientShutdownHoldoffTimer_Object = MibTableColumn
stm64ClientShutdownHoldoffTimer = _Stm64ClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 7),
    _Stm64ClientShutdownHoldoffTimer_Type()
)
stm64ClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64ClientShutdownHoldoffTimer.setStatus("current")
_Stm64NearEndAls_Type = CoriantTypesYesNo
_Stm64NearEndAls_Object = MibTableColumn
stm64NearEndAls = _Stm64NearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 8),
    _Stm64NearEndAls_Type()
)
stm64NearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64NearEndAls.setStatus("current")
_Stm64AlsDegradeMode_Type = CoriantTypesEnableSwitch
_Stm64AlsDegradeMode_Object = MibTableColumn
stm64AlsDegradeMode = _Stm64AlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 9),
    _Stm64AlsDegradeMode_Type()
)
stm64AlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64AlsDegradeMode.setStatus("current")
_Stm64LoopbackEnable_Type = CoriantTypesEnableSwitch
_Stm64LoopbackEnable_Object = MibTableColumn
stm64LoopbackEnable = _Stm64LoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 10),
    _Stm64LoopbackEnable_Type()
)
stm64LoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64LoopbackEnable.setStatus("current")


class _Stm64LoopbackType_Type(Integer32):
    """Custom type stm64LoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Stm64LoopbackType_Type.__name__ = "Integer32"
_Stm64LoopbackType_Object = MibTableColumn
stm64LoopbackType = _Stm64LoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 11),
    _Stm64LoopbackType_Type()
)
stm64LoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64LoopbackType.setStatus("current")
_Stm64TestSignalType_Type = CoriantTypesTestSignalType
_Stm64TestSignalType_Object = MibTableColumn
stm64TestSignalType = _Stm64TestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 12),
    _Stm64TestSignalType_Type()
)
stm64TestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64TestSignalType.setStatus("current")
_Stm64TestSignalEnable_Type = CoriantTypesTestSignalConfig
_Stm64TestSignalEnable_Object = MibTableColumn
stm64TestSignalEnable = _Stm64TestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 13),
    _Stm64TestSignalEnable_Type()
)
stm64TestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64TestSignalEnable.setStatus("current")


class _Stm64ServiceLabel_Type(OctetString):
    """Custom type stm64ServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Stm64ServiceLabel_Type.__name__ = "OctetString"
_Stm64ServiceLabel_Object = MibTableColumn
stm64ServiceLabel = _Stm64ServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 14),
    _Stm64ServiceLabel_Type()
)
stm64ServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64ServiceLabel.setStatus("current")


class _Stm64ExpTrc_Type(OctetString):
    """Custom type stm64ExpTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Stm64ExpTrc_Type.__name__ = "OctetString"
_Stm64ExpTrc_Object = MibTableColumn
stm64ExpTrc = _Stm64ExpTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 15),
    _Stm64ExpTrc_Type()
)
stm64ExpTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64ExpTrc.setStatus("current")


class _Stm64TxTrc_Type(OctetString):
    """Custom type stm64TxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Stm64TxTrc_Type.__name__ = "OctetString"
_Stm64TxTrc_Object = MibTableColumn
stm64TxTrc = _Stm64TxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 16),
    _Stm64TxTrc_Type()
)
stm64TxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64TxTrc.setStatus("current")


class _Stm64RxTrc_Type(OctetString):
    """Custom type stm64RxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Stm64RxTrc_Type.__name__ = "OctetString"
_Stm64RxTrc_Object = MibTableColumn
stm64RxTrc = _Stm64RxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 17),
    _Stm64RxTrc_Type()
)
stm64RxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64RxTrc.setStatus("current")
_Stm64TimAct_Type = CoriantTypesEnableSwitch
_Stm64TimAct_Object = MibTableColumn
stm64TimAct = _Stm64TimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 18),
    _Stm64TimAct_Type()
)
stm64TimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64TimAct.setStatus("current")
_Stm64TimMonitor_Type = CoriantTypesEnableSwitch
_Stm64TimMonitor_Object = MibTableColumn
stm64TimMonitor = _Stm64TimMonitor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 19),
    _Stm64TimMonitor_Type()
)
stm64TimMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64TimMonitor.setStatus("current")


class _Stm64AisType_Type(Integer32):
    """Custom type stm64AisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("genericAis", 0),
          ("msAis", 1),
          ("aisL", 2))
    )


_Stm64AisType_Type.__name__ = "Integer32"
_Stm64AisType_Object = MibTableColumn
stm64AisType = _Stm64AisType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 20),
    _Stm64AisType_Type()
)
stm64AisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64AisType.setStatus("current")
_Stm64HoldoffSignal_Type = CoriantTypesYesNo
_Stm64HoldoffSignal_Object = MibTableColumn
stm64HoldoffSignal = _Stm64HoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 16, 1, 1, 21),
    _Stm64HoldoffSignal_Type()
)
stm64HoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64HoldoffSignal.setStatus("current")
_Otuc2_ObjectIdentity = ObjectIdentity
otuc2 = _Otuc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17)
)
_Otuc2Table_Object = MibTable
otuc2Table = _Otuc2Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1)
)
if mibBuilder.loadTexts:
    otuc2Table.setStatus("current")
_Otuc2Entry_Object = MibTableRow
otuc2Entry = _Otuc2Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1)
)
otuc2Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otuc2Entry.setStatus("current")
_Otuc2FecType_Type = CoriantTypesOtukFec
_Otuc2FecType_Object = MibTableColumn
otuc2FecType = _Otuc2FecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 1),
    _Otuc2FecType_Type()
)
otuc2FecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2FecType.setStatus("current")


class _Otuc2AdminStatus_Type(Integer32):
    """Custom type otuc2AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otuc2AdminStatus_Type.__name__ = "Integer32"
_Otuc2AdminStatus_Object = MibTableColumn
otuc2AdminStatus = _Otuc2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 2),
    _Otuc2AdminStatus_Type()
)
otuc2AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2AdminStatus.setStatus("current")


class _Otuc2OperStatus_Type(Integer32):
    """Custom type otuc2OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otuc2OperStatus_Type.__name__ = "Integer32"
_Otuc2OperStatus_Object = MibTableColumn
otuc2OperStatus = _Otuc2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 3),
    _Otuc2OperStatus_Type()
)
otuc2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2OperStatus.setStatus("current")


class _Otuc2AvailStatus_Type(Bits):
    """Custom type otuc2AvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Otuc2AvailStatus_Type.__name__ = "Bits"
_Otuc2AvailStatus_Object = MibTableColumn
otuc2AvailStatus = _Otuc2AvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 4),
    _Otuc2AvailStatus_Type()
)
otuc2AvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2AvailStatus.setStatus("current")


class _Otuc2AliasName_Type(OctetString):
    """Custom type otuc2AliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Otuc2AliasName_Type.__name__ = "OctetString"
_Otuc2AliasName_Object = MibTableColumn
otuc2AliasName = _Otuc2AliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 5),
    _Otuc2AliasName_Type()
)
otuc2AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2AliasName.setStatus("current")


class _Otuc2ServiceLabel_Type(OctetString):
    """Custom type otuc2ServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Otuc2ServiceLabel_Type.__name__ = "OctetString"
_Otuc2ServiceLabel_Object = MibTableColumn
otuc2ServiceLabel = _Otuc2ServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 6),
    _Otuc2ServiceLabel_Type()
)
otuc2ServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2ServiceLabel.setStatus("current")


class _Otuc2ExpSapi_Type(OctetString):
    """Custom type otuc2ExpSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc2ExpSapi_Type.__name__ = "OctetString"
_Otuc2ExpSapi_Object = MibTableColumn
otuc2ExpSapi = _Otuc2ExpSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 7),
    _Otuc2ExpSapi_Type()
)
otuc2ExpSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2ExpSapi.setStatus("current")


class _Otuc2ExpDapi_Type(OctetString):
    """Custom type otuc2ExpDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc2ExpDapi_Type.__name__ = "OctetString"
_Otuc2ExpDapi_Object = MibTableColumn
otuc2ExpDapi = _Otuc2ExpDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 8),
    _Otuc2ExpDapi_Type()
)
otuc2ExpDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2ExpDapi.setStatus("current")


class _Otuc2ExpOperator_Type(OctetString):
    """Custom type otuc2ExpOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otuc2ExpOperator_Type.__name__ = "OctetString"
_Otuc2ExpOperator_Object = MibTableColumn
otuc2ExpOperator = _Otuc2ExpOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 9),
    _Otuc2ExpOperator_Type()
)
otuc2ExpOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2ExpOperator.setStatus("current")


class _Otuc2TxSapi_Type(OctetString):
    """Custom type otuc2TxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc2TxSapi_Type.__name__ = "OctetString"
_Otuc2TxSapi_Object = MibTableColumn
otuc2TxSapi = _Otuc2TxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 10),
    _Otuc2TxSapi_Type()
)
otuc2TxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2TxSapi.setStatus("current")


class _Otuc2TxDapi_Type(OctetString):
    """Custom type otuc2TxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc2TxDapi_Type.__name__ = "OctetString"
_Otuc2TxDapi_Object = MibTableColumn
otuc2TxDapi = _Otuc2TxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 11),
    _Otuc2TxDapi_Type()
)
otuc2TxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2TxDapi.setStatus("current")


class _Otuc2TxOperator_Type(OctetString):
    """Custom type otuc2TxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otuc2TxOperator_Type.__name__ = "OctetString"
_Otuc2TxOperator_Object = MibTableColumn
otuc2TxOperator = _Otuc2TxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 12),
    _Otuc2TxOperator_Type()
)
otuc2TxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2TxOperator.setStatus("current")
_Otuc2TimDefectMode_Type = CoriantTypesTimMode
_Otuc2TimDefectMode_Object = MibTableColumn
otuc2TimDefectMode = _Otuc2TimDefectMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 13),
    _Otuc2TimDefectMode_Type()
)
otuc2TimDefectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2TimDefectMode.setStatus("current")
_Otuc2TimAct_Type = CoriantTypesEnableSwitch
_Otuc2TimAct_Object = MibTableColumn
otuc2TimAct = _Otuc2TimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 14),
    _Otuc2TimAct_Type()
)
otuc2TimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2TimAct.setStatus("current")


class _Otuc2RxSapi_Type(OctetString):
    """Custom type otuc2RxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc2RxSapi_Type.__name__ = "OctetString"
_Otuc2RxSapi_Object = MibTableColumn
otuc2RxSapi = _Otuc2RxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 15),
    _Otuc2RxSapi_Type()
)
otuc2RxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2RxSapi.setStatus("current")


class _Otuc2RxDapi_Type(OctetString):
    """Custom type otuc2RxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc2RxDapi_Type.__name__ = "OctetString"
_Otuc2RxDapi_Object = MibTableColumn
otuc2RxDapi = _Otuc2RxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 16),
    _Otuc2RxDapi_Type()
)
otuc2RxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2RxDapi.setStatus("current")


class _Otuc2RxOperator_Type(OctetString):
    """Custom type otuc2RxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otuc2RxOperator_Type.__name__ = "OctetString"
_Otuc2RxOperator_Object = MibTableColumn
otuc2RxOperator = _Otuc2RxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 17),
    _Otuc2RxOperator_Type()
)
otuc2RxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2RxOperator.setStatus("current")


class _Otuc2DegradeInterval_Type(Unsigned32):
    """Custom type otuc2DegradeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Otuc2DegradeInterval_Type.__name__ = "Unsigned32"
_Otuc2DegradeInterval_Object = MibTableColumn
otuc2DegradeInterval = _Otuc2DegradeInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 18),
    _Otuc2DegradeInterval_Type()
)
otuc2DegradeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2DegradeInterval.setStatus("current")


class _Otuc2DegradeThreshold_Type(Unsigned32):
    """Custom type otuc2DegradeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2590845),
    )


_Otuc2DegradeThreshold_Type.__name__ = "Unsigned32"
_Otuc2DegradeThreshold_Object = MibTableColumn
otuc2DegradeThreshold = _Otuc2DegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 17, 1, 1, 19),
    _Otuc2DegradeThreshold_Type()
)
otuc2DegradeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2DegradeThreshold.setStatus("current")
_Otuc3_ObjectIdentity = ObjectIdentity
otuc3 = _Otuc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18)
)
_Otuc3Table_Object = MibTable
otuc3Table = _Otuc3Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1)
)
if mibBuilder.loadTexts:
    otuc3Table.setStatus("current")
_Otuc3Entry_Object = MibTableRow
otuc3Entry = _Otuc3Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1)
)
otuc3Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otuc3Entry.setStatus("current")
_Otuc3FecType_Type = CoriantTypesOtukFec
_Otuc3FecType_Object = MibTableColumn
otuc3FecType = _Otuc3FecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 1),
    _Otuc3FecType_Type()
)
otuc3FecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3FecType.setStatus("current")


class _Otuc3AdminStatus_Type(Integer32):
    """Custom type otuc3AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otuc3AdminStatus_Type.__name__ = "Integer32"
_Otuc3AdminStatus_Object = MibTableColumn
otuc3AdminStatus = _Otuc3AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 2),
    _Otuc3AdminStatus_Type()
)
otuc3AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3AdminStatus.setStatus("current")


class _Otuc3OperStatus_Type(Integer32):
    """Custom type otuc3OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Otuc3OperStatus_Type.__name__ = "Integer32"
_Otuc3OperStatus_Object = MibTableColumn
otuc3OperStatus = _Otuc3OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 3),
    _Otuc3OperStatus_Type()
)
otuc3OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3OperStatus.setStatus("current")


class _Otuc3AvailStatus_Type(Bits):
    """Custom type otuc3AvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Otuc3AvailStatus_Type.__name__ = "Bits"
_Otuc3AvailStatus_Object = MibTableColumn
otuc3AvailStatus = _Otuc3AvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 4),
    _Otuc3AvailStatus_Type()
)
otuc3AvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3AvailStatus.setStatus("current")


class _Otuc3AliasName_Type(OctetString):
    """Custom type otuc3AliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Otuc3AliasName_Type.__name__ = "OctetString"
_Otuc3AliasName_Object = MibTableColumn
otuc3AliasName = _Otuc3AliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 5),
    _Otuc3AliasName_Type()
)
otuc3AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3AliasName.setStatus("current")


class _Otuc3ServiceLabel_Type(OctetString):
    """Custom type otuc3ServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Otuc3ServiceLabel_Type.__name__ = "OctetString"
_Otuc3ServiceLabel_Object = MibTableColumn
otuc3ServiceLabel = _Otuc3ServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 6),
    _Otuc3ServiceLabel_Type()
)
otuc3ServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3ServiceLabel.setStatus("current")


class _Otuc3ExpSapi_Type(OctetString):
    """Custom type otuc3ExpSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc3ExpSapi_Type.__name__ = "OctetString"
_Otuc3ExpSapi_Object = MibTableColumn
otuc3ExpSapi = _Otuc3ExpSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 7),
    _Otuc3ExpSapi_Type()
)
otuc3ExpSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3ExpSapi.setStatus("current")


class _Otuc3ExpDapi_Type(OctetString):
    """Custom type otuc3ExpDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc3ExpDapi_Type.__name__ = "OctetString"
_Otuc3ExpDapi_Object = MibTableColumn
otuc3ExpDapi = _Otuc3ExpDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 8),
    _Otuc3ExpDapi_Type()
)
otuc3ExpDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3ExpDapi.setStatus("current")


class _Otuc3ExpOperator_Type(OctetString):
    """Custom type otuc3ExpOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otuc3ExpOperator_Type.__name__ = "OctetString"
_Otuc3ExpOperator_Object = MibTableColumn
otuc3ExpOperator = _Otuc3ExpOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 9),
    _Otuc3ExpOperator_Type()
)
otuc3ExpOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3ExpOperator.setStatus("current")


class _Otuc3TxSapi_Type(OctetString):
    """Custom type otuc3TxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc3TxSapi_Type.__name__ = "OctetString"
_Otuc3TxSapi_Object = MibTableColumn
otuc3TxSapi = _Otuc3TxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 10),
    _Otuc3TxSapi_Type()
)
otuc3TxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3TxSapi.setStatus("current")


class _Otuc3TxDapi_Type(OctetString):
    """Custom type otuc3TxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc3TxDapi_Type.__name__ = "OctetString"
_Otuc3TxDapi_Object = MibTableColumn
otuc3TxDapi = _Otuc3TxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 11),
    _Otuc3TxDapi_Type()
)
otuc3TxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3TxDapi.setStatus("current")


class _Otuc3TxOperator_Type(OctetString):
    """Custom type otuc3TxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otuc3TxOperator_Type.__name__ = "OctetString"
_Otuc3TxOperator_Object = MibTableColumn
otuc3TxOperator = _Otuc3TxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 12),
    _Otuc3TxOperator_Type()
)
otuc3TxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3TxOperator.setStatus("current")
_Otuc3TimDefectMode_Type = CoriantTypesTimMode
_Otuc3TimDefectMode_Object = MibTableColumn
otuc3TimDefectMode = _Otuc3TimDefectMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 13),
    _Otuc3TimDefectMode_Type()
)
otuc3TimDefectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3TimDefectMode.setStatus("current")
_Otuc3TimAct_Type = CoriantTypesEnableSwitch
_Otuc3TimAct_Object = MibTableColumn
otuc3TimAct = _Otuc3TimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 14),
    _Otuc3TimAct_Type()
)
otuc3TimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3TimAct.setStatus("current")


class _Otuc3RxSapi_Type(OctetString):
    """Custom type otuc3RxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc3RxSapi_Type.__name__ = "OctetString"
_Otuc3RxSapi_Object = MibTableColumn
otuc3RxSapi = _Otuc3RxSapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 15),
    _Otuc3RxSapi_Type()
)
otuc3RxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3RxSapi.setStatus("current")


class _Otuc3RxDapi_Type(OctetString):
    """Custom type otuc3RxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Otuc3RxDapi_Type.__name__ = "OctetString"
_Otuc3RxDapi_Object = MibTableColumn
otuc3RxDapi = _Otuc3RxDapi_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 16),
    _Otuc3RxDapi_Type()
)
otuc3RxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3RxDapi.setStatus("current")


class _Otuc3RxOperator_Type(OctetString):
    """Custom type otuc3RxOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Otuc3RxOperator_Type.__name__ = "OctetString"
_Otuc3RxOperator_Object = MibTableColumn
otuc3RxOperator = _Otuc3RxOperator_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 17),
    _Otuc3RxOperator_Type()
)
otuc3RxOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3RxOperator.setStatus("current")


class _Otuc3DegradeInterval_Type(Unsigned32):
    """Custom type otuc3DegradeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Otuc3DegradeInterval_Type.__name__ = "Unsigned32"
_Otuc3DegradeInterval_Object = MibTableColumn
otuc3DegradeInterval = _Otuc3DegradeInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 18),
    _Otuc3DegradeInterval_Type()
)
otuc3DegradeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3DegradeInterval.setStatus("current")


class _Otuc3DegradeThreshold_Type(Unsigned32):
    """Custom type otuc3DegradeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2590845),
    )


_Otuc3DegradeThreshold_Type.__name__ = "Unsigned32"
_Otuc3DegradeThreshold_Object = MibTableColumn
otuc3DegradeThreshold = _Otuc3DegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 18, 1, 1, 19),
    _Otuc3DegradeThreshold_Type()
)
otuc3DegradeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3DegradeThreshold.setStatus("current")
_OchOs_ObjectIdentity = ObjectIdentity
ochOs = _OchOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19)
)
_OchOsTable_Object = MibTable
ochOsTable = _OchOsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1)
)
if mibBuilder.loadTexts:
    ochOsTable.setStatus("current")
_OchOsEntry_Object = MibTableRow
ochOsEntry = _OchOsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1)
)
ochOsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    ochOsEntry.setStatus("current")


class _OchOsModulationFormat_Type(Integer32):
    """Custom type ochOsModulationFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("dpQpsk", 1),
          ("dp16qam", 2),
          ("dp8qam", 3),
          ("nrz", 6))
    )


_OchOsModulationFormat_Type.__name__ = "Integer32"
_OchOsModulationFormat_Object = MibTableColumn
ochOsModulationFormat = _OchOsModulationFormat_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 1),
    _OchOsModulationFormat_Type()
)
ochOsModulationFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsModulationFormat.setStatus("current")


class _OchOsLineEncoding_Type(Integer32):
    """Custom type ochOsLineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonDifferential", 1),
          ("differential", 2))
    )


_OchOsLineEncoding_Type.__name__ = "Integer32"
_OchOsLineEncoding_Object = MibTableColumn
ochOsLineEncoding = _OchOsLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 2),
    _OchOsLineEncoding_Type()
)
ochOsLineEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsLineEncoding.setStatus("current")
_OchOsFrequency_Type = CoriantTypesFreq
_OchOsFrequency_Object = MibTableColumn
ochOsFrequency = _OchOsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 3),
    _OchOsFrequency_Type()
)
ochOsFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsFrequency.setStatus("current")
_OchOsActualFrequency_Type = CoriantTypesFreq
_OchOsActualFrequency_Object = MibTableColumn
ochOsActualFrequency = _OchOsActualFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 4),
    _OchOsActualFrequency_Type()
)
ochOsActualFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsActualFrequency.setStatus("current")
_OchOsRxFrequency_Type = CoriantTypesFreq
_OchOsRxFrequency_Object = MibTableColumn
ochOsRxFrequency = _OchOsRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 5),
    _OchOsRxFrequency_Type()
)
ochOsRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsRxFrequency.setStatus("current")
_OchOsActualRxFrequency_Type = CoriantTypesFreq
_OchOsActualRxFrequency_Object = MibTableColumn
ochOsActualRxFrequency = _OchOsActualRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 6),
    _OchOsActualRxFrequency_Type()
)
ochOsActualRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsActualRxFrequency.setStatus("current")
_OchOsLaserEnable_Type = CoriantTypesEnableSwitch
_OchOsLaserEnable_Object = MibTableColumn
ochOsLaserEnable = _OchOsLaserEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 7),
    _OchOsLaserEnable_Type()
)
ochOsLaserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsLaserEnable.setStatus("current")
_OchOsRequiredTxOpticalPower_Type = CoriantTypesOpticalPower
_OchOsRequiredTxOpticalPower_Object = MibTableColumn
ochOsRequiredTxOpticalPower = _OchOsRequiredTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 8),
    _OchOsRequiredTxOpticalPower_Type()
)
ochOsRequiredTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsRequiredTxOpticalPower.setStatus("current")
_OchOsActualTxOpticalPower_Type = CoriantTypesOpticalPower
_OchOsActualTxOpticalPower_Object = MibTableColumn
ochOsActualTxOpticalPower = _OchOsActualTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 9),
    _OchOsActualTxOpticalPower_Type()
)
ochOsActualTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsActualTxOpticalPower.setStatus("current")
_OchOsFecType_Type = CoriantTypesOtukFec
_OchOsFecType_Object = MibTableColumn
ochOsFecType = _OchOsFecType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 10),
    _OchOsFecType_Type()
)
ochOsFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsFecType.setStatus("current")
_OchOsRxAttenuation_Type = CoriantTypesOpticalDB
_OchOsRxAttenuation_Object = MibTableColumn
ochOsRxAttenuation = _OchOsRxAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 11),
    _OchOsRxAttenuation_Type()
)
ochOsRxAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsRxAttenuation.setStatus("current")
_OchOsTxFilterRollOff_Type = OctetString
_OchOsTxFilterRollOff_Object = MibTableColumn
ochOsTxFilterRollOff = _OchOsTxFilterRollOff_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 12),
    _OchOsTxFilterRollOff_Type()
)
ochOsTxFilterRollOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsTxFilterRollOff.setStatus("current")
_OchOsPreemphasis_Type = CoriantTypesEnableSwitch
_OchOsPreemphasis_Object = MibTableColumn
ochOsPreemphasis = _OchOsPreemphasis_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 13),
    _OchOsPreemphasis_Type()
)
ochOsPreemphasis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsPreemphasis.setStatus("current")
_OchOsPreemphasisValue_Type = OctetString
_OchOsPreemphasisValue_Object = MibTableColumn
ochOsPreemphasisValue = _OchOsPreemphasisValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 14),
    _OchOsPreemphasisValue_Type()
)
ochOsPreemphasisValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsPreemphasisValue.setStatus("current")


class _OchOsAdminStatus_Type(Integer32):
    """Custom type ochOsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OchOsAdminStatus_Type.__name__ = "Integer32"
_OchOsAdminStatus_Object = MibTableColumn
ochOsAdminStatus = _OchOsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 15),
    _OchOsAdminStatus_Type()
)
ochOsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsAdminStatus.setStatus("current")


class _OchOsOperStatus_Type(Integer32):
    """Custom type ochOsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OchOsOperStatus_Type.__name__ = "Integer32"
_OchOsOperStatus_Object = MibTableColumn
ochOsOperStatus = _OchOsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 16),
    _OchOsOperStatus_Type()
)
ochOsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsOperStatus.setStatus("current")


class _OchOsAvailStatus_Type(Bits):
    """Custom type ochOsAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_OchOsAvailStatus_Type.__name__ = "Bits"
_OchOsAvailStatus_Object = MibTableColumn
ochOsAvailStatus = _OchOsAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 17),
    _OchOsAvailStatus_Type()
)
ochOsAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsAvailStatus.setStatus("current")


class _OchOsAliasName_Type(OctetString):
    """Custom type ochOsAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OchOsAliasName_Type.__name__ = "OctetString"
_OchOsAliasName_Object = MibTableColumn
ochOsAliasName = _OchOsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 18),
    _OchOsAliasName_Type()
)
ochOsAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsAliasName.setStatus("current")
_OchOsLoopbackEnable_Type = CoriantTypesEnableSwitch
_OchOsLoopbackEnable_Object = MibTableColumn
ochOsLoopbackEnable = _OchOsLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 19),
    _OchOsLoopbackEnable_Type()
)
ochOsLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsLoopbackEnable.setStatus("current")


class _OchOsLoopbackType_Type(Integer32):
    """Custom type ochOsLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_OchOsLoopbackType_Type.__name__ = "Integer32"
_OchOsLoopbackType_Object = MibTableColumn
ochOsLoopbackType = _OchOsLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 20),
    _OchOsLoopbackType_Type()
)
ochOsLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsLoopbackType.setStatus("current")


class _OchOsServiceLabel_Type(OctetString):
    """Custom type ochOsServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OchOsServiceLabel_Type.__name__ = "OctetString"
_OchOsServiceLabel_Object = MibTableColumn
ochOsServiceLabel = _OchOsServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 21),
    _OchOsServiceLabel_Type()
)
ochOsServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsServiceLabel.setStatus("current")
_OchOsDGD_Type = Unsigned32
_OchOsDGD_Object = MibTableColumn
ochOsDGD = _OchOsDGD_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 22),
    _OchOsDGD_Type()
)
ochOsDGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsDGD.setStatus("current")
_OchOsCD_Type = Integer32
_OchOsCD_Object = MibTableColumn
ochOsCD = _OchOsCD_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 23),
    _OchOsCD_Type()
)
ochOsCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsCD.setStatus("current")
_OchOsOSNR_Type = CoriantTypesOpticalDB
_OchOsOSNR_Object = MibTableColumn
ochOsOSNR = _OchOsOSNR_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 24),
    _OchOsOSNR_Type()
)
ochOsOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsOSNR.setStatus("current")
_OchOsQFactor_Type = CoriantTypesOpticalDB
_OchOsQFactor_Object = MibTableColumn
ochOsQFactor = _OchOsQFactor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 25),
    _OchOsQFactor_Type()
)
ochOsQFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsQFactor.setStatus("current")
_OchOsPreFecBer_Type = OctetString
_OchOsPreFecBer_Object = MibTableColumn
ochOsPreFecBer = _OchOsPreFecBer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 26),
    _OchOsPreFecBer_Type()
)
ochOsPreFecBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsPreFecBer.setStatus("current")
_OchOsCdRangeLow_Type = Integer32
_OchOsCdRangeLow_Object = MibTableColumn
ochOsCdRangeLow = _OchOsCdRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 27),
    _OchOsCdRangeLow_Type()
)
ochOsCdRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsCdRangeLow.setStatus("current")
_OchOsCdRangeHigh_Type = Integer32
_OchOsCdRangeHigh_Object = MibTableColumn
ochOsCdRangeHigh = _OchOsCdRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 28),
    _OchOsCdRangeHigh_Type()
)
ochOsCdRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsCdRangeHigh.setStatus("current")
_OchOsPropagateShutdown_Type = CoriantTypesYesNo
_OchOsPropagateShutdown_Object = MibTableColumn
ochOsPropagateShutdown = _OchOsPropagateShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 29),
    _OchOsPropagateShutdown_Type()
)
ochOsPropagateShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsPropagateShutdown.setStatus("current")
_OchOsFastSopMode_Type = CoriantTypesEnableSwitch
_OchOsFastSopMode_Object = MibTableColumn
ochOsFastSopMode = _OchOsFastSopMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 19, 1, 1, 31),
    _OchOsFastSopMode_Type()
)
ochOsFastSopMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsFastSopMode.setStatus("current")
_Wan10gSonet_ObjectIdentity = ObjectIdentity
wan10gSonet = _Wan10gSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30)
)
_Wan10gSonetTable_Object = MibTable
wan10gSonetTable = _Wan10gSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1)
)
if mibBuilder.loadTexts:
    wan10gSonetTable.setStatus("current")
_Wan10gSonetEntry_Object = MibTableRow
wan10gSonetEntry = _Wan10gSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1)
)
wan10gSonetEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    wan10gSonetEntry.setStatus("current")


class _Wan10gSonetMappingMode_Type(Integer32):
    """Custom type wan10gSonetMappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Wan10gSonetMappingMode_Type.__name__ = "Integer32"
_Wan10gSonetMappingMode_Object = MibTableColumn
wan10gSonetMappingMode = _Wan10gSonetMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 1),
    _Wan10gSonetMappingMode_Type()
)
wan10gSonetMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetMappingMode.setStatus("current")


class _Wan10gSonetAdminStatus_Type(Integer32):
    """Custom type wan10gSonetAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Wan10gSonetAdminStatus_Type.__name__ = "Integer32"
_Wan10gSonetAdminStatus_Object = MibTableColumn
wan10gSonetAdminStatus = _Wan10gSonetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 2),
    _Wan10gSonetAdminStatus_Type()
)
wan10gSonetAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetAdminStatus.setStatus("current")


class _Wan10gSonetOperStatus_Type(Integer32):
    """Custom type wan10gSonetOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Wan10gSonetOperStatus_Type.__name__ = "Integer32"
_Wan10gSonetOperStatus_Object = MibTableColumn
wan10gSonetOperStatus = _Wan10gSonetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 3),
    _Wan10gSonetOperStatus_Type()
)
wan10gSonetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetOperStatus.setStatus("current")


class _Wan10gSonetAvailStatus_Type(Bits):
    """Custom type wan10gSonetAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Wan10gSonetAvailStatus_Type.__name__ = "Bits"
_Wan10gSonetAvailStatus_Object = MibTableColumn
wan10gSonetAvailStatus = _Wan10gSonetAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 4),
    _Wan10gSonetAvailStatus_Type()
)
wan10gSonetAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetAvailStatus.setStatus("current")


class _Wan10gSonetAliasName_Type(OctetString):
    """Custom type wan10gSonetAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Wan10gSonetAliasName_Type.__name__ = "OctetString"
_Wan10gSonetAliasName_Object = MibTableColumn
wan10gSonetAliasName = _Wan10gSonetAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 5),
    _Wan10gSonetAliasName_Type()
)
wan10gSonetAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetAliasName.setStatus("current")
_Wan10gSonetClientShutdown_Type = CoriantTypesYesNo
_Wan10gSonetClientShutdown_Object = MibTableColumn
wan10gSonetClientShutdown = _Wan10gSonetClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 6),
    _Wan10gSonetClientShutdown_Type()
)
wan10gSonetClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetClientShutdown.setStatus("current")


class _Wan10gSonetClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type wan10gSonetClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Wan10gSonetClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Wan10gSonetClientShutdownHoldoffTimer_Object = MibTableColumn
wan10gSonetClientShutdownHoldoffTimer = _Wan10gSonetClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 7),
    _Wan10gSonetClientShutdownHoldoffTimer_Type()
)
wan10gSonetClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetClientShutdownHoldoffTimer.setStatus("current")
_Wan10gSonetHoldoffSignal_Type = CoriantTypesYesNo
_Wan10gSonetHoldoffSignal_Object = MibTableColumn
wan10gSonetHoldoffSignal = _Wan10gSonetHoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 8),
    _Wan10gSonetHoldoffSignal_Type()
)
wan10gSonetHoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetHoldoffSignal.setStatus("current")
_Wan10gSonetNearEndAls_Type = CoriantTypesYesNo
_Wan10gSonetNearEndAls_Object = MibTableColumn
wan10gSonetNearEndAls = _Wan10gSonetNearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 9),
    _Wan10gSonetNearEndAls_Type()
)
wan10gSonetNearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetNearEndAls.setStatus("current")
_Wan10gSonetAlsDegradeMode_Type = CoriantTypesEnableSwitch
_Wan10gSonetAlsDegradeMode_Object = MibTableColumn
wan10gSonetAlsDegradeMode = _Wan10gSonetAlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 10),
    _Wan10gSonetAlsDegradeMode_Type()
)
wan10gSonetAlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetAlsDegradeMode.setStatus("current")
_Wan10gSonetLoopbackEnable_Type = CoriantTypesEnableSwitch
_Wan10gSonetLoopbackEnable_Object = MibTableColumn
wan10gSonetLoopbackEnable = _Wan10gSonetLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 11),
    _Wan10gSonetLoopbackEnable_Type()
)
wan10gSonetLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetLoopbackEnable.setStatus("current")


class _Wan10gSonetLoopbackType_Type(Integer32):
    """Custom type wan10gSonetLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Wan10gSonetLoopbackType_Type.__name__ = "Integer32"
_Wan10gSonetLoopbackType_Object = MibTableColumn
wan10gSonetLoopbackType = _Wan10gSonetLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 12),
    _Wan10gSonetLoopbackType_Type()
)
wan10gSonetLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetLoopbackType.setStatus("current")
_Wan10gSonetTestSignalType_Type = CoriantTypesTestSignalType
_Wan10gSonetTestSignalType_Object = MibTableColumn
wan10gSonetTestSignalType = _Wan10gSonetTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 13),
    _Wan10gSonetTestSignalType_Type()
)
wan10gSonetTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetTestSignalType.setStatus("current")
_Wan10gSonetTestSignalEnable_Type = CoriantTypesTestSignalConfig
_Wan10gSonetTestSignalEnable_Object = MibTableColumn
wan10gSonetTestSignalEnable = _Wan10gSonetTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 14),
    _Wan10gSonetTestSignalEnable_Type()
)
wan10gSonetTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetTestSignalEnable.setStatus("current")


class _Wan10gSonetServiceLabel_Type(OctetString):
    """Custom type wan10gSonetServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Wan10gSonetServiceLabel_Type.__name__ = "OctetString"
_Wan10gSonetServiceLabel_Object = MibTableColumn
wan10gSonetServiceLabel = _Wan10gSonetServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 15),
    _Wan10gSonetServiceLabel_Type()
)
wan10gSonetServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetServiceLabel.setStatus("current")


class _Wan10gSonetExpTrc_Type(OctetString):
    """Custom type wan10gSonetExpTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Wan10gSonetExpTrc_Type.__name__ = "OctetString"
_Wan10gSonetExpTrc_Object = MibTableColumn
wan10gSonetExpTrc = _Wan10gSonetExpTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 16),
    _Wan10gSonetExpTrc_Type()
)
wan10gSonetExpTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetExpTrc.setStatus("current")


class _Wan10gSonetTxTrc_Type(OctetString):
    """Custom type wan10gSonetTxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Wan10gSonetTxTrc_Type.__name__ = "OctetString"
_Wan10gSonetTxTrc_Object = MibTableColumn
wan10gSonetTxTrc = _Wan10gSonetTxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 17),
    _Wan10gSonetTxTrc_Type()
)
wan10gSonetTxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetTxTrc.setStatus("current")


class _Wan10gSonetRxTrc_Type(OctetString):
    """Custom type wan10gSonetRxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Wan10gSonetRxTrc_Type.__name__ = "OctetString"
_Wan10gSonetRxTrc_Object = MibTableColumn
wan10gSonetRxTrc = _Wan10gSonetRxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 18),
    _Wan10gSonetRxTrc_Type()
)
wan10gSonetRxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetRxTrc.setStatus("current")
_Wan10gSonetTimAct_Type = CoriantTypesEnableSwitch
_Wan10gSonetTimAct_Object = MibTableColumn
wan10gSonetTimAct = _Wan10gSonetTimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 19),
    _Wan10gSonetTimAct_Type()
)
wan10gSonetTimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetTimAct.setStatus("current")
_Wan10gSonetTimMonitor_Type = CoriantTypesEnableSwitch
_Wan10gSonetTimMonitor_Object = MibTableColumn
wan10gSonetTimMonitor = _Wan10gSonetTimMonitor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 20),
    _Wan10gSonetTimMonitor_Type()
)
wan10gSonetTimMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetTimMonitor.setStatus("current")


class _Wan10gSonetAisType_Type(Integer32):
    """Custom type wan10gSonetAisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("genericAis", 0),
          ("msAis", 1),
          ("aisL", 2))
    )


_Wan10gSonetAisType_Type.__name__ = "Integer32"
_Wan10gSonetAisType_Object = MibTableColumn
wan10gSonetAisType = _Wan10gSonetAisType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 30, 1, 1, 21),
    _Wan10gSonetAisType_Type()
)
wan10gSonetAisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetAisType.setStatus("current")
_Wan10gSdh_ObjectIdentity = ObjectIdentity
wan10gSdh = _Wan10gSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31)
)
_Wan10gSdhTable_Object = MibTable
wan10gSdhTable = _Wan10gSdhTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1)
)
if mibBuilder.loadTexts:
    wan10gSdhTable.setStatus("current")
_Wan10gSdhEntry_Object = MibTableRow
wan10gSdhEntry = _Wan10gSdhEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1)
)
wan10gSdhEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    wan10gSdhEntry.setStatus("current")


class _Wan10gSdhMappingMode_Type(Integer32):
    """Custom type wan10gSdhMappingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gmp", 1),
          ("gfpF", 2),
          ("t40gbmpOdu2e", 3),
          ("preamble", 4),
          ("bmpFixedstuff", 5),
          ("bmp", 6),
          ("amp", 7))
    )


_Wan10gSdhMappingMode_Type.__name__ = "Integer32"
_Wan10gSdhMappingMode_Object = MibTableColumn
wan10gSdhMappingMode = _Wan10gSdhMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 1),
    _Wan10gSdhMappingMode_Type()
)
wan10gSdhMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhMappingMode.setStatus("current")


class _Wan10gSdhAdminStatus_Type(Integer32):
    """Custom type wan10gSdhAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Wan10gSdhAdminStatus_Type.__name__ = "Integer32"
_Wan10gSdhAdminStatus_Object = MibTableColumn
wan10gSdhAdminStatus = _Wan10gSdhAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 2),
    _Wan10gSdhAdminStatus_Type()
)
wan10gSdhAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhAdminStatus.setStatus("current")


class _Wan10gSdhOperStatus_Type(Integer32):
    """Custom type wan10gSdhOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Wan10gSdhOperStatus_Type.__name__ = "Integer32"
_Wan10gSdhOperStatus_Object = MibTableColumn
wan10gSdhOperStatus = _Wan10gSdhOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 3),
    _Wan10gSdhOperStatus_Type()
)
wan10gSdhOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhOperStatus.setStatus("current")


class _Wan10gSdhAvailStatus_Type(Bits):
    """Custom type wan10gSdhAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_Wan10gSdhAvailStatus_Type.__name__ = "Bits"
_Wan10gSdhAvailStatus_Object = MibTableColumn
wan10gSdhAvailStatus = _Wan10gSdhAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 4),
    _Wan10gSdhAvailStatus_Type()
)
wan10gSdhAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhAvailStatus.setStatus("current")


class _Wan10gSdhAliasName_Type(OctetString):
    """Custom type wan10gSdhAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Wan10gSdhAliasName_Type.__name__ = "OctetString"
_Wan10gSdhAliasName_Object = MibTableColumn
wan10gSdhAliasName = _Wan10gSdhAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 5),
    _Wan10gSdhAliasName_Type()
)
wan10gSdhAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhAliasName.setStatus("current")
_Wan10gSdhClientShutdown_Type = CoriantTypesYesNo
_Wan10gSdhClientShutdown_Object = MibTableColumn
wan10gSdhClientShutdown = _Wan10gSdhClientShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 6),
    _Wan10gSdhClientShutdown_Type()
)
wan10gSdhClientShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhClientShutdown.setStatus("current")


class _Wan10gSdhClientShutdownHoldoffTimer_Type(Unsigned32):
    """Custom type wan10gSdhClientShutdownHoldoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Wan10gSdhClientShutdownHoldoffTimer_Type.__name__ = "Unsigned32"
_Wan10gSdhClientShutdownHoldoffTimer_Object = MibTableColumn
wan10gSdhClientShutdownHoldoffTimer = _Wan10gSdhClientShutdownHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 7),
    _Wan10gSdhClientShutdownHoldoffTimer_Type()
)
wan10gSdhClientShutdownHoldoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhClientShutdownHoldoffTimer.setStatus("current")
_Wan10gSdhHoldoffSignal_Type = CoriantTypesYesNo
_Wan10gSdhHoldoffSignal_Object = MibTableColumn
wan10gSdhHoldoffSignal = _Wan10gSdhHoldoffSignal_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 8),
    _Wan10gSdhHoldoffSignal_Type()
)
wan10gSdhHoldoffSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhHoldoffSignal.setStatus("current")
_Wan10gSdhNearEndAls_Type = CoriantTypesYesNo
_Wan10gSdhNearEndAls_Object = MibTableColumn
wan10gSdhNearEndAls = _Wan10gSdhNearEndAls_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 9),
    _Wan10gSdhNearEndAls_Type()
)
wan10gSdhNearEndAls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhNearEndAls.setStatus("current")
_Wan10gSdhAlsDegradeMode_Type = CoriantTypesEnableSwitch
_Wan10gSdhAlsDegradeMode_Object = MibTableColumn
wan10gSdhAlsDegradeMode = _Wan10gSdhAlsDegradeMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 10),
    _Wan10gSdhAlsDegradeMode_Type()
)
wan10gSdhAlsDegradeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhAlsDegradeMode.setStatus("current")
_Wan10gSdhLoopbackEnable_Type = CoriantTypesEnableSwitch
_Wan10gSdhLoopbackEnable_Object = MibTableColumn
wan10gSdhLoopbackEnable = _Wan10gSdhLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 11),
    _Wan10gSdhLoopbackEnable_Type()
)
wan10gSdhLoopbackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhLoopbackEnable.setStatus("current")


class _Wan10gSdhLoopbackType_Type(Integer32):
    """Custom type wan10gSdhLoopbackType based on Integer32"""
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
          ("terminal", 1),
          ("facility", 2))
    )


_Wan10gSdhLoopbackType_Type.__name__ = "Integer32"
_Wan10gSdhLoopbackType_Object = MibTableColumn
wan10gSdhLoopbackType = _Wan10gSdhLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 12),
    _Wan10gSdhLoopbackType_Type()
)
wan10gSdhLoopbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhLoopbackType.setStatus("current")
_Wan10gSdhTestSignalType_Type = CoriantTypesTestSignalType
_Wan10gSdhTestSignalType_Object = MibTableColumn
wan10gSdhTestSignalType = _Wan10gSdhTestSignalType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 13),
    _Wan10gSdhTestSignalType_Type()
)
wan10gSdhTestSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhTestSignalType.setStatus("current")
_Wan10gSdhTestSignalEnable_Type = CoriantTypesTestSignalConfig
_Wan10gSdhTestSignalEnable_Object = MibTableColumn
wan10gSdhTestSignalEnable = _Wan10gSdhTestSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 14),
    _Wan10gSdhTestSignalEnable_Type()
)
wan10gSdhTestSignalEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhTestSignalEnable.setStatus("current")


class _Wan10gSdhServiceLabel_Type(OctetString):
    """Custom type wan10gSdhServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Wan10gSdhServiceLabel_Type.__name__ = "OctetString"
_Wan10gSdhServiceLabel_Object = MibTableColumn
wan10gSdhServiceLabel = _Wan10gSdhServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 15),
    _Wan10gSdhServiceLabel_Type()
)
wan10gSdhServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhServiceLabel.setStatus("current")


class _Wan10gSdhExpTrc_Type(OctetString):
    """Custom type wan10gSdhExpTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Wan10gSdhExpTrc_Type.__name__ = "OctetString"
_Wan10gSdhExpTrc_Object = MibTableColumn
wan10gSdhExpTrc = _Wan10gSdhExpTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 16),
    _Wan10gSdhExpTrc_Type()
)
wan10gSdhExpTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhExpTrc.setStatus("current")


class _Wan10gSdhTxTrc_Type(OctetString):
    """Custom type wan10gSdhTxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Wan10gSdhTxTrc_Type.__name__ = "OctetString"
_Wan10gSdhTxTrc_Object = MibTableColumn
wan10gSdhTxTrc = _Wan10gSdhTxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 17),
    _Wan10gSdhTxTrc_Type()
)
wan10gSdhTxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhTxTrc.setStatus("current")


class _Wan10gSdhRxTrc_Type(OctetString):
    """Custom type wan10gSdhRxTrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Wan10gSdhRxTrc_Type.__name__ = "OctetString"
_Wan10gSdhRxTrc_Object = MibTableColumn
wan10gSdhRxTrc = _Wan10gSdhRxTrc_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 18),
    _Wan10gSdhRxTrc_Type()
)
wan10gSdhRxTrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhRxTrc.setStatus("current")
_Wan10gSdhTimAct_Type = CoriantTypesEnableSwitch
_Wan10gSdhTimAct_Object = MibTableColumn
wan10gSdhTimAct = _Wan10gSdhTimAct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 19),
    _Wan10gSdhTimAct_Type()
)
wan10gSdhTimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhTimAct.setStatus("current")
_Wan10gSdhTimMonitor_Type = CoriantTypesEnableSwitch
_Wan10gSdhTimMonitor_Object = MibTableColumn
wan10gSdhTimMonitor = _Wan10gSdhTimMonitor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 20),
    _Wan10gSdhTimMonitor_Type()
)
wan10gSdhTimMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhTimMonitor.setStatus("current")


class _Wan10gSdhAisType_Type(Integer32):
    """Custom type wan10gSdhAisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("genericAis", 0),
          ("msAis", 1),
          ("aisL", 2))
    )


_Wan10gSdhAisType_Type.__name__ = "Integer32"
_Wan10gSdhAisType_Object = MibTableColumn
wan10gSdhAisType = _Wan10gSdhAisType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 31, 1, 1, 21),
    _Wan10gSdhAisType_Type()
)
wan10gSdhAisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhAisType.setStatus("current")
_Eth10gStatistics_ObjectIdentity = ObjectIdentity
eth10gStatistics = _Eth10gStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32)
)
_Eth10gStatisticsTable_Object = MibTable
eth10gStatisticsTable = _Eth10gStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1)
)
if mibBuilder.loadTexts:
    eth10gStatisticsTable.setStatus("current")
_Eth10gStatisticsEntry_Object = MibTableRow
eth10gStatisticsEntry = _Eth10gStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1)
)
eth10gStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    eth10gStatisticsEntry.setStatus("current")
_Eth10gStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Eth10gStatisticsEntryLastClear_Object = MibTableColumn
eth10gStatisticsEntryLastClear = _Eth10gStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 1),
    _Eth10gStatisticsEntryLastClear_Type()
)
eth10gStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryLastClear.setStatus("current")
_Eth10gStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Eth10gStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
eth10gStatisticsEntryLossOfSignalSeconds = _Eth10gStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 2),
    _Eth10gStatisticsEntryLossOfSignalSeconds_Type()
)
eth10gStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Eth10gStatisticsEntryBitErrorFec_Type = OctetString
_Eth10gStatisticsEntryBitErrorFec_Object = MibTableColumn
eth10gStatisticsEntryBitErrorFec = _Eth10gStatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 3),
    _Eth10gStatisticsEntryBitErrorFec_Type()
)
eth10gStatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryBitErrorFec.setStatus("current")
_Eth10gStatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Eth10gStatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
eth10gStatisticsEntryUncorrectedBlockErrorFec = _Eth10gStatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 4),
    _Eth10gStatisticsEntryUncorrectedBlockErrorFec_Type()
)
eth10gStatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Eth10gStatisticsEntryInSymbolErrors_Type = OctetString
_Eth10gStatisticsEntryInSymbolErrors_Object = MibTableColumn
eth10gStatisticsEntryInSymbolErrors = _Eth10gStatisticsEntryInSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 5),
    _Eth10gStatisticsEntryInSymbolErrors_Type()
)
eth10gStatisticsEntryInSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInSymbolErrors.setStatus("current")
_Eth10gStatisticsEntryInDropEvents_Type = OctetString
_Eth10gStatisticsEntryInDropEvents_Object = MibTableColumn
eth10gStatisticsEntryInDropEvents = _Eth10gStatisticsEntryInDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 6),
    _Eth10gStatisticsEntryInDropEvents_Type()
)
eth10gStatisticsEntryInDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInDropEvents.setStatus("current")
_Eth10gStatisticsEntryInOctets_Type = OctetString
_Eth10gStatisticsEntryInOctets_Object = MibTableColumn
eth10gStatisticsEntryInOctets = _Eth10gStatisticsEntryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 7),
    _Eth10gStatisticsEntryInOctets_Type()
)
eth10gStatisticsEntryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInOctets.setStatus("current")
_Eth10gStatisticsEntryInPackets_Type = OctetString
_Eth10gStatisticsEntryInPackets_Object = MibTableColumn
eth10gStatisticsEntryInPackets = _Eth10gStatisticsEntryInPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 8),
    _Eth10gStatisticsEntryInPackets_Type()
)
eth10gStatisticsEntryInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInPackets.setStatus("current")
_Eth10gStatisticsEntryInBroadcastPackets_Type = OctetString
_Eth10gStatisticsEntryInBroadcastPackets_Object = MibTableColumn
eth10gStatisticsEntryInBroadcastPackets = _Eth10gStatisticsEntryInBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 9),
    _Eth10gStatisticsEntryInBroadcastPackets_Type()
)
eth10gStatisticsEntryInBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInBroadcastPackets.setStatus("current")
_Eth10gStatisticsEntryInMulticastPackets_Type = OctetString
_Eth10gStatisticsEntryInMulticastPackets_Object = MibTableColumn
eth10gStatisticsEntryInMulticastPackets = _Eth10gStatisticsEntryInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 10),
    _Eth10gStatisticsEntryInMulticastPackets_Type()
)
eth10gStatisticsEntryInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInMulticastPackets.setStatus("current")
_Eth10gStatisticsEntryInCrcAlignErrors_Type = OctetString
_Eth10gStatisticsEntryInCrcAlignErrors_Object = MibTableColumn
eth10gStatisticsEntryInCrcAlignErrors = _Eth10gStatisticsEntryInCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 11),
    _Eth10gStatisticsEntryInCrcAlignErrors_Type()
)
eth10gStatisticsEntryInCrcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInCrcAlignErrors.setStatus("current")
_Eth10gStatisticsEntryInUndersizePackets_Type = OctetString
_Eth10gStatisticsEntryInUndersizePackets_Object = MibTableColumn
eth10gStatisticsEntryInUndersizePackets = _Eth10gStatisticsEntryInUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 12),
    _Eth10gStatisticsEntryInUndersizePackets_Type()
)
eth10gStatisticsEntryInUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInUndersizePackets.setStatus("current")
_Eth10gStatisticsEntryInOversizePackets_Type = OctetString
_Eth10gStatisticsEntryInOversizePackets_Object = MibTableColumn
eth10gStatisticsEntryInOversizePackets = _Eth10gStatisticsEntryInOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 13),
    _Eth10gStatisticsEntryInOversizePackets_Type()
)
eth10gStatisticsEntryInOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInOversizePackets.setStatus("current")
_Eth10gStatisticsEntryInFragments_Type = OctetString
_Eth10gStatisticsEntryInFragments_Object = MibTableColumn
eth10gStatisticsEntryInFragments = _Eth10gStatisticsEntryInFragments_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 14),
    _Eth10gStatisticsEntryInFragments_Type()
)
eth10gStatisticsEntryInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInFragments.setStatus("current")
_Eth10gStatisticsEntryInJabbers_Type = OctetString
_Eth10gStatisticsEntryInJabbers_Object = MibTableColumn
eth10gStatisticsEntryInJabbers = _Eth10gStatisticsEntryInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 15),
    _Eth10gStatisticsEntryInJabbers_Type()
)
eth10gStatisticsEntryInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInJabbers.setStatus("current")
_Eth10gStatisticsEntryInPackets64octets_Type = OctetString
_Eth10gStatisticsEntryInPackets64octets_Object = MibTableColumn
eth10gStatisticsEntryInPackets64octets = _Eth10gStatisticsEntryInPackets64octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 16),
    _Eth10gStatisticsEntryInPackets64octets_Type()
)
eth10gStatisticsEntryInPackets64octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInPackets64octets.setStatus("current")
_Eth10gStatisticsEntryInPackets65to127octets_Type = OctetString
_Eth10gStatisticsEntryInPackets65to127octets_Object = MibTableColumn
eth10gStatisticsEntryInPackets65to127octets = _Eth10gStatisticsEntryInPackets65to127octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 17),
    _Eth10gStatisticsEntryInPackets65to127octets_Type()
)
eth10gStatisticsEntryInPackets65to127octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInPackets65to127octets.setStatus("current")
_Eth10gStatisticsEntryInPackets128to255octets_Type = OctetString
_Eth10gStatisticsEntryInPackets128to255octets_Object = MibTableColumn
eth10gStatisticsEntryInPackets128to255octets = _Eth10gStatisticsEntryInPackets128to255octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 18),
    _Eth10gStatisticsEntryInPackets128to255octets_Type()
)
eth10gStatisticsEntryInPackets128to255octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInPackets128to255octets.setStatus("current")
_Eth10gStatisticsEntryInPackets256to511octets_Type = OctetString
_Eth10gStatisticsEntryInPackets256to511octets_Object = MibTableColumn
eth10gStatisticsEntryInPackets256to511octets = _Eth10gStatisticsEntryInPackets256to511octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 19),
    _Eth10gStatisticsEntryInPackets256to511octets_Type()
)
eth10gStatisticsEntryInPackets256to511octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInPackets256to511octets.setStatus("current")
_Eth10gStatisticsEntryInPackets512to1023octets_Type = OctetString
_Eth10gStatisticsEntryInPackets512to1023octets_Object = MibTableColumn
eth10gStatisticsEntryInPackets512to1023octets = _Eth10gStatisticsEntryInPackets512to1023octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 20),
    _Eth10gStatisticsEntryInPackets512to1023octets_Type()
)
eth10gStatisticsEntryInPackets512to1023octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInPackets512to1023octets.setStatus("current")
_Eth10gStatisticsEntryInPackets1024to1518octets_Type = OctetString
_Eth10gStatisticsEntryInPackets1024to1518octets_Object = MibTableColumn
eth10gStatisticsEntryInPackets1024to1518octets = _Eth10gStatisticsEntryInPackets1024to1518octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 21),
    _Eth10gStatisticsEntryInPackets1024to1518octets_Type()
)
eth10gStatisticsEntryInPackets1024to1518octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryInPackets1024to1518octets.setStatus("current")
_Eth10gStatisticsEntryOutSymbolErrors_Type = OctetString
_Eth10gStatisticsEntryOutSymbolErrors_Object = MibTableColumn
eth10gStatisticsEntryOutSymbolErrors = _Eth10gStatisticsEntryOutSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 22),
    _Eth10gStatisticsEntryOutSymbolErrors_Type()
)
eth10gStatisticsEntryOutSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutSymbolErrors.setStatus("current")
_Eth10gStatisticsEntryOutDropEvents_Type = OctetString
_Eth10gStatisticsEntryOutDropEvents_Object = MibTableColumn
eth10gStatisticsEntryOutDropEvents = _Eth10gStatisticsEntryOutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 23),
    _Eth10gStatisticsEntryOutDropEvents_Type()
)
eth10gStatisticsEntryOutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutDropEvents.setStatus("current")
_Eth10gStatisticsEntryOutOctets_Type = OctetString
_Eth10gStatisticsEntryOutOctets_Object = MibTableColumn
eth10gStatisticsEntryOutOctets = _Eth10gStatisticsEntryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 24),
    _Eth10gStatisticsEntryOutOctets_Type()
)
eth10gStatisticsEntryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutOctets.setStatus("current")
_Eth10gStatisticsEntryOutPackets_Type = OctetString
_Eth10gStatisticsEntryOutPackets_Object = MibTableColumn
eth10gStatisticsEntryOutPackets = _Eth10gStatisticsEntryOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 25),
    _Eth10gStatisticsEntryOutPackets_Type()
)
eth10gStatisticsEntryOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutPackets.setStatus("current")
_Eth10gStatisticsEntryOutBroadcastPackets_Type = OctetString
_Eth10gStatisticsEntryOutBroadcastPackets_Object = MibTableColumn
eth10gStatisticsEntryOutBroadcastPackets = _Eth10gStatisticsEntryOutBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 26),
    _Eth10gStatisticsEntryOutBroadcastPackets_Type()
)
eth10gStatisticsEntryOutBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutBroadcastPackets.setStatus("current")
_Eth10gStatisticsEntryOutMulticastPackets_Type = OctetString
_Eth10gStatisticsEntryOutMulticastPackets_Object = MibTableColumn
eth10gStatisticsEntryOutMulticastPackets = _Eth10gStatisticsEntryOutMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 27),
    _Eth10gStatisticsEntryOutMulticastPackets_Type()
)
eth10gStatisticsEntryOutMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutMulticastPackets.setStatus("current")
_Eth10gStatisticsEntryOutCrcAlignErrors_Type = OctetString
_Eth10gStatisticsEntryOutCrcAlignErrors_Object = MibTableColumn
eth10gStatisticsEntryOutCrcAlignErrors = _Eth10gStatisticsEntryOutCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 28),
    _Eth10gStatisticsEntryOutCrcAlignErrors_Type()
)
eth10gStatisticsEntryOutCrcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutCrcAlignErrors.setStatus("current")
_Eth10gStatisticsEntryOutUndersizePackets_Type = OctetString
_Eth10gStatisticsEntryOutUndersizePackets_Object = MibTableColumn
eth10gStatisticsEntryOutUndersizePackets = _Eth10gStatisticsEntryOutUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 29),
    _Eth10gStatisticsEntryOutUndersizePackets_Type()
)
eth10gStatisticsEntryOutUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutUndersizePackets.setStatus("current")
_Eth10gStatisticsEntryOutOversizePackets_Type = OctetString
_Eth10gStatisticsEntryOutOversizePackets_Object = MibTableColumn
eth10gStatisticsEntryOutOversizePackets = _Eth10gStatisticsEntryOutOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 30),
    _Eth10gStatisticsEntryOutOversizePackets_Type()
)
eth10gStatisticsEntryOutOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutOversizePackets.setStatus("current")
_Eth10gStatisticsEntryOutFragments_Type = OctetString
_Eth10gStatisticsEntryOutFragments_Object = MibTableColumn
eth10gStatisticsEntryOutFragments = _Eth10gStatisticsEntryOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 31),
    _Eth10gStatisticsEntryOutFragments_Type()
)
eth10gStatisticsEntryOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutFragments.setStatus("current")
_Eth10gStatisticsEntryOutJabbers_Type = OctetString
_Eth10gStatisticsEntryOutJabbers_Object = MibTableColumn
eth10gStatisticsEntryOutJabbers = _Eth10gStatisticsEntryOutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 32),
    _Eth10gStatisticsEntryOutJabbers_Type()
)
eth10gStatisticsEntryOutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutJabbers.setStatus("current")
_Eth10gStatisticsEntryOutPackets64octets_Type = OctetString
_Eth10gStatisticsEntryOutPackets64octets_Object = MibTableColumn
eth10gStatisticsEntryOutPackets64octets = _Eth10gStatisticsEntryOutPackets64octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 33),
    _Eth10gStatisticsEntryOutPackets64octets_Type()
)
eth10gStatisticsEntryOutPackets64octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutPackets64octets.setStatus("current")
_Eth10gStatisticsEntryOutPackets65to127octets_Type = OctetString
_Eth10gStatisticsEntryOutPackets65to127octets_Object = MibTableColumn
eth10gStatisticsEntryOutPackets65to127octets = _Eth10gStatisticsEntryOutPackets65to127octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 34),
    _Eth10gStatisticsEntryOutPackets65to127octets_Type()
)
eth10gStatisticsEntryOutPackets65to127octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutPackets65to127octets.setStatus("current")
_Eth10gStatisticsEntryOutPackets128to255octets_Type = OctetString
_Eth10gStatisticsEntryOutPackets128to255octets_Object = MibTableColumn
eth10gStatisticsEntryOutPackets128to255octets = _Eth10gStatisticsEntryOutPackets128to255octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 35),
    _Eth10gStatisticsEntryOutPackets128to255octets_Type()
)
eth10gStatisticsEntryOutPackets128to255octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutPackets128to255octets.setStatus("current")
_Eth10gStatisticsEntryOutPackets256to511octets_Type = OctetString
_Eth10gStatisticsEntryOutPackets256to511octets_Object = MibTableColumn
eth10gStatisticsEntryOutPackets256to511octets = _Eth10gStatisticsEntryOutPackets256to511octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 36),
    _Eth10gStatisticsEntryOutPackets256to511octets_Type()
)
eth10gStatisticsEntryOutPackets256to511octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutPackets256to511octets.setStatus("current")
_Eth10gStatisticsEntryOutPackets512to1023octets_Type = OctetString
_Eth10gStatisticsEntryOutPackets512to1023octets_Object = MibTableColumn
eth10gStatisticsEntryOutPackets512to1023octets = _Eth10gStatisticsEntryOutPackets512to1023octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 37),
    _Eth10gStatisticsEntryOutPackets512to1023octets_Type()
)
eth10gStatisticsEntryOutPackets512to1023octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutPackets512to1023octets.setStatus("current")
_Eth10gStatisticsEntryOutPackets1024to1518octets_Type = OctetString
_Eth10gStatisticsEntryOutPackets1024to1518octets_Object = MibTableColumn
eth10gStatisticsEntryOutPackets1024to1518octets = _Eth10gStatisticsEntryOutPackets1024to1518octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 32, 1, 1, 38),
    _Eth10gStatisticsEntryOutPackets1024to1518octets_Type()
)
eth10gStatisticsEntryOutPackets1024to1518octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth10gStatisticsEntryOutPackets1024to1518octets.setStatus("current")
_OduStatistics_ObjectIdentity = ObjectIdentity
oduStatistics = _OduStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33)
)
_OduStatisticsTable_Object = MibTable
oduStatisticsTable = _OduStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1)
)
if mibBuilder.loadTexts:
    oduStatisticsTable.setStatus("current")
_OduStatisticsEntry_Object = MibTableRow
oduStatisticsEntry = _OduStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1, 1)
)
oduStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL1"),
    (0, "CORIANT-GROOVE-MIB", "oduidL1"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL2"),
    (0, "CORIANT-GROOVE-MIB", "oduidL2"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL3"),
    (0, "CORIANT-GROOVE-MIB", "oduidL3"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL4"),
    (0, "CORIANT-GROOVE-MIB", "oduidL4"),
)
if mibBuilder.loadTexts:
    oduStatisticsEntry.setStatus("current")
_OduStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_OduStatisticsEntryLastClear_Object = MibTableColumn
oduStatisticsEntryLastClear = _OduStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1, 1, 1),
    _OduStatisticsEntryLastClear_Type()
)
oduStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduStatisticsEntryLastClear.setStatus("current")
_OduStatisticsEntryErroredBlocks_Type = OctetString
_OduStatisticsEntryErroredBlocks_Object = MibTableColumn
oduStatisticsEntryErroredBlocks = _OduStatisticsEntryErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1, 1, 2),
    _OduStatisticsEntryErroredBlocks_Type()
)
oduStatisticsEntryErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduStatisticsEntryErroredBlocks.setStatus("current")
_OduStatisticsEntryErroredSeconds_Type = OctetString
_OduStatisticsEntryErroredSeconds_Object = MibTableColumn
oduStatisticsEntryErroredSeconds = _OduStatisticsEntryErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1, 1, 3),
    _OduStatisticsEntryErroredSeconds_Type()
)
oduStatisticsEntryErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduStatisticsEntryErroredSeconds.setStatus("current")
_OduStatisticsEntrySeverelyErroredSeconds_Type = OctetString
_OduStatisticsEntrySeverelyErroredSeconds_Object = MibTableColumn
oduStatisticsEntrySeverelyErroredSeconds = _OduStatisticsEntrySeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1, 1, 4),
    _OduStatisticsEntrySeverelyErroredSeconds_Type()
)
oduStatisticsEntrySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduStatisticsEntrySeverelyErroredSeconds.setStatus("current")
_OduStatisticsEntryUnavailableSeconds_Type = OctetString
_OduStatisticsEntryUnavailableSeconds_Object = MibTableColumn
oduStatisticsEntryUnavailableSeconds = _OduStatisticsEntryUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1, 1, 5),
    _OduStatisticsEntryUnavailableSeconds_Type()
)
oduStatisticsEntryUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduStatisticsEntryUnavailableSeconds.setStatus("current")
_OduStatisticsEntryEncryptionFailRx_Type = OctetString
_OduStatisticsEntryEncryptionFailRx_Object = MibTableColumn
oduStatisticsEntryEncryptionFailRx = _OduStatisticsEntryEncryptionFailRx_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 33, 1, 1, 6),
    _OduStatisticsEntryEncryptionFailRx_Type()
)
oduStatisticsEntryEncryptionFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduStatisticsEntryEncryptionFailRx.setStatus("current")
_Eth40gStatistics_ObjectIdentity = ObjectIdentity
eth40gStatistics = _Eth40gStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34)
)
_Eth40gStatisticsTable_Object = MibTable
eth40gStatisticsTable = _Eth40gStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1)
)
if mibBuilder.loadTexts:
    eth40gStatisticsTable.setStatus("current")
_Eth40gStatisticsEntry_Object = MibTableRow
eth40gStatisticsEntry = _Eth40gStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1)
)
eth40gStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    eth40gStatisticsEntry.setStatus("current")
_Eth40gStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Eth40gStatisticsEntryLastClear_Object = MibTableColumn
eth40gStatisticsEntryLastClear = _Eth40gStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 1),
    _Eth40gStatisticsEntryLastClear_Type()
)
eth40gStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryLastClear.setStatus("current")
_Eth40gStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Eth40gStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
eth40gStatisticsEntryLossOfSignalSeconds = _Eth40gStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 2),
    _Eth40gStatisticsEntryLossOfSignalSeconds_Type()
)
eth40gStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Eth40gStatisticsEntryBitErrorFec_Type = OctetString
_Eth40gStatisticsEntryBitErrorFec_Object = MibTableColumn
eth40gStatisticsEntryBitErrorFec = _Eth40gStatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 3),
    _Eth40gStatisticsEntryBitErrorFec_Type()
)
eth40gStatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryBitErrorFec.setStatus("current")
_Eth40gStatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Eth40gStatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
eth40gStatisticsEntryUncorrectedBlockErrorFec = _Eth40gStatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 4),
    _Eth40gStatisticsEntryUncorrectedBlockErrorFec_Type()
)
eth40gStatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Eth40gStatisticsEntryInSymbolErrors_Type = OctetString
_Eth40gStatisticsEntryInSymbolErrors_Object = MibTableColumn
eth40gStatisticsEntryInSymbolErrors = _Eth40gStatisticsEntryInSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 5),
    _Eth40gStatisticsEntryInSymbolErrors_Type()
)
eth40gStatisticsEntryInSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInSymbolErrors.setStatus("current")
_Eth40gStatisticsEntryInDropEvents_Type = OctetString
_Eth40gStatisticsEntryInDropEvents_Object = MibTableColumn
eth40gStatisticsEntryInDropEvents = _Eth40gStatisticsEntryInDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 6),
    _Eth40gStatisticsEntryInDropEvents_Type()
)
eth40gStatisticsEntryInDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInDropEvents.setStatus("current")
_Eth40gStatisticsEntryInOctets_Type = OctetString
_Eth40gStatisticsEntryInOctets_Object = MibTableColumn
eth40gStatisticsEntryInOctets = _Eth40gStatisticsEntryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 7),
    _Eth40gStatisticsEntryInOctets_Type()
)
eth40gStatisticsEntryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInOctets.setStatus("current")
_Eth40gStatisticsEntryInPackets_Type = OctetString
_Eth40gStatisticsEntryInPackets_Object = MibTableColumn
eth40gStatisticsEntryInPackets = _Eth40gStatisticsEntryInPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 8),
    _Eth40gStatisticsEntryInPackets_Type()
)
eth40gStatisticsEntryInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInPackets.setStatus("current")
_Eth40gStatisticsEntryInBroadcastPackets_Type = OctetString
_Eth40gStatisticsEntryInBroadcastPackets_Object = MibTableColumn
eth40gStatisticsEntryInBroadcastPackets = _Eth40gStatisticsEntryInBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 9),
    _Eth40gStatisticsEntryInBroadcastPackets_Type()
)
eth40gStatisticsEntryInBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInBroadcastPackets.setStatus("current")
_Eth40gStatisticsEntryInMulticastPackets_Type = OctetString
_Eth40gStatisticsEntryInMulticastPackets_Object = MibTableColumn
eth40gStatisticsEntryInMulticastPackets = _Eth40gStatisticsEntryInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 10),
    _Eth40gStatisticsEntryInMulticastPackets_Type()
)
eth40gStatisticsEntryInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInMulticastPackets.setStatus("current")
_Eth40gStatisticsEntryInCrcAlignErrors_Type = OctetString
_Eth40gStatisticsEntryInCrcAlignErrors_Object = MibTableColumn
eth40gStatisticsEntryInCrcAlignErrors = _Eth40gStatisticsEntryInCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 11),
    _Eth40gStatisticsEntryInCrcAlignErrors_Type()
)
eth40gStatisticsEntryInCrcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInCrcAlignErrors.setStatus("current")
_Eth40gStatisticsEntryInUndersizePackets_Type = OctetString
_Eth40gStatisticsEntryInUndersizePackets_Object = MibTableColumn
eth40gStatisticsEntryInUndersizePackets = _Eth40gStatisticsEntryInUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 12),
    _Eth40gStatisticsEntryInUndersizePackets_Type()
)
eth40gStatisticsEntryInUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInUndersizePackets.setStatus("current")
_Eth40gStatisticsEntryInOversizePackets_Type = OctetString
_Eth40gStatisticsEntryInOversizePackets_Object = MibTableColumn
eth40gStatisticsEntryInOversizePackets = _Eth40gStatisticsEntryInOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 13),
    _Eth40gStatisticsEntryInOversizePackets_Type()
)
eth40gStatisticsEntryInOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInOversizePackets.setStatus("current")
_Eth40gStatisticsEntryInFragments_Type = OctetString
_Eth40gStatisticsEntryInFragments_Object = MibTableColumn
eth40gStatisticsEntryInFragments = _Eth40gStatisticsEntryInFragments_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 14),
    _Eth40gStatisticsEntryInFragments_Type()
)
eth40gStatisticsEntryInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInFragments.setStatus("current")
_Eth40gStatisticsEntryInJabbers_Type = OctetString
_Eth40gStatisticsEntryInJabbers_Object = MibTableColumn
eth40gStatisticsEntryInJabbers = _Eth40gStatisticsEntryInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 15),
    _Eth40gStatisticsEntryInJabbers_Type()
)
eth40gStatisticsEntryInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInJabbers.setStatus("current")
_Eth40gStatisticsEntryInPackets64octets_Type = OctetString
_Eth40gStatisticsEntryInPackets64octets_Object = MibTableColumn
eth40gStatisticsEntryInPackets64octets = _Eth40gStatisticsEntryInPackets64octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 16),
    _Eth40gStatisticsEntryInPackets64octets_Type()
)
eth40gStatisticsEntryInPackets64octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInPackets64octets.setStatus("current")
_Eth40gStatisticsEntryInPackets65to127octets_Type = OctetString
_Eth40gStatisticsEntryInPackets65to127octets_Object = MibTableColumn
eth40gStatisticsEntryInPackets65to127octets = _Eth40gStatisticsEntryInPackets65to127octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 17),
    _Eth40gStatisticsEntryInPackets65to127octets_Type()
)
eth40gStatisticsEntryInPackets65to127octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInPackets65to127octets.setStatus("current")
_Eth40gStatisticsEntryInPackets128to255octets_Type = OctetString
_Eth40gStatisticsEntryInPackets128to255octets_Object = MibTableColumn
eth40gStatisticsEntryInPackets128to255octets = _Eth40gStatisticsEntryInPackets128to255octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 18),
    _Eth40gStatisticsEntryInPackets128to255octets_Type()
)
eth40gStatisticsEntryInPackets128to255octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInPackets128to255octets.setStatus("current")
_Eth40gStatisticsEntryInPackets256to511octets_Type = OctetString
_Eth40gStatisticsEntryInPackets256to511octets_Object = MibTableColumn
eth40gStatisticsEntryInPackets256to511octets = _Eth40gStatisticsEntryInPackets256to511octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 19),
    _Eth40gStatisticsEntryInPackets256to511octets_Type()
)
eth40gStatisticsEntryInPackets256to511octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInPackets256to511octets.setStatus("current")
_Eth40gStatisticsEntryInPackets512to1023octets_Type = OctetString
_Eth40gStatisticsEntryInPackets512to1023octets_Object = MibTableColumn
eth40gStatisticsEntryInPackets512to1023octets = _Eth40gStatisticsEntryInPackets512to1023octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 20),
    _Eth40gStatisticsEntryInPackets512to1023octets_Type()
)
eth40gStatisticsEntryInPackets512to1023octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInPackets512to1023octets.setStatus("current")
_Eth40gStatisticsEntryInPackets1024to1518octets_Type = OctetString
_Eth40gStatisticsEntryInPackets1024to1518octets_Object = MibTableColumn
eth40gStatisticsEntryInPackets1024to1518octets = _Eth40gStatisticsEntryInPackets1024to1518octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 21),
    _Eth40gStatisticsEntryInPackets1024to1518octets_Type()
)
eth40gStatisticsEntryInPackets1024to1518octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryInPackets1024to1518octets.setStatus("current")
_Eth40gStatisticsEntryOutSymbolErrors_Type = OctetString
_Eth40gStatisticsEntryOutSymbolErrors_Object = MibTableColumn
eth40gStatisticsEntryOutSymbolErrors = _Eth40gStatisticsEntryOutSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 22),
    _Eth40gStatisticsEntryOutSymbolErrors_Type()
)
eth40gStatisticsEntryOutSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutSymbolErrors.setStatus("current")
_Eth40gStatisticsEntryOutDropEvents_Type = OctetString
_Eth40gStatisticsEntryOutDropEvents_Object = MibTableColumn
eth40gStatisticsEntryOutDropEvents = _Eth40gStatisticsEntryOutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 23),
    _Eth40gStatisticsEntryOutDropEvents_Type()
)
eth40gStatisticsEntryOutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutDropEvents.setStatus("current")
_Eth40gStatisticsEntryOutOctets_Type = OctetString
_Eth40gStatisticsEntryOutOctets_Object = MibTableColumn
eth40gStatisticsEntryOutOctets = _Eth40gStatisticsEntryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 24),
    _Eth40gStatisticsEntryOutOctets_Type()
)
eth40gStatisticsEntryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutOctets.setStatus("current")
_Eth40gStatisticsEntryOutPackets_Type = OctetString
_Eth40gStatisticsEntryOutPackets_Object = MibTableColumn
eth40gStatisticsEntryOutPackets = _Eth40gStatisticsEntryOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 25),
    _Eth40gStatisticsEntryOutPackets_Type()
)
eth40gStatisticsEntryOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutPackets.setStatus("current")
_Eth40gStatisticsEntryOutBroadcastPackets_Type = OctetString
_Eth40gStatisticsEntryOutBroadcastPackets_Object = MibTableColumn
eth40gStatisticsEntryOutBroadcastPackets = _Eth40gStatisticsEntryOutBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 26),
    _Eth40gStatisticsEntryOutBroadcastPackets_Type()
)
eth40gStatisticsEntryOutBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutBroadcastPackets.setStatus("current")
_Eth40gStatisticsEntryOutMulticastPackets_Type = OctetString
_Eth40gStatisticsEntryOutMulticastPackets_Object = MibTableColumn
eth40gStatisticsEntryOutMulticastPackets = _Eth40gStatisticsEntryOutMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 27),
    _Eth40gStatisticsEntryOutMulticastPackets_Type()
)
eth40gStatisticsEntryOutMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutMulticastPackets.setStatus("current")
_Eth40gStatisticsEntryOutCrcAlignErrors_Type = OctetString
_Eth40gStatisticsEntryOutCrcAlignErrors_Object = MibTableColumn
eth40gStatisticsEntryOutCrcAlignErrors = _Eth40gStatisticsEntryOutCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 28),
    _Eth40gStatisticsEntryOutCrcAlignErrors_Type()
)
eth40gStatisticsEntryOutCrcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutCrcAlignErrors.setStatus("current")
_Eth40gStatisticsEntryOutUndersizePackets_Type = OctetString
_Eth40gStatisticsEntryOutUndersizePackets_Object = MibTableColumn
eth40gStatisticsEntryOutUndersizePackets = _Eth40gStatisticsEntryOutUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 29),
    _Eth40gStatisticsEntryOutUndersizePackets_Type()
)
eth40gStatisticsEntryOutUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutUndersizePackets.setStatus("current")
_Eth40gStatisticsEntryOutOversizePackets_Type = OctetString
_Eth40gStatisticsEntryOutOversizePackets_Object = MibTableColumn
eth40gStatisticsEntryOutOversizePackets = _Eth40gStatisticsEntryOutOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 30),
    _Eth40gStatisticsEntryOutOversizePackets_Type()
)
eth40gStatisticsEntryOutOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutOversizePackets.setStatus("current")
_Eth40gStatisticsEntryOutFragments_Type = OctetString
_Eth40gStatisticsEntryOutFragments_Object = MibTableColumn
eth40gStatisticsEntryOutFragments = _Eth40gStatisticsEntryOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 31),
    _Eth40gStatisticsEntryOutFragments_Type()
)
eth40gStatisticsEntryOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutFragments.setStatus("current")
_Eth40gStatisticsEntryOutJabbers_Type = OctetString
_Eth40gStatisticsEntryOutJabbers_Object = MibTableColumn
eth40gStatisticsEntryOutJabbers = _Eth40gStatisticsEntryOutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 32),
    _Eth40gStatisticsEntryOutJabbers_Type()
)
eth40gStatisticsEntryOutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutJabbers.setStatus("current")
_Eth40gStatisticsEntryOutPackets64octets_Type = OctetString
_Eth40gStatisticsEntryOutPackets64octets_Object = MibTableColumn
eth40gStatisticsEntryOutPackets64octets = _Eth40gStatisticsEntryOutPackets64octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 33),
    _Eth40gStatisticsEntryOutPackets64octets_Type()
)
eth40gStatisticsEntryOutPackets64octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutPackets64octets.setStatus("current")
_Eth40gStatisticsEntryOutPackets65to127octets_Type = OctetString
_Eth40gStatisticsEntryOutPackets65to127octets_Object = MibTableColumn
eth40gStatisticsEntryOutPackets65to127octets = _Eth40gStatisticsEntryOutPackets65to127octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 34),
    _Eth40gStatisticsEntryOutPackets65to127octets_Type()
)
eth40gStatisticsEntryOutPackets65to127octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutPackets65to127octets.setStatus("current")
_Eth40gStatisticsEntryOutPackets128to255octets_Type = OctetString
_Eth40gStatisticsEntryOutPackets128to255octets_Object = MibTableColumn
eth40gStatisticsEntryOutPackets128to255octets = _Eth40gStatisticsEntryOutPackets128to255octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 35),
    _Eth40gStatisticsEntryOutPackets128to255octets_Type()
)
eth40gStatisticsEntryOutPackets128to255octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutPackets128to255octets.setStatus("current")
_Eth40gStatisticsEntryOutPackets256to511octets_Type = OctetString
_Eth40gStatisticsEntryOutPackets256to511octets_Object = MibTableColumn
eth40gStatisticsEntryOutPackets256to511octets = _Eth40gStatisticsEntryOutPackets256to511octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 36),
    _Eth40gStatisticsEntryOutPackets256to511octets_Type()
)
eth40gStatisticsEntryOutPackets256to511octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutPackets256to511octets.setStatus("current")
_Eth40gStatisticsEntryOutPackets512to1023octets_Type = OctetString
_Eth40gStatisticsEntryOutPackets512to1023octets_Object = MibTableColumn
eth40gStatisticsEntryOutPackets512to1023octets = _Eth40gStatisticsEntryOutPackets512to1023octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 37),
    _Eth40gStatisticsEntryOutPackets512to1023octets_Type()
)
eth40gStatisticsEntryOutPackets512to1023octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutPackets512to1023octets.setStatus("current")
_Eth40gStatisticsEntryOutPackets1024to1518octets_Type = OctetString
_Eth40gStatisticsEntryOutPackets1024to1518octets_Object = MibTableColumn
eth40gStatisticsEntryOutPackets1024to1518octets = _Eth40gStatisticsEntryOutPackets1024to1518octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 34, 1, 1, 38),
    _Eth40gStatisticsEntryOutPackets1024to1518octets_Type()
)
eth40gStatisticsEntryOutPackets1024to1518octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth40gStatisticsEntryOutPackets1024to1518octets.setStatus("current")
_Eth100gStatistics_ObjectIdentity = ObjectIdentity
eth100gStatistics = _Eth100gStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35)
)
_Eth100gStatisticsTable_Object = MibTable
eth100gStatisticsTable = _Eth100gStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1)
)
if mibBuilder.loadTexts:
    eth100gStatisticsTable.setStatus("current")
_Eth100gStatisticsEntry_Object = MibTableRow
eth100gStatisticsEntry = _Eth100gStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1)
)
eth100gStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    eth100gStatisticsEntry.setStatus("current")
_Eth100gStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Eth100gStatisticsEntryLastClear_Object = MibTableColumn
eth100gStatisticsEntryLastClear = _Eth100gStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 1),
    _Eth100gStatisticsEntryLastClear_Type()
)
eth100gStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryLastClear.setStatus("current")
_Eth100gStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Eth100gStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
eth100gStatisticsEntryLossOfSignalSeconds = _Eth100gStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 2),
    _Eth100gStatisticsEntryLossOfSignalSeconds_Type()
)
eth100gStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Eth100gStatisticsEntryBitErrorFec_Type = OctetString
_Eth100gStatisticsEntryBitErrorFec_Object = MibTableColumn
eth100gStatisticsEntryBitErrorFec = _Eth100gStatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 3),
    _Eth100gStatisticsEntryBitErrorFec_Type()
)
eth100gStatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryBitErrorFec.setStatus("current")
_Eth100gStatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Eth100gStatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
eth100gStatisticsEntryUncorrectedBlockErrorFec = _Eth100gStatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 4),
    _Eth100gStatisticsEntryUncorrectedBlockErrorFec_Type()
)
eth100gStatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Eth100gStatisticsEntryInSymbolErrors_Type = OctetString
_Eth100gStatisticsEntryInSymbolErrors_Object = MibTableColumn
eth100gStatisticsEntryInSymbolErrors = _Eth100gStatisticsEntryInSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 5),
    _Eth100gStatisticsEntryInSymbolErrors_Type()
)
eth100gStatisticsEntryInSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInSymbolErrors.setStatus("current")
_Eth100gStatisticsEntryInDropEvents_Type = OctetString
_Eth100gStatisticsEntryInDropEvents_Object = MibTableColumn
eth100gStatisticsEntryInDropEvents = _Eth100gStatisticsEntryInDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 6),
    _Eth100gStatisticsEntryInDropEvents_Type()
)
eth100gStatisticsEntryInDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInDropEvents.setStatus("current")
_Eth100gStatisticsEntryInOctets_Type = OctetString
_Eth100gStatisticsEntryInOctets_Object = MibTableColumn
eth100gStatisticsEntryInOctets = _Eth100gStatisticsEntryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 7),
    _Eth100gStatisticsEntryInOctets_Type()
)
eth100gStatisticsEntryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInOctets.setStatus("current")
_Eth100gStatisticsEntryInPackets_Type = OctetString
_Eth100gStatisticsEntryInPackets_Object = MibTableColumn
eth100gStatisticsEntryInPackets = _Eth100gStatisticsEntryInPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 8),
    _Eth100gStatisticsEntryInPackets_Type()
)
eth100gStatisticsEntryInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInPackets.setStatus("current")
_Eth100gStatisticsEntryInBroadcastPackets_Type = OctetString
_Eth100gStatisticsEntryInBroadcastPackets_Object = MibTableColumn
eth100gStatisticsEntryInBroadcastPackets = _Eth100gStatisticsEntryInBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 9),
    _Eth100gStatisticsEntryInBroadcastPackets_Type()
)
eth100gStatisticsEntryInBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInBroadcastPackets.setStatus("current")
_Eth100gStatisticsEntryInMulticastPackets_Type = OctetString
_Eth100gStatisticsEntryInMulticastPackets_Object = MibTableColumn
eth100gStatisticsEntryInMulticastPackets = _Eth100gStatisticsEntryInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 10),
    _Eth100gStatisticsEntryInMulticastPackets_Type()
)
eth100gStatisticsEntryInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInMulticastPackets.setStatus("current")
_Eth100gStatisticsEntryInCrcAlignErrors_Type = OctetString
_Eth100gStatisticsEntryInCrcAlignErrors_Object = MibTableColumn
eth100gStatisticsEntryInCrcAlignErrors = _Eth100gStatisticsEntryInCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 11),
    _Eth100gStatisticsEntryInCrcAlignErrors_Type()
)
eth100gStatisticsEntryInCrcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInCrcAlignErrors.setStatus("current")
_Eth100gStatisticsEntryInUndersizePackets_Type = OctetString
_Eth100gStatisticsEntryInUndersizePackets_Object = MibTableColumn
eth100gStatisticsEntryInUndersizePackets = _Eth100gStatisticsEntryInUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 12),
    _Eth100gStatisticsEntryInUndersizePackets_Type()
)
eth100gStatisticsEntryInUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInUndersizePackets.setStatus("current")
_Eth100gStatisticsEntryInOversizePackets_Type = OctetString
_Eth100gStatisticsEntryInOversizePackets_Object = MibTableColumn
eth100gStatisticsEntryInOversizePackets = _Eth100gStatisticsEntryInOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 13),
    _Eth100gStatisticsEntryInOversizePackets_Type()
)
eth100gStatisticsEntryInOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInOversizePackets.setStatus("current")
_Eth100gStatisticsEntryInFragments_Type = OctetString
_Eth100gStatisticsEntryInFragments_Object = MibTableColumn
eth100gStatisticsEntryInFragments = _Eth100gStatisticsEntryInFragments_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 14),
    _Eth100gStatisticsEntryInFragments_Type()
)
eth100gStatisticsEntryInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInFragments.setStatus("current")
_Eth100gStatisticsEntryInJabbers_Type = OctetString
_Eth100gStatisticsEntryInJabbers_Object = MibTableColumn
eth100gStatisticsEntryInJabbers = _Eth100gStatisticsEntryInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 15),
    _Eth100gStatisticsEntryInJabbers_Type()
)
eth100gStatisticsEntryInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInJabbers.setStatus("current")
_Eth100gStatisticsEntryInPackets64octets_Type = OctetString
_Eth100gStatisticsEntryInPackets64octets_Object = MibTableColumn
eth100gStatisticsEntryInPackets64octets = _Eth100gStatisticsEntryInPackets64octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 16),
    _Eth100gStatisticsEntryInPackets64octets_Type()
)
eth100gStatisticsEntryInPackets64octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInPackets64octets.setStatus("current")
_Eth100gStatisticsEntryInPackets65to127octets_Type = OctetString
_Eth100gStatisticsEntryInPackets65to127octets_Object = MibTableColumn
eth100gStatisticsEntryInPackets65to127octets = _Eth100gStatisticsEntryInPackets65to127octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 17),
    _Eth100gStatisticsEntryInPackets65to127octets_Type()
)
eth100gStatisticsEntryInPackets65to127octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInPackets65to127octets.setStatus("current")
_Eth100gStatisticsEntryInPackets128to255octets_Type = OctetString
_Eth100gStatisticsEntryInPackets128to255octets_Object = MibTableColumn
eth100gStatisticsEntryInPackets128to255octets = _Eth100gStatisticsEntryInPackets128to255octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 18),
    _Eth100gStatisticsEntryInPackets128to255octets_Type()
)
eth100gStatisticsEntryInPackets128to255octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInPackets128to255octets.setStatus("current")
_Eth100gStatisticsEntryInPackets256to511octets_Type = OctetString
_Eth100gStatisticsEntryInPackets256to511octets_Object = MibTableColumn
eth100gStatisticsEntryInPackets256to511octets = _Eth100gStatisticsEntryInPackets256to511octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 19),
    _Eth100gStatisticsEntryInPackets256to511octets_Type()
)
eth100gStatisticsEntryInPackets256to511octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInPackets256to511octets.setStatus("current")
_Eth100gStatisticsEntryInPackets512to1023octets_Type = OctetString
_Eth100gStatisticsEntryInPackets512to1023octets_Object = MibTableColumn
eth100gStatisticsEntryInPackets512to1023octets = _Eth100gStatisticsEntryInPackets512to1023octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 20),
    _Eth100gStatisticsEntryInPackets512to1023octets_Type()
)
eth100gStatisticsEntryInPackets512to1023octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInPackets512to1023octets.setStatus("current")
_Eth100gStatisticsEntryInPackets1024to1518octets_Type = OctetString
_Eth100gStatisticsEntryInPackets1024to1518octets_Object = MibTableColumn
eth100gStatisticsEntryInPackets1024to1518octets = _Eth100gStatisticsEntryInPackets1024to1518octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 21),
    _Eth100gStatisticsEntryInPackets1024to1518octets_Type()
)
eth100gStatisticsEntryInPackets1024to1518octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryInPackets1024to1518octets.setStatus("current")
_Eth100gStatisticsEntryOutSymbolErrors_Type = OctetString
_Eth100gStatisticsEntryOutSymbolErrors_Object = MibTableColumn
eth100gStatisticsEntryOutSymbolErrors = _Eth100gStatisticsEntryOutSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 22),
    _Eth100gStatisticsEntryOutSymbolErrors_Type()
)
eth100gStatisticsEntryOutSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutSymbolErrors.setStatus("current")
_Eth100gStatisticsEntryOutDropEvents_Type = OctetString
_Eth100gStatisticsEntryOutDropEvents_Object = MibTableColumn
eth100gStatisticsEntryOutDropEvents = _Eth100gStatisticsEntryOutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 23),
    _Eth100gStatisticsEntryOutDropEvents_Type()
)
eth100gStatisticsEntryOutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutDropEvents.setStatus("current")
_Eth100gStatisticsEntryOutOctets_Type = OctetString
_Eth100gStatisticsEntryOutOctets_Object = MibTableColumn
eth100gStatisticsEntryOutOctets = _Eth100gStatisticsEntryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 24),
    _Eth100gStatisticsEntryOutOctets_Type()
)
eth100gStatisticsEntryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutOctets.setStatus("current")
_Eth100gStatisticsEntryOutPackets_Type = OctetString
_Eth100gStatisticsEntryOutPackets_Object = MibTableColumn
eth100gStatisticsEntryOutPackets = _Eth100gStatisticsEntryOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 25),
    _Eth100gStatisticsEntryOutPackets_Type()
)
eth100gStatisticsEntryOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutPackets.setStatus("current")
_Eth100gStatisticsEntryOutBroadcastPackets_Type = OctetString
_Eth100gStatisticsEntryOutBroadcastPackets_Object = MibTableColumn
eth100gStatisticsEntryOutBroadcastPackets = _Eth100gStatisticsEntryOutBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 26),
    _Eth100gStatisticsEntryOutBroadcastPackets_Type()
)
eth100gStatisticsEntryOutBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutBroadcastPackets.setStatus("current")
_Eth100gStatisticsEntryOutMulticastPackets_Type = OctetString
_Eth100gStatisticsEntryOutMulticastPackets_Object = MibTableColumn
eth100gStatisticsEntryOutMulticastPackets = _Eth100gStatisticsEntryOutMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 27),
    _Eth100gStatisticsEntryOutMulticastPackets_Type()
)
eth100gStatisticsEntryOutMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutMulticastPackets.setStatus("current")
_Eth100gStatisticsEntryOutCrcAlignErrors_Type = OctetString
_Eth100gStatisticsEntryOutCrcAlignErrors_Object = MibTableColumn
eth100gStatisticsEntryOutCrcAlignErrors = _Eth100gStatisticsEntryOutCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 28),
    _Eth100gStatisticsEntryOutCrcAlignErrors_Type()
)
eth100gStatisticsEntryOutCrcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutCrcAlignErrors.setStatus("current")
_Eth100gStatisticsEntryOutUndersizePackets_Type = OctetString
_Eth100gStatisticsEntryOutUndersizePackets_Object = MibTableColumn
eth100gStatisticsEntryOutUndersizePackets = _Eth100gStatisticsEntryOutUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 29),
    _Eth100gStatisticsEntryOutUndersizePackets_Type()
)
eth100gStatisticsEntryOutUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutUndersizePackets.setStatus("current")
_Eth100gStatisticsEntryOutOversizePackets_Type = OctetString
_Eth100gStatisticsEntryOutOversizePackets_Object = MibTableColumn
eth100gStatisticsEntryOutOversizePackets = _Eth100gStatisticsEntryOutOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 30),
    _Eth100gStatisticsEntryOutOversizePackets_Type()
)
eth100gStatisticsEntryOutOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutOversizePackets.setStatus("current")
_Eth100gStatisticsEntryOutFragments_Type = OctetString
_Eth100gStatisticsEntryOutFragments_Object = MibTableColumn
eth100gStatisticsEntryOutFragments = _Eth100gStatisticsEntryOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 31),
    _Eth100gStatisticsEntryOutFragments_Type()
)
eth100gStatisticsEntryOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutFragments.setStatus("current")
_Eth100gStatisticsEntryOutJabbers_Type = OctetString
_Eth100gStatisticsEntryOutJabbers_Object = MibTableColumn
eth100gStatisticsEntryOutJabbers = _Eth100gStatisticsEntryOutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 32),
    _Eth100gStatisticsEntryOutJabbers_Type()
)
eth100gStatisticsEntryOutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutJabbers.setStatus("current")
_Eth100gStatisticsEntryOutPackets64octets_Type = OctetString
_Eth100gStatisticsEntryOutPackets64octets_Object = MibTableColumn
eth100gStatisticsEntryOutPackets64octets = _Eth100gStatisticsEntryOutPackets64octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 33),
    _Eth100gStatisticsEntryOutPackets64octets_Type()
)
eth100gStatisticsEntryOutPackets64octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutPackets64octets.setStatus("current")
_Eth100gStatisticsEntryOutPackets65to127octets_Type = OctetString
_Eth100gStatisticsEntryOutPackets65to127octets_Object = MibTableColumn
eth100gStatisticsEntryOutPackets65to127octets = _Eth100gStatisticsEntryOutPackets65to127octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 34),
    _Eth100gStatisticsEntryOutPackets65to127octets_Type()
)
eth100gStatisticsEntryOutPackets65to127octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutPackets65to127octets.setStatus("current")
_Eth100gStatisticsEntryOutPackets128to255octets_Type = OctetString
_Eth100gStatisticsEntryOutPackets128to255octets_Object = MibTableColumn
eth100gStatisticsEntryOutPackets128to255octets = _Eth100gStatisticsEntryOutPackets128to255octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 35),
    _Eth100gStatisticsEntryOutPackets128to255octets_Type()
)
eth100gStatisticsEntryOutPackets128to255octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutPackets128to255octets.setStatus("current")
_Eth100gStatisticsEntryOutPackets256to511octets_Type = OctetString
_Eth100gStatisticsEntryOutPackets256to511octets_Object = MibTableColumn
eth100gStatisticsEntryOutPackets256to511octets = _Eth100gStatisticsEntryOutPackets256to511octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 36),
    _Eth100gStatisticsEntryOutPackets256to511octets_Type()
)
eth100gStatisticsEntryOutPackets256to511octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutPackets256to511octets.setStatus("current")
_Eth100gStatisticsEntryOutPackets512to1023octets_Type = OctetString
_Eth100gStatisticsEntryOutPackets512to1023octets_Object = MibTableColumn
eth100gStatisticsEntryOutPackets512to1023octets = _Eth100gStatisticsEntryOutPackets512to1023octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 37),
    _Eth100gStatisticsEntryOutPackets512to1023octets_Type()
)
eth100gStatisticsEntryOutPackets512to1023octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutPackets512to1023octets.setStatus("current")
_Eth100gStatisticsEntryOutPackets1024to1518octets_Type = OctetString
_Eth100gStatisticsEntryOutPackets1024to1518octets_Object = MibTableColumn
eth100gStatisticsEntryOutPackets1024to1518octets = _Eth100gStatisticsEntryOutPackets1024to1518octets_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 35, 1, 1, 38),
    _Eth100gStatisticsEntryOutPackets1024to1518octets_Type()
)
eth100gStatisticsEntryOutPackets1024to1518octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth100gStatisticsEntryOutPackets1024to1518octets.setStatus("current")
_Otu4Statistics_ObjectIdentity = ObjectIdentity
otu4Statistics = _Otu4Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36)
)
_Otu4StatisticsTable_Object = MibTable
otu4StatisticsTable = _Otu4StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1)
)
if mibBuilder.loadTexts:
    otu4StatisticsTable.setStatus("current")
_Otu4StatisticsEntry_Object = MibTableRow
otu4StatisticsEntry = _Otu4StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1)
)
otu4StatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otu4StatisticsEntry.setStatus("current")
_Otu4StatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Otu4StatisticsEntryLastClear_Object = MibTableColumn
otu4StatisticsEntryLastClear = _Otu4StatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 1),
    _Otu4StatisticsEntryLastClear_Type()
)
otu4StatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntryLastClear.setStatus("current")
_Otu4StatisticsEntryLossOfSignalSeconds_Type = OctetString
_Otu4StatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
otu4StatisticsEntryLossOfSignalSeconds = _Otu4StatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 2),
    _Otu4StatisticsEntryLossOfSignalSeconds_Type()
)
otu4StatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntryLossOfSignalSeconds.setStatus("current")
_Otu4StatisticsEntryBitErrorFec_Type = OctetString
_Otu4StatisticsEntryBitErrorFec_Object = MibTableColumn
otu4StatisticsEntryBitErrorFec = _Otu4StatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 3),
    _Otu4StatisticsEntryBitErrorFec_Type()
)
otu4StatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntryBitErrorFec.setStatus("current")
_Otu4StatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Otu4StatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
otu4StatisticsEntryUncorrectedBlockErrorFec = _Otu4StatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 4),
    _Otu4StatisticsEntryUncorrectedBlockErrorFec_Type()
)
otu4StatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Otu4StatisticsEntryErroredBlocks_Type = OctetString
_Otu4StatisticsEntryErroredBlocks_Object = MibTableColumn
otu4StatisticsEntryErroredBlocks = _Otu4StatisticsEntryErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 5),
    _Otu4StatisticsEntryErroredBlocks_Type()
)
otu4StatisticsEntryErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntryErroredBlocks.setStatus("current")
_Otu4StatisticsEntryErroredSeconds_Type = OctetString
_Otu4StatisticsEntryErroredSeconds_Object = MibTableColumn
otu4StatisticsEntryErroredSeconds = _Otu4StatisticsEntryErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 6),
    _Otu4StatisticsEntryErroredSeconds_Type()
)
otu4StatisticsEntryErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntryErroredSeconds.setStatus("current")
_Otu4StatisticsEntrySeverelyErroredSeconds_Type = OctetString
_Otu4StatisticsEntrySeverelyErroredSeconds_Object = MibTableColumn
otu4StatisticsEntrySeverelyErroredSeconds = _Otu4StatisticsEntrySeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 7),
    _Otu4StatisticsEntrySeverelyErroredSeconds_Type()
)
otu4StatisticsEntrySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntrySeverelyErroredSeconds.setStatus("current")
_Otu4StatisticsEntryUnavailableSeconds_Type = OctetString
_Otu4StatisticsEntryUnavailableSeconds_Object = MibTableColumn
otu4StatisticsEntryUnavailableSeconds = _Otu4StatisticsEntryUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 36, 1, 1, 8),
    _Otu4StatisticsEntryUnavailableSeconds_Type()
)
otu4StatisticsEntryUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu4StatisticsEntryUnavailableSeconds.setStatus("current")
_Otu2Statistics_ObjectIdentity = ObjectIdentity
otu2Statistics = _Otu2Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37)
)
_Otu2StatisticsTable_Object = MibTable
otu2StatisticsTable = _Otu2StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1)
)
if mibBuilder.loadTexts:
    otu2StatisticsTable.setStatus("current")
_Otu2StatisticsEntry_Object = MibTableRow
otu2StatisticsEntry = _Otu2StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1)
)
otu2StatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otu2StatisticsEntry.setStatus("current")
_Otu2StatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Otu2StatisticsEntryLastClear_Object = MibTableColumn
otu2StatisticsEntryLastClear = _Otu2StatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 1),
    _Otu2StatisticsEntryLastClear_Type()
)
otu2StatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntryLastClear.setStatus("current")
_Otu2StatisticsEntryLossOfSignalSeconds_Type = OctetString
_Otu2StatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
otu2StatisticsEntryLossOfSignalSeconds = _Otu2StatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 2),
    _Otu2StatisticsEntryLossOfSignalSeconds_Type()
)
otu2StatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntryLossOfSignalSeconds.setStatus("current")
_Otu2StatisticsEntryBitErrorFec_Type = OctetString
_Otu2StatisticsEntryBitErrorFec_Object = MibTableColumn
otu2StatisticsEntryBitErrorFec = _Otu2StatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 3),
    _Otu2StatisticsEntryBitErrorFec_Type()
)
otu2StatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntryBitErrorFec.setStatus("current")
_Otu2StatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Otu2StatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
otu2StatisticsEntryUncorrectedBlockErrorFec = _Otu2StatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 4),
    _Otu2StatisticsEntryUncorrectedBlockErrorFec_Type()
)
otu2StatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Otu2StatisticsEntryErroredBlocks_Type = OctetString
_Otu2StatisticsEntryErroredBlocks_Object = MibTableColumn
otu2StatisticsEntryErroredBlocks = _Otu2StatisticsEntryErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 5),
    _Otu2StatisticsEntryErroredBlocks_Type()
)
otu2StatisticsEntryErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntryErroredBlocks.setStatus("current")
_Otu2StatisticsEntryErroredSeconds_Type = OctetString
_Otu2StatisticsEntryErroredSeconds_Object = MibTableColumn
otu2StatisticsEntryErroredSeconds = _Otu2StatisticsEntryErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 6),
    _Otu2StatisticsEntryErroredSeconds_Type()
)
otu2StatisticsEntryErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntryErroredSeconds.setStatus("current")
_Otu2StatisticsEntrySeverelyErroredSeconds_Type = OctetString
_Otu2StatisticsEntrySeverelyErroredSeconds_Object = MibTableColumn
otu2StatisticsEntrySeverelyErroredSeconds = _Otu2StatisticsEntrySeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 7),
    _Otu2StatisticsEntrySeverelyErroredSeconds_Type()
)
otu2StatisticsEntrySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntrySeverelyErroredSeconds.setStatus("current")
_Otu2StatisticsEntryUnavailableSeconds_Type = OctetString
_Otu2StatisticsEntryUnavailableSeconds_Object = MibTableColumn
otu2StatisticsEntryUnavailableSeconds = _Otu2StatisticsEntryUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 37, 1, 1, 8),
    _Otu2StatisticsEntryUnavailableSeconds_Type()
)
otu2StatisticsEntryUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2StatisticsEntryUnavailableSeconds.setStatus("current")
_Otu2eStatistics_ObjectIdentity = ObjectIdentity
otu2eStatistics = _Otu2eStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38)
)
_Otu2eStatisticsTable_Object = MibTable
otu2eStatisticsTable = _Otu2eStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1)
)
if mibBuilder.loadTexts:
    otu2eStatisticsTable.setStatus("current")
_Otu2eStatisticsEntry_Object = MibTableRow
otu2eStatisticsEntry = _Otu2eStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1)
)
otu2eStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otu2eStatisticsEntry.setStatus("current")
_Otu2eStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Otu2eStatisticsEntryLastClear_Object = MibTableColumn
otu2eStatisticsEntryLastClear = _Otu2eStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 1),
    _Otu2eStatisticsEntryLastClear_Type()
)
otu2eStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntryLastClear.setStatus("current")
_Otu2eStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Otu2eStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
otu2eStatisticsEntryLossOfSignalSeconds = _Otu2eStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 2),
    _Otu2eStatisticsEntryLossOfSignalSeconds_Type()
)
otu2eStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Otu2eStatisticsEntryBitErrorFec_Type = OctetString
_Otu2eStatisticsEntryBitErrorFec_Object = MibTableColumn
otu2eStatisticsEntryBitErrorFec = _Otu2eStatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 3),
    _Otu2eStatisticsEntryBitErrorFec_Type()
)
otu2eStatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntryBitErrorFec.setStatus("current")
_Otu2eStatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Otu2eStatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
otu2eStatisticsEntryUncorrectedBlockErrorFec = _Otu2eStatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 4),
    _Otu2eStatisticsEntryUncorrectedBlockErrorFec_Type()
)
otu2eStatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Otu2eStatisticsEntryErroredBlocks_Type = OctetString
_Otu2eStatisticsEntryErroredBlocks_Object = MibTableColumn
otu2eStatisticsEntryErroredBlocks = _Otu2eStatisticsEntryErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 5),
    _Otu2eStatisticsEntryErroredBlocks_Type()
)
otu2eStatisticsEntryErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntryErroredBlocks.setStatus("current")
_Otu2eStatisticsEntryErroredSeconds_Type = OctetString
_Otu2eStatisticsEntryErroredSeconds_Object = MibTableColumn
otu2eStatisticsEntryErroredSeconds = _Otu2eStatisticsEntryErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 6),
    _Otu2eStatisticsEntryErroredSeconds_Type()
)
otu2eStatisticsEntryErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntryErroredSeconds.setStatus("current")
_Otu2eStatisticsEntrySeverelyErroredSeconds_Type = OctetString
_Otu2eStatisticsEntrySeverelyErroredSeconds_Object = MibTableColumn
otu2eStatisticsEntrySeverelyErroredSeconds = _Otu2eStatisticsEntrySeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 7),
    _Otu2eStatisticsEntrySeverelyErroredSeconds_Type()
)
otu2eStatisticsEntrySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntrySeverelyErroredSeconds.setStatus("current")
_Otu2eStatisticsEntryUnavailableSeconds_Type = OctetString
_Otu2eStatisticsEntryUnavailableSeconds_Object = MibTableColumn
otu2eStatisticsEntryUnavailableSeconds = _Otu2eStatisticsEntryUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 38, 1, 1, 8),
    _Otu2eStatisticsEntryUnavailableSeconds_Type()
)
otu2eStatisticsEntryUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otu2eStatisticsEntryUnavailableSeconds.setStatus("current")
_Oc192Statistics_ObjectIdentity = ObjectIdentity
oc192Statistics = _Oc192Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39)
)
_Oc192StatisticsTable_Object = MibTable
oc192StatisticsTable = _Oc192StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1)
)
if mibBuilder.loadTexts:
    oc192StatisticsTable.setStatus("current")
_Oc192StatisticsEntry_Object = MibTableRow
oc192StatisticsEntry = _Oc192StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1)
)
oc192StatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    oc192StatisticsEntry.setStatus("current")
_Oc192StatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Oc192StatisticsEntryLastClear_Object = MibTableColumn
oc192StatisticsEntryLastClear = _Oc192StatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1, 1),
    _Oc192StatisticsEntryLastClear_Type()
)
oc192StatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192StatisticsEntryLastClear.setStatus("current")
_Oc192StatisticsEntryLossOfSignalSeconds_Type = OctetString
_Oc192StatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
oc192StatisticsEntryLossOfSignalSeconds = _Oc192StatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1, 2),
    _Oc192StatisticsEntryLossOfSignalSeconds_Type()
)
oc192StatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192StatisticsEntryLossOfSignalSeconds.setStatus("current")
_Oc192StatisticsEntryInCodingViolation_Type = OctetString
_Oc192StatisticsEntryInCodingViolation_Object = MibTableColumn
oc192StatisticsEntryInCodingViolation = _Oc192StatisticsEntryInCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1, 3),
    _Oc192StatisticsEntryInCodingViolation_Type()
)
oc192StatisticsEntryInCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192StatisticsEntryInCodingViolation.setStatus("current")
_Oc192StatisticsEntryInErroredSeconds_Type = OctetString
_Oc192StatisticsEntryInErroredSeconds_Object = MibTableColumn
oc192StatisticsEntryInErroredSeconds = _Oc192StatisticsEntryInErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1, 4),
    _Oc192StatisticsEntryInErroredSeconds_Type()
)
oc192StatisticsEntryInErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192StatisticsEntryInErroredSeconds.setStatus("current")
_Oc192StatisticsEntryInSeverelyErroredSeconds_Type = OctetString
_Oc192StatisticsEntryInSeverelyErroredSeconds_Object = MibTableColumn
oc192StatisticsEntryInSeverelyErroredSeconds = _Oc192StatisticsEntryInSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1, 5),
    _Oc192StatisticsEntryInSeverelyErroredSeconds_Type()
)
oc192StatisticsEntryInSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192StatisticsEntryInSeverelyErroredSeconds.setStatus("current")
_Oc192StatisticsEntryInUnavailableSeconds_Type = OctetString
_Oc192StatisticsEntryInUnavailableSeconds_Object = MibTableColumn
oc192StatisticsEntryInUnavailableSeconds = _Oc192StatisticsEntryInUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1, 6),
    _Oc192StatisticsEntryInUnavailableSeconds_Type()
)
oc192StatisticsEntryInUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192StatisticsEntryInUnavailableSeconds.setStatus("current")
_Oc192StatisticsEntryInSeverelyErroredFrameSecond_Type = OctetString
_Oc192StatisticsEntryInSeverelyErroredFrameSecond_Object = MibTableColumn
oc192StatisticsEntryInSeverelyErroredFrameSecond = _Oc192StatisticsEntryInSeverelyErroredFrameSecond_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 39, 1, 1, 7),
    _Oc192StatisticsEntryInSeverelyErroredFrameSecond_Type()
)
oc192StatisticsEntryInSeverelyErroredFrameSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc192StatisticsEntryInSeverelyErroredFrameSecond.setStatus("current")
_Stm64Statistics_ObjectIdentity = ObjectIdentity
stm64Statistics = _Stm64Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40)
)
_Stm64StatisticsTable_Object = MibTable
stm64StatisticsTable = _Stm64StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1)
)
if mibBuilder.loadTexts:
    stm64StatisticsTable.setStatus("current")
_Stm64StatisticsEntry_Object = MibTableRow
stm64StatisticsEntry = _Stm64StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1)
)
stm64StatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    stm64StatisticsEntry.setStatus("current")
_Stm64StatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Stm64StatisticsEntryLastClear_Object = MibTableColumn
stm64StatisticsEntryLastClear = _Stm64StatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1, 1),
    _Stm64StatisticsEntryLastClear_Type()
)
stm64StatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64StatisticsEntryLastClear.setStatus("current")
_Stm64StatisticsEntryLossOfSignalSeconds_Type = OctetString
_Stm64StatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
stm64StatisticsEntryLossOfSignalSeconds = _Stm64StatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1, 2),
    _Stm64StatisticsEntryLossOfSignalSeconds_Type()
)
stm64StatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64StatisticsEntryLossOfSignalSeconds.setStatus("current")
_Stm64StatisticsEntryInBackgroundBlockError_Type = OctetString
_Stm64StatisticsEntryInBackgroundBlockError_Object = MibTableColumn
stm64StatisticsEntryInBackgroundBlockError = _Stm64StatisticsEntryInBackgroundBlockError_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1, 3),
    _Stm64StatisticsEntryInBackgroundBlockError_Type()
)
stm64StatisticsEntryInBackgroundBlockError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64StatisticsEntryInBackgroundBlockError.setStatus("current")
_Stm64StatisticsEntryInErroredSeconds_Type = OctetString
_Stm64StatisticsEntryInErroredSeconds_Object = MibTableColumn
stm64StatisticsEntryInErroredSeconds = _Stm64StatisticsEntryInErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1, 4),
    _Stm64StatisticsEntryInErroredSeconds_Type()
)
stm64StatisticsEntryInErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64StatisticsEntryInErroredSeconds.setStatus("current")
_Stm64StatisticsEntryInSeverelyErroredSeconds_Type = OctetString
_Stm64StatisticsEntryInSeverelyErroredSeconds_Object = MibTableColumn
stm64StatisticsEntryInSeverelyErroredSeconds = _Stm64StatisticsEntryInSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1, 5),
    _Stm64StatisticsEntryInSeverelyErroredSeconds_Type()
)
stm64StatisticsEntryInSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64StatisticsEntryInSeverelyErroredSeconds.setStatus("current")
_Stm64StatisticsEntryInUnavailableSeconds_Type = OctetString
_Stm64StatisticsEntryInUnavailableSeconds_Object = MibTableColumn
stm64StatisticsEntryInUnavailableSeconds = _Stm64StatisticsEntryInUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1, 6),
    _Stm64StatisticsEntryInUnavailableSeconds_Type()
)
stm64StatisticsEntryInUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64StatisticsEntryInUnavailableSeconds.setStatus("current")
_Stm64StatisticsEntryInOutOfFrameSeconds_Type = OctetString
_Stm64StatisticsEntryInOutOfFrameSeconds_Object = MibTableColumn
stm64StatisticsEntryInOutOfFrameSeconds = _Stm64StatisticsEntryInOutOfFrameSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 40, 1, 1, 7),
    _Stm64StatisticsEntryInOutOfFrameSeconds_Type()
)
stm64StatisticsEntryInOutOfFrameSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm64StatisticsEntryInOutOfFrameSeconds.setStatus("current")
_Wan10gSonetStatistics_ObjectIdentity = ObjectIdentity
wan10gSonetStatistics = _Wan10gSonetStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41)
)
_Wan10gSonetStatisticsTable_Object = MibTable
wan10gSonetStatisticsTable = _Wan10gSonetStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1)
)
if mibBuilder.loadTexts:
    wan10gSonetStatisticsTable.setStatus("current")
_Wan10gSonetStatisticsEntry_Object = MibTableRow
wan10gSonetStatisticsEntry = _Wan10gSonetStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1)
)
wan10gSonetStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntry.setStatus("current")
_Wan10gSonetStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Wan10gSonetStatisticsEntryLastClear_Object = MibTableColumn
wan10gSonetStatisticsEntryLastClear = _Wan10gSonetStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1, 1),
    _Wan10gSonetStatisticsEntryLastClear_Type()
)
wan10gSonetStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntryLastClear.setStatus("current")
_Wan10gSonetStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Wan10gSonetStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
wan10gSonetStatisticsEntryLossOfSignalSeconds = _Wan10gSonetStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1, 2),
    _Wan10gSonetStatisticsEntryLossOfSignalSeconds_Type()
)
wan10gSonetStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Wan10gSonetStatisticsEntryInCodingViolation_Type = OctetString
_Wan10gSonetStatisticsEntryInCodingViolation_Object = MibTableColumn
wan10gSonetStatisticsEntryInCodingViolation = _Wan10gSonetStatisticsEntryInCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1, 3),
    _Wan10gSonetStatisticsEntryInCodingViolation_Type()
)
wan10gSonetStatisticsEntryInCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntryInCodingViolation.setStatus("current")
_Wan10gSonetStatisticsEntryInErroredSeconds_Type = OctetString
_Wan10gSonetStatisticsEntryInErroredSeconds_Object = MibTableColumn
wan10gSonetStatisticsEntryInErroredSeconds = _Wan10gSonetStatisticsEntryInErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1, 4),
    _Wan10gSonetStatisticsEntryInErroredSeconds_Type()
)
wan10gSonetStatisticsEntryInErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntryInErroredSeconds.setStatus("current")
_Wan10gSonetStatisticsEntryInSeverelyErroredSeconds_Type = OctetString
_Wan10gSonetStatisticsEntryInSeverelyErroredSeconds_Object = MibTableColumn
wan10gSonetStatisticsEntryInSeverelyErroredSeconds = _Wan10gSonetStatisticsEntryInSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1, 5),
    _Wan10gSonetStatisticsEntryInSeverelyErroredSeconds_Type()
)
wan10gSonetStatisticsEntryInSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntryInSeverelyErroredSeconds.setStatus("current")
_Wan10gSonetStatisticsEntryInUnavailableSeconds_Type = OctetString
_Wan10gSonetStatisticsEntryInUnavailableSeconds_Object = MibTableColumn
wan10gSonetStatisticsEntryInUnavailableSeconds = _Wan10gSonetStatisticsEntryInUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1, 6),
    _Wan10gSonetStatisticsEntryInUnavailableSeconds_Type()
)
wan10gSonetStatisticsEntryInUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntryInUnavailableSeconds.setStatus("current")
_Wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond_Type = OctetString
_Wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond_Object = MibTableColumn
wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond = _Wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 41, 1, 1, 7),
    _Wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond_Type()
)
wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond.setStatus("current")
_Wan10gSdhStatistics_ObjectIdentity = ObjectIdentity
wan10gSdhStatistics = _Wan10gSdhStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42)
)
_Wan10gSdhStatisticsTable_Object = MibTable
wan10gSdhStatisticsTable = _Wan10gSdhStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1)
)
if mibBuilder.loadTexts:
    wan10gSdhStatisticsTable.setStatus("current")
_Wan10gSdhStatisticsEntry_Object = MibTableRow
wan10gSdhStatisticsEntry = _Wan10gSdhStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1)
)
wan10gSdhStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntry.setStatus("current")
_Wan10gSdhStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Wan10gSdhStatisticsEntryLastClear_Object = MibTableColumn
wan10gSdhStatisticsEntryLastClear = _Wan10gSdhStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1, 1),
    _Wan10gSdhStatisticsEntryLastClear_Type()
)
wan10gSdhStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntryLastClear.setStatus("current")
_Wan10gSdhStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Wan10gSdhStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
wan10gSdhStatisticsEntryLossOfSignalSeconds = _Wan10gSdhStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1, 2),
    _Wan10gSdhStatisticsEntryLossOfSignalSeconds_Type()
)
wan10gSdhStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Wan10gSdhStatisticsEntryInBackgroundBlockError_Type = OctetString
_Wan10gSdhStatisticsEntryInBackgroundBlockError_Object = MibTableColumn
wan10gSdhStatisticsEntryInBackgroundBlockError = _Wan10gSdhStatisticsEntryInBackgroundBlockError_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1, 3),
    _Wan10gSdhStatisticsEntryInBackgroundBlockError_Type()
)
wan10gSdhStatisticsEntryInBackgroundBlockError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntryInBackgroundBlockError.setStatus("current")
_Wan10gSdhStatisticsEntryInErroredSeconds_Type = OctetString
_Wan10gSdhStatisticsEntryInErroredSeconds_Object = MibTableColumn
wan10gSdhStatisticsEntryInErroredSeconds = _Wan10gSdhStatisticsEntryInErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1, 4),
    _Wan10gSdhStatisticsEntryInErroredSeconds_Type()
)
wan10gSdhStatisticsEntryInErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntryInErroredSeconds.setStatus("current")
_Wan10gSdhStatisticsEntryInSeverelyErroredSeconds_Type = OctetString
_Wan10gSdhStatisticsEntryInSeverelyErroredSeconds_Object = MibTableColumn
wan10gSdhStatisticsEntryInSeverelyErroredSeconds = _Wan10gSdhStatisticsEntryInSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1, 5),
    _Wan10gSdhStatisticsEntryInSeverelyErroredSeconds_Type()
)
wan10gSdhStatisticsEntryInSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntryInSeverelyErroredSeconds.setStatus("current")
_Wan10gSdhStatisticsEntryInUnavailableSeconds_Type = OctetString
_Wan10gSdhStatisticsEntryInUnavailableSeconds_Object = MibTableColumn
wan10gSdhStatisticsEntryInUnavailableSeconds = _Wan10gSdhStatisticsEntryInUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1, 6),
    _Wan10gSdhStatisticsEntryInUnavailableSeconds_Type()
)
wan10gSdhStatisticsEntryInUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntryInUnavailableSeconds.setStatus("current")
_Wan10gSdhStatisticsEntryInOutOfFrameSeconds_Type = OctetString
_Wan10gSdhStatisticsEntryInOutOfFrameSeconds_Object = MibTableColumn
wan10gSdhStatisticsEntryInOutOfFrameSeconds = _Wan10gSdhStatisticsEntryInOutOfFrameSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 42, 1, 1, 7),
    _Wan10gSdhStatisticsEntryInOutOfFrameSeconds_Type()
)
wan10gSdhStatisticsEntryInOutOfFrameSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan10gSdhStatisticsEntryInOutOfFrameSeconds.setStatus("current")
_Fc8gStatistics_ObjectIdentity = ObjectIdentity
fc8gStatistics = _Fc8gStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 43)
)
_Fc8gStatisticsTable_Object = MibTable
fc8gStatisticsTable = _Fc8gStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 43, 1)
)
if mibBuilder.loadTexts:
    fc8gStatisticsTable.setStatus("current")
_Fc8gStatisticsEntry_Object = MibTableRow
fc8gStatisticsEntry = _Fc8gStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 43, 1, 1)
)
fc8gStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    fc8gStatisticsEntry.setStatus("current")
_Fc8gStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Fc8gStatisticsEntryLastClear_Object = MibTableColumn
fc8gStatisticsEntryLastClear = _Fc8gStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 43, 1, 1, 1),
    _Fc8gStatisticsEntryLastClear_Type()
)
fc8gStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gStatisticsEntryLastClear.setStatus("current")
_Fc8gStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Fc8gStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
fc8gStatisticsEntryLossOfSignalSeconds = _Fc8gStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 43, 1, 1, 2),
    _Fc8gStatisticsEntryLossOfSignalSeconds_Type()
)
fc8gStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Fc8gStatisticsEntryInSymbolErrors_Type = OctetString
_Fc8gStatisticsEntryInSymbolErrors_Object = MibTableColumn
fc8gStatisticsEntryInSymbolErrors = _Fc8gStatisticsEntryInSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 43, 1, 1, 3),
    _Fc8gStatisticsEntryInSymbolErrors_Type()
)
fc8gStatisticsEntryInSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc8gStatisticsEntryInSymbolErrors.setStatus("current")
_Fc16gStatistics_ObjectIdentity = ObjectIdentity
fc16gStatistics = _Fc16gStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 44)
)
_Fc16gStatisticsTable_Object = MibTable
fc16gStatisticsTable = _Fc16gStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 44, 1)
)
if mibBuilder.loadTexts:
    fc16gStatisticsTable.setStatus("current")
_Fc16gStatisticsEntry_Object = MibTableRow
fc16gStatisticsEntry = _Fc16gStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 44, 1, 1)
)
fc16gStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    fc16gStatisticsEntry.setStatus("current")
_Fc16gStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Fc16gStatisticsEntryLastClear_Object = MibTableColumn
fc16gStatisticsEntryLastClear = _Fc16gStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 44, 1, 1, 1),
    _Fc16gStatisticsEntryLastClear_Type()
)
fc16gStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gStatisticsEntryLastClear.setStatus("current")
_Fc16gStatisticsEntryLossOfSignalSeconds_Type = OctetString
_Fc16gStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
fc16gStatisticsEntryLossOfSignalSeconds = _Fc16gStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 44, 1, 1, 2),
    _Fc16gStatisticsEntryLossOfSignalSeconds_Type()
)
fc16gStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gStatisticsEntryLossOfSignalSeconds.setStatus("current")
_Fc16gStatisticsEntryInSymbolErrors_Type = OctetString
_Fc16gStatisticsEntryInSymbolErrors_Object = MibTableColumn
fc16gStatisticsEntryInSymbolErrors = _Fc16gStatisticsEntryInSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 44, 1, 1, 3),
    _Fc16gStatisticsEntryInSymbolErrors_Type()
)
fc16gStatisticsEntryInSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc16gStatisticsEntryInSymbolErrors.setStatus("current")
_Otuc2Statistics_ObjectIdentity = ObjectIdentity
otuc2Statistics = _Otuc2Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45)
)
_Otuc2StatisticsTable_Object = MibTable
otuc2StatisticsTable = _Otuc2StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1)
)
if mibBuilder.loadTexts:
    otuc2StatisticsTable.setStatus("current")
_Otuc2StatisticsEntry_Object = MibTableRow
otuc2StatisticsEntry = _Otuc2StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1)
)
otuc2StatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otuc2StatisticsEntry.setStatus("current")
_Otuc2StatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Otuc2StatisticsEntryLastClear_Object = MibTableColumn
otuc2StatisticsEntryLastClear = _Otuc2StatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 1),
    _Otuc2StatisticsEntryLastClear_Type()
)
otuc2StatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntryLastClear.setStatus("current")
_Otuc2StatisticsEntryLossOfSignalSeconds_Type = OctetString
_Otuc2StatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
otuc2StatisticsEntryLossOfSignalSeconds = _Otuc2StatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 2),
    _Otuc2StatisticsEntryLossOfSignalSeconds_Type()
)
otuc2StatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntryLossOfSignalSeconds.setStatus("current")
_Otuc2StatisticsEntryBitErrorFec_Type = OctetString
_Otuc2StatisticsEntryBitErrorFec_Object = MibTableColumn
otuc2StatisticsEntryBitErrorFec = _Otuc2StatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 3),
    _Otuc2StatisticsEntryBitErrorFec_Type()
)
otuc2StatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntryBitErrorFec.setStatus("current")
_Otuc2StatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Otuc2StatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
otuc2StatisticsEntryUncorrectedBlockErrorFec = _Otuc2StatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 4),
    _Otuc2StatisticsEntryUncorrectedBlockErrorFec_Type()
)
otuc2StatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Otuc2StatisticsEntryErroredBlocks_Type = OctetString
_Otuc2StatisticsEntryErroredBlocks_Object = MibTableColumn
otuc2StatisticsEntryErroredBlocks = _Otuc2StatisticsEntryErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 5),
    _Otuc2StatisticsEntryErroredBlocks_Type()
)
otuc2StatisticsEntryErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntryErroredBlocks.setStatus("current")
_Otuc2StatisticsEntryErroredSeconds_Type = OctetString
_Otuc2StatisticsEntryErroredSeconds_Object = MibTableColumn
otuc2StatisticsEntryErroredSeconds = _Otuc2StatisticsEntryErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 6),
    _Otuc2StatisticsEntryErroredSeconds_Type()
)
otuc2StatisticsEntryErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntryErroredSeconds.setStatus("current")
_Otuc2StatisticsEntrySeverelyErroredSeconds_Type = OctetString
_Otuc2StatisticsEntrySeverelyErroredSeconds_Object = MibTableColumn
otuc2StatisticsEntrySeverelyErroredSeconds = _Otuc2StatisticsEntrySeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 7),
    _Otuc2StatisticsEntrySeverelyErroredSeconds_Type()
)
otuc2StatisticsEntrySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntrySeverelyErroredSeconds.setStatus("current")
_Otuc2StatisticsEntryUnavailableSeconds_Type = OctetString
_Otuc2StatisticsEntryUnavailableSeconds_Object = MibTableColumn
otuc2StatisticsEntryUnavailableSeconds = _Otuc2StatisticsEntryUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 45, 1, 1, 8),
    _Otuc2StatisticsEntryUnavailableSeconds_Type()
)
otuc2StatisticsEntryUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc2StatisticsEntryUnavailableSeconds.setStatus("current")
_Otuc3Statistics_ObjectIdentity = ObjectIdentity
otuc3Statistics = _Otuc3Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46)
)
_Otuc3StatisticsTable_Object = MibTable
otuc3StatisticsTable = _Otuc3StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1)
)
if mibBuilder.loadTexts:
    otuc3StatisticsTable.setStatus("current")
_Otuc3StatisticsEntry_Object = MibTableRow
otuc3StatisticsEntry = _Otuc3StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1)
)
otuc3StatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    otuc3StatisticsEntry.setStatus("current")
_Otuc3StatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_Otuc3StatisticsEntryLastClear_Object = MibTableColumn
otuc3StatisticsEntryLastClear = _Otuc3StatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 1),
    _Otuc3StatisticsEntryLastClear_Type()
)
otuc3StatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntryLastClear.setStatus("current")
_Otuc3StatisticsEntryLossOfSignalSeconds_Type = OctetString
_Otuc3StatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
otuc3StatisticsEntryLossOfSignalSeconds = _Otuc3StatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 2),
    _Otuc3StatisticsEntryLossOfSignalSeconds_Type()
)
otuc3StatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntryLossOfSignalSeconds.setStatus("current")
_Otuc3StatisticsEntryBitErrorFec_Type = OctetString
_Otuc3StatisticsEntryBitErrorFec_Object = MibTableColumn
otuc3StatisticsEntryBitErrorFec = _Otuc3StatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 3),
    _Otuc3StatisticsEntryBitErrorFec_Type()
)
otuc3StatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntryBitErrorFec.setStatus("current")
_Otuc3StatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_Otuc3StatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
otuc3StatisticsEntryUncorrectedBlockErrorFec = _Otuc3StatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 4),
    _Otuc3StatisticsEntryUncorrectedBlockErrorFec_Type()
)
otuc3StatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_Otuc3StatisticsEntryErroredBlocks_Type = OctetString
_Otuc3StatisticsEntryErroredBlocks_Object = MibTableColumn
otuc3StatisticsEntryErroredBlocks = _Otuc3StatisticsEntryErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 5),
    _Otuc3StatisticsEntryErroredBlocks_Type()
)
otuc3StatisticsEntryErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntryErroredBlocks.setStatus("current")
_Otuc3StatisticsEntryErroredSeconds_Type = OctetString
_Otuc3StatisticsEntryErroredSeconds_Object = MibTableColumn
otuc3StatisticsEntryErroredSeconds = _Otuc3StatisticsEntryErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 6),
    _Otuc3StatisticsEntryErroredSeconds_Type()
)
otuc3StatisticsEntryErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntryErroredSeconds.setStatus("current")
_Otuc3StatisticsEntrySeverelyErroredSeconds_Type = OctetString
_Otuc3StatisticsEntrySeverelyErroredSeconds_Object = MibTableColumn
otuc3StatisticsEntrySeverelyErroredSeconds = _Otuc3StatisticsEntrySeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 7),
    _Otuc3StatisticsEntrySeverelyErroredSeconds_Type()
)
otuc3StatisticsEntrySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntrySeverelyErroredSeconds.setStatus("current")
_Otuc3StatisticsEntryUnavailableSeconds_Type = OctetString
_Otuc3StatisticsEntryUnavailableSeconds_Object = MibTableColumn
otuc3StatisticsEntryUnavailableSeconds = _Otuc3StatisticsEntryUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 46, 1, 1, 8),
    _Otuc3StatisticsEntryUnavailableSeconds_Type()
)
otuc3StatisticsEntryUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuc3StatisticsEntryUnavailableSeconds.setStatus("current")
_OchOsStatistics_ObjectIdentity = ObjectIdentity
ochOsStatistics = _OchOsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 47)
)
_OchOsStatisticsTable_Object = MibTable
ochOsStatisticsTable = _OchOsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 47, 1)
)
if mibBuilder.loadTexts:
    ochOsStatisticsTable.setStatus("current")
_OchOsStatisticsEntry_Object = MibTableRow
ochOsStatisticsEntry = _OchOsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 47, 1, 1)
)
ochOsStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    ochOsStatisticsEntry.setStatus("current")
_OchOsStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_OchOsStatisticsEntryLastClear_Object = MibTableColumn
ochOsStatisticsEntryLastClear = _OchOsStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 47, 1, 1, 1),
    _OchOsStatisticsEntryLastClear_Type()
)
ochOsStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsStatisticsEntryLastClear.setStatus("current")
_OchOsStatisticsEntryLossOfSignalSeconds_Type = OctetString
_OchOsStatisticsEntryLossOfSignalSeconds_Object = MibTableColumn
ochOsStatisticsEntryLossOfSignalSeconds = _OchOsStatisticsEntryLossOfSignalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 47, 1, 1, 2),
    _OchOsStatisticsEntryLossOfSignalSeconds_Type()
)
ochOsStatisticsEntryLossOfSignalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsStatisticsEntryLossOfSignalSeconds.setStatus("current")
_OchOsStatisticsEntryBitErrorFec_Type = OctetString
_OchOsStatisticsEntryBitErrorFec_Object = MibTableColumn
ochOsStatisticsEntryBitErrorFec = _OchOsStatisticsEntryBitErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 47, 1, 1, 3),
    _OchOsStatisticsEntryBitErrorFec_Type()
)
ochOsStatisticsEntryBitErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsStatisticsEntryBitErrorFec.setStatus("current")
_OchOsStatisticsEntryUncorrectedBlockErrorFec_Type = OctetString
_OchOsStatisticsEntryUncorrectedBlockErrorFec_Object = MibTableColumn
ochOsStatisticsEntryUncorrectedBlockErrorFec = _OchOsStatisticsEntryUncorrectedBlockErrorFec_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 1, 47, 1, 1, 4),
    _OchOsStatisticsEntryUncorrectedBlockErrorFec_Type()
)
ochOsStatisticsEntryUncorrectedBlockErrorFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochOsStatisticsEntryUncorrectedBlockErrorFec.setStatus("current")
_CRS_ObjectIdentity = ObjectIdentity
cRS = _CRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3)
)
_CRSTable_Object = MibTable
cRSTable = _CRSTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cRSTable.setStatus("current")
_CRSEntry_Object = MibTableRow
cRSEntry = _CRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3, 1, 1)
)
cRSEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "cRSSrcTp"),
    (0, "CORIANT-GROOVE-MIB", "cRSDstTp"),
)
if mibBuilder.loadTexts:
    cRSEntry.setStatus("current")
_CRSSrcTp_Type = RowPointer
_CRSSrcTp_Object = MibTableColumn
cRSSrcTp = _CRSSrcTp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3, 1, 1, 1),
    _CRSSrcTp_Type()
)
cRSSrcTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRSSrcTp.setStatus("current")
_CRSDstTp_Type = RowPointer
_CRSDstTp_Object = MibTableColumn
cRSDstTp = _CRSDstTp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3, 1, 1, 2),
    _CRSDstTp_Type()
)
cRSDstTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRSDstTp.setStatus("current")


class _CRSServiceLabel_Type(OctetString):
    """Custom type cRSServiceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CRSServiceLabel_Type.__name__ = "OctetString"
_CRSServiceLabel_Object = MibTableColumn
cRSServiceLabel = _CRSServiceLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3, 1, 1, 3),
    _CRSServiceLabel_Type()
)
cRSServiceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRSServiceLabel.setStatus("current")


class _CRSManagedBy_Type(Integer32):
    """Custom type cRSManagedBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("user", 2))
    )


_CRSManagedBy_Type.__name__ = "Integer32"
_CRSManagedBy_Object = MibTableColumn
cRSManagedBy = _CRSManagedBy_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3, 1, 1, 4),
    _CRSManagedBy_Type()
)
cRSManagedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRSManagedBy.setStatus("current")


class _CRSAliasName_Type(OctetString):
    """Custom type cRSAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CRSAliasName_Type.__name__ = "OctetString"
_CRSAliasName_Object = MibTableColumn
cRSAliasName = _CRSAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 3, 1, 1, 5),
    _CRSAliasName_Type()
)
cRSAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRSAliasName.setStatus("current")
_FiberConnection_ObjectIdentity = ObjectIdentity
fiberConnection = _FiberConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4)
)
_FiberConnectionTable_Object = MibTable
fiberConnectionTable = _FiberConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    fiberConnectionTable.setStatus("current")
_FiberConnectionEntry_Object = MibTableRow
fiberConnectionEntry = _FiberConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4, 1, 1)
)
fiberConnectionEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "fiberConnectionSrcPort"),
    (0, "CORIANT-GROOVE-MIB", "fiberConnectionDstPort"),
)
if mibBuilder.loadTexts:
    fiberConnectionEntry.setStatus("current")
_FiberConnectionSrcPort_Type = RowPointer
_FiberConnectionSrcPort_Object = MibTableColumn
fiberConnectionSrcPort = _FiberConnectionSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4, 1, 1, 1),
    _FiberConnectionSrcPort_Type()
)
fiberConnectionSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberConnectionSrcPort.setStatus("current")
_FiberConnectionDstPort_Type = RowPointer
_FiberConnectionDstPort_Object = MibTableColumn
fiberConnectionDstPort = _FiberConnectionDstPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4, 1, 1, 2),
    _FiberConnectionDstPort_Type()
)
fiberConnectionDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberConnectionDstPort.setStatus("current")


class _FiberConnectionType_Type(Integer32):
    """Custom type fiberConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoWay", 1),
          ("oneWay", 2))
    )


_FiberConnectionType_Type.__name__ = "Integer32"
_FiberConnectionType_Object = MibTableColumn
fiberConnectionType = _FiberConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4, 1, 1, 3),
    _FiberConnectionType_Type()
)
fiberConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberConnectionType.setStatus("current")


class _FiberConnectionFiberLabel_Type(OctetString):
    """Custom type fiberConnectionFiberLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FiberConnectionFiberLabel_Type.__name__ = "OctetString"
_FiberConnectionFiberLabel_Object = MibTableColumn
fiberConnectionFiberLabel = _FiberConnectionFiberLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4, 1, 1, 4),
    _FiberConnectionFiberLabel_Type()
)
fiberConnectionFiberLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberConnectionFiberLabel.setStatus("current")


class _FiberConnectionAliasName_Type(OctetString):
    """Custom type fiberConnectionAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FiberConnectionAliasName_Type.__name__ = "OctetString"
_FiberConnectionAliasName_Object = MibTableColumn
fiberConnectionAliasName = _FiberConnectionAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 4, 1, 1, 5),
    _FiberConnectionAliasName_Type()
)
fiberConnectionAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberConnectionAliasName.setStatus("current")
_Optical_ObjectIdentity = ObjectIdentity
optical = _Optical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5)
)
_Ots_ObjectIdentity = ObjectIdentity
ots = _Ots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2)
)
_OtsTable_Object = MibTable
otsTable = _OtsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    otsTable.setStatus("current")
_OtsEntry_Object = MibTableRow
otsEntry = _OtsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1)
)
otsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "otsName"),
)
if mibBuilder.loadTexts:
    otsEntry.setStatus("current")
_OtsName_Type = CoriantTypesNameIdentifier
_OtsName_Object = MibTableColumn
otsName = _OtsName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 1),
    _OtsName_Type()
)
otsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsName.setStatus("current")


class _OtsAdminStatus_Type(Integer32):
    """Custom type otsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OtsAdminStatus_Type.__name__ = "Integer32"
_OtsAdminStatus_Object = MibTableColumn
otsAdminStatus = _OtsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 2),
    _OtsAdminStatus_Type()
)
otsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsAdminStatus.setStatus("current")


class _OtsOperStatus_Type(Integer32):
    """Custom type otsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OtsOperStatus_Type.__name__ = "Integer32"
_OtsOperStatus_Object = MibTableColumn
otsOperStatus = _OtsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 3),
    _OtsOperStatus_Type()
)
otsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsOperStatus.setStatus("current")


class _OtsAvailStatus_Type(Bits):
    """Custom type otsAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_OtsAvailStatus_Type.__name__ = "Bits"
_OtsAvailStatus_Object = MibTableColumn
otsAvailStatus = _OtsAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 4),
    _OtsAvailStatus_Type()
)
otsAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsAvailStatus.setStatus("current")


class _OtsAliasName_Type(OctetString):
    """Custom type otsAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OtsAliasName_Type.__name__ = "OctetString"
_OtsAliasName_Object = MibTableColumn
otsAliasName = _OtsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 5),
    _OtsAliasName_Type()
)
otsAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsAliasName.setStatus("current")
_OtsSupportingRxPort_Type = OpticalCommonSupportingPort
_OtsSupportingRxPort_Object = MibTableColumn
otsSupportingRxPort = _OtsSupportingRxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 6),
    _OtsSupportingRxPort_Type()
)
otsSupportingRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsSupportingRxPort.setStatus("current")
_OtsSupportingTxPort_Type = OpticalCommonSupportingPort
_OtsSupportingTxPort_Object = MibTableColumn
otsSupportingTxPort = _OtsSupportingTxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 7),
    _OtsSupportingTxPort_Type()
)
otsSupportingTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsSupportingTxPort.setStatus("current")
_OtsMeasuredSpanLoss_Type = CoriantTypesOpticalDB
_OtsMeasuredSpanLoss_Object = MibTableColumn
otsMeasuredSpanLoss = _OtsMeasuredSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 2, 1, 1, 8),
    _OtsMeasuredSpanLoss_Type()
)
otsMeasuredSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsMeasuredSpanLoss.setStatus("current")
_Oms_ObjectIdentity = ObjectIdentity
oms = _Oms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3)
)
_OmsTable_Object = MibTable
omsTable = _OmsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1)
)
if mibBuilder.loadTexts:
    omsTable.setStatus("current")
_OmsEntry_Object = MibTableRow
omsEntry = _OmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1)
)
omsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "omsName"),
)
if mibBuilder.loadTexts:
    omsEntry.setStatus("current")
_OmsName_Type = CoriantTypesNameIdentifier
_OmsName_Object = MibTableColumn
omsName = _OmsName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 1),
    _OmsName_Type()
)
omsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsName.setStatus("current")


class _OmsAdminStatus_Type(Integer32):
    """Custom type omsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OmsAdminStatus_Type.__name__ = "Integer32"
_OmsAdminStatus_Object = MibTableColumn
omsAdminStatus = _OmsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 2),
    _OmsAdminStatus_Type()
)
omsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsAdminStatus.setStatus("current")


class _OmsOperStatus_Type(Integer32):
    """Custom type omsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OmsOperStatus_Type.__name__ = "Integer32"
_OmsOperStatus_Object = MibTableColumn
omsOperStatus = _OmsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 3),
    _OmsOperStatus_Type()
)
omsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsOperStatus.setStatus("current")


class _OmsAvailStatus_Type(Bits):
    """Custom type omsAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_OmsAvailStatus_Type.__name__ = "Bits"
_OmsAvailStatus_Object = MibTableColumn
omsAvailStatus = _OmsAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 4),
    _OmsAvailStatus_Type()
)
omsAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsAvailStatus.setStatus("current")


class _OmsAliasName_Type(OctetString):
    """Custom type omsAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OmsAliasName_Type.__name__ = "OctetString"
_OmsAliasName_Object = MibTableColumn
omsAliasName = _OmsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 5),
    _OmsAliasName_Type()
)
omsAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsAliasName.setStatus("current")
_OmsSupportingRxPort_Type = OpticalCommonSupportingPort
_OmsSupportingRxPort_Object = MibTableColumn
omsSupportingRxPort = _OmsSupportingRxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 6),
    _OmsSupportingRxPort_Type()
)
omsSupportingRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsSupportingRxPort.setStatus("current")
_OmsSupportingTxPort_Type = OpticalCommonSupportingPort
_OmsSupportingTxPort_Object = MibTableColumn
omsSupportingTxPort = _OmsSupportingTxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 7),
    _OmsSupportingTxPort_Type()
)
omsSupportingTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsSupportingTxPort.setStatus("current")
_OmsParentOtsInterface_Type = RowPointer
_OmsParentOtsInterface_Object = MibTableColumn
omsParentOtsInterface = _OmsParentOtsInterface_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 8),
    _OmsParentOtsInterface_Type()
)
omsParentOtsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsParentOtsInterface.setStatus("current")
_OmsRxOpticalPower_Type = CoriantTypesOpticalPower
_OmsRxOpticalPower_Object = MibTableColumn
omsRxOpticalPower = _OmsRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 9),
    _OmsRxOpticalPower_Type()
)
omsRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsRxOpticalPower.setStatus("current")
_OmsTxOpticalPower_Type = CoriantTypesOpticalPower
_OmsTxOpticalPower_Object = MibTableColumn
omsTxOpticalPower = _OmsTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 3, 1, 1, 10),
    _OmsTxOpticalPower_Type()
)
omsTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTxOpticalPower.setStatus("current")
_Osc_ObjectIdentity = ObjectIdentity
osc = _Osc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4)
)
_OscTable_Object = MibTable
oscTable = _OscTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1)
)
if mibBuilder.loadTexts:
    oscTable.setStatus("current")
_OscEntry_Object = MibTableRow
oscEntry = _OscEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1)
)
oscEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "oscName"),
)
if mibBuilder.loadTexts:
    oscEntry.setStatus("current")
_OscName_Type = CoriantTypesNameIdentifier
_OscName_Object = MibTableColumn
oscName = _OscName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 1),
    _OscName_Type()
)
oscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscName.setStatus("current")


class _OscAdminStatus_Type(Integer32):
    """Custom type oscAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OscAdminStatus_Type.__name__ = "Integer32"
_OscAdminStatus_Object = MibTableColumn
oscAdminStatus = _OscAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 2),
    _OscAdminStatus_Type()
)
oscAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscAdminStatus.setStatus("current")


class _OscOperStatus_Type(Integer32):
    """Custom type oscOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OscOperStatus_Type.__name__ = "Integer32"
_OscOperStatus_Object = MibTableColumn
oscOperStatus = _OscOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 3),
    _OscOperStatus_Type()
)
oscOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscOperStatus.setStatus("current")


class _OscAvailStatus_Type(Bits):
    """Custom type oscAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_OscAvailStatus_Type.__name__ = "Bits"
_OscAvailStatus_Object = MibTableColumn
oscAvailStatus = _OscAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 4),
    _OscAvailStatus_Type()
)
oscAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscAvailStatus.setStatus("current")


class _OscAliasName_Type(OctetString):
    """Custom type oscAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OscAliasName_Type.__name__ = "OctetString"
_OscAliasName_Object = MibTableColumn
oscAliasName = _OscAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 5),
    _OscAliasName_Type()
)
oscAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscAliasName.setStatus("current")
_OscSupportingRxPort_Type = OpticalCommonSupportingPort
_OscSupportingRxPort_Object = MibTableColumn
oscSupportingRxPort = _OscSupportingRxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 6),
    _OscSupportingRxPort_Type()
)
oscSupportingRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscSupportingRxPort.setStatus("current")
_OscSupportingTxPort_Type = OpticalCommonSupportingPort
_OscSupportingTxPort_Object = MibTableColumn
oscSupportingTxPort = _OscSupportingTxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 7),
    _OscSupportingTxPort_Type()
)
oscSupportingTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscSupportingTxPort.setStatus("current")
_OscParentOtsInterface_Type = RowPointer
_OscParentOtsInterface_Object = MibTableColumn
oscParentOtsInterface = _OscParentOtsInterface_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 8),
    _OscParentOtsInterface_Type()
)
oscParentOtsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscParentOtsInterface.setStatus("current")


class _OscMode_Type(Integer32):
    """Custom type oscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("t155m52", 1))
    )


_OscMode_Type.__name__ = "Integer32"
_OscMode_Object = MibTableColumn
oscMode = _OscMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 9),
    _OscMode_Type()
)
oscMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscMode.setStatus("current")
_OscWavelength_Type = OctetString
_OscWavelength_Object = MibTableColumn
oscWavelength = _OscWavelength_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 10),
    _OscWavelength_Type()
)
oscWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscWavelength.setStatus("current")
_OscDataCommunication_Type = CoriantTypesEnableSwitch
_OscDataCommunication_Object = MibTableColumn
oscDataCommunication = _OscDataCommunication_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 11),
    _OscDataCommunication_Type()
)
oscDataCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscDataCommunication.setStatus("current")
_OscRxOpticalPower_Type = CoriantTypesOpticalPower
_OscRxOpticalPower_Object = MibTableColumn
oscRxOpticalPower = _OscRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 12),
    _OscRxOpticalPower_Type()
)
oscRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscRxOpticalPower.setStatus("current")
_OscTxOpticalPower_Type = CoriantTypesOpticalPower
_OscTxOpticalPower_Object = MibTableColumn
oscTxOpticalPower = _OscTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 4, 1, 1, 13),
    _OscTxOpticalPower_Type()
)
oscTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscTxOpticalPower.setStatus("current")
_Gopt_ObjectIdentity = ObjectIdentity
gopt = _Gopt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5)
)
_GoptTable_Object = MibTable
goptTable = _GoptTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1)
)
if mibBuilder.loadTexts:
    goptTable.setStatus("current")
_GoptEntry_Object = MibTableRow
goptEntry = _GoptEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1)
)
goptEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "goptName"),
)
if mibBuilder.loadTexts:
    goptEntry.setStatus("current")
_GoptName_Type = CoriantTypesNameIdentifier
_GoptName_Object = MibTableColumn
goptName = _GoptName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 1),
    _GoptName_Type()
)
goptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptName.setStatus("current")


class _GoptAdminStatus_Type(Integer32):
    """Custom type goptAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_GoptAdminStatus_Type.__name__ = "Integer32"
_GoptAdminStatus_Object = MibTableColumn
goptAdminStatus = _GoptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 2),
    _GoptAdminStatus_Type()
)
goptAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptAdminStatus.setStatus("current")


class _GoptOperStatus_Type(Integer32):
    """Custom type goptOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_GoptOperStatus_Type.__name__ = "Integer32"
_GoptOperStatus_Object = MibTableColumn
goptOperStatus = _GoptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 3),
    _GoptOperStatus_Type()
)
goptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptOperStatus.setStatus("current")


class _GoptAvailStatus_Type(Bits):
    """Custom type goptAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_GoptAvailStatus_Type.__name__ = "Bits"
_GoptAvailStatus_Object = MibTableColumn
goptAvailStatus = _GoptAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 4),
    _GoptAvailStatus_Type()
)
goptAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptAvailStatus.setStatus("current")


class _GoptAliasName_Type(OctetString):
    """Custom type goptAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GoptAliasName_Type.__name__ = "OctetString"
_GoptAliasName_Object = MibTableColumn
goptAliasName = _GoptAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 5),
    _GoptAliasName_Type()
)
goptAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptAliasName.setStatus("current")
_GoptSupportingRxPort_Type = OpticalCommonSupportingPort
_GoptSupportingRxPort_Object = MibTableColumn
goptSupportingRxPort = _GoptSupportingRxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 6),
    _GoptSupportingRxPort_Type()
)
goptSupportingRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSupportingRxPort.setStatus("current")
_GoptSupportingTxPort_Type = OpticalCommonSupportingPort
_GoptSupportingTxPort_Object = MibTableColumn
goptSupportingTxPort = _GoptSupportingTxPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 7),
    _GoptSupportingTxPort_Type()
)
goptSupportingTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptSupportingTxPort.setStatus("current")
_GoptRxOpticalPower_Type = CoriantTypesOpticalPower
_GoptRxOpticalPower_Object = MibTableColumn
goptRxOpticalPower = _GoptRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 8),
    _GoptRxOpticalPower_Type()
)
goptRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptRxOpticalPower.setStatus("current")
_GoptTxOpticalPower_Type = CoriantTypesOpticalPower
_GoptTxOpticalPower_Object = MibTableColumn
goptTxOpticalPower = _GoptTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 5, 1, 1, 9),
    _GoptTxOpticalPower_Type()
)
goptTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptTxOpticalPower.setStatus("current")
_OmsStatistics_ObjectIdentity = ObjectIdentity
omsStatistics = _OmsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 9)
)
_OmsStatisticsTable_Object = MibTable
omsStatisticsTable = _OmsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 9, 1)
)
if mibBuilder.loadTexts:
    omsStatisticsTable.setStatus("current")
_OmsStatisticsEntry_Object = MibTableRow
omsStatisticsEntry = _OmsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 9, 1, 1)
)
omsStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "omsName"),
)
if mibBuilder.loadTexts:
    omsStatisticsEntry.setStatus("current")
_OmsStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_OmsStatisticsEntryLastClear_Object = MibTableColumn
omsStatisticsEntryLastClear = _OmsStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 9, 1, 1, 1),
    _OmsStatisticsEntryLastClear_Type()
)
omsStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsStatisticsEntryLastClear.setStatus("current")
_OscStatistics_ObjectIdentity = ObjectIdentity
oscStatistics = _OscStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 10)
)
_OscStatisticsTable_Object = MibTable
oscStatisticsTable = _OscStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 10, 1)
)
if mibBuilder.loadTexts:
    oscStatisticsTable.setStatus("current")
_OscStatisticsEntry_Object = MibTableRow
oscStatisticsEntry = _OscStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 10, 1, 1)
)
oscStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "oscName"),
)
if mibBuilder.loadTexts:
    oscStatisticsEntry.setStatus("current")
_OscStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_OscStatisticsEntryLastClear_Object = MibTableColumn
oscStatisticsEntryLastClear = _OscStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 10, 1, 1, 1),
    _OscStatisticsEntryLastClear_Type()
)
oscStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscStatisticsEntryLastClear.setStatus("current")
_GoptStatistics_ObjectIdentity = ObjectIdentity
goptStatistics = _GoptStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11)
)
_GoptStatisticsTable_Object = MibTable
goptStatisticsTable = _GoptStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11, 1)
)
if mibBuilder.loadTexts:
    goptStatisticsTable.setStatus("current")
_GoptStatisticsEntry_Object = MibTableRow
goptStatisticsEntry = _GoptStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11, 1, 1)
)
goptStatisticsEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "goptName"),
)
if mibBuilder.loadTexts:
    goptStatisticsEntry.setStatus("current")
_GoptStatisticsEntryProtectionSwitchDuration_Type = OctetString
_GoptStatisticsEntryProtectionSwitchDuration_Object = MibTableColumn
goptStatisticsEntryProtectionSwitchDuration = _GoptStatisticsEntryProtectionSwitchDuration_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11, 1, 1, 1),
    _GoptStatisticsEntryProtectionSwitchDuration_Type()
)
goptStatisticsEntryProtectionSwitchDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptStatisticsEntryProtectionSwitchDuration.setStatus("current")
_GoptStatisticsEntryProtectionSwitchCount_Type = OctetString
_GoptStatisticsEntryProtectionSwitchCount_Object = MibTableColumn
goptStatisticsEntryProtectionSwitchCount = _GoptStatisticsEntryProtectionSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11, 1, 1, 2),
    _GoptStatisticsEntryProtectionSwitchCount_Type()
)
goptStatisticsEntryProtectionSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptStatisticsEntryProtectionSwitchCount.setStatus("current")
_GoptStatisticsEntryLossTx_Type = OctetString
_GoptStatisticsEntryLossTx_Object = MibTableColumn
goptStatisticsEntryLossTx = _GoptStatisticsEntryLossTx_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11, 1, 1, 3),
    _GoptStatisticsEntryLossTx_Type()
)
goptStatisticsEntryLossTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptStatisticsEntryLossTx.setStatus("current")
_GoptStatisticsEntryLossRx_Type = OctetString
_GoptStatisticsEntryLossRx_Object = MibTableColumn
goptStatisticsEntryLossRx = _GoptStatisticsEntryLossRx_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11, 1, 1, 4),
    _GoptStatisticsEntryLossRx_Type()
)
goptStatisticsEntryLossRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptStatisticsEntryLossRx.setStatus("current")
_GoptStatisticsEntryLastClear_Type = IetfYangTypesDateAndTime
_GoptStatisticsEntryLastClear_Object = MibTableColumn
goptStatisticsEntryLastClear = _GoptStatisticsEntryLastClear_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 5, 11, 1, 1, 5),
    _GoptStatisticsEntryLastClear_Type()
)
goptStatisticsEntryLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    goptStatisticsEntryLastClear.setStatus("current")
_Lldp_ObjectIdentity = ObjectIdentity
lldp = _Lldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 6)
)
_LldpStatusNe_Type = CoriantTypesEnableSwitch
_LldpStatusNe_Object = MibScalar
lldpStatusNe = _LldpStatusNe_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 4, 6, 1),
    _LldpStatusNe_Type()
)
lldpStatusNe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatusNe.setStatus("current")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5)
)
_PerformanceInfo_ObjectIdentity = ObjectIdentity
performanceInfo = _PerformanceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 1)
)


class _PerformancePmdaystart_Type(Unsigned32):
    """Custom type performancePmdaystart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_PerformancePmdaystart_Type.__name__ = "Unsigned32"
_PerformancePmdaystart_Object = MibScalar
performancePmdaystart = _PerformancePmdaystart_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 1, 1),
    _PerformancePmdaystart_Type()
)
performancePmdaystart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performancePmdaystart.setStatus("current")
_PerformanceStatisticsEnable_Type = CoriantTypesEnableSwitch
_PerformanceStatisticsEnable_Object = MibScalar
performanceStatisticsEnable = _PerformanceStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 1, 2),
    _PerformanceStatisticsEnable_Type()
)
performanceStatisticsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceStatisticsEnable.setStatus("current")
_PmPoint_ObjectIdentity = ObjectIdentity
pmPoint = _PmPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2)
)
_PmPointTable_Object = MibTable
pmPointTable = _PmPointTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    pmPointTable.setStatus("current")
_PmPointEntry_Object = MibTableRow
pmPointEntry = _PmPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1, 1)
)
pmPointEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "pmPointPmEntity"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmpType"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmTimePeriod"),
)
if mibBuilder.loadTexts:
    pmPointEntry.setStatus("current")
_PmPointPmEntity_Type = RowPointer
_PmPointPmEntity_Object = MibTableColumn
pmPointPmEntity = _PmPointPmEntity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1, 1, 1),
    _PmPointPmEntity_Type()
)
pmPointPmEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPointPmEntity.setStatus("current")
_PmPointPmpType_Type = CoriantPmtypesPmpType
_PmPointPmpType_Object = MibTableColumn
pmPointPmpType = _PmPointPmpType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1, 1, 2),
    _PmPointPmpType_Type()
)
pmPointPmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPointPmpType.setStatus("current")
_PmPointPmTimePeriod_Type = CoriantTypesManagementTimePeriod
_PmPointPmTimePeriod_Object = MibTableColumn
pmPointPmTimePeriod = _PmPointPmTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1, 1, 3),
    _PmPointPmTimePeriod_Type()
)
pmPointPmTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPointPmTimePeriod.setStatus("current")
_PmPointSupervisionSwitch_Type = CoriantTypesEnableSwitch
_PmPointSupervisionSwitch_Object = MibTableColumn
pmPointSupervisionSwitch = _PmPointSupervisionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1, 1, 4),
    _PmPointSupervisionSwitch_Type()
)
pmPointSupervisionSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPointSupervisionSwitch.setStatus("current")
_PmPointThresholdingSwitch_Type = CoriantTypesEnableSwitch
_PmPointThresholdingSwitch_Object = MibTableColumn
pmPointThresholdingSwitch = _PmPointThresholdingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1, 1, 5),
    _PmPointThresholdingSwitch_Type()
)
pmPointThresholdingSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPointThresholdingSwitch.setStatus("current")
_PmPointHistoryRecording_Type = CoriantTypesEnableSwitch
_PmPointHistoryRecording_Object = MibTableColumn
pmPointHistoryRecording = _PmPointHistoryRecording_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 2, 1, 1, 6),
    _PmPointHistoryRecording_Type()
)
pmPointHistoryRecording.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPointHistoryRecording.setStatus("current")
_PmData_ObjectIdentity = ObjectIdentity
pmData = _PmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3)
)
_PmDataCurrentTable_Object = MibTable
pmDataCurrentTable = _PmDataCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    pmDataCurrentTable.setStatus("current")
_PmDataCurrentEntry_Object = MibTableRow
pmDataCurrentEntry = _PmDataCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 2, 1)
)
pmDataCurrentEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "pmPointPmEntity"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmpType"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmTimePeriod"),
    (0, "CORIANT-GROOVE-MIB", "pmDataCurrentPmParameter"),
)
if mibBuilder.loadTexts:
    pmDataCurrentEntry.setStatus("current")
_PmDataCurrentMonitoringDateTime_Type = OctetString
_PmDataCurrentMonitoringDateTime_Object = MibTableColumn
pmDataCurrentMonitoringDateTime = _PmDataCurrentMonitoringDateTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 2, 1, 1),
    _PmDataCurrentMonitoringDateTime_Type()
)
pmDataCurrentMonitoringDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataCurrentMonitoringDateTime.setStatus("current")
_PmDataCurrentPmParameter_Type = CoriantPmtypesPmParameter
_PmDataCurrentPmParameter_Object = MibTableColumn
pmDataCurrentPmParameter = _PmDataCurrentPmParameter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 2, 1, 2),
    _PmDataCurrentPmParameter_Type()
)
pmDataCurrentPmParameter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDataCurrentPmParameter.setStatus("current")


class _PmDataCurrentPmValue_Type(OctetString):
    """Custom type pmDataCurrentPmValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PmDataCurrentPmValue_Type.__name__ = "OctetString"
_PmDataCurrentPmValue_Object = MibTableColumn
pmDataCurrentPmValue = _PmDataCurrentPmValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 2, 1, 3),
    _PmDataCurrentPmValue_Type()
)
pmDataCurrentPmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataCurrentPmValue.setStatus("current")
_PmDataCurrentPmUnit_Type = CoriantCommonpmUnitOfValue
_PmDataCurrentPmUnit_Object = MibTableColumn
pmDataCurrentPmUnit = _PmDataCurrentPmUnit_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 2, 1, 4),
    _PmDataCurrentPmUnit_Type()
)
pmDataCurrentPmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataCurrentPmUnit.setStatus("current")
_PmDataCurrentValidity_Type = CoriantPmtypesValidityType
_PmDataCurrentValidity_Object = MibTableColumn
pmDataCurrentValidity = _PmDataCurrentValidity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 2, 1, 5),
    _PmDataCurrentValidity_Type()
)
pmDataCurrentValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataCurrentValidity.setStatus("current")
_PmDataLatestHistoryTable_Object = MibTable
pmDataLatestHistoryTable = _PmDataLatestHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 3)
)
if mibBuilder.loadTexts:
    pmDataLatestHistoryTable.setStatus("current")
_PmDataLatestHistoryEntry_Object = MibTableRow
pmDataLatestHistoryEntry = _PmDataLatestHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 3, 1)
)
pmDataLatestHistoryEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "pmPointPmEntity"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmpType"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmTimePeriod"),
    (0, "CORIANT-GROOVE-MIB", "pmDataLatestHistoryPmParameter"),
)
if mibBuilder.loadTexts:
    pmDataLatestHistoryEntry.setStatus("current")
_PmDataLatestHistoryMonitoringDateTime_Type = OctetString
_PmDataLatestHistoryMonitoringDateTime_Object = MibTableColumn
pmDataLatestHistoryMonitoringDateTime = _PmDataLatestHistoryMonitoringDateTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 3, 1, 1),
    _PmDataLatestHistoryMonitoringDateTime_Type()
)
pmDataLatestHistoryMonitoringDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataLatestHistoryMonitoringDateTime.setStatus("current")
_PmDataLatestHistoryPmParameter_Type = CoriantPmtypesPmParameter
_PmDataLatestHistoryPmParameter_Object = MibTableColumn
pmDataLatestHistoryPmParameter = _PmDataLatestHistoryPmParameter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 3, 1, 2),
    _PmDataLatestHistoryPmParameter_Type()
)
pmDataLatestHistoryPmParameter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDataLatestHistoryPmParameter.setStatus("current")


class _PmDataLatestHistoryPmValue_Type(OctetString):
    """Custom type pmDataLatestHistoryPmValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PmDataLatestHistoryPmValue_Type.__name__ = "OctetString"
_PmDataLatestHistoryPmValue_Object = MibTableColumn
pmDataLatestHistoryPmValue = _PmDataLatestHistoryPmValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 3, 1, 3),
    _PmDataLatestHistoryPmValue_Type()
)
pmDataLatestHistoryPmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataLatestHistoryPmValue.setStatus("current")
_PmDataLatestHistoryPmUnit_Type = CoriantCommonpmUnitOfValue
_PmDataLatestHistoryPmUnit_Object = MibTableColumn
pmDataLatestHistoryPmUnit = _PmDataLatestHistoryPmUnit_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 3, 1, 4),
    _PmDataLatestHistoryPmUnit_Type()
)
pmDataLatestHistoryPmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataLatestHistoryPmUnit.setStatus("current")
_PmDataLatestHistoryValidity_Type = CoriantPmtypesValidityType
_PmDataLatestHistoryValidity_Object = MibTableColumn
pmDataLatestHistoryValidity = _PmDataLatestHistoryValidity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 3, 1, 5),
    _PmDataLatestHistoryValidity_Type()
)
pmDataLatestHistoryValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataLatestHistoryValidity.setStatus("current")
_PmDataHistoryTable_Object = MibTable
pmDataHistoryTable = _PmDataHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4)
)
if mibBuilder.loadTexts:
    pmDataHistoryTable.setStatus("current")
_PmDataHistoryEntry_Object = MibTableRow
pmDataHistoryEntry = _PmDataHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4, 1)
)
pmDataHistoryEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "pmPointPmEntity"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmpType"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmTimePeriod"),
    (0, "CORIANT-GROOVE-MIB", "pmDataHistoryRecordIndex"),
    (0, "CORIANT-GROOVE-MIB", "pmDataHistoryPmParameter"),
)
if mibBuilder.loadTexts:
    pmDataHistoryEntry.setStatus("current")
_PmDataHistoryRecordIndex_Type = Unsigned32
_PmDataHistoryRecordIndex_Object = MibTableColumn
pmDataHistoryRecordIndex = _PmDataHistoryRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4, 1, 1),
    _PmDataHistoryRecordIndex_Type()
)
pmDataHistoryRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDataHistoryRecordIndex.setStatus("current")
_PmDataHistoryMonitoringDateTime_Type = OctetString
_PmDataHistoryMonitoringDateTime_Object = MibTableColumn
pmDataHistoryMonitoringDateTime = _PmDataHistoryMonitoringDateTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4, 1, 2),
    _PmDataHistoryMonitoringDateTime_Type()
)
pmDataHistoryMonitoringDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataHistoryMonitoringDateTime.setStatus("current")
_PmDataHistoryPmParameter_Type = CoriantPmtypesPmParameter
_PmDataHistoryPmParameter_Object = MibTableColumn
pmDataHistoryPmParameter = _PmDataHistoryPmParameter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4, 1, 3),
    _PmDataHistoryPmParameter_Type()
)
pmDataHistoryPmParameter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDataHistoryPmParameter.setStatus("current")


class _PmDataHistoryPmValue_Type(OctetString):
    """Custom type pmDataHistoryPmValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PmDataHistoryPmValue_Type.__name__ = "OctetString"
_PmDataHistoryPmValue_Object = MibTableColumn
pmDataHistoryPmValue = _PmDataHistoryPmValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4, 1, 4),
    _PmDataHistoryPmValue_Type()
)
pmDataHistoryPmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataHistoryPmValue.setStatus("current")
_PmDataHistoryPmUnit_Type = CoriantCommonpmUnitOfValue
_PmDataHistoryPmUnit_Object = MibTableColumn
pmDataHistoryPmUnit = _PmDataHistoryPmUnit_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4, 1, 5),
    _PmDataHistoryPmUnit_Type()
)
pmDataHistoryPmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataHistoryPmUnit.setStatus("current")
_PmDataHistoryValidity_Type = CoriantPmtypesValidityType
_PmDataHistoryValidity_Object = MibTableColumn
pmDataHistoryValidity = _PmDataHistoryValidity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 3, 4, 1, 6),
    _PmDataHistoryValidity_Type()
)
pmDataHistoryValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDataHistoryValidity.setStatus("current")
_PmThresholdsValue_ObjectIdentity = ObjectIdentity
pmThresholdsValue = _PmThresholdsValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 4)
)
_PmThresholdsValueTable_Object = MibTable
pmThresholdsValueTable = _PmThresholdsValueTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    pmThresholdsValueTable.setStatus("current")
_PmThresholdsValueEntry_Object = MibTableRow
pmThresholdsValueEntry = _PmThresholdsValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 4, 1, 1)
)
pmThresholdsValueEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "pmPointPmEntity"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmpType"),
    (0, "CORIANT-GROOVE-MIB", "pmPointPmTimePeriod"),
    (0, "CORIANT-GROOVE-MIB", "pmThresholdsValuePmParameter"),
)
if mibBuilder.loadTexts:
    pmThresholdsValueEntry.setStatus("current")
_PmThresholdsValuePmParameter_Type = CoriantPmtypesPmParameter
_PmThresholdsValuePmParameter_Object = MibTableColumn
pmThresholdsValuePmParameter = _PmThresholdsValuePmParameter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 4, 1, 1, 1),
    _PmThresholdsValuePmParameter_Type()
)
pmThresholdsValuePmParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmThresholdsValuePmParameter.setStatus("current")
_PmThresholdsValuePmHighThreshold_Type = CoriantCommonpmThresholdValue
_PmThresholdsValuePmHighThreshold_Object = MibTableColumn
pmThresholdsValuePmHighThreshold = _PmThresholdsValuePmHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 4, 1, 1, 2),
    _PmThresholdsValuePmHighThreshold_Type()
)
pmThresholdsValuePmHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmThresholdsValuePmHighThreshold.setStatus("current")
_PmThresholdsValuePmLowThreshold_Type = CoriantCommonpmThresholdValue
_PmThresholdsValuePmLowThreshold_Object = MibTableColumn
pmThresholdsValuePmLowThreshold = _PmThresholdsValuePmLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 4, 1, 1, 3),
    _PmThresholdsValuePmLowThreshold_Type()
)
pmThresholdsValuePmLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmThresholdsValuePmLowThreshold.setStatus("current")
_PmThresholdsValuePmUnit_Type = CoriantCommonpmUnitOfValue
_PmThresholdsValuePmUnit_Object = MibTableColumn
pmThresholdsValuePmUnit = _PmThresholdsValuePmUnit_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 5, 4, 1, 1, 4),
    _PmThresholdsValuePmUnit_Type()
)
pmThresholdsValuePmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmThresholdsValuePmUnit.setStatus("current")
_Networking_ObjectIdentity = ObjectIdentity
networking = _Networking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6)
)
_NetworkingInfo_ObjectIdentity = ObjectIdentity
networkingInfo = _NetworkingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 1)
)


class _NetworkingSourceAddressSelectMode_Type(Integer32):
    """Custom type networkingSourceAddressSelectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopbackPrefer", 1),
          ("linkPrefer", 2))
    )


_NetworkingSourceAddressSelectMode_Type.__name__ = "Integer32"
_NetworkingSourceAddressSelectMode_Object = MibScalar
networkingSourceAddressSelectMode = _NetworkingSourceAddressSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 1, 1),
    _NetworkingSourceAddressSelectMode_Type()
)
networkingSourceAddressSelectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkingSourceAddressSelectMode.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2)
)
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("current")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1)
)
interfaceEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "interfaceIfName"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("current")


class _InterfaceIfName_Type(OctetString):
    """Custom type interfaceIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_InterfaceIfName_Type.__name__ = "OctetString"
_InterfaceIfName_Object = MibTableColumn
interfaceIfName = _InterfaceIfName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1, 1),
    _InterfaceIfName_Type()
)
interfaceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfName.setStatus("current")


class _InterfaceIfDescription_Type(OctetString):
    """Custom type interfaceIfDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceIfDescription_Type.__name__ = "OctetString"
_InterfaceIfDescription_Object = MibTableColumn
interfaceIfDescription = _InterfaceIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1, 2),
    _InterfaceIfDescription_Type()
)
interfaceIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfDescription.setStatus("current")


class _InterfaceIfType_Type(Integer32):
    """Custom type interfaceIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ethernetcsmacd", 1),
          ("ppp", 2),
          ("softwareloopback", 3),
          ("lapd", 4),
          ("oscx", 5))
    )


_InterfaceIfType_Type.__name__ = "Integer32"
_InterfaceIfType_Object = MibTableColumn
interfaceIfType = _InterfaceIfType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1, 3),
    _InterfaceIfType_Type()
)
interfaceIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfType.setStatus("current")


class _InterfaceAdminStatus_Type(Integer32):
    """Custom type interfaceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_InterfaceAdminStatus_Type.__name__ = "Integer32"
_InterfaceAdminStatus_Object = MibTableColumn
interfaceAdminStatus = _InterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1, 4),
    _InterfaceAdminStatus_Type()
)
interfaceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAdminStatus.setStatus("current")


class _InterfaceOperStatus_Type(Integer32):
    """Custom type interfaceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_InterfaceOperStatus_Type.__name__ = "Integer32"
_InterfaceOperStatus_Object = MibTableColumn
interfaceOperStatus = _InterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1, 5),
    _InterfaceOperStatus_Type()
)
interfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceOperStatus.setStatus("current")


class _InterfaceAvailStatus_Type(Bits):
    """Custom type interfaceAvailStatus based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("failed", 1),
          ("mismatch", 2),
          ("lowerLayerDown", 3),
          ("notPresent", 4),
          ("shutdown", 5),
          ("degraded", 6),
          ("idle", 7),
          ("busy", 8),
          ("hibernation", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("softwareUpgrade", 12),
          ("initializing", 13),
          ("unknown", 14),
          ("incomplete", 15),
          ("laserSafetyShutoff", 16),
          ("measuring", 17),
          ("firmwareLoading", 18),
          ("connected", 19))
    )

_InterfaceAvailStatus_Type.__name__ = "Bits"
_InterfaceAvailStatus_Object = MibTableColumn
interfaceAvailStatus = _InterfaceAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1, 6),
    _InterfaceAvailStatus_Type()
)
interfaceAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAvailStatus.setStatus("current")


class _InterfaceAliasName_Type(OctetString):
    """Custom type interfaceAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_InterfaceAliasName_Type.__name__ = "OctetString"
_InterfaceAliasName_Object = MibTableColumn
interfaceAliasName = _InterfaceAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 2, 1, 1, 7),
    _InterfaceAliasName_Type()
)
interfaceAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAliasName.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3)
)
_EthernetTable_Object = MibTable
ethernetTable = _EthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    ethernetTable.setStatus("current")
_EthernetEntry_Object = MibTableRow
ethernetEntry = _EthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1)
)
ethernetEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "interfaceIfName"),
)
if mibBuilder.loadTexts:
    ethernetEntry.setStatus("current")
_EthernetAutoNegotiation_Type = CoriantTypesEnableSwitch
_EthernetAutoNegotiation_Object = MibTableColumn
ethernetAutoNegotiation = _EthernetAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 1),
    _EthernetAutoNegotiation_Type()
)
ethernetAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetAutoNegotiation.setStatus("current")
_EthernetDuplexMode_Type = CoriantTypesDuplexMode
_EthernetDuplexMode_Object = MibTableColumn
ethernetDuplexMode = _EthernetDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 2),
    _EthernetDuplexMode_Type()
)
ethernetDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetDuplexMode.setStatus("current")
_EthernetOperationalDuplexMode_Type = CoriantTypesDuplexMode
_EthernetOperationalDuplexMode_Object = MibTableColumn
ethernetOperationalDuplexMode = _EthernetOperationalDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 3),
    _EthernetOperationalDuplexMode_Type()
)
ethernetOperationalDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOperationalDuplexMode.setStatus("current")
_EthernetRate_Type = CoriantTypesEthernetRate
_EthernetRate_Object = MibTableColumn
ethernetRate = _EthernetRate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 4),
    _EthernetRate_Type()
)
ethernetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetRate.setStatus("current")
_EthernetOperationalEthernetRate_Type = CoriantTypesEthernetRate
_EthernetOperationalEthernetRate_Object = MibTableColumn
ethernetOperationalEthernetRate = _EthernetOperationalEthernetRate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 5),
    _EthernetOperationalEthernetRate_Type()
)
ethernetOperationalEthernetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOperationalEthernetRate.setStatus("current")
_EthernetFlowControl_Type = CoriantTypesFlowControl
_EthernetFlowControl_Object = MibTableColumn
ethernetFlowControl = _EthernetFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 6),
    _EthernetFlowControl_Type()
)
ethernetFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFlowControl.setStatus("current")
_EthernetOperationalFlowControl_Type = CoriantTypesFlowControl
_EthernetOperationalFlowControl_Object = MibTableColumn
ethernetOperationalFlowControl = _EthernetOperationalFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 7),
    _EthernetOperationalFlowControl_Type()
)
ethernetOperationalFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOperationalFlowControl.setStatus("current")
_EthernetMacAddress_Type = IetfYangTypesMacAddress
_EthernetMacAddress_Object = MibTableColumn
ethernetMacAddress = _EthernetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 8),
    _EthernetMacAddress_Type()
)
ethernetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMacAddress.setStatus("current")


class _EthernetAliasName_Type(OctetString):
    """Custom type ethernetAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EthernetAliasName_Type.__name__ = "OctetString"
_EthernetAliasName_Object = MibTableColumn
ethernetAliasName = _EthernetAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 3, 1, 1, 9),
    _EthernetAliasName_Type()
)
ethernetAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetAliasName.setStatus("current")
_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 4)
)
_PppTable_Object = MibTable
pppTable = _PppTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 4, 1)
)
if mibBuilder.loadTexts:
    pppTable.setStatus("current")
_PppEntry_Object = MibTableRow
pppEntry = _PppEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 4, 1, 1)
)
pppEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "interfaceIfName"),
)
if mibBuilder.loadTexts:
    pppEntry.setStatus("current")


class _PppType_Type(Integer32):
    """Custom type pppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gcc0", 1)
    )


_PppType_Type.__name__ = "Integer32"
_PppType_Object = MibTableColumn
pppType = _PppType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 4, 1, 1, 1),
    _PppType_Type()
)
pppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppType.setStatus("current")
_PppPfRef_Type = RowPointer
_PppPfRef_Object = MibTableColumn
pppPfRef = _PppPfRef_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 4, 1, 1, 2),
    _PppPfRef_Type()
)
pppPfRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPfRef.setStatus("current")
_PppResourceRef_Type = RowPointer
_PppResourceRef_Object = MibTableColumn
pppResourceRef = _PppResourceRef_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 4, 1, 1, 3),
    _PppResourceRef_Type()
)
pppResourceRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppResourceRef.setStatus("current")


class _PppAliasName_Type(OctetString):
    """Custom type pppAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PppAliasName_Type.__name__ = "OctetString"
_PppAliasName_Object = MibTableColumn
pppAliasName = _PppAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 4, 1, 1, 4),
    _PppAliasName_Type()
)
pppAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppAliasName.setStatus("current")
_Ipv4_ObjectIdentity = ObjectIdentity
ipv4 = _Ipv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 5)
)
_Ipv4Table_Object = MibTable
ipv4Table = _Ipv4Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    ipv4Table.setStatus("current")
_Ipv4Entry_Object = MibTableRow
ipv4Entry = _Ipv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 5, 1, 1)
)
ipv4Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "interfaceIfName"),
)
if mibBuilder.loadTexts:
    ipv4Entry.setStatus("current")
_Ipv4Forwarding_Type = TruthValue
_Ipv4Forwarding_Object = MibTableColumn
ipv4Forwarding = _Ipv4Forwarding_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 5, 1, 1, 1),
    _Ipv4Forwarding_Type()
)
ipv4Forwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4Forwarding.setStatus("current")


class _Ipv4Mtu_Type(Unsigned32):
    """Custom type ipv4Mtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 65535),
    )


_Ipv4Mtu_Type.__name__ = "Unsigned32"
_Ipv4Mtu_Object = MibTableColumn
ipv4Mtu = _Ipv4Mtu_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 5, 1, 1, 2),
    _Ipv4Mtu_Type()
)
ipv4Mtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4Mtu.setStatus("current")


class _Ipv4AddressAssignmentMethod_Type(Integer32):
    """Custom type ipv4AddressAssignmentMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_Ipv4AddressAssignmentMethod_Type.__name__ = "Integer32"
_Ipv4AddressAssignmentMethod_Object = MibTableColumn
ipv4AddressAssignmentMethod = _Ipv4AddressAssignmentMethod_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 5, 1, 1, 3),
    _Ipv4AddressAssignmentMethod_Type()
)
ipv4AddressAssignmentMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4AddressAssignmentMethod.setStatus("current")
_IpAddress_ObjectIdentity = ObjectIdentity
ipAddress = _IpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 6)
)
_IpAddressTable_Object = MibTable
ipAddressTable = _IpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 6, 1)
)
if mibBuilder.loadTexts:
    ipAddressTable.setStatus("current")
_IpAddressEntry_Object = MibTableRow
ipAddressEntry = _IpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 6, 1, 1)
)
ipAddressEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "interfaceIfName"),
)
if mibBuilder.loadTexts:
    ipAddressEntry.setStatus("current")
_IpAddressIp_Type = IetfInetTypesIpv4Address
_IpAddressIp_Object = MibTableColumn
ipAddressIp = _IpAddressIp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 6, 1, 1, 1),
    _IpAddressIp_Type()
)
ipAddressIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressIp.setStatus("current")


class _IpAddressOrigin_Type(Integer32):
    """Custom type ipAddressOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("static", 2),
          ("dhcp", 3),
          ("linkLayer", 4),
          ("random", 5))
    )


_IpAddressOrigin_Type.__name__ = "Integer32"
_IpAddressOrigin_Object = MibTableColumn
ipAddressOrigin = _IpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 6, 1, 1, 2),
    _IpAddressOrigin_Type()
)
ipAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressOrigin.setStatus("current")


class _IpAddressPrefixLength_Type(Unsigned32):
    """Custom type ipAddressPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_IpAddressPrefixLength_Type.__name__ = "Unsigned32"
_IpAddressPrefixLength_Object = MibTableColumn
ipAddressPrefixLength = _IpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 6, 1, 1, 3),
    _IpAddressPrefixLength_Type()
)
ipAddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPrefixLength.setStatus("current")
_IpUnnumbered_ObjectIdentity = ObjectIdentity
ipUnnumbered = _IpUnnumbered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 7)
)
_IpUnnumberedTable_Object = MibTable
ipUnnumberedTable = _IpUnnumberedTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 7, 1)
)
if mibBuilder.loadTexts:
    ipUnnumberedTable.setStatus("current")
_IpUnnumberedEntry_Object = MibTableRow
ipUnnumberedEntry = _IpUnnumberedEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 7, 1, 1)
)
ipUnnumberedEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "interfaceIfName"),
)
if mibBuilder.loadTexts:
    ipUnnumberedEntry.setStatus("current")
_IpUnnumberedUnnumEnabled_Type = TruthValue
_IpUnnumberedUnnumEnabled_Object = MibTableColumn
ipUnnumberedUnnumEnabled = _IpUnnumberedUnnumEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 7, 1, 1, 1),
    _IpUnnumberedUnnumEnabled_Type()
)
ipUnnumberedUnnumEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipUnnumberedUnnumEnabled.setStatus("current")
_IpUnnumberedParentInterface_Type = RowPointer
_IpUnnumberedParentInterface_Object = MibTableColumn
ipUnnumberedParentInterface = _IpUnnumberedParentInterface_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 7, 1, 1, 2),
    _IpUnnumberedParentInterface_Type()
)
ipUnnumberedParentInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipUnnumberedParentInterface.setStatus("current")
_RoutingProtocol_ObjectIdentity = ObjectIdentity
routingProtocol = _RoutingProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 9)
)
_RoutingProtocolTable_Object = MibTable
routingProtocolTable = _RoutingProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 9, 1)
)
if mibBuilder.loadTexts:
    routingProtocolTable.setStatus("current")
_RoutingProtocolEntry_Object = MibTableRow
routingProtocolEntry = _RoutingProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 9, 1, 1)
)
routingProtocolEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpType"),
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpName"),
)
if mibBuilder.loadTexts:
    routingProtocolEntry.setStatus("current")
_RoutingProtocolRtpType_Type = CoriantTypesRtpType
_RoutingProtocolRtpType_Object = MibTableColumn
routingProtocolRtpType = _RoutingProtocolRtpType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 9, 1, 1, 1),
    _RoutingProtocolRtpType_Type()
)
routingProtocolRtpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingProtocolRtpType.setStatus("current")


class _RoutingProtocolRtpName_Type(OctetString):
    """Custom type routingProtocolRtpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RoutingProtocolRtpName_Type.__name__ = "OctetString"
_RoutingProtocolRtpName_Object = MibTableColumn
routingProtocolRtpName = _RoutingProtocolRtpName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 9, 1, 1, 2),
    _RoutingProtocolRtpName_Type()
)
routingProtocolRtpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingProtocolRtpName.setStatus("current")
_RoutingProtocolDescription_Type = OctetString
_RoutingProtocolDescription_Object = MibTableColumn
routingProtocolDescription = _RoutingProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 9, 1, 1, 3),
    _RoutingProtocolDescription_Type()
)
routingProtocolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingProtocolDescription.setStatus("current")
_StaticRoute_ObjectIdentity = ObjectIdentity
staticRoute = _StaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 10)
)
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 10, 1)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 10, 1, 1)
)
staticRouteEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpType"),
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpName"),
    (0, "CORIANT-GROOVE-MIB", "staticRouteDestinationPrefix"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")


class _StaticRouteDestinationPrefix_Type(IetfInetTypesIpv4Prefix):
    """Custom type staticRouteDestinationPrefix based on IetfInetTypesIpv4Prefix"""
    subtypeSpec = IetfInetTypesIpv4Prefix.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_StaticRouteDestinationPrefix_Type.__name__ = "IetfInetTypesIpv4Prefix"
_StaticRouteDestinationPrefix_Object = MibTableColumn
staticRouteDestinationPrefix = _StaticRouteDestinationPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 10, 1, 1, 1),
    _StaticRouteDestinationPrefix_Type()
)
staticRouteDestinationPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteDestinationPrefix.setStatus("current")
_StaticRouteDescription_Type = OctetString
_StaticRouteDescription_Object = MibTableColumn
staticRouteDescription = _StaticRouteDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 10, 1, 1, 2),
    _StaticRouteDescription_Type()
)
staticRouteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteDescription.setStatus("current")
_StaticRouteAdvertised_Type = TruthValue
_StaticRouteAdvertised_Object = MibTableColumn
staticRouteAdvertised = _StaticRouteAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 10, 1, 1, 3),
    _StaticRouteAdvertised_Type()
)
staticRouteAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteAdvertised.setStatus("current")
_NextHop_ObjectIdentity = ObjectIdentity
nextHop = _NextHop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 11)
)
_NextHopTable_Object = MibTable
nextHopTable = _NextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 11, 1)
)
if mibBuilder.loadTexts:
    nextHopTable.setStatus("current")
_NextHopEntry_Object = MibTableRow
nextHopEntry = _NextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 11, 1, 1)
)
nextHopEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpType"),
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpName"),
    (0, "CORIANT-GROOVE-MIB", "staticRouteDestinationPrefix"),
    (0, "CORIANT-GROOVE-MIB", "nextHopIndex"),
    (0, "CORIANT-GROOVE-MIB", "ribName"),
    (0, "CORIANT-GROOVE-MIB", "routeSourceProtocol"),
    (0, "CORIANT-GROOVE-MIB", "routeDestinationPrefix"),
)
if mibBuilder.loadTexts:
    nextHopEntry.setStatus("current")


class _NextHopIndex_Type(OctetString):
    """Custom type nextHopIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NextHopIndex_Type.__name__ = "OctetString"
_NextHopIndex_Object = MibTableColumn
nextHopIndex = _NextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 11, 1, 1, 1),
    _NextHopIndex_Type()
)
nextHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopIndex.setStatus("current")
_NextHopOutgoingInterface_Type = RowPointer
_NextHopOutgoingInterface_Object = MibTableColumn
nextHopOutgoingInterface = _NextHopOutgoingInterface_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 11, 1, 1, 2),
    _NextHopOutgoingInterface_Type()
)
nextHopOutgoingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopOutgoingInterface.setStatus("current")
_NextHopAddress_Type = IetfInetTypesIpv4Address
_NextHopAddress_Object = MibTableColumn
nextHopAddress = _NextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 11, 1, 1, 3),
    _NextHopAddress_Type()
)
nextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopAddress.setStatus("current")
_NextHopMetric_Type = Unsigned32
_NextHopMetric_Object = MibTableColumn
nextHopMetric = _NextHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 11, 1, 1, 4),
    _NextHopMetric_Type()
)
nextHopMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopMetric.setStatus("current")
_Ospf_ObjectIdentity = ObjectIdentity
ospf = _Ospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12)
)
_OspfTable_Object = MibTable
ospfTable = _OspfTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1)
)
if mibBuilder.loadTexts:
    ospfTable.setStatus("current")
_OspfEntry_Object = MibTableRow
ospfEntry = _OspfEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1, 1)
)
ospfEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpType"),
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpName"),
)
if mibBuilder.loadTexts:
    ospfEntry.setStatus("current")
_OspfRouterId_Type = IetfYangTypesDottedQuad
_OspfRouterId_Object = MibTableColumn
ospfRouterId = _OspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1, 1, 1),
    _OspfRouterId_Type()
)
ospfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRouterId.setStatus("current")
_OspfDescription_Type = OctetString
_OspfDescription_Object = MibTableColumn
ospfDescription = _OspfDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1, 1, 2),
    _OspfDescription_Type()
)
ospfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDescription.setStatus("current")
_OspfAsbr_Type = TruthValue
_OspfAsbr_Object = MibTableColumn
ospfAsbr = _OspfAsbr_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1, 1, 3),
    _OspfAsbr_Type()
)
ospfAsbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsbr.setStatus("current")


class _OspfAdminStatus_Type(Integer32):
    """Custom type ospfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OspfAdminStatus_Type.__name__ = "Integer32"
_OspfAdminStatus_Object = MibTableColumn
ospfAdminStatus = _OspfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1, 1, 4),
    _OspfAdminStatus_Type()
)
ospfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAdminStatus.setStatus("current")


class _OspfOperStatus_Type(Integer32):
    """Custom type ospfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OspfOperStatus_Type.__name__ = "Integer32"
_OspfOperStatus_Object = MibTableColumn
ospfOperStatus = _OspfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1, 1, 5),
    _OspfOperStatus_Type()
)
ospfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfOperStatus.setStatus("current")


class _OspfAliasName_Type(OctetString):
    """Custom type ospfAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfAliasName_Type.__name__ = "OctetString"
_OspfAliasName_Object = MibTableColumn
ospfAliasName = _OspfAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 12, 1, 1, 6),
    _OspfAliasName_Type()
)
ospfAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAliasName.setStatus("current")
_OspfArea_ObjectIdentity = ObjectIdentity
ospfArea = _OspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13)
)
_OspfAreaTable_Object = MibTable
ospfAreaTable = _OspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13, 1)
)
if mibBuilder.loadTexts:
    ospfAreaTable.setStatus("current")
_OspfAreaEntry_Object = MibTableRow
ospfAreaEntry = _OspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13, 1, 1)
)
ospfAreaEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpType"),
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpName"),
    (0, "CORIANT-GROOVE-MIB", "ospfAreaId"),
)
if mibBuilder.loadTexts:
    ospfAreaEntry.setStatus("current")


class _OspfAreaId_Type(IetfYangTypesDottedQuad):
    """Custom type ospfAreaId based on IetfYangTypesDottedQuad"""
    subtypeSpec = IetfYangTypesDottedQuad.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OspfAreaId_Type.__name__ = "IetfYangTypesDottedQuad"
_OspfAreaId_Object = MibTableColumn
ospfAreaId = _OspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13, 1, 1, 1),
    _OspfAreaId_Type()
)
ospfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaId.setStatus("current")


class _OspfAreaAdminStatus_Type(Integer32):
    """Custom type ospfAreaAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OspfAreaAdminStatus_Type.__name__ = "Integer32"
_OspfAreaAdminStatus_Object = MibTableColumn
ospfAreaAdminStatus = _OspfAreaAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13, 1, 1, 2),
    _OspfAreaAdminStatus_Type()
)
ospfAreaAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAdminStatus.setStatus("current")


class _OspfAreaOperStatus_Type(Integer32):
    """Custom type ospfAreaOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OspfAreaOperStatus_Type.__name__ = "Integer32"
_OspfAreaOperStatus_Object = MibTableColumn
ospfAreaOperStatus = _OspfAreaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13, 1, 1, 3),
    _OspfAreaOperStatus_Type()
)
ospfAreaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaOperStatus.setStatus("current")


class _OspfAreaAliasName_Type(OctetString):
    """Custom type ospfAreaAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfAreaAliasName_Type.__name__ = "OctetString"
_OspfAreaAliasName_Object = MibTableColumn
ospfAreaAliasName = _OspfAreaAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13, 1, 1, 4),
    _OspfAreaAliasName_Type()
)
ospfAreaAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAliasName.setStatus("current")


class _OspfAreaType_Type(Integer32):
    """Custom type ospfAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("stub", 2))
    )


_OspfAreaType_Type.__name__ = "Integer32"
_OspfAreaType_Object = MibTableColumn
ospfAreaType = _OspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 13, 1, 1, 5),
    _OspfAreaType_Type()
)
ospfAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaType.setStatus("current")
_OspfInterface_ObjectIdentity = ObjectIdentity
ospfInterface = _OspfInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14)
)
_OspfInterfaceTable_Object = MibTable
ospfInterfaceTable = _OspfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14, 1)
)
if mibBuilder.loadTexts:
    ospfInterfaceTable.setStatus("current")
_OspfInterfaceEntry_Object = MibTableRow
ospfInterfaceEntry = _OspfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14, 1, 1)
)
ospfInterfaceEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpType"),
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpName"),
    (0, "CORIANT-GROOVE-MIB", "ospfAreaId"),
    (0, "CORIANT-GROOVE-MIB", "ospfInterfaceOspfIfName"),
)
if mibBuilder.loadTexts:
    ospfInterfaceEntry.setStatus("current")


class _OspfInterfaceOspfIfName_Type(OctetString):
    """Custom type ospfInterfaceOspfIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OspfInterfaceOspfIfName_Type.__name__ = "OctetString"
_OspfInterfaceOspfIfName_Object = MibTableColumn
ospfInterfaceOspfIfName = _OspfInterfaceOspfIfName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14, 1, 1, 1),
    _OspfInterfaceOspfIfName_Type()
)
ospfInterfaceOspfIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceOspfIfName.setStatus("current")
_OspfInterfaceOspfLinkpf_Type = OctetString
_OspfInterfaceOspfLinkpf_Object = MibTableColumn
ospfInterfaceOspfLinkpf = _OspfInterfaceOspfLinkpf_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14, 1, 1, 2),
    _OspfInterfaceOspfLinkpf_Type()
)
ospfInterfaceOspfLinkpf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceOspfLinkpf.setStatus("current")


class _OspfInterfaceOspfCost_Type(Unsigned32):
    """Custom type ospfInterfaceOspfCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfInterfaceOspfCost_Type.__name__ = "Unsigned32"
_OspfInterfaceOspfCost_Object = MibTableColumn
ospfInterfaceOspfCost = _OspfInterfaceOspfCost_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14, 1, 1, 3),
    _OspfInterfaceOspfCost_Type()
)
ospfInterfaceOspfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceOspfCost.setStatus("current")


class _OspfInterfaceOspfIfRouting_Type(Integer32):
    """Custom type ospfInterfaceOspfIfRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_OspfInterfaceOspfIfRouting_Type.__name__ = "Integer32"
_OspfInterfaceOspfIfRouting_Object = MibTableColumn
ospfInterfaceOspfIfRouting = _OspfInterfaceOspfIfRouting_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14, 1, 1, 4),
    _OspfInterfaceOspfIfRouting_Type()
)
ospfInterfaceOspfIfRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceOspfIfRouting.setStatus("current")


class _OspfInterfaceOspfNetworkType_Type(Integer32):
    """Custom type ospfInterfaceOspfNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("pointToPoint", 2),
          ("pointToMultipoint", 3))
    )


_OspfInterfaceOspfNetworkType_Type.__name__ = "Integer32"
_OspfInterfaceOspfNetworkType_Object = MibTableColumn
ospfInterfaceOspfNetworkType = _OspfInterfaceOspfNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 14, 1, 1, 5),
    _OspfInterfaceOspfNetworkType_Type()
)
ospfInterfaceOspfNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceOspfNetworkType.setStatus("current")
_OspfAdjacency_ObjectIdentity = ObjectIdentity
ospfAdjacency = _OspfAdjacency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 15)
)
_OspfAdjacencyTable_Object = MibTable
ospfAdjacencyTable = _OspfAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 15, 1)
)
if mibBuilder.loadTexts:
    ospfAdjacencyTable.setStatus("current")
_OspfAdjacencyEntry_Object = MibTableRow
ospfAdjacencyEntry = _OspfAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 15, 1, 1)
)
ospfAdjacencyEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpType"),
    (0, "CORIANT-GROOVE-MIB", "routingProtocolRtpName"),
    (0, "CORIANT-GROOVE-MIB", "ospfAreaId"),
    (0, "CORIANT-GROOVE-MIB", "ospfInterfaceOspfIfName"),
    (0, "CORIANT-GROOVE-MIB", "ospfAdjacencyOspfNeighborAddress"),
)
if mibBuilder.loadTexts:
    ospfAdjacencyEntry.setStatus("current")


class _OspfAdjacencyOspfNeighborAddress_Type(IetfInetTypesIpv4Address):
    """Custom type ospfAdjacencyOspfNeighborAddress based on IetfInetTypesIpv4Address"""
    subtypeSpec = IetfInetTypesIpv4Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OspfAdjacencyOspfNeighborAddress_Type.__name__ = "IetfInetTypesIpv4Address"
_OspfAdjacencyOspfNeighborAddress_Object = MibTableColumn
ospfAdjacencyOspfNeighborAddress = _OspfAdjacencyOspfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 15, 1, 1, 1),
    _OspfAdjacencyOspfNeighborAddress_Type()
)
ospfAdjacencyOspfNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAdjacencyOspfNeighborAddress.setStatus("current")
_OspfAdjacencyNeighborRouterId_Type = IetfYangTypesDottedQuad
_OspfAdjacencyNeighborRouterId_Object = MibTableColumn
ospfAdjacencyNeighborRouterId = _OspfAdjacencyNeighborRouterId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 15, 1, 1, 2),
    _OspfAdjacencyNeighborRouterId_Type()
)
ospfAdjacencyNeighborRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAdjacencyNeighborRouterId.setStatus("current")


class _OspfAdjacencyOspfAdjStatus_Type(Integer32):
    """Custom type ospfAdjacencyOspfAdjStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("init", 2),
          ("attempt", 3),
          ("twoWay", 4),
          ("exstart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_OspfAdjacencyOspfAdjStatus_Type.__name__ = "Integer32"
_OspfAdjacencyOspfAdjStatus_Object = MibTableColumn
ospfAdjacencyOspfAdjStatus = _OspfAdjacencyOspfAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 15, 1, 1, 3),
    _OspfAdjacencyOspfAdjStatus_Type()
)
ospfAdjacencyOspfAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAdjacencyOspfAdjStatus.setStatus("current")
_Rib_ObjectIdentity = ObjectIdentity
rib = _Rib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 16)
)
_RibTable_Object = MibTable
ribTable = _RibTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 16, 1)
)
if mibBuilder.loadTexts:
    ribTable.setStatus("current")
_RibEntry_Object = MibTableRow
ribEntry = _RibEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 16, 1, 1)
)
ribEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "ribName"),
)
if mibBuilder.loadTexts:
    ribEntry.setStatus("current")


class _RibName_Type(OctetString):
    """Custom type ribName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RibName_Type.__name__ = "OctetString"
_RibName_Object = MibTableColumn
ribName = _RibName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 16, 1, 1, 1),
    _RibName_Type()
)
ribName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ribName.setStatus("current")


class _RibAddressFamily_Type(Integer32):
    """Custom type ribAddressFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv4Unicast", 2),
          ("ipv6", 3))
    )


_RibAddressFamily_Type.__name__ = "Integer32"
_RibAddressFamily_Object = MibTableColumn
ribAddressFamily = _RibAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 16, 1, 1, 2),
    _RibAddressFamily_Type()
)
ribAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ribAddressFamily.setStatus("current")
_RibDefaultRib_Type = TruthValue
_RibDefaultRib_Object = MibTableColumn
ribDefaultRib = _RibDefaultRib_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 16, 1, 1, 3),
    _RibDefaultRib_Type()
)
ribDefaultRib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ribDefaultRib.setStatus("current")
_RibDescription_Type = OctetString
_RibDescription_Object = MibTableColumn
ribDescription = _RibDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 16, 1, 1, 4),
    _RibDescription_Type()
)
ribDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ribDescription.setStatus("current")
_Route_ObjectIdentity = ObjectIdentity
route = _Route_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17)
)
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17, 1)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("current")
_RouteEntry_Object = MibTableRow
routeEntry = _RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17, 1, 1)
)
routeEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "ribName"),
    (0, "CORIANT-GROOVE-MIB", "routeSourceProtocol"),
    (0, "CORIANT-GROOVE-MIB", "routeDestinationPrefix"),
)
if mibBuilder.loadTexts:
    routeEntry.setStatus("current")
_RouteSourceProtocol_Type = CoriantTypesSourceProtocol
_RouteSourceProtocol_Object = MibTableColumn
routeSourceProtocol = _RouteSourceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17, 1, 1, 1),
    _RouteSourceProtocol_Type()
)
routeSourceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeSourceProtocol.setStatus("current")


class _RouteDestinationPrefix_Type(IetfInetTypesIpv4Prefix):
    """Custom type routeDestinationPrefix based on IetfInetTypesIpv4Prefix"""
    subtypeSpec = IetfInetTypesIpv4Prefix.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RouteDestinationPrefix_Type.__name__ = "IetfInetTypesIpv4Prefix"
_RouteDestinationPrefix_Object = MibTableColumn
routeDestinationPrefix = _RouteDestinationPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17, 1, 1, 2),
    _RouteDestinationPrefix_Type()
)
routeDestinationPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeDestinationPrefix.setStatus("current")
_RouteDescription_Type = OctetString
_RouteDescription_Object = MibTableColumn
routeDescription = _RouteDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17, 1, 1, 3),
    _RouteDescription_Type()
)
routeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeDescription.setStatus("current")
_RoutePreference_Type = Unsigned32
_RoutePreference_Object = MibTableColumn
routePreference = _RoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17, 1, 1, 4),
    _RoutePreference_Type()
)
routePreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routePreference.setStatus("current")
_RouteActive_Type = TruthValue
_RouteActive_Object = MibTableColumn
routeActive = _RouteActive_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 17, 1, 1, 5),
    _RouteActive_Type()
)
routeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeActive.setStatus("current")
_Profiles_ObjectIdentity = ObjectIdentity
profiles = _Profiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18)
)
_PppProfile_ObjectIdentity = ObjectIdentity
pppProfile = _PppProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1)
)
_PppProfileTable_Object = MibTable
pppProfileTable = _PppProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1, 1)
)
if mibBuilder.loadTexts:
    pppProfileTable.setStatus("current")
_PppProfileEntry_Object = MibTableRow
pppProfileEntry = _PppProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1, 1, 1)
)
pppProfileEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "pppProfilePppPfName"),
)
if mibBuilder.loadTexts:
    pppProfileEntry.setStatus("current")


class _PppProfilePppPfName_Type(OctetString):
    """Custom type pppProfilePppPfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_PppProfilePppPfName_Type.__name__ = "OctetString"
_PppProfilePppPfName_Object = MibTableColumn
pppProfilePppPfName = _PppProfilePppPfName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1, 1, 1, 1),
    _PppProfilePppPfName_Type()
)
pppProfilePppPfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProfilePppPfName.setStatus("current")


class _PppProfilePppFcsLength_Type(Integer32):
    """Custom type pppProfilePppFcsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("t16", 16),
          ("t32", 32))
    )


_PppProfilePppFcsLength_Type.__name__ = "Integer32"
_PppProfilePppFcsLength_Object = MibTableColumn
pppProfilePppFcsLength = _PppProfilePppFcsLength_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1, 1, 1, 2),
    _PppProfilePppFcsLength_Type()
)
pppProfilePppFcsLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProfilePppFcsLength.setStatus("current")


class _PppProfilePppMru_Type(Unsigned32):
    """Custom type pppProfilePppMru based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_PppProfilePppMru_Type.__name__ = "Unsigned32"
_PppProfilePppMru_Object = MibTableColumn
pppProfilePppMru = _PppProfilePppMru_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1, 1, 1, 3),
    _PppProfilePppMru_Type()
)
pppProfilePppMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProfilePppMru.setStatus("current")


class _PppProfilePppRestartTimer_Type(Unsigned32):
    """Custom type pppProfilePppRestartTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PppProfilePppRestartTimer_Type.__name__ = "Unsigned32"
_PppProfilePppRestartTimer_Object = MibTableColumn
pppProfilePppRestartTimer = _PppProfilePppRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1, 1, 1, 4),
    _PppProfilePppRestartTimer_Type()
)
pppProfilePppRestartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProfilePppRestartTimer.setStatus("current")


class _PppProfilePppMaxFailure_Type(Unsigned32):
    """Custom type pppProfilePppMaxFailure based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PppProfilePppMaxFailure_Type.__name__ = "Unsigned32"
_PppProfilePppMaxFailure_Object = MibTableColumn
pppProfilePppMaxFailure = _PppProfilePppMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 1, 1, 1, 5),
    _PppProfilePppMaxFailure_Type()
)
pppProfilePppMaxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProfilePppMaxFailure.setStatus("current")
_OspfLinkProfile_ObjectIdentity = ObjectIdentity
ospfLinkProfile = _OspfLinkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 2)
)
_OspfLinkProfileTable_Object = MibTable
ospfLinkProfileTable = _OspfLinkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 2, 1)
)
if mibBuilder.loadTexts:
    ospfLinkProfileTable.setStatus("current")
_OspfLinkProfileEntry_Object = MibTableRow
ospfLinkProfileEntry = _OspfLinkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 2, 1, 1)
)
ospfLinkProfileEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "ospfLinkProfileOspfLinkpfName"),
)
if mibBuilder.loadTexts:
    ospfLinkProfileEntry.setStatus("current")


class _OspfLinkProfileOspfLinkpfName_Type(OctetString):
    """Custom type ospfLinkProfileOspfLinkpfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OspfLinkProfileOspfLinkpfName_Type.__name__ = "OctetString"
_OspfLinkProfileOspfLinkpfName_Object = MibTableColumn
ospfLinkProfileOspfLinkpfName = _OspfLinkProfileOspfLinkpfName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 2, 1, 1, 1),
    _OspfLinkProfileOspfLinkpfName_Type()
)
ospfLinkProfileOspfLinkpfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLinkProfileOspfLinkpfName.setStatus("current")


class _OspfLinkProfileHelloInterval_Type(Unsigned32):
    """Custom type ospfLinkProfileHelloInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OspfLinkProfileHelloInterval_Type.__name__ = "Unsigned32"
_OspfLinkProfileHelloInterval_Object = MibTableColumn
ospfLinkProfileHelloInterval = _OspfLinkProfileHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 2, 1, 1, 2),
    _OspfLinkProfileHelloInterval_Type()
)
ospfLinkProfileHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLinkProfileHelloInterval.setStatus("current")


class _OspfLinkProfileRouterDeadInterval_Type(Unsigned32):
    """Custom type ospfLinkProfileRouterDeadInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1024),
    )


_OspfLinkProfileRouterDeadInterval_Type.__name__ = "Unsigned32"
_OspfLinkProfileRouterDeadInterval_Object = MibTableColumn
ospfLinkProfileRouterDeadInterval = _OspfLinkProfileRouterDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 2, 1, 1, 3),
    _OspfLinkProfileRouterDeadInterval_Type()
)
ospfLinkProfileRouterDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLinkProfileRouterDeadInterval.setStatus("current")


class _OspfLinkProfileRetransmissionInterval_Type(Unsigned32):
    """Custom type ospfLinkProfileRetransmissionInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OspfLinkProfileRetransmissionInterval_Type.__name__ = "Unsigned32"
_OspfLinkProfileRetransmissionInterval_Object = MibTableColumn
ospfLinkProfileRetransmissionInterval = _OspfLinkProfileRetransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 18, 2, 1, 1, 4),
    _OspfLinkProfileRetransmissionInterval_Type()
)
ospfLinkProfileRetransmissionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLinkProfileRetransmissionInterval.setStatus("current")
_Oscx_ObjectIdentity = ObjectIdentity
oscx = _Oscx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 19)
)
_OscxTable_Object = MibTable
oscxTable = _OscxTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 19, 1)
)
if mibBuilder.loadTexts:
    oscxTable.setStatus("current")
_OscxEntry_Object = MibTableRow
oscxEntry = _OscxEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 19, 1, 1)
)
oscxEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "interfaceIfName"),
)
if mibBuilder.loadTexts:
    oscxEntry.setStatus("current")


class _OscxChannel_Type(Integer32):
    """Custom type oscxChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1", 1),
          ("t2", 2))
    )


_OscxChannel_Type.__name__ = "Integer32"
_OscxChannel_Object = MibTableColumn
oscxChannel = _OscxChannel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 19, 1, 1, 1),
    _OscxChannel_Type()
)
oscxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscxChannel.setStatus("current")
_OscxResourceRef_Type = RowPointer
_OscxResourceRef_Object = MibTableColumn
oscxResourceRef = _OscxResourceRef_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 19, 1, 1, 2),
    _OscxResourceRef_Type()
)
oscxResourceRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscxResourceRef.setStatus("current")


class _OscxAliasName_Type(OctetString):
    """Custom type oscxAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OscxAliasName_Type.__name__ = "OctetString"
_OscxAliasName_Object = MibTableColumn
oscxAliasName = _OscxAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 6, 19, 1, 1, 3),
    _OscxAliasName_Type()
)
oscxAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscxAliasName.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7)
)
_SecurityInfo_ObjectIdentity = ObjectIdentity
securityInfo = _SecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1)
)


class _SecuritySshPublicKey_Type(OctetString):
    """Custom type securitySshPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2500),
    )


_SecuritySshPublicKey_Type.__name__ = "OctetString"
_SecuritySshPublicKey_Object = MibScalar
securitySshPublicKey = _SecuritySshPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1, 1),
    _SecuritySshPublicKey_Type()
)
securitySshPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securitySshPublicKey.setStatus("current")


class _SecuritySshPublicKeyFingerprint_Type(OctetString):
    """Custom type securitySshPublicKeyFingerprint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SecuritySshPublicKeyFingerprint_Type.__name__ = "OctetString"
_SecuritySshPublicKeyFingerprint_Object = MibScalar
securitySshPublicKeyFingerprint = _SecuritySshPublicKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1, 2),
    _SecuritySshPublicKeyFingerprint_Type()
)
securitySshPublicKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securitySshPublicKeyFingerprint.setStatus("current")


class _SecurityPreLoginMessage_Type(OctetString):
    """Custom type securityPreLoginMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1440),
    )


_SecurityPreLoginMessage_Type.__name__ = "OctetString"
_SecurityPreLoginMessage_Object = MibScalar
securityPreLoginMessage = _SecurityPreLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1, 3),
    _SecurityPreLoginMessage_Type()
)
securityPreLoginMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityPreLoginMessage.setStatus("current")


class _SecurityWarningMessage_Type(OctetString):
    """Custom type securityWarningMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1440),
    )


_SecurityWarningMessage_Type.__name__ = "OctetString"
_SecurityWarningMessage_Object = MibScalar
securityWarningMessage = _SecurityWarningMessage_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1, 4),
    _SecurityWarningMessage_Type()
)
securityWarningMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityWarningMessage.setStatus("current")


class _SecurityAaaAuthenticationMethod_Type(Integer32):
    """Custom type securityAaaAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("localOnly", 1),
          ("localFirstThenRemote", 3),
          ("remoteFirstThenLocal", 4),
          ("remoteUnavailableThenLocal", 5))
    )


_SecurityAaaAuthenticationMethod_Type.__name__ = "Integer32"
_SecurityAaaAuthenticationMethod_Object = MibScalar
securityAaaAuthenticationMethod = _SecurityAaaAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1, 5),
    _SecurityAaaAuthenticationMethod_Type()
)
securityAaaAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAaaAuthenticationMethod.setStatus("current")


class _SecuritySystemFips_Type(Integer32):
    """Custom type securitySystemFips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SecuritySystemFips_Type.__name__ = "Integer32"
_SecuritySystemFips_Object = MibScalar
securitySystemFips = _SecuritySystemFips_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1, 6),
    _SecuritySystemFips_Type()
)
securitySystemFips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securitySystemFips.setStatus("current")
_SecurityHttpSupport_Type = CoriantTypesEnableSwitch
_SecurityHttpSupport_Object = MibScalar
securityHttpSupport = _SecurityHttpSupport_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 1, 7),
    _SecurityHttpSupport_Type()
)
securityHttpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityHttpSupport.setStatus("current")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2)
)
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1)
)
userEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")
_UserName_Type = CoriantTypesUserName
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserPassword_Type(OctetString):
    """Custom type userPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_UserPassword_Type.__name__ = "OctetString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 2),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")


class _UserClass_Type(Integer32):
    """Custom type userClass based on Integer32"""
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
        *(("cryptoOfficer", 0),
          ("administration", 1),
          ("configuration", 2),
          ("operation", 3),
          ("supervision", 4))
    )


_UserClass_Type.__name__ = "Integer32"
_UserClass_Object = MibTableColumn
userClass = _UserClass_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 3),
    _UserClass_Type()
)
userClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userClass.setStatus("current")


class _UserMaxInvalidLogin_Type(Unsigned32):
    """Custom type userMaxInvalidLogin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_UserMaxInvalidLogin_Type.__name__ = "Unsigned32"
_UserMaxInvalidLogin_Object = MibTableColumn
userMaxInvalidLogin = _UserMaxInvalidLogin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 4),
    _UserMaxInvalidLogin_Type()
)
userMaxInvalidLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userMaxInvalidLogin.setStatus("current")


class _UserSuspensionTime_Type(Unsigned32):
    """Custom type userSuspensionTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_UserSuspensionTime_Type.__name__ = "Unsigned32"
_UserSuspensionTime_Object = MibTableColumn
userSuspensionTime = _UserSuspensionTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 5),
    _UserSuspensionTime_Type()
)
userSuspensionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSuspensionTime.setStatus("current")


class _UserTimeout_Type(Unsigned32):
    """Custom type userTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_UserTimeout_Type.__name__ = "Unsigned32"
_UserTimeout_Object = MibTableColumn
userTimeout = _UserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 6),
    _UserTimeout_Type()
)
userTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTimeout.setStatus("current")


class _UserPasswordAgingInterval_Type(Unsigned32):
    """Custom type userPasswordAgingInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_UserPasswordAgingInterval_Type.__name__ = "Unsigned32"
_UserPasswordAgingInterval_Object = MibTableColumn
userPasswordAgingInterval = _UserPasswordAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 7),
    _UserPasswordAgingInterval_Type()
)
userPasswordAgingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPasswordAgingInterval.setStatus("current")
_UserPasswordExpirationDate_Type = IetfYangTypesDateAndTime
_UserPasswordExpirationDate_Object = MibTableColumn
userPasswordExpirationDate = _UserPasswordExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 8),
    _UserPasswordExpirationDate_Type()
)
userPasswordExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPasswordExpirationDate.setStatus("current")


class _UserAdminStatus_Type(Integer32):
    """Custom type userAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_UserAdminStatus_Type.__name__ = "Integer32"
_UserAdminStatus_Object = MibTableColumn
userAdminStatus = _UserAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 9),
    _UserAdminStatus_Type()
)
userAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAdminStatus.setStatus("current")


class _UserStatus_Type(Integer32):
    """Custom type userStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("passwordAged", 3),
          ("lockout", 4))
    )


_UserStatus_Type.__name__ = "Integer32"
_UserStatus_Object = MibTableColumn
userStatus = _UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 10),
    _UserStatus_Type()
)
userStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatus.setStatus("current")


class _UserMaxSessions_Type(Unsigned32):
    """Custom type userMaxSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_UserMaxSessions_Type.__name__ = "Unsigned32"
_UserMaxSessions_Object = MibTableColumn
userMaxSessions = _UserMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 11),
    _UserMaxSessions_Type()
)
userMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userMaxSessions.setStatus("current")
_UserLastLoginDate_Type = IetfYangTypesDateAndTime
_UserLastLoginDate_Object = MibTableColumn
userLastLoginDate = _UserLastLoginDate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 12),
    _UserLastLoginDate_Type()
)
userLastLoginDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLastLoginDate.setStatus("current")


class _UserAaaType_Type(Integer32):
    """Custom type userAaaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_UserAaaType_Type.__name__ = "Integer32"
_UserAaaType_Object = MibTableColumn
userAaaType = _UserAaaType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 2, 1, 1, 13),
    _UserAaaType_Type()
)
userAaaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAaaType.setStatus("current")
_Session_ObjectIdentity = ObjectIdentity
session = _Session_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3)
)
_SessionTable_Object = MibTable
sessionTable = _SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    sessionTable.setStatus("current")
_SessionEntry_Object = MibTableRow
sessionEntry = _SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3, 1, 1)
)
sessionEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "sessionId"),
)
if mibBuilder.loadTexts:
    sessionEntry.setStatus("current")
_SessionId_Type = CoriantTypesSessionId
_SessionId_Object = MibTableColumn
sessionId = _SessionId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3, 1, 1, 1),
    _SessionId_Type()
)
sessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionId.setStatus("current")
_SessionUser_Type = RowPointer
_SessionUser_Object = MibTableColumn
sessionUser = _SessionUser_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3, 1, 1, 2),
    _SessionUser_Type()
)
sessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUser.setStatus("current")


class _SessionType_Type(Integer32):
    """Custom type sessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("snmp", 2),
          ("netconf", 3),
          ("restconf", 4),
          ("webgui", 5),
          ("gnmi", 6))
    )


_SessionType_Type.__name__ = "Integer32"
_SessionType_Object = MibTableColumn
sessionType = _SessionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3, 1, 1, 3),
    _SessionType_Type()
)
sessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionType.setStatus("current")


class _SessionProtocol_Type(Integer32):
    """Custom type sessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("telnetRaw", 2),
          ("serial", 3),
          ("ssh", 4),
          ("sshRaw", 5),
          ("https", 6),
          ("http", 7))
    )


_SessionProtocol_Type.__name__ = "Integer32"
_SessionProtocol_Object = MibTableColumn
sessionProtocol = _SessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3, 1, 1, 4),
    _SessionProtocol_Type()
)
sessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionProtocol.setStatus("current")
_SessionCreatedTime_Type = IetfYangTypesDateAndTime
_SessionCreatedTime_Object = MibTableColumn
sessionCreatedTime = _SessionCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 3, 1, 1, 5),
    _SessionCreatedTime_Type()
)
sessionCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCreatedTime.setStatus("current")
_AaaServer_ObjectIdentity = ObjectIdentity
aaaServer = _AaaServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4)
)
_AaaServerTable_Object = MibTable
aaaServerTable = _AaaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    aaaServerTable.setStatus("current")
_AaaServerEntry_Object = MibTableRow
aaaServerEntry = _AaaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1)
)
aaaServerEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "aaaServerServerName"),
)
if mibBuilder.loadTexts:
    aaaServerEntry.setStatus("current")


class _AaaServerServerName_Type(OctetString):
    """Custom type aaaServerServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaServerServerName_Type.__name__ = "OctetString"
_AaaServerServerName_Object = MibTableColumn
aaaServerServerName = _AaaServerServerName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 1),
    _AaaServerServerName_Type()
)
aaaServerServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerServerName.setStatus("current")


class _AaaServerServerPriority_Type(Unsigned32):
    """Custom type aaaServerServerPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AaaServerServerPriority_Type.__name__ = "Unsigned32"
_AaaServerServerPriority_Object = MibTableColumn
aaaServerServerPriority = _AaaServerServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 2),
    _AaaServerServerPriority_Type()
)
aaaServerServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerServerPriority.setStatus("current")


class _AaaServerProtocolSupported_Type(Integer32):
    """Custom type aaaServerProtocolSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tacacsplus", 1)
    )


_AaaServerProtocolSupported_Type.__name__ = "Integer32"
_AaaServerProtocolSupported_Object = MibTableColumn
aaaServerProtocolSupported = _AaaServerProtocolSupported_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 3),
    _AaaServerProtocolSupported_Type()
)
aaaServerProtocolSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerProtocolSupported.setStatus("current")
_AaaServerServerIp_Type = IetfInetTypesIpv4Address
_AaaServerServerIp_Object = MibTableColumn
aaaServerServerIp = _AaaServerServerIp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 4),
    _AaaServerServerIp_Type()
)
aaaServerServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerServerIp.setStatus("current")
_AaaServerServerPort_Type = IetfInetTypesPortNumber
_AaaServerServerPort_Object = MibTableColumn
aaaServerServerPort = _AaaServerServerPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 5),
    _AaaServerServerPort_Type()
)
aaaServerServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerServerPort.setStatus("current")


class _AaaServerSharedSecret_Type(OctetString):
    """Custom type aaaServerSharedSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AaaServerSharedSecret_Type.__name__ = "OctetString"
_AaaServerSharedSecret_Object = MibTableColumn
aaaServerSharedSecret = _AaaServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 6),
    _AaaServerSharedSecret_Type()
)
aaaServerSharedSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerSharedSecret.setStatus("current")


class _AaaServerRoleSupported_Type(Bits):
    """Custom type aaaServerRoleSupported based on Bits"""
    namedValues = NamedValues(
        *(("authentication", 0),
          ("authorization", 1),
          ("accounting", 2))
    )

_AaaServerRoleSupported_Type.__name__ = "Bits"
_AaaServerRoleSupported_Object = MibTableColumn
aaaServerRoleSupported = _AaaServerRoleSupported_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 7),
    _AaaServerRoleSupported_Type()
)
aaaServerRoleSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerRoleSupported.setStatus("current")


class _AaaServerAdminStatus_Type(Integer32):
    """Custom type aaaServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AaaServerAdminStatus_Type.__name__ = "Integer32"
_AaaServerAdminStatus_Object = MibTableColumn
aaaServerAdminStatus = _AaaServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 8),
    _AaaServerAdminStatus_Type()
)
aaaServerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerAdminStatus.setStatus("current")


class _AaaServerTimeOut_Type(Unsigned32):
    """Custom type aaaServerTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AaaServerTimeOut_Type.__name__ = "Unsigned32"
_AaaServerTimeOut_Object = MibTableColumn
aaaServerTimeOut = _AaaServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 9),
    _AaaServerTimeOut_Type()
)
aaaServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerTimeOut.setStatus("current")


class _AaaServerRetry_Type(Unsigned32):
    """Custom type aaaServerRetry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AaaServerRetry_Type.__name__ = "Unsigned32"
_AaaServerRetry_Object = MibTableColumn
aaaServerRetry = _AaaServerRetry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 4, 1, 1, 10),
    _AaaServerRetry_Type()
)
aaaServerRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaServerRetry.setStatus("current")
_KeySyncSession_ObjectIdentity = ObjectIdentity
keySyncSession = _KeySyncSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5)
)
_KeySyncSessionTable_Object = MibTable
keySyncSessionTable = _KeySyncSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1)
)
if mibBuilder.loadTexts:
    keySyncSessionTable.setStatus("current")
_KeySyncSessionEntry_Object = MibTableRow
keySyncSessionEntry = _KeySyncSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1)
)
keySyncSessionEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "keySyncSessionId"),
)
if mibBuilder.loadTexts:
    keySyncSessionEntry.setStatus("current")


class _KeySyncSessionId_Type(Unsigned32):
    """Custom type keySyncSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_KeySyncSessionId_Type.__name__ = "Unsigned32"
_KeySyncSessionId_Object = MibTableColumn
keySyncSessionId = _KeySyncSessionId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 1),
    _KeySyncSessionId_Type()
)
keySyncSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionId.setStatus("current")


class _KeySyncSessionAdminStatus_Type(Integer32):
    """Custom type keySyncSessionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_KeySyncSessionAdminStatus_Type.__name__ = "Integer32"
_KeySyncSessionAdminStatus_Object = MibTableColumn
keySyncSessionAdminStatus = _KeySyncSessionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 2),
    _KeySyncSessionAdminStatus_Type()
)
keySyncSessionAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionAdminStatus.setStatus("current")


class _KeySyncSessionSessionStatus_Type(Integer32):
    """Custom type keySyncSessionSessionStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("connecting", 2),
          ("incomplete", 3),
          ("connected", 4),
          ("unreachable", 5),
          ("failedAuth", 6),
          ("failed", 7))
    )


_KeySyncSessionSessionStatus_Type.__name__ = "Integer32"
_KeySyncSessionSessionStatus_Object = MibTableColumn
keySyncSessionSessionStatus = _KeySyncSessionSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 4),
    _KeySyncSessionSessionStatus_Type()
)
keySyncSessionSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionSessionStatus.setStatus("current")
_KeySyncSessionRemoteIp_Type = IetfInetTypesIpv4Address
_KeySyncSessionRemoteIp_Object = MibTableColumn
keySyncSessionRemoteIp = _KeySyncSessionRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 5),
    _KeySyncSessionRemoteIp_Type()
)
keySyncSessionRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionRemoteIp.setStatus("current")
_KeySyncSessionRemotePort_Type = IetfInetTypesPortNumber
_KeySyncSessionRemotePort_Object = MibTableColumn
keySyncSessionRemotePort = _KeySyncSessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 6),
    _KeySyncSessionRemotePort_Type()
)
keySyncSessionRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionRemotePort.setStatus("current")
_KeySyncSessionLocalIp_Type = IetfInetTypesIpv4Address
_KeySyncSessionLocalIp_Object = MibTableColumn
keySyncSessionLocalIp = _KeySyncSessionLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 7),
    _KeySyncSessionLocalIp_Type()
)
keySyncSessionLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionLocalIp.setStatus("current")
_KeySyncSessionLocalPort_Type = IetfInetTypesPortNumber
_KeySyncSessionLocalPort_Object = MibTableColumn
keySyncSessionLocalPort = _KeySyncSessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 8),
    _KeySyncSessionLocalPort_Type()
)
keySyncSessionLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionLocalPort.setStatus("current")
_KeySyncSessionSourceAddressFrom_Type = OctetString
_KeySyncSessionSourceAddressFrom_Object = MibTableColumn
keySyncSessionSourceAddressFrom = _KeySyncSessionSourceAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 9),
    _KeySyncSessionSourceAddressFrom_Type()
)
keySyncSessionSourceAddressFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionSourceAddressFrom.setStatus("current")
_KeySyncSessionConnectedTime_Type = IetfYangTypesDateAndTime
_KeySyncSessionConnectedTime_Object = MibTableColumn
keySyncSessionConnectedTime = _KeySyncSessionConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 10),
    _KeySyncSessionConnectedTime_Type()
)
keySyncSessionConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionConnectedTime.setStatus("current")


class _KeySyncSessionType_Type(Integer32):
    """Custom type keySyncSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_KeySyncSessionType_Type.__name__ = "Integer32"
_KeySyncSessionType_Object = MibTableColumn
keySyncSessionType = _KeySyncSessionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 11),
    _KeySyncSessionType_Type()
)
keySyncSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionType.setStatus("current")


class _KeySyncSessionAuthType_Type(Integer32):
    """Custom type keySyncSessionAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tlsCertificate", 1),
          ("proprietaryPsk", 2))
    )


_KeySyncSessionAuthType_Type.__name__ = "Integer32"
_KeySyncSessionAuthType_Object = MibTableColumn
keySyncSessionAuthType = _KeySyncSessionAuthType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 12),
    _KeySyncSessionAuthType_Type()
)
keySyncSessionAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionAuthType.setStatus("current")
_KeySyncSessionLocalCertificate_Type = OctetString
_KeySyncSessionLocalCertificate_Object = MibTableColumn
keySyncSessionLocalCertificate = _KeySyncSessionLocalCertificate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 5, 1, 1, 13),
    _KeySyncSessionLocalCertificate_Type()
)
keySyncSessionLocalCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySyncSessionLocalCertificate.setStatus("current")
_PskMap_ObjectIdentity = ObjectIdentity
pskMap = _PskMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7)
)
_PskMapTable_Object = MibTable
pskMapTable = _PskMapTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1)
)
if mibBuilder.loadTexts:
    pskMapTable.setStatus("current")
_PskMapEntry_Object = MibTableRow
pskMapEntry = _PskMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1)
)
pskMapEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "pskMapPskIdentity"),
)
if mibBuilder.loadTexts:
    pskMapEntry.setStatus("current")


class _PskMapPskIdentity_Type(OctetString):
    """Custom type pskMapPskIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PskMapPskIdentity_Type.__name__ = "OctetString"
_PskMapPskIdentity_Object = MibTableColumn
pskMapPskIdentity = _PskMapPskIdentity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 1),
    _PskMapPskIdentity_Type()
)
pskMapPskIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapPskIdentity.setStatus("current")
_PskMapKey_Type = IetfYangTypesHexString
_PskMapKey_Object = MibTableColumn
pskMapKey = _PskMapKey_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 2),
    _PskMapKey_Type()
)
pskMapKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapKey.setStatus("current")


class _PskMapPskStatus_Type(Integer32):
    """Custom type pskMapPskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("sync", 2),
          ("fail", 3),
          ("authenticate", 4))
    )


_PskMapPskStatus_Type.__name__ = "Integer32"
_PskMapPskStatus_Object = MibTableColumn
pskMapPskStatus = _PskMapPskStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 4),
    _PskMapPskStatus_Type()
)
pskMapPskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapPskStatus.setStatus("current")


class _PskMapPskInfo_Type(OctetString):
    """Custom type pskMapPskInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PskMapPskInfo_Type.__name__ = "OctetString"
_PskMapPskInfo_Object = MibTableColumn
pskMapPskInfo = _PskMapPskInfo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 5),
    _PskMapPskInfo_Type()
)
pskMapPskInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapPskInfo.setStatus("current")


class _PskMapWarningTimer_Type(Unsigned32):
    """Custom type pskMapWarningTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_PskMapWarningTimer_Type.__name__ = "Unsigned32"
_PskMapWarningTimer_Object = MibTableColumn
pskMapWarningTimer = _PskMapWarningTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 6),
    _PskMapWarningTimer_Type()
)
pskMapWarningTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapWarningTimer.setStatus("current")


class _PskMapCriticalTimer_Type(Unsigned32):
    """Custom type pskMapCriticalTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_PskMapCriticalTimer_Type.__name__ = "Unsigned32"
_PskMapCriticalTimer_Object = MibTableColumn
pskMapCriticalTimer = _PskMapCriticalTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 7),
    _PskMapCriticalTimer_Type()
)
pskMapCriticalTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapCriticalTimer.setStatus("current")


class _PskMapTrafficOffTimer_Type(Unsigned32):
    """Custom type pskMapTrafficOffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_PskMapTrafficOffTimer_Type.__name__ = "Unsigned32"
_PskMapTrafficOffTimer_Object = MibTableColumn
pskMapTrafficOffTimer = _PskMapTrafficOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 8),
    _PskMapTrafficOffTimer_Type()
)
pskMapTrafficOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapTrafficOffTimer.setStatus("current")
_PskMapEffectiveTimestamp_Type = IetfYangTypesDateAndTime
_PskMapEffectiveTimestamp_Object = MibTableColumn
pskMapEffectiveTimestamp = _PskMapEffectiveTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 7, 1, 1, 9),
    _PskMapEffectiveTimestamp_Type()
)
pskMapEffectiveTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pskMapEffectiveTimestamp.setStatus("current")
_Key_ObjectIdentity = ObjectIdentity
key = _Key_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 9)
)
_KeyTable_Object = MibTable
keyTable = _KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 9, 1)
)
if mibBuilder.loadTexts:
    keyTable.setStatus("current")
_KeyEntry_Object = MibTableRow
keyEntry = _KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 9, 1, 1)
)
keyEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "keyName"),
)
if mibBuilder.loadTexts:
    keyEntry.setStatus("current")


class _KeyName_Type(OctetString):
    """Custom type keyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_KeyName_Type.__name__ = "OctetString"
_KeyName_Object = MibTableColumn
keyName = _KeyName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 9, 1, 1, 1),
    _KeyName_Type()
)
keyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyName.setStatus("current")


class _KeyAlgorithmIdentifier_Type(Integer32):
    """Custom type keyAlgorithmIdentifier based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("rsa1024", 1),
          ("rsa2048", 2),
          ("rsa3072", 3),
          ("rsa4096", 4),
          ("rsa7680", 5),
          ("rsa15360", 6),
          ("secp192r1", 7),
          ("secp256r1", 8),
          ("secp384r1", 9),
          ("secp521r1", 10))
    )


_KeyAlgorithmIdentifier_Type.__name__ = "Integer32"
_KeyAlgorithmIdentifier_Object = MibTableColumn
keyAlgorithmIdentifier = _KeyAlgorithmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 9, 1, 1, 2),
    _KeyAlgorithmIdentifier_Type()
)
keyAlgorithmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyAlgorithmIdentifier.setStatus("current")


class _KeyPublicKey_Type(OctetString):
    """Custom type keyPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2500),
    )


_KeyPublicKey_Type.__name__ = "OctetString"
_KeyPublicKey_Object = MibTableColumn
keyPublicKey = _KeyPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 9, 1, 1, 3),
    _KeyPublicKey_Type()
)
keyPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyPublicKey.setStatus("current")
_Certificate_ObjectIdentity = ObjectIdentity
certificate = _Certificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10)
)
_CertificateTable_Object = MibTable
certificateTable = _CertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1)
)
if mibBuilder.loadTexts:
    certificateTable.setStatus("current")
_CertificateEntry_Object = MibTableRow
certificateEntry = _CertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1)
)
certificateEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "keyName"),
    (0, "CORIANT-GROOVE-MIB", "certificateName"),
)
if mibBuilder.loadTexts:
    certificateEntry.setStatus("current")


class _CertificateName_Type(OctetString):
    """Custom type certificateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CertificateName_Type.__name__ = "OctetString"
_CertificateName_Object = MibTableColumn
certificateName = _CertificateName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 1),
    _CertificateName_Type()
)
certificateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateName.setStatus("current")


class _CertificateVersion_Type(Integer32):
    """Custom type certificateVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("x509v1", 1),
          ("x509v2", 2),
          ("x509v3", 3))
    )


_CertificateVersion_Type.__name__ = "Integer32"
_CertificateVersion_Object = MibTableColumn
certificateVersion = _CertificateVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 2),
    _CertificateVersion_Type()
)
certificateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateVersion.setStatus("current")
_CertificateSerialNumber_Type = OctetString
_CertificateSerialNumber_Object = MibTableColumn
certificateSerialNumber = _CertificateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 3),
    _CertificateSerialNumber_Type()
)
certificateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSerialNumber.setStatus("current")
_CertificateSignatureAlgorithm_Type = OctetString
_CertificateSignatureAlgorithm_Object = MibTableColumn
certificateSignatureAlgorithm = _CertificateSignatureAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 4),
    _CertificateSignatureAlgorithm_Type()
)
certificateSignatureAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSignatureAlgorithm.setStatus("current")


class _CertificateIssuer_Type(OctetString):
    """Custom type certificateIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CertificateIssuer_Type.__name__ = "OctetString"
_CertificateIssuer_Object = MibTableColumn
certificateIssuer = _CertificateIssuer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 5),
    _CertificateIssuer_Type()
)
certificateIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateIssuer.setStatus("current")
_CertificateValidFrom_Type = OctetString
_CertificateValidFrom_Object = MibTableColumn
certificateValidFrom = _CertificateValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 6),
    _CertificateValidFrom_Type()
)
certificateValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateValidFrom.setStatus("current")
_CertificateValidTo_Type = OctetString
_CertificateValidTo_Object = MibTableColumn
certificateValidTo = _CertificateValidTo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 7),
    _CertificateValidTo_Type()
)
certificateValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateValidTo.setStatus("current")


class _CertificateSubject_Type(OctetString):
    """Custom type certificateSubject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CertificateSubject_Type.__name__ = "OctetString"
_CertificateSubject_Object = MibTableColumn
certificateSubject = _CertificateSubject_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 8),
    _CertificateSubject_Type()
)
certificateSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSubject.setStatus("current")
_CertificatePublicKeyAlgorithm_Type = OctetString
_CertificatePublicKeyAlgorithm_Object = MibTableColumn
certificatePublicKeyAlgorithm = _CertificatePublicKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 10, 1, 1, 9),
    _CertificatePublicKeyAlgorithm_Type()
)
certificatePublicKeyAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificatePublicKeyAlgorithm.setStatus("current")
_TrustedCertificateGroup_ObjectIdentity = ObjectIdentity
trustedCertificateGroup = _TrustedCertificateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 11)
)
_TrustedCertificateGroupTable_Object = MibTable
trustedCertificateGroupTable = _TrustedCertificateGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 11, 1)
)
if mibBuilder.loadTexts:
    trustedCertificateGroupTable.setStatus("current")
_TrustedCertificateGroupEntry_Object = MibTableRow
trustedCertificateGroupEntry = _TrustedCertificateGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 11, 1, 1)
)
trustedCertificateGroupEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "trustedCertificateGroupName"),
)
if mibBuilder.loadTexts:
    trustedCertificateGroupEntry.setStatus("current")


class _TrustedCertificateGroupName_Type(OctetString):
    """Custom type trustedCertificateGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrustedCertificateGroupName_Type.__name__ = "OctetString"
_TrustedCertificateGroupName_Object = MibTableColumn
trustedCertificateGroupName = _TrustedCertificateGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 11, 1, 1, 1),
    _TrustedCertificateGroupName_Type()
)
trustedCertificateGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateGroupName.setStatus("current")
_TrustedCertificate_ObjectIdentity = ObjectIdentity
trustedCertificate = _TrustedCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12)
)
_TrustedCertificateTable_Object = MibTable
trustedCertificateTable = _TrustedCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1)
)
if mibBuilder.loadTexts:
    trustedCertificateTable.setStatus("current")
_TrustedCertificateEntry_Object = MibTableRow
trustedCertificateEntry = _TrustedCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1)
)
trustedCertificateEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "trustedCertificateGroupName"),
    (0, "CORIANT-GROOVE-MIB", "trustedCertificateName"),
)
if mibBuilder.loadTexts:
    trustedCertificateEntry.setStatus("current")


class _TrustedCertificateName_Type(OctetString):
    """Custom type trustedCertificateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrustedCertificateName_Type.__name__ = "OctetString"
_TrustedCertificateName_Object = MibTableColumn
trustedCertificateName = _TrustedCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 1),
    _TrustedCertificateName_Type()
)
trustedCertificateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateName.setStatus("current")


class _TrustedCertificateVersion_Type(Integer32):
    """Custom type trustedCertificateVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("x509v1", 1),
          ("x509v2", 2),
          ("x509v3", 3))
    )


_TrustedCertificateVersion_Type.__name__ = "Integer32"
_TrustedCertificateVersion_Object = MibTableColumn
trustedCertificateVersion = _TrustedCertificateVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 2),
    _TrustedCertificateVersion_Type()
)
trustedCertificateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateVersion.setStatus("current")
_TrustedCertificateSerialNumber_Type = OctetString
_TrustedCertificateSerialNumber_Object = MibTableColumn
trustedCertificateSerialNumber = _TrustedCertificateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 3),
    _TrustedCertificateSerialNumber_Type()
)
trustedCertificateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateSerialNumber.setStatus("current")
_TrustedCertificateSignatureAlgorithm_Type = OctetString
_TrustedCertificateSignatureAlgorithm_Object = MibTableColumn
trustedCertificateSignatureAlgorithm = _TrustedCertificateSignatureAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 4),
    _TrustedCertificateSignatureAlgorithm_Type()
)
trustedCertificateSignatureAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateSignatureAlgorithm.setStatus("current")


class _TrustedCertificateIssuer_Type(OctetString):
    """Custom type trustedCertificateIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrustedCertificateIssuer_Type.__name__ = "OctetString"
_TrustedCertificateIssuer_Object = MibTableColumn
trustedCertificateIssuer = _TrustedCertificateIssuer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 5),
    _TrustedCertificateIssuer_Type()
)
trustedCertificateIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateIssuer.setStatus("current")
_TrustedCertificateValidFrom_Type = OctetString
_TrustedCertificateValidFrom_Object = MibTableColumn
trustedCertificateValidFrom = _TrustedCertificateValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 6),
    _TrustedCertificateValidFrom_Type()
)
trustedCertificateValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateValidFrom.setStatus("current")
_TrustedCertificateValidTo_Type = OctetString
_TrustedCertificateValidTo_Object = MibTableColumn
trustedCertificateValidTo = _TrustedCertificateValidTo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 7),
    _TrustedCertificateValidTo_Type()
)
trustedCertificateValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateValidTo.setStatus("current")


class _TrustedCertificateSubject_Type(OctetString):
    """Custom type trustedCertificateSubject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrustedCertificateSubject_Type.__name__ = "OctetString"
_TrustedCertificateSubject_Object = MibTableColumn
trustedCertificateSubject = _TrustedCertificateSubject_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 8),
    _TrustedCertificateSubject_Type()
)
trustedCertificateSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificateSubject.setStatus("current")
_TrustedCertificatePublicKeyAlgorithm_Type = OctetString
_TrustedCertificatePublicKeyAlgorithm_Object = MibTableColumn
trustedCertificatePublicKeyAlgorithm = _TrustedCertificatePublicKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 7, 12, 1, 1, 9),
    _TrustedCertificatePublicKeyAlgorithm_Type()
)
trustedCertificatePublicKeyAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedCertificatePublicKeyAlgorithm.setStatus("current")
_Nbi_ObjectIdentity = ObjectIdentity
nbi = _Nbi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1)
)
_Snmpv3_ObjectIdentity = ObjectIdentity
snmpv3 = _Snmpv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1)
)
_Snmpv3Table_Object = MibTable
snmpv3Table = _Snmpv3Table_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snmpv3Table.setStatus("current")
_Snmpv3Entry_Object = MibTableRow
snmpv3Entry = _Snmpv3Entry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1, 1, 1)
)
snmpv3Entry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "userName"),
)
if mibBuilder.loadTexts:
    snmpv3Entry.setStatus("current")


class _Snmpv3UserSecLevel_Type(Integer32):
    """Custom type snmpv3UserSecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authPriv", 1),
          ("authNoPriv", 2),
          ("noAuthNoPriv", 3))
    )


_Snmpv3UserSecLevel_Type.__name__ = "Integer32"
_Snmpv3UserSecLevel_Object = MibTableColumn
snmpv3UserSecLevel = _Snmpv3UserSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1, 1, 1, 1),
    _Snmpv3UserSecLevel_Type()
)
snmpv3UserSecLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3UserSecLevel.setStatus("current")


class _Snmpv3AuthProtocol_Type(Integer32):
    """Custom type snmpv3AuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_Snmpv3AuthProtocol_Type.__name__ = "Integer32"
_Snmpv3AuthProtocol_Object = MibTableColumn
snmpv3AuthProtocol = _Snmpv3AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1, 1, 1, 2),
    _Snmpv3AuthProtocol_Type()
)
snmpv3AuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3AuthProtocol.setStatus("current")


class _Snmpv3AuthPassphrase_Type(OctetString):
    """Custom type snmpv3AuthPassphrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 64),
    )


_Snmpv3AuthPassphrase_Type.__name__ = "OctetString"
_Snmpv3AuthPassphrase_Object = MibTableColumn
snmpv3AuthPassphrase = _Snmpv3AuthPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1, 1, 1, 3),
    _Snmpv3AuthPassphrase_Type()
)
snmpv3AuthPassphrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3AuthPassphrase.setStatus("current")


class _Snmpv3PrivProtocol_Type(Integer32):
    """Custom type snmpv3PrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("aes", 2))
    )


_Snmpv3PrivProtocol_Type.__name__ = "Integer32"
_Snmpv3PrivProtocol_Object = MibTableColumn
snmpv3PrivProtocol = _Snmpv3PrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1, 1, 1, 4),
    _Snmpv3PrivProtocol_Type()
)
snmpv3PrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3PrivProtocol.setStatus("current")


class _Snmpv3PrivPassphrase_Type(OctetString):
    """Custom type snmpv3PrivPassphrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 64),
    )


_Snmpv3PrivPassphrase_Type.__name__ = "OctetString"
_Snmpv3PrivPassphrase_Object = MibTableColumn
snmpv3PrivPassphrase = _Snmpv3PrivPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 1, 1, 1, 5),
    _Snmpv3PrivPassphrase_Type()
)
snmpv3PrivPassphrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3PrivPassphrase.setStatus("current")
_SnmpInfo_ObjectIdentity = ObjectIdentity
snmpInfo = _SnmpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 2)
)


class _SnmpEngineId_Type(OctetString):
    """Custom type snmpEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SnmpEngineId_Type.__name__ = "OctetString"
_SnmpEngineId_Object = MibScalar
snmpEngineId = _SnmpEngineId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 2, 1),
    _SnmpEngineId_Type()
)
snmpEngineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineId.setStatus("current")
_SnmpCommunity_ObjectIdentity = ObjectIdentity
snmpCommunity = _SnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 3)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 3, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "snmpCommunityCommunityString"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")
_SnmpCommunityCommunityString_Type = CoriantTypesSnmpString
_SnmpCommunityCommunityString_Object = MibTableColumn
snmpCommunityCommunityString = _SnmpCommunityCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 3, 1, 1, 1),
    _SnmpCommunityCommunityString_Type()
)
snmpCommunityCommunityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityCommunityString.setStatus("current")


class _SnmpCommunityCommunityStringAccess_Type(Integer32):
    """Custom type snmpCommunityCommunityStringAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("readOnly", 1)
    )


_SnmpCommunityCommunityStringAccess_Type.__name__ = "Integer32"
_SnmpCommunityCommunityStringAccess_Object = MibTableColumn
snmpCommunityCommunityStringAccess = _SnmpCommunityCommunityStringAccess_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 3, 1, 1, 2),
    _SnmpCommunityCommunityStringAccess_Type()
)
snmpCommunityCommunityStringAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityCommunityStringAccess.setStatus("current")
_SnmpTarget_ObjectIdentity = ObjectIdentity
snmpTarget = _SnmpTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4)
)
_SnmpTargetTable_Object = MibTable
snmpTargetTable = _SnmpTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snmpTargetTable.setStatus("current")
_SnmpTargetEntry_Object = MibTableRow
snmpTargetEntry = _SnmpTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1)
)
snmpTargetEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "snmpTargetTargetName"),
)
if mibBuilder.loadTexts:
    snmpTargetEntry.setStatus("current")


class _SnmpTargetSnmpVersion_Type(Integer32):
    """Custom type snmpTargetSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2c", 2),
          ("v3", 3))
    )


_SnmpTargetSnmpVersion_Type.__name__ = "Integer32"
_SnmpTargetSnmpVersion_Object = MibTableColumn
snmpTargetSnmpVersion = _SnmpTargetSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1, 1),
    _SnmpTargetSnmpVersion_Type()
)
snmpTargetSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTargetSnmpVersion.setStatus("current")
_SnmpTargetSnmpv3User_Type = RowPointer
_SnmpTargetSnmpv3User_Object = MibTableColumn
snmpTargetSnmpv3User = _SnmpTargetSnmpv3User_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1, 2),
    _SnmpTargetSnmpv3User_Type()
)
snmpTargetSnmpv3User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTargetSnmpv3User.setStatus("current")


class _SnmpTargetTargetName_Type(OctetString):
    """Custom type snmpTargetTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpTargetTargetName_Type.__name__ = "OctetString"
_SnmpTargetTargetName_Object = MibTableColumn
snmpTargetTargetName = _SnmpTargetTargetName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1, 3),
    _SnmpTargetTargetName_Type()
)
snmpTargetTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTargetTargetName.setStatus("current")
_SnmpTargetTargetIp_Type = IetfInetTypesIpv4Address
_SnmpTargetTargetIp_Object = MibTableColumn
snmpTargetTargetIp = _SnmpTargetTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1, 4),
    _SnmpTargetTargetIp_Type()
)
snmpTargetTargetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTargetTargetIp.setStatus("current")
_SnmpTargetTargetPort_Type = IetfInetTypesPortNumber
_SnmpTargetTargetPort_Object = MibTableColumn
snmpTargetTargetPort = _SnmpTargetTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1, 5),
    _SnmpTargetTargetPort_Type()
)
snmpTargetTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTargetTargetPort.setStatus("current")


class _SnmpTargetTargetTransport_Type(Integer32):
    """Custom type snmpTargetTargetTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("udp", 1)
    )


_SnmpTargetTargetTransport_Type.__name__ = "Integer32"
_SnmpTargetTargetTransport_Object = MibTableColumn
snmpTargetTargetTransport = _SnmpTargetTargetTransport_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1, 6),
    _SnmpTargetTargetTransport_Type()
)
snmpTargetTargetTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTargetTargetTransport.setStatus("current")
_SnmpTargetTrapCommunityString_Type = CoriantTypesSnmpString
_SnmpTargetTrapCommunityString_Object = MibTableColumn
snmpTargetTrapCommunityString = _SnmpTargetTrapCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 1, 4, 1, 1, 7),
    _SnmpTargetTrapCommunityString_Type()
)
snmpTargetTrapCommunityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTargetTrapCommunityString.setStatus("current")
_Cli_ObjectIdentity = ObjectIdentity
cli = _Cli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2)
)
_CliConfig_ObjectIdentity = ObjectIdentity
cliConfig = _CliConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2, 1)
)
_CliConfigTable_Object = MibTable
cliConfigTable = _CliConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cliConfigTable.setStatus("current")
_CliConfigEntry_Object = MibTableRow
cliConfigEntry = _CliConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2, 1, 1, 1)
)
cliConfigEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "sessionId"),
)
if mibBuilder.loadTexts:
    cliConfigEntry.setStatus("current")


class _CliConfigCliLines_Type(Unsigned32):
    """Custom type cliConfigCliLines based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_CliConfigCliLines_Type.__name__ = "Unsigned32"
_CliConfigCliLines_Object = MibTableColumn
cliConfigCliLines = _CliConfigCliLines_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2, 1, 1, 1, 1),
    _CliConfigCliLines_Type()
)
cliConfigCliLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliConfigCliLines.setStatus("current")


class _CliConfigCliColumns_Type(Unsigned32):
    """Custom type cliConfigCliColumns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 4000),
    )


_CliConfigCliColumns_Type.__name__ = "Unsigned32"
_CliConfigCliColumns_Object = MibTableColumn
cliConfigCliColumns = _CliConfigCliColumns_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2, 1, 1, 1, 2),
    _CliConfigCliColumns_Type()
)
cliConfigCliColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliConfigCliColumns.setStatus("current")
_CliConfigMaxHistorySize_Type = Unsigned32
_CliConfigMaxHistorySize_Object = MibTableColumn
cliConfigMaxHistorySize = _CliConfigMaxHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2, 1, 1, 1, 3),
    _CliConfigMaxHistorySize_Type()
)
cliConfigMaxHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliConfigMaxHistorySize.setStatus("current")
_CliConfigInteractiveMode_Type = CoriantTypesEnableSwitch
_CliConfigInteractiveMode_Object = MibTableColumn
cliConfigInteractiveMode = _CliConfigInteractiveMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 2, 1, 1, 1, 4),
    _CliConfigInteractiveMode_Type()
)
cliConfigInteractiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliConfigInteractiveMode.setStatus("current")
_Restconf_ObjectIdentity = ObjectIdentity
restconf = _Restconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 3)
)
_RestconfRestHttpSupport_Type = CoriantTypesEnableSwitch
_RestconfRestHttpSupport_Object = MibScalar
restconfRestHttpSupport = _RestconfRestHttpSupport_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 3, 1),
    _RestconfRestHttpSupport_Type()
)
restconfRestHttpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restconfRestHttpSupport.setStatus("current")
_RestconfRestHttpsSupport_Type = CoriantTypesEnableSwitch
_RestconfRestHttpsSupport_Object = MibScalar
restconfRestHttpsSupport = _RestconfRestHttpsSupport_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 3, 2),
    _RestconfRestHttpsSupport_Type()
)
restconfRestHttpsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restconfRestHttpsSupport.setStatus("current")


class _RestconfRestSessionTimeout_Type(Unsigned32):
    """Custom type restconfRestSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_RestconfRestSessionTimeout_Type.__name__ = "Unsigned32"
_RestconfRestSessionTimeout_Object = MibScalar
restconfRestSessionTimeout = _RestconfRestSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 3, 3),
    _RestconfRestSessionTimeout_Type()
)
restconfRestSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restconfRestSessionTimeout.setStatus("current")
_CliAlias_ObjectIdentity = ObjectIdentity
cliAlias = _CliAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 4)
)
_CliAliasTable_Object = MibTable
cliAliasTable = _CliAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    cliAliasTable.setStatus("current")
_CliAliasEntry_Object = MibTableRow
cliAliasEntry = _CliAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 4, 1, 1)
)
cliAliasEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "cliAliasName"),
)
if mibBuilder.loadTexts:
    cliAliasEntry.setStatus("current")


class _CliAliasName_Type(OctetString):
    """Custom type cliAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CliAliasName_Type.__name__ = "OctetString"
_CliAliasName_Object = MibTableColumn
cliAliasName = _CliAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 4, 1, 1, 1),
    _CliAliasName_Type()
)
cliAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliAliasName.setStatus("current")


class _CliAliasValue_Type(OctetString):
    """Custom type cliAliasValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CliAliasValue_Type.__name__ = "OctetString"
_CliAliasValue_Object = MibTableColumn
cliAliasValue = _CliAliasValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 4, 1, 1, 2),
    _CliAliasValue_Type()
)
cliAliasValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliAliasValue.setStatus("current")
_CliScript_ObjectIdentity = ObjectIdentity
cliScript = _CliScript_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 5)
)
_CliScriptTable_Object = MibTable
cliScriptTable = _CliScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 5, 1)
)
if mibBuilder.loadTexts:
    cliScriptTable.setStatus("current")
_CliScriptEntry_Object = MibTableRow
cliScriptEntry = _CliScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 5, 1, 1)
)
cliScriptEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "cliScriptScriptName"),
)
if mibBuilder.loadTexts:
    cliScriptEntry.setStatus("current")


class _CliScriptScriptName_Type(OctetString):
    """Custom type cliScriptScriptName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CliScriptScriptName_Type.__name__ = "OctetString"
_CliScriptScriptName_Object = MibTableColumn
cliScriptScriptName = _CliScriptScriptName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 5, 1, 1, 1),
    _CliScriptScriptName_Type()
)
cliScriptScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliScriptScriptName.setStatus("current")


class _CliScriptDescription_Type(OctetString):
    """Custom type cliScriptDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CliScriptDescription_Type.__name__ = "OctetString"
_CliScriptDescription_Object = MibTableColumn
cliScriptDescription = _CliScriptDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 8, 5, 1, 1, 2),
    _CliScriptDescription_Type()
)
cliScriptDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliScriptDescription.setStatus("current")
_Filesw_ObjectIdentity = ObjectIdentity
filesw = _Filesw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9)
)
_Softwareload_ObjectIdentity = ObjectIdentity
softwareload = _Softwareload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2)
)
_SoftwareloadTable_Object = MibTable
softwareloadTable = _SoftwareloadTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    softwareloadTable.setStatus("current")
_SoftwareloadEntry_Object = MibTableRow
softwareloadEntry = _SoftwareloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1, 1)
)
softwareloadEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "softwareloadSwloadId"),
)
if mibBuilder.loadTexts:
    softwareloadEntry.setStatus("current")


class _SoftwareloadSwloadId_Type(Unsigned32):
    """Custom type softwareloadSwloadId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SoftwareloadSwloadId_Type.__name__ = "Unsigned32"
_SoftwareloadSwloadId_Object = MibTableColumn
softwareloadSwloadId = _SoftwareloadSwloadId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1, 1, 1),
    _SoftwareloadSwloadId_Type()
)
softwareloadSwloadId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareloadSwloadId.setStatus("current")


class _SoftwareloadSwloadState_Type(Integer32):
    """Custom type softwareloadSwloadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SoftwareloadSwloadState_Type.__name__ = "Integer32"
_SoftwareloadSwloadState_Object = MibTableColumn
softwareloadSwloadState = _SoftwareloadSwloadState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1, 1, 2),
    _SoftwareloadSwloadState_Type()
)
softwareloadSwloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareloadSwloadState.setStatus("current")
_SoftwareloadSwloadVersion_Type = CoriantFileSwTypesSwVersion
_SoftwareloadSwloadVersion_Object = MibTableColumn
softwareloadSwloadVersion = _SoftwareloadSwloadVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1, 1, 3),
    _SoftwareloadSwloadVersion_Type()
)
softwareloadSwloadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareloadSwloadVersion.setStatus("current")
_SoftwareloadSwloadVendor_Type = CoriantFileSwTypesSwloadVendor
_SoftwareloadSwloadVendor_Object = MibTableColumn
softwareloadSwloadVendor = _SoftwareloadSwloadVendor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1, 1, 4),
    _SoftwareloadSwloadVendor_Type()
)
softwareloadSwloadVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareloadSwloadVendor.setStatus("current")
_SoftwareloadSwloadProduct_Type = CoriantFileSwTypesSwloadProduct
_SoftwareloadSwloadProduct_Object = MibTableColumn
softwareloadSwloadProduct = _SoftwareloadSwloadProduct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1, 1, 5),
    _SoftwareloadSwloadProduct_Type()
)
softwareloadSwloadProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareloadSwloadProduct.setStatus("current")


class _SoftwareloadSwloadLabel_Type(OctetString):
    """Custom type softwareloadSwloadLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SoftwareloadSwloadLabel_Type.__name__ = "OctetString"
_SoftwareloadSwloadLabel_Object = MibTableColumn
softwareloadSwloadLabel = _SoftwareloadSwloadLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 2, 1, 1, 6),
    _SoftwareloadSwloadLabel_Type()
)
softwareloadSwloadLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareloadSwloadLabel.setStatus("current")
_Database_ObjectIdentity = ObjectIdentity
database = _Database_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3)
)
_DatabaseTable_Object = MibTable
databaseTable = _DatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1)
)
if mibBuilder.loadTexts:
    databaseTable.setStatus("current")
_DatabaseEntry_Object = MibTableRow
databaseEntry = _DatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1, 1)
)
databaseEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "softwareloadSwloadId"),
    (0, "CORIANT-GROOVE-MIB", "databaseId"),
)
if mibBuilder.loadTexts:
    databaseEntry.setStatus("current")


class _DatabaseId_Type(Unsigned32):
    """Custom type databaseId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DatabaseId_Type.__name__ = "Unsigned32"
_DatabaseId_Object = MibTableColumn
databaseId = _DatabaseId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1, 1, 1),
    _DatabaseId_Type()
)
databaseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseId.setStatus("current")


class _DatabaseState_Type(Integer32):
    """Custom type databaseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DatabaseState_Type.__name__ = "Integer32"
_DatabaseState_Object = MibTableColumn
databaseState = _DatabaseState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1, 1, 2),
    _DatabaseState_Type()
)
databaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseState.setStatus("current")
_DatabaseVersion_Type = CoriantFileSwTypesSwVersion
_DatabaseVersion_Object = MibTableColumn
databaseVersion = _DatabaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1, 1, 3),
    _DatabaseVersion_Type()
)
databaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseVersion.setStatus("current")
_DatabaseVendor_Type = CoriantFileSwTypesSwloadVendor
_DatabaseVendor_Object = MibTableColumn
databaseVendor = _DatabaseVendor_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1, 1, 4),
    _DatabaseVendor_Type()
)
databaseVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseVendor.setStatus("current")
_DatabaseProduct_Type = CoriantFileSwTypesSwloadProduct
_DatabaseProduct_Object = MibTableColumn
databaseProduct = _DatabaseProduct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1, 1, 5),
    _DatabaseProduct_Type()
)
databaseProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseProduct.setStatus("current")
_DatabaseBackupTime_Type = OctetString
_DatabaseBackupTime_Object = MibTableColumn
databaseBackupTime = _DatabaseBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 3, 1, 1, 6),
    _DatabaseBackupTime_Type()
)
databaseBackupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseBackupTime.setStatus("current")
_FwVersionMap_ObjectIdentity = ObjectIdentity
fwVersionMap = _FwVersionMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 4)
)
_FwVersionMapTable_Object = MibTable
fwVersionMapTable = _FwVersionMapTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    fwVersionMapTable.setStatus("current")
_FwVersionMapEntry_Object = MibTableRow
fwVersionMapEntry = _FwVersionMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 4, 1, 1)
)
fwVersionMapEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "softwareloadSwloadId"),
    (0, "CORIANT-GROOVE-MIB", "fwVersionMapDeviceName"),
)
if mibBuilder.loadTexts:
    fwVersionMapEntry.setStatus("current")
_FwVersionMapDeviceName_Type = CoriantFileSwTypesDeviceName
_FwVersionMapDeviceName_Object = MibTableColumn
fwVersionMapDeviceName = _FwVersionMapDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 4, 1, 1, 1),
    _FwVersionMapDeviceName_Type()
)
fwVersionMapDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersionMapDeviceName.setStatus("current")
_FwVersionMapDeviceFwVersion_Type = CoriantFileSwTypesDeviceFwVersion
_FwVersionMapDeviceFwVersion_Object = MibTableColumn
fwVersionMapDeviceFwVersion = _FwVersionMapDeviceFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 4, 1, 1, 2),
    _FwVersionMapDeviceFwVersion_Type()
)
fwVersionMapDeviceFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersionMapDeviceFwVersion.setStatus("current")
_CurrentFwVersion_ObjectIdentity = ObjectIdentity
currentFwVersion = _CurrentFwVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5)
)
_CurrentFwVersionTable_Object = MibTable
currentFwVersionTable = _CurrentFwVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    currentFwVersionTable.setStatus("current")
_CurrentFwVersionEntry_Object = MibTableRow
currentFwVersionEntry = _CurrentFwVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5, 1, 1)
)
currentFwVersionEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "currentFwVersionEquipmentEntity"),
    (0, "CORIANT-GROOVE-MIB", "currentFwVersionDeviceName"),
)
if mibBuilder.loadTexts:
    currentFwVersionEntry.setStatus("current")
_CurrentFwVersionEquipmentEntity_Type = RowPointer
_CurrentFwVersionEquipmentEntity_Object = MibTableColumn
currentFwVersionEquipmentEntity = _CurrentFwVersionEquipmentEntity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5, 1, 1, 1),
    _CurrentFwVersionEquipmentEntity_Type()
)
currentFwVersionEquipmentEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFwVersionEquipmentEntity.setStatus("current")
_CurrentFwVersionFwEquipmentType_Type = CoriantTypesEquipmentType
_CurrentFwVersionFwEquipmentType_Object = MibTableColumn
currentFwVersionFwEquipmentType = _CurrentFwVersionFwEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5, 1, 1, 2),
    _CurrentFwVersionFwEquipmentType_Type()
)
currentFwVersionFwEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFwVersionFwEquipmentType.setStatus("current")
_CurrentFwVersionDeviceName_Type = CoriantFileSwTypesDeviceName
_CurrentFwVersionDeviceName_Object = MibTableColumn
currentFwVersionDeviceName = _CurrentFwVersionDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5, 1, 1, 3),
    _CurrentFwVersionDeviceName_Type()
)
currentFwVersionDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFwVersionDeviceName.setStatus("current")
_CurrentFwVersionDeviceFwVersion_Type = CoriantFileSwTypesDeviceFwVersion
_CurrentFwVersionDeviceFwVersion_Object = MibTableColumn
currentFwVersionDeviceFwVersion = _CurrentFwVersionDeviceFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5, 1, 1, 4),
    _CurrentFwVersionDeviceFwVersion_Type()
)
currentFwVersionDeviceFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFwVersionDeviceFwVersion.setStatus("current")


class _CurrentFwVersionFwState_Type(Integer32):
    """Custom type currentFwVersionFwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("current", 1),
          ("notCurrent", 2))
    )


_CurrentFwVersionFwState_Type.__name__ = "Integer32"
_CurrentFwVersionFwState_Object = MibTableColumn
currentFwVersionFwState = _CurrentFwVersionFwState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 5, 1, 1, 5),
    _CurrentFwVersionFwState_Type()
)
currentFwVersionFwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFwVersionFwState.setStatus("current")
_RollbackPoint_ObjectIdentity = ObjectIdentity
rollbackPoint = _RollbackPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6)
)
_RollbackPointTable_Object = MibTable
rollbackPointTable = _RollbackPointTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6, 1)
)
if mibBuilder.loadTexts:
    rollbackPointTable.setStatus("current")
_RollbackPointEntry_Object = MibTableRow
rollbackPointEntry = _RollbackPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6, 1, 1)
)
rollbackPointEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "rollbackPointId"),
)
if mibBuilder.loadTexts:
    rollbackPointEntry.setStatus("current")


class _RollbackPointId_Type(Unsigned32):
    """Custom type rollbackPointId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RollbackPointId_Type.__name__ = "Unsigned32"
_RollbackPointId_Object = MibTableColumn
rollbackPointId = _RollbackPointId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6, 1, 1, 1),
    _RollbackPointId_Type()
)
rollbackPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rollbackPointId.setStatus("current")
_RollbackPointCreationTime_Type = IetfYangTypesDateAndTime
_RollbackPointCreationTime_Object = MibTableColumn
rollbackPointCreationTime = _RollbackPointCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6, 1, 1, 2),
    _RollbackPointCreationTime_Type()
)
rollbackPointCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rollbackPointCreationTime.setStatus("current")
_RollbackPointCreationTrigger_Type = CoriantTypesUserName
_RollbackPointCreationTrigger_Object = MibTableColumn
rollbackPointCreationTrigger = _RollbackPointCreationTrigger_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6, 1, 1, 3),
    _RollbackPointCreationTrigger_Type()
)
rollbackPointCreationTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rollbackPointCreationTrigger.setStatus("current")


class _RollbackPointDescription_Type(OctetString):
    """Custom type rollbackPointDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_RollbackPointDescription_Type.__name__ = "OctetString"
_RollbackPointDescription_Object = MibTableColumn
rollbackPointDescription = _RollbackPointDescription_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6, 1, 1, 4),
    _RollbackPointDescription_Type()
)
rollbackPointDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rollbackPointDescription.setStatus("current")


class _RollbackPointType_Type(Integer32):
    """Custom type rollbackPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("backup", 2))
    )


_RollbackPointType_Type.__name__ = "Integer32"
_RollbackPointType_Object = MibTableColumn
rollbackPointType = _RollbackPointType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 6, 1, 1, 5),
    _RollbackPointType_Type()
)
rollbackPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rollbackPointType.setStatus("current")
_LogServer_ObjectIdentity = ObjectIdentity
logServer = _LogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8)
)
_LogServerTable_Object = MibTable
logServerTable = _LogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1)
)
if mibBuilder.loadTexts:
    logServerTable.setStatus("current")
_LogServerEntry_Object = MibTableRow
logServerEntry = _LogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1, 1)
)
logServerEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "logServerName"),
)
if mibBuilder.loadTexts:
    logServerEntry.setStatus("current")


class _LogServerName_Type(OctetString):
    """Custom type logServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LogServerName_Type.__name__ = "OctetString"
_LogServerName_Object = MibTableColumn
logServerName = _LogServerName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1, 1, 1),
    _LogServerName_Type()
)
logServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerName.setStatus("current")
_LogServerIpAddress_Type = IetfInetTypesIpv4Address
_LogServerIpAddress_Object = MibTableColumn
logServerIpAddress = _LogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1, 1, 2),
    _LogServerIpAddress_Type()
)
logServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerIpAddress.setStatus("current")


class _LogServerTransport_Type(Integer32):
    """Custom type logServerTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_LogServerTransport_Type.__name__ = "Integer32"
_LogServerTransport_Object = MibTableColumn
logServerTransport = _LogServerTransport_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1, 1, 3),
    _LogServerTransport_Type()
)
logServerTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerTransport.setStatus("current")
_LogServerPort_Type = IetfInetTypesPortNumber
_LogServerPort_Object = MibTableColumn
logServerPort = _LogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1, 1, 4),
    _LogServerPort_Type()
)
logServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerPort.setStatus("current")
_LogServerDestinationFacilityType_Type = CoriantTypesEnableSwitch
_LogServerDestinationFacilityType_Object = MibTableColumn
logServerDestinationFacilityType = _LogServerDestinationFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1, 1, 5),
    _LogServerDestinationFacilityType_Type()
)
logServerDestinationFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerDestinationFacilityType.setStatus("current")
_LogServerDestinationFacility_Type = OctetString
_LogServerDestinationFacility_Object = MibTableColumn
logServerDestinationFacility = _LogServerDestinationFacility_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 8, 1, 1, 6),
    _LogServerDestinationFacility_Type()
)
logServerDestinationFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerDestinationFacility.setStatus("current")
_LogFacility_ObjectIdentity = ObjectIdentity
logFacility = _LogFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 10)
)
_LogFacilityTable_Object = MibTable
logFacilityTable = _LogFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 10, 1)
)
if mibBuilder.loadTexts:
    logFacilityTable.setStatus("current")
_LogFacilityEntry_Object = MibTableRow
logFacilityEntry = _LogFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 10, 1, 1)
)
logFacilityEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "logServerName"),
    (0, "CORIANT-GROOVE-MIB", "logFacilityLogSelectorFacility"),
)
if mibBuilder.loadTexts:
    logFacilityEntry.setStatus("current")


class _LogFacilityLogSelectorFacility_Type(Integer32):
    """Custom type logFacilityLogSelectorFacility based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("security", 1),
          ("alarm", 2),
          ("event", 3),
          ("configuration", 4),
          ("cryptoConfiguration", 5),
          ("cryptoSecurity", 6),
          ("cryptoEvent", 7),
          ("cryptoAlarm", 8))
    )


_LogFacilityLogSelectorFacility_Type.__name__ = "Integer32"
_LogFacilityLogSelectorFacility_Object = MibTableColumn
logFacilityLogSelectorFacility = _LogFacilityLogSelectorFacility_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 10, 1, 1, 1),
    _LogFacilityLogSelectorFacility_Type()
)
logFacilityLogSelectorFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFacilityLogSelectorFacility.setStatus("current")


class _LogFacilityLogSelectorSeverity_Type(Integer32):
    """Custom type logFacilityLogSelectorSeverity based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )


_LogFacilityLogSelectorSeverity_Type.__name__ = "Integer32"
_LogFacilityLogSelectorSeverity_Object = MibTableColumn
logFacilityLogSelectorSeverity = _LogFacilityLogSelectorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 10, 1, 1, 2),
    _LogFacilityLogSelectorSeverity_Type()
)
logFacilityLogSelectorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFacilityLogSelectorSeverity.setStatus("current")


class _LogFacilityCompareOp_Type(Integer32):
    """Custom type logFacilityCompareOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equalsOrHigher", 1),
          ("equals", 2),
          ("notEquals", 3))
    )


_LogFacilityCompareOp_Type.__name__ = "Integer32"
_LogFacilityCompareOp_Object = MibTableColumn
logFacilityCompareOp = _LogFacilityCompareOp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 9, 10, 1, 1, 3),
    _LogFacilityCompareOp_Type()
)
logFacilityCompareOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFacilityCompareOp.setStatus("current")
_TimeManager_ObjectIdentity = ObjectIdentity
timeManager = _TimeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10)
)
_TimeManagerInfo_ObjectIdentity = ObjectIdentity
timeManagerInfo = _TimeManagerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 1)
)


class _TimeManagerTimezone_Type(Integer32):
    """Custom type timeManagerTimezone based on Integer32"""
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
              76)
        )
    )
    namedValues = NamedValues(
        *(("internationalDateLineWestGmt1200", 1),
          ("midwayIslandSamoaGmt1100", 2),
          ("hawaiiGmt1000", 3),
          ("alaskaGmt0900", 4),
          ("pacificTimeUsAndCanadaGmt0800", 5),
          ("arizonaGmt0700", 6),
          ("mountainTimeUsAndCanadaGmt0700", 7),
          ("centralamericaGmt0600", 8),
          ("centralTimeUsAndCanadaGmt0600", 9),
          ("mexicoCityTegucigalpaGmt0600", 10),
          ("saskatchewanGmt0600", 11),
          ("bagotaLimaQuitoGmt0500", 12),
          ("easternTimeUsAndCanadaGmt0500", 13),
          ("indianaEastGmt0500", 14),
          ("caracasLaPazGmt0430", 15),
          ("atlanticTimeCanadaGmt0400", 16),
          ("santiagoGmt0400", 17),
          ("newfoundlandGmt0330", 18),
          ("brasiliaGmt0300", 19),
          ("buenosAiresGeorgetownGmt0300", 20),
          ("greenlandGmt0300", 21),
          ("midAtlanticGmt0200", 22),
          ("azoresGmt0100", 23),
          ("capeVerdeIsGmt0100", 24),
          ("casablancaMonroviaGmt", 25),
          ("greenwichMeanTimeDublinEdinburghLisbonLondonGmt", 26),
          ("amsterdamCopenhagenMadridParisvilniusGmtplus0100", 27),
          ("belgradeSarajevoSkopjeSofijaZargrebGmtplus0100", 28),
          ("bratislavaBudapestLjublijanaPragueWasawGmtplus0100", 29),
          ("brusselsBerlinBernRomeStockholmViennaGmtplus0100", 30),
          ("westCentralAfricaGmtplus0100", 31),
          ("athensIstanbulMinskGmtplus0200", 32),
          ("bucharestGmtplus0200", 33),
          ("cairoGmtplus0200", 34),
          ("hararePretoriaGmtplus0200", 35),
          ("helsinkiRigaTallinnGmtplus0200", 36),
          ("jerusalemGmtplus0200", 37),
          ("israelGmtplus0200", 38),
          ("baghdadGmtplus0300", 39),
          ("kuwaitRiyadhGmtplus0300", 40),
          ("moscowStPetersburgVolgogradGmtplus0300", 41),
          ("nairobiGmtplus0300", 42),
          ("tehranGmtplus0330", 43),
          ("abuDhabiMuscatGmtplus0400", 44),
          ("bakuGmtplus0400", 45),
          ("tbilisiGmtplus0400", 46),
          ("kabulGmtplus0430", 47),
          ("ekaterinburgGmtplus0500", 48),
          ("islamabadKarachiTashkentGmtplus0500", 49),
          ("mumbaiCalcuttaChennaiNewDelhiGmtplus0530", 50),
          ("colomboGmtplus0530", 51),
          ("kathmanduGmtplus0545", 52),
          ("dhakaGmtplus0600", 53),
          ("almatyGmtplus0600", 54),
          ("rangoonGmtplus0630", 55),
          ("bangkokHanoiJakartaGmtplus0700", 56),
          ("beijingChongqingHongKongUrumqiGmtplus0800", 57),
          ("perthGmtplus0800", 58),
          ("singaporeKualaLumpurGmtplus0800", 59),
          ("taipeiGmtplus0800", 60),
          ("osakaSapporoTokyoGmtplus0900", 61),
          ("seoulGmtplus0900", 62),
          ("yakutskGmtplus0900", 63),
          ("adelaideGmtplus0930", 64),
          ("darwinGmtplus0930", 65),
          ("brisbaneGmtplus1000", 66),
          ("canberraMelbourneSydneyGmtplus1000", 67),
          ("guamPortMoresbyGmtplus1000", 68),
          ("hobartGmtplus1000", 69),
          ("vladivostokGmtplus1000", 70),
          ("magadanSolomonIsNewCaledoniaGmtplus1100", 71),
          ("aucklandWellingtonGmtplus1200", 72),
          ("fijiKamchatkaMarshallIsGmtplus1200", 73),
          ("eniwetokKwajaleinGmtplus1200", 74),
          ("nukuAlofaGmtplus1300", 75),
          ("kiritimatiGmtplus1400", 76))
    )


_TimeManagerTimezone_Type.__name__ = "Integer32"
_TimeManagerTimezone_Object = MibScalar
timeManagerTimezone = _TimeManagerTimezone_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 1, 1),
    _TimeManagerTimezone_Type()
)
timeManagerTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeManagerTimezone.setStatus("current")
_TimeManagerCurrentTime_Type = IetfYangTypesDateAndTime
_TimeManagerCurrentTime_Object = MibScalar
timeManagerCurrentTime = _TimeManagerCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 1, 2),
    _TimeManagerCurrentTime_Type()
)
timeManagerCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeManagerCurrentTime.setStatus("current")
_TimeManagerLastStartTime_Type = IetfYangTypesDateAndTime
_TimeManagerLastStartTime_Object = MibScalar
timeManagerLastStartTime = _TimeManagerLastStartTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 1, 3),
    _TimeManagerLastStartTime_Type()
)
timeManagerLastStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeManagerLastStartTime.setStatus("current")
_TimeManagerUpTime_Type = OctetString
_TimeManagerUpTime_Object = MibScalar
timeManagerUpTime = _TimeManagerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 1, 4),
    _TimeManagerUpTime_Type()
)
timeManagerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeManagerUpTime.setStatus("current")


class _TimeManagerTimeSourceState_Type(Integer32):
    """Custom type timeManagerTimeSourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("freerun", 2))
    )


_TimeManagerTimeSourceState_Type.__name__ = "Integer32"
_TimeManagerTimeSourceState_Object = MibScalar
timeManagerTimeSourceState = _TimeManagerTimeSourceState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 1, 5),
    _TimeManagerTimeSourceState_Type()
)
timeManagerTimeSourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeManagerTimeSourceState.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 2)
)
_NtpEnabled_Type = TruthValue
_NtpEnabled_Object = MibScalar
ntpEnabled = _NtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 2, 1),
    _NtpEnabled_Type()
)
ntpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEnabled.setStatus("current")
_NtpCurrentTimeSource_Type = IetfInetTypesIpv4AddressNoZone
_NtpCurrentTimeSource_Object = MibScalar
ntpCurrentTimeSource = _NtpCurrentTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 2, 2),
    _NtpCurrentTimeSource_Type()
)
ntpCurrentTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpCurrentTimeSource.setStatus("current")
_NtpAssociation_ObjectIdentity = ObjectIdentity
ntpAssociation = _NtpAssociation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 3)
)
_NtpAssociationTable_Object = MibTable
ntpAssociationTable = _NtpAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    ntpAssociationTable.setStatus("current")
_NtpAssociationEntry_Object = MibTableRow
ntpAssociationEntry = _NtpAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 3, 1, 1)
)
ntpAssociationEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "ntpAssociationSource"),
)
if mibBuilder.loadTexts:
    ntpAssociationEntry.setStatus("current")


class _NtpAssociationSource_Type(IetfInetTypesIpv4AddressNoZone):
    """Custom type ntpAssociationSource based on IetfInetTypesIpv4AddressNoZone"""
    subtypeSpec = IetfInetTypesIpv4AddressNoZone.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NtpAssociationSource_Type.__name__ = "IetfInetTypesIpv4AddressNoZone"
_NtpAssociationSource_Object = MibTableColumn
ntpAssociationSource = _NtpAssociationSource_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 3, 1, 1, 1),
    _NtpAssociationSource_Type()
)
ntpAssociationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationSource.setStatus("current")


class _NtpAssociationType_Type(Integer32):
    """Custom type ntpAssociationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntpServer", 1),
          ("ntpPeer", 2))
    )


_NtpAssociationType_Type.__name__ = "Integer32"
_NtpAssociationType_Object = MibTableColumn
ntpAssociationType = _NtpAssociationType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 3, 1, 1, 2),
    _NtpAssociationType_Type()
)
ntpAssociationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationType.setStatus("current")
_NtpAssociationPreferredNtpAssociation_Type = TruthValue
_NtpAssociationPreferredNtpAssociation_Object = MibTableColumn
ntpAssociationPreferredNtpAssociation = _NtpAssociationPreferredNtpAssociation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 3, 1, 1, 3),
    _NtpAssociationPreferredNtpAssociation_Type()
)
ntpAssociationPreferredNtpAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationPreferredNtpAssociation.setStatus("current")


class _NtpAssociationNtpAdminState_Type(Integer32):
    """Custom type ntpAssociationNtpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_NtpAssociationNtpAdminState_Type.__name__ = "Integer32"
_NtpAssociationNtpAdminState_Object = MibTableColumn
ntpAssociationNtpAdminState = _NtpAssociationNtpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 3, 1, 1, 4),
    _NtpAssociationNtpAdminState_Type()
)
ntpAssociationNtpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationNtpAdminState.setStatus("current")
_NtpAssociationStatus_ObjectIdentity = ObjectIdentity
ntpAssociationStatus = _NtpAssociationStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4)
)
_NtpAssociationStatusTable_Object = MibTable
ntpAssociationStatusTable = _NtpAssociationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1)
)
if mibBuilder.loadTexts:
    ntpAssociationStatusTable.setStatus("current")
_NtpAssociationStatusEntry_Object = MibTableRow
ntpAssociationStatusEntry = _NtpAssociationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1)
)
ntpAssociationStatusEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "ntpAssociationSource"),
)
if mibBuilder.loadTexts:
    ntpAssociationStatusEntry.setStatus("current")


class _NtpAssociationStatusNtpAssociationRefid_Type(OctetString):
    """Custom type ntpAssociationStatusNtpAssociationRefid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NtpAssociationStatusNtpAssociationRefid_Type.__name__ = "OctetString"
_NtpAssociationStatusNtpAssociationRefid_Object = MibTableColumn
ntpAssociationStatusNtpAssociationRefid = _NtpAssociationStatusNtpAssociationRefid_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 1),
    _NtpAssociationStatusNtpAssociationRefid_Type()
)
ntpAssociationStatusNtpAssociationRefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpAssociationRefid.setStatus("current")
_NtpAssociationStatusNtpStratum_Type = Unsigned32
_NtpAssociationStatusNtpStratum_Object = MibTableColumn
ntpAssociationStatusNtpStratum = _NtpAssociationStatusNtpStratum_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 2),
    _NtpAssociationStatusNtpStratum_Type()
)
ntpAssociationStatusNtpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpStratum.setStatus("current")
_NtpAssociationStatusNtpPollingInterval_Type = Unsigned32
_NtpAssociationStatusNtpPollingInterval_Object = MibTableColumn
ntpAssociationStatusNtpPollingInterval = _NtpAssociationStatusNtpPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 3),
    _NtpAssociationStatusNtpPollingInterval_Type()
)
ntpAssociationStatusNtpPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpPollingInterval.setStatus("current")
_NtpAssociationStatusNtpPrecision_Type = OctetString
_NtpAssociationStatusNtpPrecision_Object = MibTableColumn
ntpAssociationStatusNtpPrecision = _NtpAssociationStatusNtpPrecision_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 4),
    _NtpAssociationStatusNtpPrecision_Type()
)
ntpAssociationStatusNtpPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpPrecision.setStatus("current")
_NtpAssociationStatusNtpAssociationOffset_Type = OctetString
_NtpAssociationStatusNtpAssociationOffset_Object = MibTableColumn
ntpAssociationStatusNtpAssociationOffset = _NtpAssociationStatusNtpAssociationOffset_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 5),
    _NtpAssociationStatusNtpAssociationOffset_Type()
)
ntpAssociationStatusNtpAssociationOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpAssociationOffset.setStatus("current")
_NtpAssociationStatusNtpAssociationReach_Type = Unsigned32
_NtpAssociationStatusNtpAssociationReach_Object = MibTableColumn
ntpAssociationStatusNtpAssociationReach = _NtpAssociationStatusNtpAssociationReach_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 6),
    _NtpAssociationStatusNtpAssociationReach_Type()
)
ntpAssociationStatusNtpAssociationReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpAssociationReach.setStatus("current")
_NtpAssociationStatusNtpAssociationDelay_Type = OctetString
_NtpAssociationStatusNtpAssociationDelay_Object = MibTableColumn
ntpAssociationStatusNtpAssociationDelay = _NtpAssociationStatusNtpAssociationDelay_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 7),
    _NtpAssociationStatusNtpAssociationDelay_Type()
)
ntpAssociationStatusNtpAssociationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpAssociationDelay.setStatus("current")
_NtpAssociationStatusNtpAssociationDispersion_Type = OctetString
_NtpAssociationStatusNtpAssociationDispersion_Object = MibTableColumn
ntpAssociationStatusNtpAssociationDispersion = _NtpAssociationStatusNtpAssociationDispersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 10, 4, 1, 1, 8),
    _NtpAssociationStatusNtpAssociationDispersion_Type()
)
ntpAssociationStatusNtpAssociationDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationStatusNtpAssociationDispersion.setStatus("current")
_Ztc_ObjectIdentity = ObjectIdentity
ztc = _Ztc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 11)
)
_ZtcInfo_ObjectIdentity = ObjectIdentity
ztcInfo = _ZtcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 11, 1)
)
_ZtcEnabled_Type = TruthValue
_ZtcEnabled_Object = MibScalar
ztcEnabled = _ZtcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 11, 1, 1),
    _ZtcEnabled_Type()
)
ztcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztcEnabled.setStatus("current")


class _ZtcStatus_Type(Integer32):
    """Custom type ztcStatus based on Integer32"""
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
        *(("disabled", 0),
          ("ready", 1),
          ("ongoing", 2),
          ("failed", 3),
          ("done", 4))
    )


_ZtcStatus_Type.__name__ = "Integer32"
_ZtcStatus_Object = MibScalar
ztcStatus = _ZtcStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 11, 1, 2),
    _ZtcStatus_Type()
)
ztcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztcStatus.setStatus("current")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13)
)
_BitErrorRatePreFec_ObjectIdentity = ObjectIdentity
bitErrorRatePreFec = _BitErrorRatePreFec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 1)
)
_BitErrorRatePreFecTable_Object = MibTable
bitErrorRatePreFecTable = _BitErrorRatePreFecTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    bitErrorRatePreFecTable.setStatus("current")
_BitErrorRatePreFecEntry_Object = MibTableRow
bitErrorRatePreFecEntry = _BitErrorRatePreFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 1, 1, 1)
)
bitErrorRatePreFecEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    bitErrorRatePreFecEntry.setStatus("current")
_BitErrorRatePreFecInstant_Type = OctetString
_BitErrorRatePreFecInstant_Object = MibTableColumn
bitErrorRatePreFecInstant = _BitErrorRatePreFecInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 1, 1, 1, 1),
    _BitErrorRatePreFecInstant_Type()
)
bitErrorRatePreFecInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePreFecInstant.setStatus("current")
_BitErrorRatePreFecAvg_Type = OctetString
_BitErrorRatePreFecAvg_Object = MibTableColumn
bitErrorRatePreFecAvg = _BitErrorRatePreFecAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 1, 1, 1, 2),
    _BitErrorRatePreFecAvg_Type()
)
bitErrorRatePreFecAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePreFecAvg.setStatus("current")
_BitErrorRatePreFecMin_Type = OctetString
_BitErrorRatePreFecMin_Object = MibTableColumn
bitErrorRatePreFecMin = _BitErrorRatePreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 1, 1, 1, 3),
    _BitErrorRatePreFecMin_Type()
)
bitErrorRatePreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePreFecMin.setStatus("current")
_BitErrorRatePreFecMax_Type = OctetString
_BitErrorRatePreFecMax_Object = MibTableColumn
bitErrorRatePreFecMax = _BitErrorRatePreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 1, 1, 1, 4),
    _BitErrorRatePreFecMax_Type()
)
bitErrorRatePreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePreFecMax.setStatus("current")
_BitErrorRatePostFec_ObjectIdentity = ObjectIdentity
bitErrorRatePostFec = _BitErrorRatePostFec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 2)
)
_BitErrorRatePostFecTable_Object = MibTable
bitErrorRatePostFecTable = _BitErrorRatePostFecTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    bitErrorRatePostFecTable.setStatus("current")
_BitErrorRatePostFecEntry_Object = MibTableRow
bitErrorRatePostFecEntry = _BitErrorRatePostFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 2, 1, 1)
)
bitErrorRatePostFecEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    bitErrorRatePostFecEntry.setStatus("current")
_BitErrorRatePostFecInstant_Type = OctetString
_BitErrorRatePostFecInstant_Object = MibTableColumn
bitErrorRatePostFecInstant = _BitErrorRatePostFecInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 2, 1, 1, 1),
    _BitErrorRatePostFecInstant_Type()
)
bitErrorRatePostFecInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePostFecInstant.setStatus("current")
_BitErrorRatePostFecAvg_Type = OctetString
_BitErrorRatePostFecAvg_Object = MibTableColumn
bitErrorRatePostFecAvg = _BitErrorRatePostFecAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 2, 1, 1, 2),
    _BitErrorRatePostFecAvg_Type()
)
bitErrorRatePostFecAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePostFecAvg.setStatus("current")
_BitErrorRatePostFecMin_Type = OctetString
_BitErrorRatePostFecMin_Object = MibTableColumn
bitErrorRatePostFecMin = _BitErrorRatePostFecMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 2, 1, 1, 3),
    _BitErrorRatePostFecMin_Type()
)
bitErrorRatePostFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePostFecMin.setStatus("current")
_BitErrorRatePostFecMax_Type = OctetString
_BitErrorRatePostFecMax_Object = MibTableColumn
bitErrorRatePostFecMax = _BitErrorRatePostFecMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 2, 1, 1, 4),
    _BitErrorRatePostFecMax_Type()
)
bitErrorRatePostFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorRatePostFecMax.setStatus("current")
_InUtilization_ObjectIdentity = ObjectIdentity
inUtilization = _InUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 3)
)
_InUtilizationTable_Object = MibTable
inUtilizationTable = _InUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 3, 1)
)
if mibBuilder.loadTexts:
    inUtilizationTable.setStatus("current")
_InUtilizationEntry_Object = MibTableRow
inUtilizationEntry = _InUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 3, 1, 1)
)
inUtilizationEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    inUtilizationEntry.setStatus("current")
_InUtilizationInstant_Type = CoriantTypesPercentage
_InUtilizationInstant_Object = MibTableColumn
inUtilizationInstant = _InUtilizationInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 3, 1, 1, 1),
    _InUtilizationInstant_Type()
)
inUtilizationInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUtilizationInstant.setStatus("current")
_InUtilizationAvg_Type = CoriantTypesPercentage
_InUtilizationAvg_Object = MibTableColumn
inUtilizationAvg = _InUtilizationAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 3, 1, 1, 2),
    _InUtilizationAvg_Type()
)
inUtilizationAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUtilizationAvg.setStatus("current")
_InUtilizationMin_Type = CoriantTypesPercentage
_InUtilizationMin_Object = MibTableColumn
inUtilizationMin = _InUtilizationMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 3, 1, 1, 3),
    _InUtilizationMin_Type()
)
inUtilizationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUtilizationMin.setStatus("current")
_InUtilizationMax_Type = CoriantTypesPercentage
_InUtilizationMax_Object = MibTableColumn
inUtilizationMax = _InUtilizationMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 3, 1, 1, 4),
    _InUtilizationMax_Type()
)
inUtilizationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUtilizationMax.setStatus("current")
_OutUtilization_ObjectIdentity = ObjectIdentity
outUtilization = _OutUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 4)
)
_OutUtilizationTable_Object = MibTable
outUtilizationTable = _OutUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 4, 1)
)
if mibBuilder.loadTexts:
    outUtilizationTable.setStatus("current")
_OutUtilizationEntry_Object = MibTableRow
outUtilizationEntry = _OutUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 4, 1, 1)
)
outUtilizationEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
)
if mibBuilder.loadTexts:
    outUtilizationEntry.setStatus("current")
_OutUtilizationInstant_Type = CoriantTypesPercentage
_OutUtilizationInstant_Object = MibTableColumn
outUtilizationInstant = _OutUtilizationInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 4, 1, 1, 1),
    _OutUtilizationInstant_Type()
)
outUtilizationInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outUtilizationInstant.setStatus("current")
_OutUtilizationAvg_Type = CoriantTypesPercentage
_OutUtilizationAvg_Object = MibTableColumn
outUtilizationAvg = _OutUtilizationAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 4, 1, 1, 2),
    _OutUtilizationAvg_Type()
)
outUtilizationAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outUtilizationAvg.setStatus("current")
_OutUtilizationMin_Type = CoriantTypesPercentage
_OutUtilizationMin_Object = MibTableColumn
outUtilizationMin = _OutUtilizationMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 4, 1, 1, 3),
    _OutUtilizationMin_Type()
)
outUtilizationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outUtilizationMin.setStatus("current")
_OutUtilizationMax_Type = CoriantTypesPercentage
_OutUtilizationMax_Object = MibTableColumn
outUtilizationMax = _OutUtilizationMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 4, 1, 1, 4),
    _OutUtilizationMax_Type()
)
outUtilizationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outUtilizationMax.setStatus("current")
_OduDelay_ObjectIdentity = ObjectIdentity
oduDelay = _OduDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 23)
)
_OduDelayTable_Object = MibTable
oduDelayTable = _OduDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 23, 1)
)
if mibBuilder.loadTexts:
    oduDelayTable.setStatus("current")
_OduDelayEntry_Object = MibTableRow
oduDelayEntry = _OduDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 23, 1, 1)
)
oduDelayEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL1"),
    (0, "CORIANT-GROOVE-MIB", "oduidL1"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL2"),
    (0, "CORIANT-GROOVE-MIB", "oduidL2"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL3"),
    (0, "CORIANT-GROOVE-MIB", "oduidL3"),
    (0, "CORIANT-GROOVE-MIB", "odutypeL4"),
    (0, "CORIANT-GROOVE-MIB", "oduidL4"),
)
if mibBuilder.loadTexts:
    oduDelayEntry.setStatus("current")
_OduDelayInstant_Type = OctetString
_OduDelayInstant_Object = MibTableColumn
oduDelayInstant = _OduDelayInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 23, 1, 1, 1),
    _OduDelayInstant_Type()
)
oduDelayInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduDelayInstant.setStatus("current")
_OduDelayAvg_Type = OctetString
_OduDelayAvg_Object = MibTableColumn
oduDelayAvg = _OduDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 23, 1, 1, 2),
    _OduDelayAvg_Type()
)
oduDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduDelayAvg.setStatus("current")
_OduDelayMin_Type = OctetString
_OduDelayMin_Object = MibTableColumn
oduDelayMin = _OduDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 23, 1, 1, 3),
    _OduDelayMin_Type()
)
oduDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduDelayMin.setStatus("current")
_OduDelayMax_Type = OctetString
_OduDelayMax_Object = MibTableColumn
oduDelayMax = _OduDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 23, 1, 1, 4),
    _OduDelayMax_Type()
)
oduDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduDelayMax.setStatus("current")
_InOpticalPower_ObjectIdentity = ObjectIdentity
inOpticalPower = _InOpticalPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 24)
)
_InOpticalPowerTable_Object = MibTable
inOpticalPowerTable = _InOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 24, 1)
)
if mibBuilder.loadTexts:
    inOpticalPowerTable.setStatus("current")
_InOpticalPowerEntry_Object = MibTableRow
inOpticalPowerEntry = _InOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 24, 1, 1)
)
inOpticalPowerEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "omsName"),
    (0, "CORIANT-GROOVE-MIB", "oscName"),
    (0, "CORIANT-GROOVE-MIB", "goptName"),
)
if mibBuilder.loadTexts:
    inOpticalPowerEntry.setStatus("current")
_InOpticalPowerInstant_Type = CoriantTypesOpticalPower
_InOpticalPowerInstant_Object = MibTableColumn
inOpticalPowerInstant = _InOpticalPowerInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 24, 1, 1, 1),
    _InOpticalPowerInstant_Type()
)
inOpticalPowerInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerInstant.setStatus("current")
_InOpticalPowerAvg_Type = CoriantTypesOpticalPower
_InOpticalPowerAvg_Object = MibTableColumn
inOpticalPowerAvg = _InOpticalPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 24, 1, 1, 2),
    _InOpticalPowerAvg_Type()
)
inOpticalPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerAvg.setStatus("current")
_InOpticalPowerMin_Type = CoriantTypesOpticalPower
_InOpticalPowerMin_Object = MibTableColumn
inOpticalPowerMin = _InOpticalPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 24, 1, 1, 3),
    _InOpticalPowerMin_Type()
)
inOpticalPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerMin.setStatus("current")
_InOpticalPowerMax_Type = CoriantTypesOpticalPower
_InOpticalPowerMax_Object = MibTableColumn
inOpticalPowerMax = _InOpticalPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 24, 1, 1, 4),
    _InOpticalPowerMax_Type()
)
inOpticalPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerMax.setStatus("current")
_OutOpticalPower_ObjectIdentity = ObjectIdentity
outOpticalPower = _OutOpticalPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 25)
)
_OutOpticalPowerTable_Object = MibTable
outOpticalPowerTable = _OutOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 25, 1)
)
if mibBuilder.loadTexts:
    outOpticalPowerTable.setStatus("current")
_OutOpticalPowerEntry_Object = MibTableRow
outOpticalPowerEntry = _OutOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 25, 1, 1)
)
outOpticalPowerEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
    (0, "CORIANT-GROOVE-MIB", "subportId"),
    (0, "CORIANT-GROOVE-MIB", "omsName"),
    (0, "CORIANT-GROOVE-MIB", "oscName"),
    (0, "CORIANT-GROOVE-MIB", "goptName"),
)
if mibBuilder.loadTexts:
    outOpticalPowerEntry.setStatus("current")
_OutOpticalPowerInstant_Type = CoriantTypesOpticalPower
_OutOpticalPowerInstant_Object = MibTableColumn
outOpticalPowerInstant = _OutOpticalPowerInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 25, 1, 1, 1),
    _OutOpticalPowerInstant_Type()
)
outOpticalPowerInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerInstant.setStatus("current")
_OutOpticalPowerAvg_Type = CoriantTypesOpticalPower
_OutOpticalPowerAvg_Object = MibTableColumn
outOpticalPowerAvg = _OutOpticalPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 25, 1, 1, 2),
    _OutOpticalPowerAvg_Type()
)
outOpticalPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerAvg.setStatus("current")
_OutOpticalPowerMin_Type = CoriantTypesOpticalPower
_OutOpticalPowerMin_Object = MibTableColumn
outOpticalPowerMin = _OutOpticalPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 25, 1, 1, 3),
    _OutOpticalPowerMin_Type()
)
outOpticalPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerMin.setStatus("current")
_OutOpticalPowerMax_Type = CoriantTypesOpticalPower
_OutOpticalPowerMax_Object = MibTableColumn
outOpticalPowerMax = _OutOpticalPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 25, 1, 1, 4),
    _OutOpticalPowerMax_Type()
)
outOpticalPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerMax.setStatus("current")
_DifferentialGroupDelay_ObjectIdentity = ObjectIdentity
differentialGroupDelay = _DifferentialGroupDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 26)
)
_DifferentialGroupDelayTable_Object = MibTable
differentialGroupDelayTable = _DifferentialGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 26, 1)
)
if mibBuilder.loadTexts:
    differentialGroupDelayTable.setStatus("current")
_DifferentialGroupDelayEntry_Object = MibTableRow
differentialGroupDelayEntry = _DifferentialGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 26, 1, 1)
)
differentialGroupDelayEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    differentialGroupDelayEntry.setStatus("current")
_DifferentialGroupDelayInstant_Type = Unsigned32
_DifferentialGroupDelayInstant_Object = MibTableColumn
differentialGroupDelayInstant = _DifferentialGroupDelayInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 26, 1, 1, 1),
    _DifferentialGroupDelayInstant_Type()
)
differentialGroupDelayInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    differentialGroupDelayInstant.setStatus("current")
_DifferentialGroupDelayAvg_Type = Unsigned32
_DifferentialGroupDelayAvg_Object = MibTableColumn
differentialGroupDelayAvg = _DifferentialGroupDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 26, 1, 1, 2),
    _DifferentialGroupDelayAvg_Type()
)
differentialGroupDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    differentialGroupDelayAvg.setStatus("current")
_DifferentialGroupDelayMin_Type = Unsigned32
_DifferentialGroupDelayMin_Object = MibTableColumn
differentialGroupDelayMin = _DifferentialGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 26, 1, 1, 3),
    _DifferentialGroupDelayMin_Type()
)
differentialGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    differentialGroupDelayMin.setStatus("current")
_DifferentialGroupDelayMax_Type = Unsigned32
_DifferentialGroupDelayMax_Object = MibTableColumn
differentialGroupDelayMax = _DifferentialGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 26, 1, 1, 4),
    _DifferentialGroupDelayMax_Type()
)
differentialGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    differentialGroupDelayMax.setStatus("current")
_ChromaticDispersion_ObjectIdentity = ObjectIdentity
chromaticDispersion = _ChromaticDispersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 27)
)
_ChromaticDispersionTable_Object = MibTable
chromaticDispersionTable = _ChromaticDispersionTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 27, 1)
)
if mibBuilder.loadTexts:
    chromaticDispersionTable.setStatus("current")
_ChromaticDispersionEntry_Object = MibTableRow
chromaticDispersionEntry = _ChromaticDispersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 27, 1, 1)
)
chromaticDispersionEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    chromaticDispersionEntry.setStatus("current")
_ChromaticDispersionInstant_Type = Integer32
_ChromaticDispersionInstant_Object = MibTableColumn
chromaticDispersionInstant = _ChromaticDispersionInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 27, 1, 1, 1),
    _ChromaticDispersionInstant_Type()
)
chromaticDispersionInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chromaticDispersionInstant.setStatus("current")
_ChromaticDispersionAvg_Type = Integer32
_ChromaticDispersionAvg_Object = MibTableColumn
chromaticDispersionAvg = _ChromaticDispersionAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 27, 1, 1, 2),
    _ChromaticDispersionAvg_Type()
)
chromaticDispersionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chromaticDispersionAvg.setStatus("current")
_ChromaticDispersionMin_Type = Integer32
_ChromaticDispersionMin_Object = MibTableColumn
chromaticDispersionMin = _ChromaticDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 27, 1, 1, 3),
    _ChromaticDispersionMin_Type()
)
chromaticDispersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chromaticDispersionMin.setStatus("current")
_ChromaticDispersionMax_Type = Integer32
_ChromaticDispersionMax_Object = MibTableColumn
chromaticDispersionMax = _ChromaticDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 27, 1, 1, 4),
    _ChromaticDispersionMax_Type()
)
chromaticDispersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chromaticDispersionMax.setStatus("current")
_Osnr_ObjectIdentity = ObjectIdentity
osnr = _Osnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 28)
)
_OsnrTable_Object = MibTable
osnrTable = _OsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 28, 1)
)
if mibBuilder.loadTexts:
    osnrTable.setStatus("current")
_OsnrEntry_Object = MibTableRow
osnrEntry = _OsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 28, 1, 1)
)
osnrEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    osnrEntry.setStatus("current")
_OsnrInstant_Type = CoriantTypesDBPrecision1
_OsnrInstant_Object = MibTableColumn
osnrInstant = _OsnrInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 28, 1, 1, 1),
    _OsnrInstant_Type()
)
osnrInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnrInstant.setStatus("current")
_OsnrAvg_Type = CoriantTypesDBPrecision1
_OsnrAvg_Object = MibTableColumn
osnrAvg = _OsnrAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 28, 1, 1, 2),
    _OsnrAvg_Type()
)
osnrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnrAvg.setStatus("current")
_OsnrMin_Type = CoriantTypesDBPrecision1
_OsnrMin_Object = MibTableColumn
osnrMin = _OsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 28, 1, 1, 3),
    _OsnrMin_Type()
)
osnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnrMin.setStatus("current")
_OsnrMax_Type = CoriantTypesDBPrecision1
_OsnrMax_Object = MibTableColumn
osnrMax = _OsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 28, 1, 1, 4),
    _OsnrMax_Type()
)
osnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnrMax.setStatus("current")
_QFactor_ObjectIdentity = ObjectIdentity
qFactor = _QFactor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 29)
)
_QFactorTable_Object = MibTable
qFactorTable = _QFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 29, 1)
)
if mibBuilder.loadTexts:
    qFactorTable.setStatus("current")
_QFactorEntry_Object = MibTableRow
qFactorEntry = _QFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 29, 1, 1)
)
qFactorEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    qFactorEntry.setStatus("current")
_QFactorInstant_Type = CoriantTypesDBPrecision1
_QFactorInstant_Object = MibTableColumn
qFactorInstant = _QFactorInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 29, 1, 1, 1),
    _QFactorInstant_Type()
)
qFactorInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qFactorInstant.setStatus("current")
_QFactorAvg_Type = CoriantTypesDBPrecision1
_QFactorAvg_Object = MibTableColumn
qFactorAvg = _QFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 29, 1, 1, 2),
    _QFactorAvg_Type()
)
qFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qFactorAvg.setStatus("current")
_QFactorMin_Type = CoriantTypesDBPrecision1
_QFactorMin_Object = MibTableColumn
qFactorMin = _QFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 29, 1, 1, 3),
    _QFactorMin_Type()
)
qFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qFactorMin.setStatus("current")
_QFactorMax_Type = CoriantTypesDBPrecision1
_QFactorMax_Object = MibTableColumn
qFactorMax = _QFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 29, 1, 1, 4),
    _QFactorMax_Type()
)
qFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qFactorMax.setStatus("current")
_PolarizationDependentLoss_ObjectIdentity = ObjectIdentity
polarizationDependentLoss = _PolarizationDependentLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 30)
)
_PolarizationDependentLossTable_Object = MibTable
polarizationDependentLossTable = _PolarizationDependentLossTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 30, 1)
)
if mibBuilder.loadTexts:
    polarizationDependentLossTable.setStatus("current")
_PolarizationDependentLossEntry_Object = MibTableRow
polarizationDependentLossEntry = _PolarizationDependentLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 30, 1, 1)
)
polarizationDependentLossEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    polarizationDependentLossEntry.setStatus("current")
_PolarizationDependentLossInstant_Type = CoriantTypesDBPrecision1
_PolarizationDependentLossInstant_Object = MibTableColumn
polarizationDependentLossInstant = _PolarizationDependentLossInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 30, 1, 1, 1),
    _PolarizationDependentLossInstant_Type()
)
polarizationDependentLossInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polarizationDependentLossInstant.setStatus("current")
_PolarizationDependentLossAvg_Type = CoriantTypesDBPrecision1
_PolarizationDependentLossAvg_Object = MibTableColumn
polarizationDependentLossAvg = _PolarizationDependentLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 30, 1, 1, 2),
    _PolarizationDependentLossAvg_Type()
)
polarizationDependentLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polarizationDependentLossAvg.setStatus("current")
_PolarizationDependentLossMin_Type = CoriantTypesDBPrecision1
_PolarizationDependentLossMin_Object = MibTableColumn
polarizationDependentLossMin = _PolarizationDependentLossMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 30, 1, 1, 3),
    _PolarizationDependentLossMin_Type()
)
polarizationDependentLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polarizationDependentLossMin.setStatus("current")
_PolarizationDependentLossMax_Type = CoriantTypesDBPrecision1
_PolarizationDependentLossMax_Object = MibTableColumn
polarizationDependentLossMax = _PolarizationDependentLossMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 30, 1, 1, 4),
    _PolarizationDependentLossMax_Type()
)
polarizationDependentLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polarizationDependentLossMax.setStatus("current")
_InOpticalFrequency_ObjectIdentity = ObjectIdentity
inOpticalFrequency = _InOpticalFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 31)
)
_InOpticalFrequencyTable_Object = MibTable
inOpticalFrequencyTable = _InOpticalFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 31, 1)
)
if mibBuilder.loadTexts:
    inOpticalFrequencyTable.setStatus("current")
_InOpticalFrequencyEntry_Object = MibTableRow
inOpticalFrequencyEntry = _InOpticalFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 31, 1, 1)
)
inOpticalFrequencyEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    inOpticalFrequencyEntry.setStatus("current")
_InOpticalFrequencyInstant_Type = Unsigned32
_InOpticalFrequencyInstant_Object = MibTableColumn
inOpticalFrequencyInstant = _InOpticalFrequencyInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 31, 1, 1, 1),
    _InOpticalFrequencyInstant_Type()
)
inOpticalFrequencyInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalFrequencyInstant.setStatus("current")
_InOpticalFrequencyAvg_Type = Unsigned32
_InOpticalFrequencyAvg_Object = MibTableColumn
inOpticalFrequencyAvg = _InOpticalFrequencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 31, 1, 1, 2),
    _InOpticalFrequencyAvg_Type()
)
inOpticalFrequencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalFrequencyAvg.setStatus("current")
_InOpticalFrequencyMin_Type = Unsigned32
_InOpticalFrequencyMin_Object = MibTableColumn
inOpticalFrequencyMin = _InOpticalFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 31, 1, 1, 3),
    _InOpticalFrequencyMin_Type()
)
inOpticalFrequencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalFrequencyMin.setStatus("current")
_InOpticalFrequencyMax_Type = Unsigned32
_InOpticalFrequencyMax_Object = MibTableColumn
inOpticalFrequencyMax = _InOpticalFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 31, 1, 1, 4),
    _InOpticalFrequencyMax_Type()
)
inOpticalFrequencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalFrequencyMax.setStatus("current")
_OutOpticalFrequency_ObjectIdentity = ObjectIdentity
outOpticalFrequency = _OutOpticalFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 32)
)
_OutOpticalFrequencyTable_Object = MibTable
outOpticalFrequencyTable = _OutOpticalFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 32, 1)
)
if mibBuilder.loadTexts:
    outOpticalFrequencyTable.setStatus("current")
_OutOpticalFrequencyEntry_Object = MibTableRow
outOpticalFrequencyEntry = _OutOpticalFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 32, 1, 1)
)
outOpticalFrequencyEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    outOpticalFrequencyEntry.setStatus("current")
_OutOpticalFrequencyInstant_Type = Unsigned32
_OutOpticalFrequencyInstant_Object = MibTableColumn
outOpticalFrequencyInstant = _OutOpticalFrequencyInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 32, 1, 1, 1),
    _OutOpticalFrequencyInstant_Type()
)
outOpticalFrequencyInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalFrequencyInstant.setStatus("current")
_OutOpticalFrequencyAvg_Type = Unsigned32
_OutOpticalFrequencyAvg_Object = MibTableColumn
outOpticalFrequencyAvg = _OutOpticalFrequencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 32, 1, 1, 2),
    _OutOpticalFrequencyAvg_Type()
)
outOpticalFrequencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalFrequencyAvg.setStatus("current")
_OutOpticalFrequencyMin_Type = Unsigned32
_OutOpticalFrequencyMin_Object = MibTableColumn
outOpticalFrequencyMin = _OutOpticalFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 32, 1, 1, 3),
    _OutOpticalFrequencyMin_Type()
)
outOpticalFrequencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalFrequencyMin.setStatus("current")
_OutOpticalFrequencyMax_Type = Unsigned32
_OutOpticalFrequencyMax_Object = MibTableColumn
outOpticalFrequencyMax = _OutOpticalFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 32, 1, 1, 4),
    _OutOpticalFrequencyMax_Type()
)
outOpticalFrequencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalFrequencyMax.setStatus("current")
_InOpticalPowerLaneHigh_ObjectIdentity = ObjectIdentity
inOpticalPowerLaneHigh = _InOpticalPowerLaneHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 33)
)
_InOpticalPowerLaneHighTable_Object = MibTable
inOpticalPowerLaneHighTable = _InOpticalPowerLaneHighTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 33, 1)
)
if mibBuilder.loadTexts:
    inOpticalPowerLaneHighTable.setStatus("current")
_InOpticalPowerLaneHighEntry_Object = MibTableRow
inOpticalPowerLaneHighEntry = _InOpticalPowerLaneHighEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 33, 1, 1)
)
inOpticalPowerLaneHighEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    inOpticalPowerLaneHighEntry.setStatus("current")
_InOpticalPowerLaneHighInstant_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneHighInstant_Object = MibTableColumn
inOpticalPowerLaneHighInstant = _InOpticalPowerLaneHighInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 33, 1, 1, 1),
    _InOpticalPowerLaneHighInstant_Type()
)
inOpticalPowerLaneHighInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneHighInstant.setStatus("current")
_InOpticalPowerLaneHighAvg_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneHighAvg_Object = MibTableColumn
inOpticalPowerLaneHighAvg = _InOpticalPowerLaneHighAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 33, 1, 1, 2),
    _InOpticalPowerLaneHighAvg_Type()
)
inOpticalPowerLaneHighAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneHighAvg.setStatus("current")
_InOpticalPowerLaneHighMin_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneHighMin_Object = MibTableColumn
inOpticalPowerLaneHighMin = _InOpticalPowerLaneHighMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 33, 1, 1, 3),
    _InOpticalPowerLaneHighMin_Type()
)
inOpticalPowerLaneHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneHighMin.setStatus("current")
_InOpticalPowerLaneHighMax_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneHighMax_Object = MibTableColumn
inOpticalPowerLaneHighMax = _InOpticalPowerLaneHighMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 33, 1, 1, 4),
    _InOpticalPowerLaneHighMax_Type()
)
inOpticalPowerLaneHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneHighMax.setStatus("current")
_InOpticalPowerLaneLow_ObjectIdentity = ObjectIdentity
inOpticalPowerLaneLow = _InOpticalPowerLaneLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 34)
)
_InOpticalPowerLaneLowTable_Object = MibTable
inOpticalPowerLaneLowTable = _InOpticalPowerLaneLowTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 34, 1)
)
if mibBuilder.loadTexts:
    inOpticalPowerLaneLowTable.setStatus("current")
_InOpticalPowerLaneLowEntry_Object = MibTableRow
inOpticalPowerLaneLowEntry = _InOpticalPowerLaneLowEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 34, 1, 1)
)
inOpticalPowerLaneLowEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    inOpticalPowerLaneLowEntry.setStatus("current")
_InOpticalPowerLaneLowInstant_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneLowInstant_Object = MibTableColumn
inOpticalPowerLaneLowInstant = _InOpticalPowerLaneLowInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 34, 1, 1, 1),
    _InOpticalPowerLaneLowInstant_Type()
)
inOpticalPowerLaneLowInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneLowInstant.setStatus("current")
_InOpticalPowerLaneLowAvg_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneLowAvg_Object = MibTableColumn
inOpticalPowerLaneLowAvg = _InOpticalPowerLaneLowAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 34, 1, 1, 2),
    _InOpticalPowerLaneLowAvg_Type()
)
inOpticalPowerLaneLowAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneLowAvg.setStatus("current")
_InOpticalPowerLaneLowMin_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneLowMin_Object = MibTableColumn
inOpticalPowerLaneLowMin = _InOpticalPowerLaneLowMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 34, 1, 1, 3),
    _InOpticalPowerLaneLowMin_Type()
)
inOpticalPowerLaneLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneLowMin.setStatus("current")
_InOpticalPowerLaneLowMax_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneLowMax_Object = MibTableColumn
inOpticalPowerLaneLowMax = _InOpticalPowerLaneLowMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 34, 1, 1, 4),
    _InOpticalPowerLaneLowMax_Type()
)
inOpticalPowerLaneLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneLowMax.setStatus("current")
_InOpticalPowerLaneTotal_ObjectIdentity = ObjectIdentity
inOpticalPowerLaneTotal = _InOpticalPowerLaneTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 35)
)
_InOpticalPowerLaneTotalTable_Object = MibTable
inOpticalPowerLaneTotalTable = _InOpticalPowerLaneTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 35, 1)
)
if mibBuilder.loadTexts:
    inOpticalPowerLaneTotalTable.setStatus("current")
_InOpticalPowerLaneTotalEntry_Object = MibTableRow
inOpticalPowerLaneTotalEntry = _InOpticalPowerLaneTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 35, 1, 1)
)
inOpticalPowerLaneTotalEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    inOpticalPowerLaneTotalEntry.setStatus("current")
_InOpticalPowerLaneTotalInstant_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneTotalInstant_Object = MibTableColumn
inOpticalPowerLaneTotalInstant = _InOpticalPowerLaneTotalInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 35, 1, 1, 1),
    _InOpticalPowerLaneTotalInstant_Type()
)
inOpticalPowerLaneTotalInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneTotalInstant.setStatus("current")
_InOpticalPowerLaneTotalAvg_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneTotalAvg_Object = MibTableColumn
inOpticalPowerLaneTotalAvg = _InOpticalPowerLaneTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 35, 1, 1, 2),
    _InOpticalPowerLaneTotalAvg_Type()
)
inOpticalPowerLaneTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneTotalAvg.setStatus("current")
_InOpticalPowerLaneTotalMin_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneTotalMin_Object = MibTableColumn
inOpticalPowerLaneTotalMin = _InOpticalPowerLaneTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 35, 1, 1, 3),
    _InOpticalPowerLaneTotalMin_Type()
)
inOpticalPowerLaneTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneTotalMin.setStatus("current")
_InOpticalPowerLaneTotalMax_Type = CoriantTypesOpticalPower
_InOpticalPowerLaneTotalMax_Object = MibTableColumn
inOpticalPowerLaneTotalMax = _InOpticalPowerLaneTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 35, 1, 1, 4),
    _InOpticalPowerLaneTotalMax_Type()
)
inOpticalPowerLaneTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inOpticalPowerLaneTotalMax.setStatus("current")
_OutOpticalPowerLaneHigh_ObjectIdentity = ObjectIdentity
outOpticalPowerLaneHigh = _OutOpticalPowerLaneHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 36)
)
_OutOpticalPowerLaneHighTable_Object = MibTable
outOpticalPowerLaneHighTable = _OutOpticalPowerLaneHighTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 36, 1)
)
if mibBuilder.loadTexts:
    outOpticalPowerLaneHighTable.setStatus("current")
_OutOpticalPowerLaneHighEntry_Object = MibTableRow
outOpticalPowerLaneHighEntry = _OutOpticalPowerLaneHighEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 36, 1, 1)
)
outOpticalPowerLaneHighEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    outOpticalPowerLaneHighEntry.setStatus("current")
_OutOpticalPowerLaneHighInstant_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneHighInstant_Object = MibTableColumn
outOpticalPowerLaneHighInstant = _OutOpticalPowerLaneHighInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 36, 1, 1, 1),
    _OutOpticalPowerLaneHighInstant_Type()
)
outOpticalPowerLaneHighInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneHighInstant.setStatus("current")
_OutOpticalPowerLaneHighAvg_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneHighAvg_Object = MibTableColumn
outOpticalPowerLaneHighAvg = _OutOpticalPowerLaneHighAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 36, 1, 1, 2),
    _OutOpticalPowerLaneHighAvg_Type()
)
outOpticalPowerLaneHighAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneHighAvg.setStatus("current")
_OutOpticalPowerLaneHighMin_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneHighMin_Object = MibTableColumn
outOpticalPowerLaneHighMin = _OutOpticalPowerLaneHighMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 36, 1, 1, 3),
    _OutOpticalPowerLaneHighMin_Type()
)
outOpticalPowerLaneHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneHighMin.setStatus("current")
_OutOpticalPowerLaneHighMax_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneHighMax_Object = MibTableColumn
outOpticalPowerLaneHighMax = _OutOpticalPowerLaneHighMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 36, 1, 1, 4),
    _OutOpticalPowerLaneHighMax_Type()
)
outOpticalPowerLaneHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneHighMax.setStatus("current")
_OutOpticalPowerLaneLow_ObjectIdentity = ObjectIdentity
outOpticalPowerLaneLow = _OutOpticalPowerLaneLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 37)
)
_OutOpticalPowerLaneLowTable_Object = MibTable
outOpticalPowerLaneLowTable = _OutOpticalPowerLaneLowTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 37, 1)
)
if mibBuilder.loadTexts:
    outOpticalPowerLaneLowTable.setStatus("current")
_OutOpticalPowerLaneLowEntry_Object = MibTableRow
outOpticalPowerLaneLowEntry = _OutOpticalPowerLaneLowEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 37, 1, 1)
)
outOpticalPowerLaneLowEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    outOpticalPowerLaneLowEntry.setStatus("current")
_OutOpticalPowerLaneLowInstant_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneLowInstant_Object = MibTableColumn
outOpticalPowerLaneLowInstant = _OutOpticalPowerLaneLowInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 37, 1, 1, 1),
    _OutOpticalPowerLaneLowInstant_Type()
)
outOpticalPowerLaneLowInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneLowInstant.setStatus("current")
_OutOpticalPowerLaneLowAvg_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneLowAvg_Object = MibTableColumn
outOpticalPowerLaneLowAvg = _OutOpticalPowerLaneLowAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 37, 1, 1, 2),
    _OutOpticalPowerLaneLowAvg_Type()
)
outOpticalPowerLaneLowAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneLowAvg.setStatus("current")
_OutOpticalPowerLaneLowMin_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneLowMin_Object = MibTableColumn
outOpticalPowerLaneLowMin = _OutOpticalPowerLaneLowMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 37, 1, 1, 3),
    _OutOpticalPowerLaneLowMin_Type()
)
outOpticalPowerLaneLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneLowMin.setStatus("current")
_OutOpticalPowerLaneLowMax_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneLowMax_Object = MibTableColumn
outOpticalPowerLaneLowMax = _OutOpticalPowerLaneLowMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 37, 1, 1, 4),
    _OutOpticalPowerLaneLowMax_Type()
)
outOpticalPowerLaneLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneLowMax.setStatus("current")
_OutOpticalPowerLaneTotal_ObjectIdentity = ObjectIdentity
outOpticalPowerLaneTotal = _OutOpticalPowerLaneTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 38)
)
_OutOpticalPowerLaneTotalTable_Object = MibTable
outOpticalPowerLaneTotalTable = _OutOpticalPowerLaneTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 38, 1)
)
if mibBuilder.loadTexts:
    outOpticalPowerLaneTotalTable.setStatus("current")
_OutOpticalPowerLaneTotalEntry_Object = MibTableRow
outOpticalPowerLaneTotalEntry = _OutOpticalPowerLaneTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 38, 1, 1)
)
outOpticalPowerLaneTotalEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
    (0, "CORIANT-GROOVE-MIB", "portId"),
)
if mibBuilder.loadTexts:
    outOpticalPowerLaneTotalEntry.setStatus("current")
_OutOpticalPowerLaneTotalInstant_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneTotalInstant_Object = MibTableColumn
outOpticalPowerLaneTotalInstant = _OutOpticalPowerLaneTotalInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 38, 1, 1, 1),
    _OutOpticalPowerLaneTotalInstant_Type()
)
outOpticalPowerLaneTotalInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneTotalInstant.setStatus("current")
_OutOpticalPowerLaneTotalAvg_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneTotalAvg_Object = MibTableColumn
outOpticalPowerLaneTotalAvg = _OutOpticalPowerLaneTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 38, 1, 1, 2),
    _OutOpticalPowerLaneTotalAvg_Type()
)
outOpticalPowerLaneTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneTotalAvg.setStatus("current")
_OutOpticalPowerLaneTotalMin_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneTotalMin_Object = MibTableColumn
outOpticalPowerLaneTotalMin = _OutOpticalPowerLaneTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 38, 1, 1, 3),
    _OutOpticalPowerLaneTotalMin_Type()
)
outOpticalPowerLaneTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneTotalMin.setStatus("current")
_OutOpticalPowerLaneTotalMax_Type = CoriantTypesOpticalPower
_OutOpticalPowerLaneTotalMax_Object = MibTableColumn
outOpticalPowerLaneTotalMax = _OutOpticalPowerLaneTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 38, 1, 1, 4),
    _OutOpticalPowerLaneTotalMax_Type()
)
outOpticalPowerLaneTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOpticalPowerLaneTotalMax.setStatus("current")
_ModuleTemperature_ObjectIdentity = ObjectIdentity
moduleTemperature = _ModuleTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 39)
)
_ModuleTemperatureTable_Object = MibTable
moduleTemperatureTable = _ModuleTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 39, 1)
)
if mibBuilder.loadTexts:
    moduleTemperatureTable.setStatus("current")
_ModuleTemperatureEntry_Object = MibTableRow
moduleTemperatureEntry = _ModuleTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 39, 1, 1)
)
moduleTemperatureEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
    (0, "CORIANT-GROOVE-MIB", "slotId"),
    (0, "CORIANT-GROOVE-MIB", "subslotId"),
)
if mibBuilder.loadTexts:
    moduleTemperatureEntry.setStatus("current")
_ModuleTemperatureInstant_Type = CoriantTypesTemperaturePrecision3
_ModuleTemperatureInstant_Object = MibTableColumn
moduleTemperatureInstant = _ModuleTemperatureInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 39, 1, 1, 1),
    _ModuleTemperatureInstant_Type()
)
moduleTemperatureInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperatureInstant.setStatus("current")
_ModuleTemperatureAvg_Type = CoriantTypesTemperaturePrecision3
_ModuleTemperatureAvg_Object = MibTableColumn
moduleTemperatureAvg = _ModuleTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 39, 1, 1, 2),
    _ModuleTemperatureAvg_Type()
)
moduleTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperatureAvg.setStatus("current")
_ModuleTemperatureMin_Type = CoriantTypesTemperaturePrecision3
_ModuleTemperatureMin_Object = MibTableColumn
moduleTemperatureMin = _ModuleTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 39, 1, 1, 3),
    _ModuleTemperatureMin_Type()
)
moduleTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperatureMin.setStatus("current")
_ModuleTemperatureMax_Type = CoriantTypesTemperaturePrecision3
_ModuleTemperatureMax_Object = MibTableColumn
moduleTemperatureMax = _ModuleTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 39, 1, 1, 4),
    _ModuleTemperatureMax_Type()
)
moduleTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperatureMax.setStatus("current")
_InletTemperature_ObjectIdentity = ObjectIdentity
inletTemperature = _InletTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 40)
)
_InletTemperatureTable_Object = MibTable
inletTemperatureTable = _InletTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 40, 1)
)
if mibBuilder.loadTexts:
    inletTemperatureTable.setStatus("current")
_InletTemperatureEntry_Object = MibTableRow
inletTemperatureEntry = _InletTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 40, 1, 1)
)
inletTemperatureEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
)
if mibBuilder.loadTexts:
    inletTemperatureEntry.setStatus("current")
_InletTemperatureInstant_Type = CoriantTypesTemperaturePrecision3
_InletTemperatureInstant_Object = MibTableColumn
inletTemperatureInstant = _InletTemperatureInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 40, 1, 1, 1),
    _InletTemperatureInstant_Type()
)
inletTemperatureInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletTemperatureInstant.setStatus("current")
_InletTemperatureAvg_Type = CoriantTypesTemperaturePrecision3
_InletTemperatureAvg_Object = MibTableColumn
inletTemperatureAvg = _InletTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 40, 1, 1, 2),
    _InletTemperatureAvg_Type()
)
inletTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletTemperatureAvg.setStatus("current")
_InletTemperatureMin_Type = CoriantTypesTemperaturePrecision3
_InletTemperatureMin_Object = MibTableColumn
inletTemperatureMin = _InletTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 40, 1, 1, 3),
    _InletTemperatureMin_Type()
)
inletTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletTemperatureMin.setStatus("current")
_InletTemperatureMax_Type = CoriantTypesTemperaturePrecision3
_InletTemperatureMax_Object = MibTableColumn
inletTemperatureMax = _InletTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 40, 1, 1, 4),
    _InletTemperatureMax_Type()
)
inletTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletTemperatureMax.setStatus("current")
_OutletTemperature_ObjectIdentity = ObjectIdentity
outletTemperature = _OutletTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 41)
)
_OutletTemperatureTable_Object = MibTable
outletTemperatureTable = _OutletTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 41, 1)
)
if mibBuilder.loadTexts:
    outletTemperatureTable.setStatus("current")
_OutletTemperatureEntry_Object = MibTableRow
outletTemperatureEntry = _OutletTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 41, 1, 1)
)
outletTemperatureEntry.setIndexNames(
    (0, "CORIANT-GROOVE-MIB", "shelfId"),
)
if mibBuilder.loadTexts:
    outletTemperatureEntry.setStatus("current")
_OutletTemperatureInstant_Type = CoriantTypesTemperaturePrecision3
_OutletTemperatureInstant_Object = MibTableColumn
outletTemperatureInstant = _OutletTemperatureInstant_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 41, 1, 1, 1),
    _OutletTemperatureInstant_Type()
)
outletTemperatureInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletTemperatureInstant.setStatus("current")
_OutletTemperatureAvg_Type = CoriantTypesTemperaturePrecision3
_OutletTemperatureAvg_Object = MibTableColumn
outletTemperatureAvg = _OutletTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 41, 1, 1, 2),
    _OutletTemperatureAvg_Type()
)
outletTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletTemperatureAvg.setStatus("current")
_OutletTemperatureMin_Type = CoriantTypesTemperaturePrecision3
_OutletTemperatureMin_Object = MibTableColumn
outletTemperatureMin = _OutletTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 41, 1, 1, 3),
    _OutletTemperatureMin_Type()
)
outletTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletTemperatureMin.setStatus("current")
_OutletTemperatureMax_Type = CoriantTypesTemperaturePrecision3
_OutletTemperatureMax_Object = MibTableColumn
outletTemperatureMax = _OutletTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 13, 41, 1, 1, 4),
    _OutletTemperatureMax_Type()
)
outletTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletTemperatureMax.setStatus("current")

# Managed Objects groups


# Notification objects

alarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 2, 1)
)
alarmNotification.setObjects(
      *(("CORIANT-GROOVE-MIB", "notificationFmEntity"),
        ("CORIANT-GROOVE-MIB", "notificationConditionType"),
        ("CORIANT-GROOVE-MIB", "notificationLocation"),
        ("CORIANT-GROOVE-MIB", "notificationDirection"),
        ("CORIANT-GROOVE-MIB", "notificationTimePeriod"),
        ("CORIANT-GROOVE-MIB", "notificationServiceAffect"),
        ("CORIANT-GROOVE-MIB", "notificationSeverityLevel"),
        ("CORIANT-GROOVE-MIB", "notificationOccurrenceDateTime"),
        ("CORIANT-GROOVE-MIB", "notificationConditionDescription"),
        ("CORIANT-GROOVE-MIB", "notificationFmEntityType"),
        ("CORIANT-GROOVE-MIB", "notificationAlarmConditionType"),
        ("CORIANT-GROOVE-MIB", "notificationLastSeverityLevel"),
        ("CORIANT-GROOVE-MIB", "notificationExtensionDescription"))
)
if mibBuilder.loadTexts:
    alarmNotification.setStatus(
        "current"
    )

notAlarmedEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 1, 2, 1, 2, 2)
)
notAlarmedEventNotification.setObjects(
      *(("CORIANT-GROOVE-MIB", "notificationFmEntity"),
        ("CORIANT-GROOVE-MIB", "notificationConditionType"),
        ("CORIANT-GROOVE-MIB", "notificationLocation"),
        ("CORIANT-GROOVE-MIB", "notificationDirection"),
        ("CORIANT-GROOVE-MIB", "notificationTimePeriod"),
        ("CORIANT-GROOVE-MIB", "notificationServiceAffect"),
        ("CORIANT-GROOVE-MIB", "notificationSeverityLevel"),
        ("CORIANT-GROOVE-MIB", "notificationOccurrenceDateTime"),
        ("CORIANT-GROOVE-MIB", "notificationConditionDescription"),
        ("CORIANT-GROOVE-MIB", "notificationFmEntityType"),
        ("CORIANT-GROOVE-MIB", "notificationAlarmConditionType"),
        ("CORIANT-GROOVE-MIB", "notificationLastSeverityLevel"),
        ("CORIANT-GROOVE-MIB", "notificationExtensionDescription"))
)
if mibBuilder.loadTexts:
    notAlarmedEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORIANT-GROOVE-MIB",
    **{"CoriantCommonOtnEncryStatusEnum": CoriantCommonOtnEncryStatusEnum,
       "CoriantCommonOtnKeySyncSession": CoriantCommonOtnKeySyncSession,
       "CoriantCommonpmThresholdValue": CoriantCommonpmThresholdValue,
       "CoriantCommonpmUnitOfValue": CoriantCommonpmUnitOfValue,
       "CoriantFileSwTypesDeviceFwVersion": CoriantFileSwTypesDeviceFwVersion,
       "CoriantFileSwTypesDeviceName": CoriantFileSwTypesDeviceName,
       "CoriantFileSwTypesSwVersion": CoriantFileSwTypesSwVersion,
       "CoriantFileSwTypesSwloadProduct": CoriantFileSwTypesSwloadProduct,
       "CoriantFileSwTypesSwloadVendor": CoriantFileSwTypesSwloadVendor,
       "CoriantFmtypesConditionType": CoriantFmtypesConditionType,
       "CoriantFmtypesEntityTypeFm": CoriantFmtypesEntityTypeFm,
       "CoriantFmtypesServiceAffectFm": CoriantFmtypesServiceAffectFm,
       "CoriantFmtypesSeverityLevel": CoriantFmtypesSeverityLevel,
       "CoriantPmtypesPmParameter": CoriantPmtypesPmParameter,
       "CoriantPmtypesPmpType": CoriantPmtypesPmpType,
       "CoriantPmtypesValidityType": CoriantPmtypesValidityType,
       "CoriantRpcConfigurableLedTypes": CoriantRpcConfigurableLedTypes,
       "CoriantTypesCardType": CoriantTypesCardType,
       "CoriantTypesCreationscope": CoriantTypesCreationscope,
       "CoriantTypesDBPrecision1": CoriantTypesDBPrecision1,
       "CoriantTypesDate": CoriantTypesDate,
       "CoriantTypesDecimalFract1": CoriantTypesDecimalFract1,
       "CoriantTypesDuplexMode": CoriantTypesDuplexMode,
       "CoriantTypesEnableSwitch": CoriantTypesEnableSwitch,
       "CoriantTypesEquipmentType": CoriantTypesEquipmentType,
       "CoriantTypesEthFec": CoriantTypesEthFec,
       "CoriantTypesEthernetRate": CoriantTypesEthernetRate,
       "CoriantTypesFilename": CoriantTypesFilename,
       "CoriantTypesFlowControl": CoriantTypesFlowControl,
       "CoriantTypesFreq": CoriantTypesFreq,
       "CoriantTypesFtpPath": CoriantTypesFtpPath,
       "CoriantTypesManagementDirection": CoriantTypesManagementDirection,
       "CoriantTypesManagementLocation": CoriantTypesManagementLocation,
       "CoriantTypesManagementTimePeriod": CoriantTypesManagementTimePeriod,
       "CoriantTypesNameIdentifier": CoriantTypesNameIdentifier,
       "CoriantTypesNumberList": CoriantTypesNumberList,
       "CoriantTypesOduType": CoriantTypesOduType,
       "CoriantTypesOnOff": CoriantTypesOnOff,
       "CoriantTypesOpticalDB": CoriantTypesOpticalDB,
       "CoriantTypesOpticalPower": CoriantTypesOpticalPower,
       "CoriantTypesOtukFec": CoriantTypesOtukFec,
       "CoriantTypesPassword": CoriantTypesPassword,
       "CoriantTypesPercentage": CoriantTypesPercentage,
       "CoriantTypesPluggableFormFactor": CoriantTypesPluggableFormFactor,
       "CoriantTypesPluggableType": CoriantTypesPluggableType,
       "CoriantTypesPortId": CoriantTypesPortId,
       "CoriantTypesPortMode": CoriantTypesPortMode,
       "CoriantTypesPower": CoriantTypesPower,
       "CoriantTypesRtpType": CoriantTypesRtpType,
       "CoriantTypesSessionId": CoriantTypesSessionId,
       "CoriantTypesShelfId": CoriantTypesShelfId,
       "CoriantTypesSlotId": CoriantTypesSlotId,
       "CoriantTypesSnmpString": CoriantTypesSnmpString,
       "CoriantTypesSourceProtocol": CoriantTypesSourceProtocol,
       "CoriantTypesSubslotId": CoriantTypesSubslotId,
       "CoriantTypesTemperature": CoriantTypesTemperature,
       "CoriantTypesTemperaturePrecision3": CoriantTypesTemperaturePrecision3,
       "CoriantTypesTestSignalConfig": CoriantTypesTestSignalConfig,
       "CoriantTypesTestSignalType": CoriantTypesTestSignalType,
       "CoriantTypesTimMode": CoriantTypesTimMode,
       "CoriantTypesTimePeriod": CoriantTypesTimePeriod,
       "CoriantTypesTypeOfDirection": CoriantTypesTypeOfDirection,
       "CoriantTypesUserName": CoriantTypesUserName,
       "CoriantTypesYesNo": CoriantTypesYesNo,
       "IetfInetTypesAsNumber": IetfInetTypesAsNumber,
       "IetfInetTypesDomainName": IetfInetTypesDomainName,
       "IetfInetTypesDscp": IetfInetTypesDscp,
       "IetfInetTypesHost": IetfInetTypesHost,
       "IetfInetTypesIpAddress": IetfInetTypesIpAddress,
       "IetfInetTypesIpAddressNoZone": IetfInetTypesIpAddressNoZone,
       "IetfInetTypesIpPrefix": IetfInetTypesIpPrefix,
       "IetfInetTypesIpVersion": IetfInetTypesIpVersion,
       "IetfInetTypesIpv4Address": IetfInetTypesIpv4Address,
       "IetfInetTypesIpv4AddressNoZone": IetfInetTypesIpv4AddressNoZone,
       "IetfInetTypesIpv4Prefix": IetfInetTypesIpv4Prefix,
       "IetfInetTypesIpv6Address": IetfInetTypesIpv6Address,
       "IetfInetTypesIpv6AddressNoZone": IetfInetTypesIpv6AddressNoZone,
       "IetfInetTypesIpv6FlowLabel": IetfInetTypesIpv6FlowLabel,
       "IetfInetTypesIpv6Prefix": IetfInetTypesIpv6Prefix,
       "IetfInetTypesPortNumber": IetfInetTypesPortNumber,
       "IetfInetTypesUri": IetfInetTypesUri,
       "IetfNetconfAcmAccessOperationsType": IetfNetconfAcmAccessOperationsType,
       "IetfNetconfAcmActionType": IetfNetconfAcmActionType,
       "IetfNetconfAcmGroupNameType": IetfNetconfAcmGroupNameType,
       "IetfNetconfAcmMatchallStringType": IetfNetconfAcmMatchallStringType,
       "IetfNetconfAcmNodeInstanceIdentifier": IetfNetconfAcmNodeInstanceIdentifier,
       "IetfNetconfAcmUserNameType": IetfNetconfAcmUserNameType,
       "IetfNetconfEditOperationType": IetfNetconfEditOperationType,
       "IetfNetconfErrorSeverityType": IetfNetconfErrorSeverityType,
       "IetfNetconfErrorTagType": IetfNetconfErrorTagType,
       "IetfNetconfSessionIdOrZeroType": IetfNetconfSessionIdOrZeroType,
       "IetfNetconfSessionIdType": IetfNetconfSessionIdType,
       "IetfNetconfWithDefaultsWithDefaultsMode": IetfNetconfWithDefaultsWithDefaultsMode,
       "IetfYangTypesCounter32": IetfYangTypesCounter32,
       "IetfYangTypesCounter64": IetfYangTypesCounter64,
       "IetfYangTypesDateAndTime": IetfYangTypesDateAndTime,
       "IetfYangTypesDottedQuad": IetfYangTypesDottedQuad,
       "IetfYangTypesGauge32": IetfYangTypesGauge32,
       "IetfYangTypesGauge64": IetfYangTypesGauge64,
       "IetfYangTypesHexString": IetfYangTypesHexString,
       "IetfYangTypesMacAddress": IetfYangTypesMacAddress,
       "IetfYangTypesObjectIdentifier": IetfYangTypesObjectIdentifier,
       "IetfYangTypesObjectIdentifier128": IetfYangTypesObjectIdentifier128,
       "IetfYangTypesPhysAddress": IetfYangTypesPhysAddress,
       "IetfYangTypesTimestamp": IetfYangTypesTimestamp,
       "IetfYangTypesTimeticks": IetfYangTypesTimeticks,
       "IetfYangTypesUuid": IetfYangTypesUuid,
       "IetfYangTypesXpath10": IetfYangTypesXpath10,
       "IetfYangTypesYangIdentifier": IetfYangTypesYangIdentifier,
       "IetfYangTypesZeroBasedCounter32": IetfYangTypesZeroBasedCounter32,
       "IetfYangTypesZeroBasedCounter64": IetfYangTypesZeroBasedCounter64,
       "KeySyncSessionCertificateRef": KeySyncSessionCertificateRef,
       "KeySyncSessionInterfaceRef": KeySyncSessionInterfaceRef,
       "LldpLldpSysCap": LldpLldpSysCap,
       "OpticalCommonSupportingPort": OpticalCommonSupportingPort,
       "OtdrOtdrIor": OtdrOtdrIor,
       "OtdrOtdrPulseWidth": OtdrOtdrPulseWidth,
       "OtdrOtdrRange": OtdrOtdrRange,
       "coriant": coriant,
       "products": products,
       "groove": groove,
       "fault": fault,
       "notificationInfo": notificationInfo,
       "notificationObject": notificationObject,
       "notificationFmEntity": notificationFmEntity,
       "notificationConditionType": notificationConditionType,
       "notificationLocation": notificationLocation,
       "notificationDirection": notificationDirection,
       "notificationTimePeriod": notificationTimePeriod,
       "notificationServiceAffect": notificationServiceAffect,
       "notificationSeverityLevel": notificationSeverityLevel,
       "notificationOccurrenceDateTime": notificationOccurrenceDateTime,
       "notificationConditionDescription": notificationConditionDescription,
       "notificationAlarmConditionType": notificationAlarmConditionType,
       "notificationLastSeverityLevel": notificationLastSeverityLevel,
       "notificationExtensionDescription": notificationExtensionDescription,
       "notificationFmEntityType": notificationFmEntityType,
       "notificationTrap": notificationTrap,
       "alarmNotification": alarmNotification,
       "notAlarmedEventNotification": notAlarmedEventNotification,
       "alarmProfile": alarmProfile,
       "alarmProfileTable": alarmProfileTable,
       "alarmProfileEntry": alarmProfileEntry,
       "alarmProfileId": alarmProfileId,
       "alarmProfileENTR": alarmProfileENTR,
       "alarmProfileENTRTable": alarmProfileENTRTable,
       "alarmProfileENTREntry": alarmProfileENTREntry,
       "alarmProfileENTRConditionType": alarmProfileENTRConditionType,
       "alarmProfileENTRFmEntityType": alarmProfileENTRFmEntityType,
       "alarmProfileENTRTimePeriod": alarmProfileENTRTimePeriod,
       "alarmProfileENTRSeverityLevelSa": alarmProfileENTRSeverityLevelSa,
       "alarmProfileENTRSeverityLevelNsa": alarmProfileENTRSeverityLevelNsa,
       "standingCondition": standingCondition,
       "standingConditionTable": standingConditionTable,
       "standingConditionEntry": standingConditionEntry,
       "standingConditionFmEntity": standingConditionFmEntity,
       "standingConditionConditionType": standingConditionConditionType,
       "standingConditionLocation": standingConditionLocation,
       "standingConditionDirection": standingConditionDirection,
       "standingConditionTimePeriod": standingConditionTimePeriod,
       "standingConditionServiceAffect": standingConditionServiceAffect,
       "standingConditionSeverityLevel": standingConditionSeverityLevel,
       "standingConditionOccurrenceDateTime": standingConditionOccurrenceDateTime,
       "standingConditionConditionDescription": standingConditionConditionDescription,
       "standingConditionFmEntityType": standingConditionFmEntityType,
       "ne": ne,
       "neInfo": neInfo,
       "neId": neId,
       "neName": neName,
       "neType": neType,
       "neLocation": neLocation,
       "neSite": neSite,
       "neAltitude": neAltitude,
       "neVendor": neVendor,
       "neTemperature": neTemperature,
       "system": system,
       "systemUnknownPluggableReport": systemUnknownPluggableReport,
       "systemPowerConsumptionCurrent": systemPowerConsumptionCurrent,
       "systemPowerConsumptionEstimatedMax": systemPowerConsumptionEstimatedMax,
       "systemFactoryResetButton": systemFactoryResetButton,
       "console": console,
       "consoleBaudRate": consoleBaudRate,
       "equipment": equipment,
       "shelf": shelf,
       "shelfTable": shelfTable,
       "shelfEntry": shelfEntry,
       "shelfId": shelfId,
       "shelfLocation": shelfLocation,
       "shelfInletTemperature": shelfInletTemperature,
       "shelfOutletTemperature": shelfOutletTemperature,
       "shelfAdminStatus": shelfAdminStatus,
       "shelfOperStatus": shelfOperStatus,
       "shelfAvailStatus": shelfAvailStatus,
       "shelfAliasName": shelfAliasName,
       "slot": slot,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotId": slotId,
       "slotActualCardType": slotActualCardType,
       "slotPossibleCardTypes": slotPossibleCardTypes,
       "slotAdminStatus": slotAdminStatus,
       "slotOperStatus": slotOperStatus,
       "slotAvailStatus": slotAvailStatus,
       "slotAliasName": slotAliasName,
       "card": card,
       "cardTable": cardTable,
       "cardEntry": cardEntry,
       "cardRequiredType": cardRequiredType,
       "cardEquipmentName": cardEquipmentName,
       "cardAdminStatus": cardAdminStatus,
       "cardOperStatus": cardOperStatus,
       "cardAvailStatus": cardAvailStatus,
       "cardAliasName": cardAliasName,
       "cardFanSpeedRate": cardFanSpeedRate,
       "cardSwitchingType": cardSwitchingType,
       "cardTemperature": cardTemperature,
       "cardMode": cardMode,
       "subslot": subslot,
       "subslotTable": subslotTable,
       "subslotEntry": subslotEntry,
       "subslotId": subslotId,
       "subslotActualCardType": subslotActualCardType,
       "subslotPossibleCardTypes": subslotPossibleCardTypes,
       "subslotAdminStatus": subslotAdminStatus,
       "subslotOperStatus": subslotOperStatus,
       "subslotAvailStatus": subslotAvailStatus,
       "subslotAliasName": subslotAliasName,
       "subcard": subcard,
       "subcardTable": subcardTable,
       "subcardEntry": subcardEntry,
       "subcardRequiredType": subcardRequiredType,
       "subcardEquipmentName": subcardEquipmentName,
       "subcardAdminStatus": subcardAdminStatus,
       "subcardOperStatus": subcardOperStatus,
       "subcardAvailStatus": subcardAvailStatus,
       "subcardAliasName": subcardAliasName,
       "subcardTemperature": subcardTemperature,
       "port": port,
       "portTable": portTable,
       "portEntry": portEntry,
       "portId": portId,
       "portPossiblePluggableTypes": portPossiblePluggableTypes,
       "portActualPluggableType": portActualPluggableType,
       "portRxOpticalPower": portRxOpticalPower,
       "portTxOpticalPower": portTxOpticalPower,
       "portRxOpticalPowerSelectedChannel": portRxOpticalPowerSelectedChannel,
       "portRxOpticalPowerLane1": portRxOpticalPowerLane1,
       "portRxOpticalPowerLane2": portRxOpticalPowerLane2,
       "portRxOpticalPowerLane3": portRxOpticalPowerLane3,
       "portRxOpticalPowerLane4": portRxOpticalPowerLane4,
       "portTxOpticalPowerLane1": portTxOpticalPowerLane1,
       "portTxOpticalPowerLane2": portTxOpticalPowerLane2,
       "portTxOpticalPowerLane3": portTxOpticalPowerLane3,
       "portTxOpticalPowerLane4": portTxOpticalPowerLane4,
       "portDirectionType": portDirectionType,
       "portName": portName,
       "portType": portType,
       "portMode": portMode,
       "portAdminStatus": portAdminStatus,
       "portOperStatus": portOperStatus,
       "portAvailStatus": portAvailStatus,
       "portAliasName": portAliasName,
       "portServiceLabel": portServiceLabel,
       "portConnectedTo": portConnectedTo,
       "portArcConfig": portArcConfig,
       "portArcState": portArcState,
       "portArcSubState": portArcSubState,
       "portArcTimer": portArcTimer,
       "portArcRemainingTime": portArcRemainingTime,
       "portExternalConnectivity": portExternalConnectivity,
       "subport": subport,
       "subportTable": subportTable,
       "subportEntry": subportEntry,
       "subportId": subportId,
       "subportPortName": subportPortName,
       "subportPortType": subportPortType,
       "subportPortMode": subportPortMode,
       "subportAdminStatus": subportAdminStatus,
       "subportOperStatus": subportOperStatus,
       "subportAvailStatus": subportAvailStatus,
       "subportAliasName": subportAliasName,
       "subportServiceLabel": subportServiceLabel,
       "subportConnectedTo": subportConnectedTo,
       "subportArcConfig": subportArcConfig,
       "subportArcState": subportArcState,
       "subportArcSubState": subportArcSubState,
       "subportArcTimer": subportArcTimer,
       "subportArcRemainingTime": subportArcRemainingTime,
       "subportRxOpticalPower": subportRxOpticalPower,
       "subportTxOpticalPower": subportTxOpticalPower,
       "subportExternalConnectivity": subportExternalConnectivity,
       "pluggable": pluggable,
       "pluggableTable": pluggableTable,
       "pluggableEntry": pluggableEntry,
       "pluggableRequiredType": pluggableRequiredType,
       "pluggableFormFactor": pluggableFormFactor,
       "pluggableInterfaceType": pluggableInterfaceType,
       "pluggableLaserSource": pluggableLaserSource,
       "pluggableHwVersion": pluggableHwVersion,
       "pluggableVendor": pluggableVendor,
       "pluggableSerialNumber": pluggableSerialNumber,
       "pluggableFwVersion": pluggableFwVersion,
       "pluggablePartNumber": pluggablePartNumber,
       "pluggableClei": pluggableClei,
       "pluggableEquipmentName": pluggableEquipmentName,
       "pluggableAdminStatus": pluggableAdminStatus,
       "pluggableOperStatus": pluggableOperStatus,
       "pluggableAvailStatus": pluggableAvailStatus,
       "pluggableAliasName": pluggableAliasName,
       "pluggableTemperature": pluggableTemperature,
       "amplifier": amplifier,
       "amplifierTable": amplifierTable,
       "amplifierEntry": amplifierEntry,
       "amplifierName": amplifierName,
       "amplifierSupportingInputPort": amplifierSupportingInputPort,
       "amplifierSupportingOutputPort": amplifierSupportingOutputPort,
       "amplifierAdminStatus": amplifierAdminStatus,
       "amplifierOperStatus": amplifierOperStatus,
       "amplifierAvailStatus": amplifierAvailStatus,
       "amplifierAliasName": amplifierAliasName,
       "amplifierEnable": amplifierEnable,
       "amplifierInputLosShutdown": amplifierInputLosShutdown,
       "amplifierControlMode": amplifierControlMode,
       "amplifierMode": amplifierMode,
       "amplifierType": amplifierType,
       "amplifierTargetGain": amplifierTargetGain,
       "amplifierOperatingGain": amplifierOperatingGain,
       "amplifierGainAdjustment": amplifierGainAdjustment,
       "amplifierGainRangeMin": amplifierGainRangeMin,
       "amplifierGainRangeMax": amplifierGainRangeMax,
       "amplifierOutputPowerMon": amplifierOutputPowerMon,
       "amplifierOutputPowerMonWithAse": amplifierOutputPowerMonWithAse,
       "amplifierInputPowerMon": amplifierInputPowerMon,
       "amplifierOutputVoa": amplifierOutputVoa,
       "amplifierPowerBeforeOutputVoa": amplifierPowerBeforeOutputVoa,
       "tdc": tdc,
       "tdcTable": tdcTable,
       "tdcEntry": tdcEntry,
       "tdcName": tdcName,
       "tdcSupportingInputPort": tdcSupportingInputPort,
       "tdcSupportingOutputPort": tdcSupportingOutputPort,
       "tdcAdminStatus": tdcAdminStatus,
       "tdcOperStatus": tdcOperStatus,
       "tdcAvailStatus": tdcAvailStatus,
       "tdcAliasName": tdcAliasName,
       "tdcMode": tdcMode,
       "tdcReferenceFrequency": tdcReferenceFrequency,
       "tdcActualReferenceFrequency": tdcActualReferenceFrequency,
       "tdcFrequencyRangeMin": tdcFrequencyRangeMin,
       "tdcFrequencyRangeMax": tdcFrequencyRangeMax,
       "tdcChromaticDispersion": tdcChromaticDispersion,
       "tdcChromaticDispersionAdjustment": tdcChromaticDispersionAdjustment,
       "tdcActualChromaticDispersion": tdcActualChromaticDispersion,
       "tdcCdRangeMin": tdcCdRangeMin,
       "tdcCdRangeMax": tdcCdRangeMax,
       "inventory": inventory,
       "inventoryTable": inventoryTable,
       "inventoryEntry": inventoryEntry,
       "inventoryEquipmentType": inventoryEquipmentType,
       "inventoryShelfId": inventoryShelfId,
       "inventorySlotId": inventorySlotId,
       "inventorySubslotId": inventorySubslotId,
       "inventoryPortId": inventoryPortId,
       "inventoryEquipmentVersion": inventoryEquipmentVersion,
       "inventoryModuleType": inventoryModuleType,
       "inventoryVendor": inventoryVendor,
       "inventorySerialNumber": inventorySerialNumber,
       "inventoryFwVersion": inventoryFwVersion,
       "inventoryPartNumber": inventoryPartNumber,
       "inventoryClei": inventoryClei,
       "inventoryInterfaceType": inventoryInterfaceType,
       "inventoryManufactureDate": inventoryManufactureDate,
       "inventoryManufacturerNumber": inventoryManufacturerNumber,
       "led": led,
       "ledTable": ledTable,
       "ledEntry": ledEntry,
       "ledEquipmentType": ledEquipmentType,
       "ledShelfId": ledShelfId,
       "ledSlotId": ledSlotId,
       "ledName": ledName,
       "ledStatus": ledStatus,
       "ledSubslotId": ledSubslotId,
       "temperatureDetails": temperatureDetails,
       "temperatureDetailsTable": temperatureDetailsTable,
       "temperatureDetailsEntry": temperatureDetailsEntry,
       "temperatureDetailsMonitoringPoint": temperatureDetailsMonitoringPoint,
       "temperatureDetailsTemperature": temperatureDetailsTemperature,
       "temperatureDetailsTemperatureRangeLow": temperatureDetailsTemperatureRangeLow,
       "temperatureDetailsTemperatureRangeHigh": temperatureDetailsTemperatureRangeHigh,
       "otdr": otdr,
       "otdrTable": otdrTable,
       "otdrEntry": otdrEntry,
       "otdrState": otdrState,
       "otdrMeasurementTime": otdrMeasurementTime,
       "otdrError": otdrError,
       "otdrLaserStatus": otdrLaserStatus,
       "otdrMeasurementPort": otdrMeasurementPort,
       "otdrPort": otdrPort,
       "otdrPortTable": otdrPortTable,
       "otdrPortEntry": otdrPortEntry,
       "otdrPortOtdrRange": otdrPortOtdrRange,
       "otdrPortOtdrPulseWidth": otdrPortOtdrPulseWidth,
       "otdrPortOtdrMeasurementSpeed": otdrPortOtdrMeasurementSpeed,
       "otdrPortOtdrIor": otdrPortOtdrIor,
       "otdrPortOtdrFiberType": otdrPortOtdrFiberType,
       "otdrPortOtdrLastMeasurement": otdrPortOtdrLastMeasurement,
       "otdrPortOtdrResolution": otdrPortOtdrResolution,
       "ops": ops,
       "opsTable": opsTable,
       "opsEntry": opsEntry,
       "opsName": opsName,
       "opsWorkingEntity": opsWorkingEntity,
       "opsProtectionEntity": opsProtectionEntity,
       "opsAdminStatus": opsAdminStatus,
       "opsOperStatus": opsOperStatus,
       "opsAvailStatus": opsAvailStatus,
       "opsAliasName": opsAliasName,
       "opsProtectionStatus": opsProtectionStatus,
       "opsActivePath": opsActivePath,
       "opsRevertive": opsRevertive,
       "opsWaitToRestore": opsWaitToRestore,
       "opsWorkingSwitchThreshold": opsWorkingSwitchThreshold,
       "opsProtectionSwitchThreshold": opsProtectionSwitchThreshold,
       "opsWorkingLosThreshold": opsWorkingLosThreshold,
       "opsProtectionLosThreshold": opsProtectionLosThreshold,
       "opsHoldoffTimer": opsHoldoffTimer,
       "opsWavelengthBand": opsWavelengthBand,
       "subportStatistics": subportStatistics,
       "subportStatisticsTable": subportStatisticsTable,
       "subportStatisticsEntry": subportStatisticsEntry,
       "subportStatisticsEntryLastClear": subportStatisticsEntryLastClear,
       "portStatistics": portStatistics,
       "portStatisticsTable": portStatisticsTable,
       "portStatisticsEntry": portStatisticsEntry,
       "portStatisticsEntryLastClear": portStatisticsEntryLastClear,
       "subcardStatistics": subcardStatistics,
       "subcardStatisticsTable": subcardStatisticsTable,
       "subcardStatisticsEntry": subcardStatisticsEntry,
       "subcardStatisticsEntryLastClear": subcardStatisticsEntryLastClear,
       "cardStatistics": cardStatistics,
       "cardStatisticsTable": cardStatisticsTable,
       "cardStatisticsEntry": cardStatisticsEntry,
       "cardStatisticsEntryLastClear": cardStatisticsEntryLastClear,
       "shelfStatistics": shelfStatistics,
       "shelfStatisticsTable": shelfStatisticsTable,
       "shelfStatisticsEntry": shelfStatisticsEntry,
       "shelfStatisticsEntryLastClear": shelfStatisticsEntryLastClear,
       "services": services,
       "otn": otn,
       "eth10g": eth10g,
       "eth10gTable": eth10gTable,
       "eth10gEntry": eth10gEntry,
       "eth10gEthFecType": eth10gEthFecType,
       "eth10gEthFecTypeState": eth10gEthFecTypeState,
       "eth10gTransmitInterpacketgap": eth10gTransmitInterpacketgap,
       "eth10gGfpPayloadFcs": eth10gGfpPayloadFcs,
       "eth10gMappingMode": eth10gMappingMode,
       "eth10gAdminStatus": eth10gAdminStatus,
       "eth10gOperStatus": eth10gOperStatus,
       "eth10gAvailStatus": eth10gAvailStatus,
       "eth10gAliasName": eth10gAliasName,
       "eth10gClientShutdown": eth10gClientShutdown,
       "eth10gClientShutdownHoldoffTimer": eth10gClientShutdownHoldoffTimer,
       "eth10gNearEndAls": eth10gNearEndAls,
       "eth10gAlsDegradeMode": eth10gAlsDegradeMode,
       "eth10gLoopbackEnable": eth10gLoopbackEnable,
       "eth10gLoopbackType": eth10gLoopbackType,
       "eth10gTestSignalType": eth10gTestSignalType,
       "eth10gTestSignalEnable": eth10gTestSignalEnable,
       "eth10gServiceLabel": eth10gServiceLabel,
       "eth10gLldpStatusIf": eth10gLldpStatusIf,
       "eth10gUpiValue": eth10gUpiValue,
       "eth10gHoldoffSignal": eth10gHoldoffSignal,
       "testSignalFacilityStatus": testSignalFacilityStatus,
       "testSignalFacilityStatusTable": testSignalFacilityStatusTable,
       "testSignalFacilityStatusEntry": testSignalFacilityStatusEntry,
       "testSignalFacilityStatusPrbsSync": testSignalFacilityStatusPrbsSync,
       "testSignalFacilityStatusTestTimeDuration": testSignalFacilityStatusTestTimeDuration,
       "testSignalFacilityStatusPrbsBitErrorCount": testSignalFacilityStatusPrbsBitErrorCount,
       "lldpRemoteSystem": lldpRemoteSystem,
       "lldpRemoteSystemTable": lldpRemoteSystemTable,
       "lldpRemoteSystemEntry": lldpRemoteSystemEntry,
       "lldpRemoteSystemLldpRemoteIndex": lldpRemoteSystemLldpRemoteIndex,
       "lldpRemoteSystemRemoteChassisIdSubtype": lldpRemoteSystemRemoteChassisIdSubtype,
       "lldpRemoteSystemRemoteChassisId": lldpRemoteSystemRemoteChassisId,
       "lldpRemoteSystemRemotePortIdSubtype": lldpRemoteSystemRemotePortIdSubtype,
       "lldpRemoteSystemRemotePortId": lldpRemoteSystemRemotePortId,
       "lldpRemoteSystemRemotePortDesc": lldpRemoteSystemRemotePortDesc,
       "lldpRemoteSystemRemoteSysName": lldpRemoteSystemRemoteSysName,
       "lldpRemoteSystemRemoteSysDesc": lldpRemoteSystemRemoteSysDesc,
       "lldpRemoteSystemRemoteSysCapSupported": lldpRemoteSystemRemoteSysCapSupported,
       "lldpRemoteSystemRemoteSysCapEnabled": lldpRemoteSystemRemoteSysCapEnabled,
       "remoteManAddresses": remoteManAddresses,
       "remoteManAddressesTable": remoteManAddressesTable,
       "remoteManAddressesEntry": remoteManAddressesEntry,
       "remoteManAddressesRemoteManAddrSubtype": remoteManAddressesRemoteManAddrSubtype,
       "remoteManAddressesRemoteManAddr": remoteManAddressesRemoteManAddr,
       "remoteManAddressesRemoteManAddrIfSubtype": remoteManAddressesRemoteManAddrIfSubtype,
       "remoteManAddressesRemoteManAddrIfId": remoteManAddressesRemoteManAddrIfId,
       "remoteManAddressesRemoteManAddrOid": remoteManAddressesRemoteManAddrOid,
       "odu": odu,
       "oduTable": oduTable,
       "oduEntry": oduEntry,
       "odutypeL1": odutypeL1,
       "oduidL1": oduidL1,
       "odutypeL2": odutypeL2,
       "oduidL2": oduidL2,
       "odutypeL3": odutypeL3,
       "oduidL3": oduidL3,
       "odutypeL4": odutypeL4,
       "oduidL4": oduidL4,
       "oduAdminStatus": oduAdminStatus,
       "oduOperStatus": oduOperStatus,
       "oduAvailStatus": oduAvailStatus,
       "oduAliasName": oduAliasName,
       "oduServiceLabel": oduServiceLabel,
       "oduTribSlot": oduTribSlot,
       "oduRxPayloadType": oduRxPayloadType,
       "oduTxPayloadType": oduTxPayloadType,
       "oduNimEnable": oduNimEnable,
       "oduDelayMeasurementEnable": oduDelayMeasurementEnable,
       "oduOpuConfigActual": oduOpuConfigActual,
       "oduClientSignalType": oduClientSignalType,
       "oduExpSapi": oduExpSapi,
       "oduExpDapi": oduExpDapi,
       "oduExpOperator": oduExpOperator,
       "oduTxSapi": oduTxSapi,
       "oduTxDapi": oduTxDapi,
       "oduTxOperator": oduTxOperator,
       "oduTimDefectMode": oduTimDefectMode,
       "oduTimAct": oduTimAct,
       "oduRxSapi": oduRxSapi,
       "oduRxDapi": oduRxDapi,
       "oduRxOperator": oduRxOperator,
       "oduDegradeInterval": oduDegradeInterval,
       "oduDegradeThreshold": oduDegradeThreshold,
       "oduTestSignalType": oduTestSignalType,
       "oduTestSignalEnable": oduTestSignalEnable,
       "oduTerminationMode": oduTerminationMode,
       "oduEncryption": oduEncryption,
       "oduEncryptionTable": oduEncryptionTable,
       "oduEncryptionEntry": oduEncryptionEntry,
       "oduEncryptionEncryptionEnable": oduEncryptionEncryptionEnable,
       "oduEncryptionBlockCipherMode": oduEncryptionBlockCipherMode,
       "oduEncryptionEncryptionInterval": oduEncryptionEncryptionInterval,
       "oduEncryptionEncryptionTxStatus": oduEncryptionEncryptionTxStatus,
       "oduEncryptionEncryptionRxStatus": oduEncryptionEncryptionRxStatus,
       "oduEncryptionOduKeySyncSession": oduEncryptionOduKeySyncSession,
       "oduEncryptionEncryptionTxChannelId": oduEncryptionEncryptionTxChannelId,
       "oduEncryptionTimeToNextKey": oduEncryptionTimeToNextKey,
       "testSignalStatus": testSignalStatus,
       "testSignalStatusTable": testSignalStatusTable,
       "testSignalStatusEntry": testSignalStatusEntry,
       "testSignalStatusPrbsSync": testSignalStatusPrbsSync,
       "testSignalStatusTestTimeDuration": testSignalStatusTestTimeDuration,
       "testSignalStatusPrbsBitErrorCount": testSignalStatusPrbsBitErrorCount,
       "eth40g": eth40g,
       "eth40gTable": eth40gTable,
       "eth40gEntry": eth40gEntry,
       "eth40gEthFecType": eth40gEthFecType,
       "eth40gEthFecTypeState": eth40gEthFecTypeState,
       "eth40gTransmitInterpacketgap": eth40gTransmitInterpacketgap,
       "eth40gGfpPayloadFcs": eth40gGfpPayloadFcs,
       "eth40gMappingMode": eth40gMappingMode,
       "eth40gAdminStatus": eth40gAdminStatus,
       "eth40gOperStatus": eth40gOperStatus,
       "eth40gAvailStatus": eth40gAvailStatus,
       "eth40gAliasName": eth40gAliasName,
       "eth40gClientShutdown": eth40gClientShutdown,
       "eth40gClientShutdownHoldoffTimer": eth40gClientShutdownHoldoffTimer,
       "eth40gNearEndAls": eth40gNearEndAls,
       "eth40gAlsDegradeMode": eth40gAlsDegradeMode,
       "eth40gLoopbackEnable": eth40gLoopbackEnable,
       "eth40gLoopbackType": eth40gLoopbackType,
       "eth40gTestSignalType": eth40gTestSignalType,
       "eth40gTestSignalEnable": eth40gTestSignalEnable,
       "eth40gServiceLabel": eth40gServiceLabel,
       "eth40gLldpStatusIf": eth40gLldpStatusIf,
       "eth40gHoldoffSignal": eth40gHoldoffSignal,
       "eth100g": eth100g,
       "eth100gTable": eth100gTable,
       "eth100gEntry": eth100gEntry,
       "eth100gEthFecType": eth100gEthFecType,
       "eth100gEthFecTypeState": eth100gEthFecTypeState,
       "eth100gTransmitInterpacketgap": eth100gTransmitInterpacketgap,
       "eth100gGfpPayloadFcs": eth100gGfpPayloadFcs,
       "eth100gMappingMode": eth100gMappingMode,
       "eth100gAdminStatus": eth100gAdminStatus,
       "eth100gOperStatus": eth100gOperStatus,
       "eth100gAvailStatus": eth100gAvailStatus,
       "eth100gAliasName": eth100gAliasName,
       "eth100gClientShutdown": eth100gClientShutdown,
       "eth100gClientShutdownHoldoffTimer": eth100gClientShutdownHoldoffTimer,
       "eth100gNearEndAls": eth100gNearEndAls,
       "eth100gAlsDegradeMode": eth100gAlsDegradeMode,
       "eth100gLoopbackEnable": eth100gLoopbackEnable,
       "eth100gLoopbackType": eth100gLoopbackType,
       "eth100gTestSignalType": eth100gTestSignalType,
       "eth100gTestSignalEnable": eth100gTestSignalEnable,
       "eth100gServiceLabel": eth100gServiceLabel,
       "eth100gLldpStatusIf": eth100gLldpStatusIf,
       "eth100gHoldoffSignal": eth100gHoldoffSignal,
       "otu4": otu4,
       "otu4Table": otu4Table,
       "otu4Entry": otu4Entry,
       "otu4FecType": otu4FecType,
       "otu4AdminStatus": otu4AdminStatus,
       "otu4OperStatus": otu4OperStatus,
       "otu4AvailStatus": otu4AvailStatus,
       "otu4AliasName": otu4AliasName,
       "otu4ServiceLabel": otu4ServiceLabel,
       "otu4ExpSapi": otu4ExpSapi,
       "otu4ExpDapi": otu4ExpDapi,
       "otu4ExpOperator": otu4ExpOperator,
       "otu4TxSapi": otu4TxSapi,
       "otu4TxDapi": otu4TxDapi,
       "otu4TxOperator": otu4TxOperator,
       "otu4TimDefectMode": otu4TimDefectMode,
       "otu4TimAct": otu4TimAct,
       "otu4RxSapi": otu4RxSapi,
       "otu4RxDapi": otu4RxDapi,
       "otu4RxOperator": otu4RxOperator,
       "otu4DegradeInterval": otu4DegradeInterval,
       "otu4DegradeThreshold": otu4DegradeThreshold,
       "otu4LoopbackEnable": otu4LoopbackEnable,
       "otu4LoopbackType": otu4LoopbackType,
       "otu4ClientShutdown": otu4ClientShutdown,
       "otu4ClientShutdownHoldoffTimer": otu4ClientShutdownHoldoffTimer,
       "otu4HoldoffSignal": otu4HoldoffSignal,
       "otu4NearEndAls": otu4NearEndAls,
       "otu4AlsDegradeMode": otu4AlsDegradeMode,
       "otu2": otu2,
       "otu2Table": otu2Table,
       "otu2Entry": otu2Entry,
       "otu2FecType": otu2FecType,
       "otu2AdminStatus": otu2AdminStatus,
       "otu2OperStatus": otu2OperStatus,
       "otu2AvailStatus": otu2AvailStatus,
       "otu2AliasName": otu2AliasName,
       "otu2ServiceLabel": otu2ServiceLabel,
       "otu2ExpSapi": otu2ExpSapi,
       "otu2ExpDapi": otu2ExpDapi,
       "otu2ExpOperator": otu2ExpOperator,
       "otu2TxSapi": otu2TxSapi,
       "otu2TxDapi": otu2TxDapi,
       "otu2TxOperator": otu2TxOperator,
       "otu2TimDefectMode": otu2TimDefectMode,
       "otu2TimAct": otu2TimAct,
       "otu2RxSapi": otu2RxSapi,
       "otu2RxDapi": otu2RxDapi,
       "otu2RxOperator": otu2RxOperator,
       "otu2DegradeInterval": otu2DegradeInterval,
       "otu2DegradeThreshold": otu2DegradeThreshold,
       "otu2LoopbackEnable": otu2LoopbackEnable,
       "otu2LoopbackType": otu2LoopbackType,
       "otu2e": otu2e,
       "otu2eTable": otu2eTable,
       "otu2eEntry": otu2eEntry,
       "otu2eFecType": otu2eFecType,
       "otu2eAdminStatus": otu2eAdminStatus,
       "otu2eOperStatus": otu2eOperStatus,
       "otu2eAvailStatus": otu2eAvailStatus,
       "otu2eAliasName": otu2eAliasName,
       "otu2eServiceLabel": otu2eServiceLabel,
       "otu2eExpSapi": otu2eExpSapi,
       "otu2eExpDapi": otu2eExpDapi,
       "otu2eExpOperator": otu2eExpOperator,
       "otu2eTxSapi": otu2eTxSapi,
       "otu2eTxDapi": otu2eTxDapi,
       "otu2eTxOperator": otu2eTxOperator,
       "otu2eTimDefectMode": otu2eTimDefectMode,
       "otu2eTimAct": otu2eTimAct,
       "otu2eRxSapi": otu2eRxSapi,
       "otu2eRxDapi": otu2eRxDapi,
       "otu2eRxOperator": otu2eRxOperator,
       "otu2eDegradeInterval": otu2eDegradeInterval,
       "otu2eDegradeThreshold": otu2eDegradeThreshold,
       "otu2eLoopbackEnable": otu2eLoopbackEnable,
       "otu2eLoopbackType": otu2eLoopbackType,
       "fc8g": fc8g,
       "fc8gTable": fc8gTable,
       "fc8gEntry": fc8gEntry,
       "fc8gMappingMode": fc8gMappingMode,
       "fc8gAdminStatus": fc8gAdminStatus,
       "fc8gOperStatus": fc8gOperStatus,
       "fc8gAvailStatus": fc8gAvailStatus,
       "fc8gAliasName": fc8gAliasName,
       "fc8gClientShutdown": fc8gClientShutdown,
       "fc8gClientShutdownHoldoffTimer": fc8gClientShutdownHoldoffTimer,
       "fc8gNearEndAls": fc8gNearEndAls,
       "fc8gAlsDegradeMode": fc8gAlsDegradeMode,
       "fc8gLoopbackEnable": fc8gLoopbackEnable,
       "fc8gLoopbackType": fc8gLoopbackType,
       "fc8gTestSignalType": fc8gTestSignalType,
       "fc8gTestSignalEnable": fc8gTestSignalEnable,
       "fc8gServiceLabel": fc8gServiceLabel,
       "fc8gHoldoffSignal": fc8gHoldoffSignal,
       "fc16g": fc16g,
       "fc16gTable": fc16gTable,
       "fc16gEntry": fc16gEntry,
       "fc16gMappingMode": fc16gMappingMode,
       "fc16gAdminStatus": fc16gAdminStatus,
       "fc16gOperStatus": fc16gOperStatus,
       "fc16gAvailStatus": fc16gAvailStatus,
       "fc16gAliasName": fc16gAliasName,
       "fc16gClientShutdown": fc16gClientShutdown,
       "fc16gClientShutdownHoldoffTimer": fc16gClientShutdownHoldoffTimer,
       "fc16gNearEndAls": fc16gNearEndAls,
       "fc16gAlsDegradeMode": fc16gAlsDegradeMode,
       "fc16gLoopbackEnable": fc16gLoopbackEnable,
       "fc16gLoopbackType": fc16gLoopbackType,
       "fc16gTestSignalType": fc16gTestSignalType,
       "fc16gTestSignalEnable": fc16gTestSignalEnable,
       "fc16gServiceLabel": fc16gServiceLabel,
       "fc16gHoldoffSignal": fc16gHoldoffSignal,
       "oc192": oc192,
       "oc192Table": oc192Table,
       "oc192Entry": oc192Entry,
       "oc192MappingMode": oc192MappingMode,
       "oc192AdminStatus": oc192AdminStatus,
       "oc192OperStatus": oc192OperStatus,
       "oc192AvailStatus": oc192AvailStatus,
       "oc192AliasName": oc192AliasName,
       "oc192ClientShutdown": oc192ClientShutdown,
       "oc192ClientShutdownHoldoffTimer": oc192ClientShutdownHoldoffTimer,
       "oc192NearEndAls": oc192NearEndAls,
       "oc192AlsDegradeMode": oc192AlsDegradeMode,
       "oc192LoopbackEnable": oc192LoopbackEnable,
       "oc192LoopbackType": oc192LoopbackType,
       "oc192TestSignalType": oc192TestSignalType,
       "oc192TestSignalEnable": oc192TestSignalEnable,
       "oc192ServiceLabel": oc192ServiceLabel,
       "oc192ExpTrc": oc192ExpTrc,
       "oc192TxTrc": oc192TxTrc,
       "oc192RxTrc": oc192RxTrc,
       "oc192TimAct": oc192TimAct,
       "oc192TimMonitor": oc192TimMonitor,
       "oc192AisType": oc192AisType,
       "oc192HoldoffSignal": oc192HoldoffSignal,
       "stm64": stm64,
       "stm64Table": stm64Table,
       "stm64Entry": stm64Entry,
       "stm64MappingMode": stm64MappingMode,
       "stm64AdminStatus": stm64AdminStatus,
       "stm64OperStatus": stm64OperStatus,
       "stm64AvailStatus": stm64AvailStatus,
       "stm64AliasName": stm64AliasName,
       "stm64ClientShutdown": stm64ClientShutdown,
       "stm64ClientShutdownHoldoffTimer": stm64ClientShutdownHoldoffTimer,
       "stm64NearEndAls": stm64NearEndAls,
       "stm64AlsDegradeMode": stm64AlsDegradeMode,
       "stm64LoopbackEnable": stm64LoopbackEnable,
       "stm64LoopbackType": stm64LoopbackType,
       "stm64TestSignalType": stm64TestSignalType,
       "stm64TestSignalEnable": stm64TestSignalEnable,
       "stm64ServiceLabel": stm64ServiceLabel,
       "stm64ExpTrc": stm64ExpTrc,
       "stm64TxTrc": stm64TxTrc,
       "stm64RxTrc": stm64RxTrc,
       "stm64TimAct": stm64TimAct,
       "stm64TimMonitor": stm64TimMonitor,
       "stm64AisType": stm64AisType,
       "stm64HoldoffSignal": stm64HoldoffSignal,
       "otuc2": otuc2,
       "otuc2Table": otuc2Table,
       "otuc2Entry": otuc2Entry,
       "otuc2FecType": otuc2FecType,
       "otuc2AdminStatus": otuc2AdminStatus,
       "otuc2OperStatus": otuc2OperStatus,
       "otuc2AvailStatus": otuc2AvailStatus,
       "otuc2AliasName": otuc2AliasName,
       "otuc2ServiceLabel": otuc2ServiceLabel,
       "otuc2ExpSapi": otuc2ExpSapi,
       "otuc2ExpDapi": otuc2ExpDapi,
       "otuc2ExpOperator": otuc2ExpOperator,
       "otuc2TxSapi": otuc2TxSapi,
       "otuc2TxDapi": otuc2TxDapi,
       "otuc2TxOperator": otuc2TxOperator,
       "otuc2TimDefectMode": otuc2TimDefectMode,
       "otuc2TimAct": otuc2TimAct,
       "otuc2RxSapi": otuc2RxSapi,
       "otuc2RxDapi": otuc2RxDapi,
       "otuc2RxOperator": otuc2RxOperator,
       "otuc2DegradeInterval": otuc2DegradeInterval,
       "otuc2DegradeThreshold": otuc2DegradeThreshold,
       "otuc3": otuc3,
       "otuc3Table": otuc3Table,
       "otuc3Entry": otuc3Entry,
       "otuc3FecType": otuc3FecType,
       "otuc3AdminStatus": otuc3AdminStatus,
       "otuc3OperStatus": otuc3OperStatus,
       "otuc3AvailStatus": otuc3AvailStatus,
       "otuc3AliasName": otuc3AliasName,
       "otuc3ServiceLabel": otuc3ServiceLabel,
       "otuc3ExpSapi": otuc3ExpSapi,
       "otuc3ExpDapi": otuc3ExpDapi,
       "otuc3ExpOperator": otuc3ExpOperator,
       "otuc3TxSapi": otuc3TxSapi,
       "otuc3TxDapi": otuc3TxDapi,
       "otuc3TxOperator": otuc3TxOperator,
       "otuc3TimDefectMode": otuc3TimDefectMode,
       "otuc3TimAct": otuc3TimAct,
       "otuc3RxSapi": otuc3RxSapi,
       "otuc3RxDapi": otuc3RxDapi,
       "otuc3RxOperator": otuc3RxOperator,
       "otuc3DegradeInterval": otuc3DegradeInterval,
       "otuc3DegradeThreshold": otuc3DegradeThreshold,
       "ochOs": ochOs,
       "ochOsTable": ochOsTable,
       "ochOsEntry": ochOsEntry,
       "ochOsModulationFormat": ochOsModulationFormat,
       "ochOsLineEncoding": ochOsLineEncoding,
       "ochOsFrequency": ochOsFrequency,
       "ochOsActualFrequency": ochOsActualFrequency,
       "ochOsRxFrequency": ochOsRxFrequency,
       "ochOsActualRxFrequency": ochOsActualRxFrequency,
       "ochOsLaserEnable": ochOsLaserEnable,
       "ochOsRequiredTxOpticalPower": ochOsRequiredTxOpticalPower,
       "ochOsActualTxOpticalPower": ochOsActualTxOpticalPower,
       "ochOsFecType": ochOsFecType,
       "ochOsRxAttenuation": ochOsRxAttenuation,
       "ochOsTxFilterRollOff": ochOsTxFilterRollOff,
       "ochOsPreemphasis": ochOsPreemphasis,
       "ochOsPreemphasisValue": ochOsPreemphasisValue,
       "ochOsAdminStatus": ochOsAdminStatus,
       "ochOsOperStatus": ochOsOperStatus,
       "ochOsAvailStatus": ochOsAvailStatus,
       "ochOsAliasName": ochOsAliasName,
       "ochOsLoopbackEnable": ochOsLoopbackEnable,
       "ochOsLoopbackType": ochOsLoopbackType,
       "ochOsServiceLabel": ochOsServiceLabel,
       "ochOsDGD": ochOsDGD,
       "ochOsCD": ochOsCD,
       "ochOsOSNR": ochOsOSNR,
       "ochOsQFactor": ochOsQFactor,
       "ochOsPreFecBer": ochOsPreFecBer,
       "ochOsCdRangeLow": ochOsCdRangeLow,
       "ochOsCdRangeHigh": ochOsCdRangeHigh,
       "ochOsPropagateShutdown": ochOsPropagateShutdown,
       "ochOsFastSopMode": ochOsFastSopMode,
       "wan10gSonet": wan10gSonet,
       "wan10gSonetTable": wan10gSonetTable,
       "wan10gSonetEntry": wan10gSonetEntry,
       "wan10gSonetMappingMode": wan10gSonetMappingMode,
       "wan10gSonetAdminStatus": wan10gSonetAdminStatus,
       "wan10gSonetOperStatus": wan10gSonetOperStatus,
       "wan10gSonetAvailStatus": wan10gSonetAvailStatus,
       "wan10gSonetAliasName": wan10gSonetAliasName,
       "wan10gSonetClientShutdown": wan10gSonetClientShutdown,
       "wan10gSonetClientShutdownHoldoffTimer": wan10gSonetClientShutdownHoldoffTimer,
       "wan10gSonetHoldoffSignal": wan10gSonetHoldoffSignal,
       "wan10gSonetNearEndAls": wan10gSonetNearEndAls,
       "wan10gSonetAlsDegradeMode": wan10gSonetAlsDegradeMode,
       "wan10gSonetLoopbackEnable": wan10gSonetLoopbackEnable,
       "wan10gSonetLoopbackType": wan10gSonetLoopbackType,
       "wan10gSonetTestSignalType": wan10gSonetTestSignalType,
       "wan10gSonetTestSignalEnable": wan10gSonetTestSignalEnable,
       "wan10gSonetServiceLabel": wan10gSonetServiceLabel,
       "wan10gSonetExpTrc": wan10gSonetExpTrc,
       "wan10gSonetTxTrc": wan10gSonetTxTrc,
       "wan10gSonetRxTrc": wan10gSonetRxTrc,
       "wan10gSonetTimAct": wan10gSonetTimAct,
       "wan10gSonetTimMonitor": wan10gSonetTimMonitor,
       "wan10gSonetAisType": wan10gSonetAisType,
       "wan10gSdh": wan10gSdh,
       "wan10gSdhTable": wan10gSdhTable,
       "wan10gSdhEntry": wan10gSdhEntry,
       "wan10gSdhMappingMode": wan10gSdhMappingMode,
       "wan10gSdhAdminStatus": wan10gSdhAdminStatus,
       "wan10gSdhOperStatus": wan10gSdhOperStatus,
       "wan10gSdhAvailStatus": wan10gSdhAvailStatus,
       "wan10gSdhAliasName": wan10gSdhAliasName,
       "wan10gSdhClientShutdown": wan10gSdhClientShutdown,
       "wan10gSdhClientShutdownHoldoffTimer": wan10gSdhClientShutdownHoldoffTimer,
       "wan10gSdhHoldoffSignal": wan10gSdhHoldoffSignal,
       "wan10gSdhNearEndAls": wan10gSdhNearEndAls,
       "wan10gSdhAlsDegradeMode": wan10gSdhAlsDegradeMode,
       "wan10gSdhLoopbackEnable": wan10gSdhLoopbackEnable,
       "wan10gSdhLoopbackType": wan10gSdhLoopbackType,
       "wan10gSdhTestSignalType": wan10gSdhTestSignalType,
       "wan10gSdhTestSignalEnable": wan10gSdhTestSignalEnable,
       "wan10gSdhServiceLabel": wan10gSdhServiceLabel,
       "wan10gSdhExpTrc": wan10gSdhExpTrc,
       "wan10gSdhTxTrc": wan10gSdhTxTrc,
       "wan10gSdhRxTrc": wan10gSdhRxTrc,
       "wan10gSdhTimAct": wan10gSdhTimAct,
       "wan10gSdhTimMonitor": wan10gSdhTimMonitor,
       "wan10gSdhAisType": wan10gSdhAisType,
       "eth10gStatistics": eth10gStatistics,
       "eth10gStatisticsTable": eth10gStatisticsTable,
       "eth10gStatisticsEntry": eth10gStatisticsEntry,
       "eth10gStatisticsEntryLastClear": eth10gStatisticsEntryLastClear,
       "eth10gStatisticsEntryLossOfSignalSeconds": eth10gStatisticsEntryLossOfSignalSeconds,
       "eth10gStatisticsEntryBitErrorFec": eth10gStatisticsEntryBitErrorFec,
       "eth10gStatisticsEntryUncorrectedBlockErrorFec": eth10gStatisticsEntryUncorrectedBlockErrorFec,
       "eth10gStatisticsEntryInSymbolErrors": eth10gStatisticsEntryInSymbolErrors,
       "eth10gStatisticsEntryInDropEvents": eth10gStatisticsEntryInDropEvents,
       "eth10gStatisticsEntryInOctets": eth10gStatisticsEntryInOctets,
       "eth10gStatisticsEntryInPackets": eth10gStatisticsEntryInPackets,
       "eth10gStatisticsEntryInBroadcastPackets": eth10gStatisticsEntryInBroadcastPackets,
       "eth10gStatisticsEntryInMulticastPackets": eth10gStatisticsEntryInMulticastPackets,
       "eth10gStatisticsEntryInCrcAlignErrors": eth10gStatisticsEntryInCrcAlignErrors,
       "eth10gStatisticsEntryInUndersizePackets": eth10gStatisticsEntryInUndersizePackets,
       "eth10gStatisticsEntryInOversizePackets": eth10gStatisticsEntryInOversizePackets,
       "eth10gStatisticsEntryInFragments": eth10gStatisticsEntryInFragments,
       "eth10gStatisticsEntryInJabbers": eth10gStatisticsEntryInJabbers,
       "eth10gStatisticsEntryInPackets64octets": eth10gStatisticsEntryInPackets64octets,
       "eth10gStatisticsEntryInPackets65to127octets": eth10gStatisticsEntryInPackets65to127octets,
       "eth10gStatisticsEntryInPackets128to255octets": eth10gStatisticsEntryInPackets128to255octets,
       "eth10gStatisticsEntryInPackets256to511octets": eth10gStatisticsEntryInPackets256to511octets,
       "eth10gStatisticsEntryInPackets512to1023octets": eth10gStatisticsEntryInPackets512to1023octets,
       "eth10gStatisticsEntryInPackets1024to1518octets": eth10gStatisticsEntryInPackets1024to1518octets,
       "eth10gStatisticsEntryOutSymbolErrors": eth10gStatisticsEntryOutSymbolErrors,
       "eth10gStatisticsEntryOutDropEvents": eth10gStatisticsEntryOutDropEvents,
       "eth10gStatisticsEntryOutOctets": eth10gStatisticsEntryOutOctets,
       "eth10gStatisticsEntryOutPackets": eth10gStatisticsEntryOutPackets,
       "eth10gStatisticsEntryOutBroadcastPackets": eth10gStatisticsEntryOutBroadcastPackets,
       "eth10gStatisticsEntryOutMulticastPackets": eth10gStatisticsEntryOutMulticastPackets,
       "eth10gStatisticsEntryOutCrcAlignErrors": eth10gStatisticsEntryOutCrcAlignErrors,
       "eth10gStatisticsEntryOutUndersizePackets": eth10gStatisticsEntryOutUndersizePackets,
       "eth10gStatisticsEntryOutOversizePackets": eth10gStatisticsEntryOutOversizePackets,
       "eth10gStatisticsEntryOutFragments": eth10gStatisticsEntryOutFragments,
       "eth10gStatisticsEntryOutJabbers": eth10gStatisticsEntryOutJabbers,
       "eth10gStatisticsEntryOutPackets64octets": eth10gStatisticsEntryOutPackets64octets,
       "eth10gStatisticsEntryOutPackets65to127octets": eth10gStatisticsEntryOutPackets65to127octets,
       "eth10gStatisticsEntryOutPackets128to255octets": eth10gStatisticsEntryOutPackets128to255octets,
       "eth10gStatisticsEntryOutPackets256to511octets": eth10gStatisticsEntryOutPackets256to511octets,
       "eth10gStatisticsEntryOutPackets512to1023octets": eth10gStatisticsEntryOutPackets512to1023octets,
       "eth10gStatisticsEntryOutPackets1024to1518octets": eth10gStatisticsEntryOutPackets1024to1518octets,
       "oduStatistics": oduStatistics,
       "oduStatisticsTable": oduStatisticsTable,
       "oduStatisticsEntry": oduStatisticsEntry,
       "oduStatisticsEntryLastClear": oduStatisticsEntryLastClear,
       "oduStatisticsEntryErroredBlocks": oduStatisticsEntryErroredBlocks,
       "oduStatisticsEntryErroredSeconds": oduStatisticsEntryErroredSeconds,
       "oduStatisticsEntrySeverelyErroredSeconds": oduStatisticsEntrySeverelyErroredSeconds,
       "oduStatisticsEntryUnavailableSeconds": oduStatisticsEntryUnavailableSeconds,
       "oduStatisticsEntryEncryptionFailRx": oduStatisticsEntryEncryptionFailRx,
       "eth40gStatistics": eth40gStatistics,
       "eth40gStatisticsTable": eth40gStatisticsTable,
       "eth40gStatisticsEntry": eth40gStatisticsEntry,
       "eth40gStatisticsEntryLastClear": eth40gStatisticsEntryLastClear,
       "eth40gStatisticsEntryLossOfSignalSeconds": eth40gStatisticsEntryLossOfSignalSeconds,
       "eth40gStatisticsEntryBitErrorFec": eth40gStatisticsEntryBitErrorFec,
       "eth40gStatisticsEntryUncorrectedBlockErrorFec": eth40gStatisticsEntryUncorrectedBlockErrorFec,
       "eth40gStatisticsEntryInSymbolErrors": eth40gStatisticsEntryInSymbolErrors,
       "eth40gStatisticsEntryInDropEvents": eth40gStatisticsEntryInDropEvents,
       "eth40gStatisticsEntryInOctets": eth40gStatisticsEntryInOctets,
       "eth40gStatisticsEntryInPackets": eth40gStatisticsEntryInPackets,
       "eth40gStatisticsEntryInBroadcastPackets": eth40gStatisticsEntryInBroadcastPackets,
       "eth40gStatisticsEntryInMulticastPackets": eth40gStatisticsEntryInMulticastPackets,
       "eth40gStatisticsEntryInCrcAlignErrors": eth40gStatisticsEntryInCrcAlignErrors,
       "eth40gStatisticsEntryInUndersizePackets": eth40gStatisticsEntryInUndersizePackets,
       "eth40gStatisticsEntryInOversizePackets": eth40gStatisticsEntryInOversizePackets,
       "eth40gStatisticsEntryInFragments": eth40gStatisticsEntryInFragments,
       "eth40gStatisticsEntryInJabbers": eth40gStatisticsEntryInJabbers,
       "eth40gStatisticsEntryInPackets64octets": eth40gStatisticsEntryInPackets64octets,
       "eth40gStatisticsEntryInPackets65to127octets": eth40gStatisticsEntryInPackets65to127octets,
       "eth40gStatisticsEntryInPackets128to255octets": eth40gStatisticsEntryInPackets128to255octets,
       "eth40gStatisticsEntryInPackets256to511octets": eth40gStatisticsEntryInPackets256to511octets,
       "eth40gStatisticsEntryInPackets512to1023octets": eth40gStatisticsEntryInPackets512to1023octets,
       "eth40gStatisticsEntryInPackets1024to1518octets": eth40gStatisticsEntryInPackets1024to1518octets,
       "eth40gStatisticsEntryOutSymbolErrors": eth40gStatisticsEntryOutSymbolErrors,
       "eth40gStatisticsEntryOutDropEvents": eth40gStatisticsEntryOutDropEvents,
       "eth40gStatisticsEntryOutOctets": eth40gStatisticsEntryOutOctets,
       "eth40gStatisticsEntryOutPackets": eth40gStatisticsEntryOutPackets,
       "eth40gStatisticsEntryOutBroadcastPackets": eth40gStatisticsEntryOutBroadcastPackets,
       "eth40gStatisticsEntryOutMulticastPackets": eth40gStatisticsEntryOutMulticastPackets,
       "eth40gStatisticsEntryOutCrcAlignErrors": eth40gStatisticsEntryOutCrcAlignErrors,
       "eth40gStatisticsEntryOutUndersizePackets": eth40gStatisticsEntryOutUndersizePackets,
       "eth40gStatisticsEntryOutOversizePackets": eth40gStatisticsEntryOutOversizePackets,
       "eth40gStatisticsEntryOutFragments": eth40gStatisticsEntryOutFragments,
       "eth40gStatisticsEntryOutJabbers": eth40gStatisticsEntryOutJabbers,
       "eth40gStatisticsEntryOutPackets64octets": eth40gStatisticsEntryOutPackets64octets,
       "eth40gStatisticsEntryOutPackets65to127octets": eth40gStatisticsEntryOutPackets65to127octets,
       "eth40gStatisticsEntryOutPackets128to255octets": eth40gStatisticsEntryOutPackets128to255octets,
       "eth40gStatisticsEntryOutPackets256to511octets": eth40gStatisticsEntryOutPackets256to511octets,
       "eth40gStatisticsEntryOutPackets512to1023octets": eth40gStatisticsEntryOutPackets512to1023octets,
       "eth40gStatisticsEntryOutPackets1024to1518octets": eth40gStatisticsEntryOutPackets1024to1518octets,
       "eth100gStatistics": eth100gStatistics,
       "eth100gStatisticsTable": eth100gStatisticsTable,
       "eth100gStatisticsEntry": eth100gStatisticsEntry,
       "eth100gStatisticsEntryLastClear": eth100gStatisticsEntryLastClear,
       "eth100gStatisticsEntryLossOfSignalSeconds": eth100gStatisticsEntryLossOfSignalSeconds,
       "eth100gStatisticsEntryBitErrorFec": eth100gStatisticsEntryBitErrorFec,
       "eth100gStatisticsEntryUncorrectedBlockErrorFec": eth100gStatisticsEntryUncorrectedBlockErrorFec,
       "eth100gStatisticsEntryInSymbolErrors": eth100gStatisticsEntryInSymbolErrors,
       "eth100gStatisticsEntryInDropEvents": eth100gStatisticsEntryInDropEvents,
       "eth100gStatisticsEntryInOctets": eth100gStatisticsEntryInOctets,
       "eth100gStatisticsEntryInPackets": eth100gStatisticsEntryInPackets,
       "eth100gStatisticsEntryInBroadcastPackets": eth100gStatisticsEntryInBroadcastPackets,
       "eth100gStatisticsEntryInMulticastPackets": eth100gStatisticsEntryInMulticastPackets,
       "eth100gStatisticsEntryInCrcAlignErrors": eth100gStatisticsEntryInCrcAlignErrors,
       "eth100gStatisticsEntryInUndersizePackets": eth100gStatisticsEntryInUndersizePackets,
       "eth100gStatisticsEntryInOversizePackets": eth100gStatisticsEntryInOversizePackets,
       "eth100gStatisticsEntryInFragments": eth100gStatisticsEntryInFragments,
       "eth100gStatisticsEntryInJabbers": eth100gStatisticsEntryInJabbers,
       "eth100gStatisticsEntryInPackets64octets": eth100gStatisticsEntryInPackets64octets,
       "eth100gStatisticsEntryInPackets65to127octets": eth100gStatisticsEntryInPackets65to127octets,
       "eth100gStatisticsEntryInPackets128to255octets": eth100gStatisticsEntryInPackets128to255octets,
       "eth100gStatisticsEntryInPackets256to511octets": eth100gStatisticsEntryInPackets256to511octets,
       "eth100gStatisticsEntryInPackets512to1023octets": eth100gStatisticsEntryInPackets512to1023octets,
       "eth100gStatisticsEntryInPackets1024to1518octets": eth100gStatisticsEntryInPackets1024to1518octets,
       "eth100gStatisticsEntryOutSymbolErrors": eth100gStatisticsEntryOutSymbolErrors,
       "eth100gStatisticsEntryOutDropEvents": eth100gStatisticsEntryOutDropEvents,
       "eth100gStatisticsEntryOutOctets": eth100gStatisticsEntryOutOctets,
       "eth100gStatisticsEntryOutPackets": eth100gStatisticsEntryOutPackets,
       "eth100gStatisticsEntryOutBroadcastPackets": eth100gStatisticsEntryOutBroadcastPackets,
       "eth100gStatisticsEntryOutMulticastPackets": eth100gStatisticsEntryOutMulticastPackets,
       "eth100gStatisticsEntryOutCrcAlignErrors": eth100gStatisticsEntryOutCrcAlignErrors,
       "eth100gStatisticsEntryOutUndersizePackets": eth100gStatisticsEntryOutUndersizePackets,
       "eth100gStatisticsEntryOutOversizePackets": eth100gStatisticsEntryOutOversizePackets,
       "eth100gStatisticsEntryOutFragments": eth100gStatisticsEntryOutFragments,
       "eth100gStatisticsEntryOutJabbers": eth100gStatisticsEntryOutJabbers,
       "eth100gStatisticsEntryOutPackets64octets": eth100gStatisticsEntryOutPackets64octets,
       "eth100gStatisticsEntryOutPackets65to127octets": eth100gStatisticsEntryOutPackets65to127octets,
       "eth100gStatisticsEntryOutPackets128to255octets": eth100gStatisticsEntryOutPackets128to255octets,
       "eth100gStatisticsEntryOutPackets256to511octets": eth100gStatisticsEntryOutPackets256to511octets,
       "eth100gStatisticsEntryOutPackets512to1023octets": eth100gStatisticsEntryOutPackets512to1023octets,
       "eth100gStatisticsEntryOutPackets1024to1518octets": eth100gStatisticsEntryOutPackets1024to1518octets,
       "otu4Statistics": otu4Statistics,
       "otu4StatisticsTable": otu4StatisticsTable,
       "otu4StatisticsEntry": otu4StatisticsEntry,
       "otu4StatisticsEntryLastClear": otu4StatisticsEntryLastClear,
       "otu4StatisticsEntryLossOfSignalSeconds": otu4StatisticsEntryLossOfSignalSeconds,
       "otu4StatisticsEntryBitErrorFec": otu4StatisticsEntryBitErrorFec,
       "otu4StatisticsEntryUncorrectedBlockErrorFec": otu4StatisticsEntryUncorrectedBlockErrorFec,
       "otu4StatisticsEntryErroredBlocks": otu4StatisticsEntryErroredBlocks,
       "otu4StatisticsEntryErroredSeconds": otu4StatisticsEntryErroredSeconds,
       "otu4StatisticsEntrySeverelyErroredSeconds": otu4StatisticsEntrySeverelyErroredSeconds,
       "otu4StatisticsEntryUnavailableSeconds": otu4StatisticsEntryUnavailableSeconds,
       "otu2Statistics": otu2Statistics,
       "otu2StatisticsTable": otu2StatisticsTable,
       "otu2StatisticsEntry": otu2StatisticsEntry,
       "otu2StatisticsEntryLastClear": otu2StatisticsEntryLastClear,
       "otu2StatisticsEntryLossOfSignalSeconds": otu2StatisticsEntryLossOfSignalSeconds,
       "otu2StatisticsEntryBitErrorFec": otu2StatisticsEntryBitErrorFec,
       "otu2StatisticsEntryUncorrectedBlockErrorFec": otu2StatisticsEntryUncorrectedBlockErrorFec,
       "otu2StatisticsEntryErroredBlocks": otu2StatisticsEntryErroredBlocks,
       "otu2StatisticsEntryErroredSeconds": otu2StatisticsEntryErroredSeconds,
       "otu2StatisticsEntrySeverelyErroredSeconds": otu2StatisticsEntrySeverelyErroredSeconds,
       "otu2StatisticsEntryUnavailableSeconds": otu2StatisticsEntryUnavailableSeconds,
       "otu2eStatistics": otu2eStatistics,
       "otu2eStatisticsTable": otu2eStatisticsTable,
       "otu2eStatisticsEntry": otu2eStatisticsEntry,
       "otu2eStatisticsEntryLastClear": otu2eStatisticsEntryLastClear,
       "otu2eStatisticsEntryLossOfSignalSeconds": otu2eStatisticsEntryLossOfSignalSeconds,
       "otu2eStatisticsEntryBitErrorFec": otu2eStatisticsEntryBitErrorFec,
       "otu2eStatisticsEntryUncorrectedBlockErrorFec": otu2eStatisticsEntryUncorrectedBlockErrorFec,
       "otu2eStatisticsEntryErroredBlocks": otu2eStatisticsEntryErroredBlocks,
       "otu2eStatisticsEntryErroredSeconds": otu2eStatisticsEntryErroredSeconds,
       "otu2eStatisticsEntrySeverelyErroredSeconds": otu2eStatisticsEntrySeverelyErroredSeconds,
       "otu2eStatisticsEntryUnavailableSeconds": otu2eStatisticsEntryUnavailableSeconds,
       "oc192Statistics": oc192Statistics,
       "oc192StatisticsTable": oc192StatisticsTable,
       "oc192StatisticsEntry": oc192StatisticsEntry,
       "oc192StatisticsEntryLastClear": oc192StatisticsEntryLastClear,
       "oc192StatisticsEntryLossOfSignalSeconds": oc192StatisticsEntryLossOfSignalSeconds,
       "oc192StatisticsEntryInCodingViolation": oc192StatisticsEntryInCodingViolation,
       "oc192StatisticsEntryInErroredSeconds": oc192StatisticsEntryInErroredSeconds,
       "oc192StatisticsEntryInSeverelyErroredSeconds": oc192StatisticsEntryInSeverelyErroredSeconds,
       "oc192StatisticsEntryInUnavailableSeconds": oc192StatisticsEntryInUnavailableSeconds,
       "oc192StatisticsEntryInSeverelyErroredFrameSecond": oc192StatisticsEntryInSeverelyErroredFrameSecond,
       "stm64Statistics": stm64Statistics,
       "stm64StatisticsTable": stm64StatisticsTable,
       "stm64StatisticsEntry": stm64StatisticsEntry,
       "stm64StatisticsEntryLastClear": stm64StatisticsEntryLastClear,
       "stm64StatisticsEntryLossOfSignalSeconds": stm64StatisticsEntryLossOfSignalSeconds,
       "stm64StatisticsEntryInBackgroundBlockError": stm64StatisticsEntryInBackgroundBlockError,
       "stm64StatisticsEntryInErroredSeconds": stm64StatisticsEntryInErroredSeconds,
       "stm64StatisticsEntryInSeverelyErroredSeconds": stm64StatisticsEntryInSeverelyErroredSeconds,
       "stm64StatisticsEntryInUnavailableSeconds": stm64StatisticsEntryInUnavailableSeconds,
       "stm64StatisticsEntryInOutOfFrameSeconds": stm64StatisticsEntryInOutOfFrameSeconds,
       "wan10gSonetStatistics": wan10gSonetStatistics,
       "wan10gSonetStatisticsTable": wan10gSonetStatisticsTable,
       "wan10gSonetStatisticsEntry": wan10gSonetStatisticsEntry,
       "wan10gSonetStatisticsEntryLastClear": wan10gSonetStatisticsEntryLastClear,
       "wan10gSonetStatisticsEntryLossOfSignalSeconds": wan10gSonetStatisticsEntryLossOfSignalSeconds,
       "wan10gSonetStatisticsEntryInCodingViolation": wan10gSonetStatisticsEntryInCodingViolation,
       "wan10gSonetStatisticsEntryInErroredSeconds": wan10gSonetStatisticsEntryInErroredSeconds,
       "wan10gSonetStatisticsEntryInSeverelyErroredSeconds": wan10gSonetStatisticsEntryInSeverelyErroredSeconds,
       "wan10gSonetStatisticsEntryInUnavailableSeconds": wan10gSonetStatisticsEntryInUnavailableSeconds,
       "wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond": wan10gSonetStatisticsEntryInSeverelyErroredFrameSecond,
       "wan10gSdhStatistics": wan10gSdhStatistics,
       "wan10gSdhStatisticsTable": wan10gSdhStatisticsTable,
       "wan10gSdhStatisticsEntry": wan10gSdhStatisticsEntry,
       "wan10gSdhStatisticsEntryLastClear": wan10gSdhStatisticsEntryLastClear,
       "wan10gSdhStatisticsEntryLossOfSignalSeconds": wan10gSdhStatisticsEntryLossOfSignalSeconds,
       "wan10gSdhStatisticsEntryInBackgroundBlockError": wan10gSdhStatisticsEntryInBackgroundBlockError,
       "wan10gSdhStatisticsEntryInErroredSeconds": wan10gSdhStatisticsEntryInErroredSeconds,
       "wan10gSdhStatisticsEntryInSeverelyErroredSeconds": wan10gSdhStatisticsEntryInSeverelyErroredSeconds,
       "wan10gSdhStatisticsEntryInUnavailableSeconds": wan10gSdhStatisticsEntryInUnavailableSeconds,
       "wan10gSdhStatisticsEntryInOutOfFrameSeconds": wan10gSdhStatisticsEntryInOutOfFrameSeconds,
       "fc8gStatistics": fc8gStatistics,
       "fc8gStatisticsTable": fc8gStatisticsTable,
       "fc8gStatisticsEntry": fc8gStatisticsEntry,
       "fc8gStatisticsEntryLastClear": fc8gStatisticsEntryLastClear,
       "fc8gStatisticsEntryLossOfSignalSeconds": fc8gStatisticsEntryLossOfSignalSeconds,
       "fc8gStatisticsEntryInSymbolErrors": fc8gStatisticsEntryInSymbolErrors,
       "fc16gStatistics": fc16gStatistics,
       "fc16gStatisticsTable": fc16gStatisticsTable,
       "fc16gStatisticsEntry": fc16gStatisticsEntry,
       "fc16gStatisticsEntryLastClear": fc16gStatisticsEntryLastClear,
       "fc16gStatisticsEntryLossOfSignalSeconds": fc16gStatisticsEntryLossOfSignalSeconds,
       "fc16gStatisticsEntryInSymbolErrors": fc16gStatisticsEntryInSymbolErrors,
       "otuc2Statistics": otuc2Statistics,
       "otuc2StatisticsTable": otuc2StatisticsTable,
       "otuc2StatisticsEntry": otuc2StatisticsEntry,
       "otuc2StatisticsEntryLastClear": otuc2StatisticsEntryLastClear,
       "otuc2StatisticsEntryLossOfSignalSeconds": otuc2StatisticsEntryLossOfSignalSeconds,
       "otuc2StatisticsEntryBitErrorFec": otuc2StatisticsEntryBitErrorFec,
       "otuc2StatisticsEntryUncorrectedBlockErrorFec": otuc2StatisticsEntryUncorrectedBlockErrorFec,
       "otuc2StatisticsEntryErroredBlocks": otuc2StatisticsEntryErroredBlocks,
       "otuc2StatisticsEntryErroredSeconds": otuc2StatisticsEntryErroredSeconds,
       "otuc2StatisticsEntrySeverelyErroredSeconds": otuc2StatisticsEntrySeverelyErroredSeconds,
       "otuc2StatisticsEntryUnavailableSeconds": otuc2StatisticsEntryUnavailableSeconds,
       "otuc3Statistics": otuc3Statistics,
       "otuc3StatisticsTable": otuc3StatisticsTable,
       "otuc3StatisticsEntry": otuc3StatisticsEntry,
       "otuc3StatisticsEntryLastClear": otuc3StatisticsEntryLastClear,
       "otuc3StatisticsEntryLossOfSignalSeconds": otuc3StatisticsEntryLossOfSignalSeconds,
       "otuc3StatisticsEntryBitErrorFec": otuc3StatisticsEntryBitErrorFec,
       "otuc3StatisticsEntryUncorrectedBlockErrorFec": otuc3StatisticsEntryUncorrectedBlockErrorFec,
       "otuc3StatisticsEntryErroredBlocks": otuc3StatisticsEntryErroredBlocks,
       "otuc3StatisticsEntryErroredSeconds": otuc3StatisticsEntryErroredSeconds,
       "otuc3StatisticsEntrySeverelyErroredSeconds": otuc3StatisticsEntrySeverelyErroredSeconds,
       "otuc3StatisticsEntryUnavailableSeconds": otuc3StatisticsEntryUnavailableSeconds,
       "ochOsStatistics": ochOsStatistics,
       "ochOsStatisticsTable": ochOsStatisticsTable,
       "ochOsStatisticsEntry": ochOsStatisticsEntry,
       "ochOsStatisticsEntryLastClear": ochOsStatisticsEntryLastClear,
       "ochOsStatisticsEntryLossOfSignalSeconds": ochOsStatisticsEntryLossOfSignalSeconds,
       "ochOsStatisticsEntryBitErrorFec": ochOsStatisticsEntryBitErrorFec,
       "ochOsStatisticsEntryUncorrectedBlockErrorFec": ochOsStatisticsEntryUncorrectedBlockErrorFec,
       "cRS": cRS,
       "cRSTable": cRSTable,
       "cRSEntry": cRSEntry,
       "cRSSrcTp": cRSSrcTp,
       "cRSDstTp": cRSDstTp,
       "cRSServiceLabel": cRSServiceLabel,
       "cRSManagedBy": cRSManagedBy,
       "cRSAliasName": cRSAliasName,
       "fiberConnection": fiberConnection,
       "fiberConnectionTable": fiberConnectionTable,
       "fiberConnectionEntry": fiberConnectionEntry,
       "fiberConnectionSrcPort": fiberConnectionSrcPort,
       "fiberConnectionDstPort": fiberConnectionDstPort,
       "fiberConnectionType": fiberConnectionType,
       "fiberConnectionFiberLabel": fiberConnectionFiberLabel,
       "fiberConnectionAliasName": fiberConnectionAliasName,
       "optical": optical,
       "ots": ots,
       "otsTable": otsTable,
       "otsEntry": otsEntry,
       "otsName": otsName,
       "otsAdminStatus": otsAdminStatus,
       "otsOperStatus": otsOperStatus,
       "otsAvailStatus": otsAvailStatus,
       "otsAliasName": otsAliasName,
       "otsSupportingRxPort": otsSupportingRxPort,
       "otsSupportingTxPort": otsSupportingTxPort,
       "otsMeasuredSpanLoss": otsMeasuredSpanLoss,
       "oms": oms,
       "omsTable": omsTable,
       "omsEntry": omsEntry,
       "omsName": omsName,
       "omsAdminStatus": omsAdminStatus,
       "omsOperStatus": omsOperStatus,
       "omsAvailStatus": omsAvailStatus,
       "omsAliasName": omsAliasName,
       "omsSupportingRxPort": omsSupportingRxPort,
       "omsSupportingTxPort": omsSupportingTxPort,
       "omsParentOtsInterface": omsParentOtsInterface,
       "omsRxOpticalPower": omsRxOpticalPower,
       "omsTxOpticalPower": omsTxOpticalPower,
       "osc": osc,
       "oscTable": oscTable,
       "oscEntry": oscEntry,
       "oscName": oscName,
       "oscAdminStatus": oscAdminStatus,
       "oscOperStatus": oscOperStatus,
       "oscAvailStatus": oscAvailStatus,
       "oscAliasName": oscAliasName,
       "oscSupportingRxPort": oscSupportingRxPort,
       "oscSupportingTxPort": oscSupportingTxPort,
       "oscParentOtsInterface": oscParentOtsInterface,
       "oscMode": oscMode,
       "oscWavelength": oscWavelength,
       "oscDataCommunication": oscDataCommunication,
       "oscRxOpticalPower": oscRxOpticalPower,
       "oscTxOpticalPower": oscTxOpticalPower,
       "gopt": gopt,
       "goptTable": goptTable,
       "goptEntry": goptEntry,
       "goptName": goptName,
       "goptAdminStatus": goptAdminStatus,
       "goptOperStatus": goptOperStatus,
       "goptAvailStatus": goptAvailStatus,
       "goptAliasName": goptAliasName,
       "goptSupportingRxPort": goptSupportingRxPort,
       "goptSupportingTxPort": goptSupportingTxPort,
       "goptRxOpticalPower": goptRxOpticalPower,
       "goptTxOpticalPower": goptTxOpticalPower,
       "omsStatistics": omsStatistics,
       "omsStatisticsTable": omsStatisticsTable,
       "omsStatisticsEntry": omsStatisticsEntry,
       "omsStatisticsEntryLastClear": omsStatisticsEntryLastClear,
       "oscStatistics": oscStatistics,
       "oscStatisticsTable": oscStatisticsTable,
       "oscStatisticsEntry": oscStatisticsEntry,
       "oscStatisticsEntryLastClear": oscStatisticsEntryLastClear,
       "goptStatistics": goptStatistics,
       "goptStatisticsTable": goptStatisticsTable,
       "goptStatisticsEntry": goptStatisticsEntry,
       "goptStatisticsEntryProtectionSwitchDuration": goptStatisticsEntryProtectionSwitchDuration,
       "goptStatisticsEntryProtectionSwitchCount": goptStatisticsEntryProtectionSwitchCount,
       "goptStatisticsEntryLossTx": goptStatisticsEntryLossTx,
       "goptStatisticsEntryLossRx": goptStatisticsEntryLossRx,
       "goptStatisticsEntryLastClear": goptStatisticsEntryLastClear,
       "lldp": lldp,
       "lldpStatusNe": lldpStatusNe,
       "performance": performance,
       "performanceInfo": performanceInfo,
       "performancePmdaystart": performancePmdaystart,
       "performanceStatisticsEnable": performanceStatisticsEnable,
       "pmPoint": pmPoint,
       "pmPointTable": pmPointTable,
       "pmPointEntry": pmPointEntry,
       "pmPointPmEntity": pmPointPmEntity,
       "pmPointPmpType": pmPointPmpType,
       "pmPointPmTimePeriod": pmPointPmTimePeriod,
       "pmPointSupervisionSwitch": pmPointSupervisionSwitch,
       "pmPointThresholdingSwitch": pmPointThresholdingSwitch,
       "pmPointHistoryRecording": pmPointHistoryRecording,
       "pmData": pmData,
       "pmDataCurrentTable": pmDataCurrentTable,
       "pmDataCurrentEntry": pmDataCurrentEntry,
       "pmDataCurrentMonitoringDateTime": pmDataCurrentMonitoringDateTime,
       "pmDataCurrentPmParameter": pmDataCurrentPmParameter,
       "pmDataCurrentPmValue": pmDataCurrentPmValue,
       "pmDataCurrentPmUnit": pmDataCurrentPmUnit,
       "pmDataCurrentValidity": pmDataCurrentValidity,
       "pmDataLatestHistoryTable": pmDataLatestHistoryTable,
       "pmDataLatestHistoryEntry": pmDataLatestHistoryEntry,
       "pmDataLatestHistoryMonitoringDateTime": pmDataLatestHistoryMonitoringDateTime,
       "pmDataLatestHistoryPmParameter": pmDataLatestHistoryPmParameter,
       "pmDataLatestHistoryPmValue": pmDataLatestHistoryPmValue,
       "pmDataLatestHistoryPmUnit": pmDataLatestHistoryPmUnit,
       "pmDataLatestHistoryValidity": pmDataLatestHistoryValidity,
       "pmDataHistoryTable": pmDataHistoryTable,
       "pmDataHistoryEntry": pmDataHistoryEntry,
       "pmDataHistoryRecordIndex": pmDataHistoryRecordIndex,
       "pmDataHistoryMonitoringDateTime": pmDataHistoryMonitoringDateTime,
       "pmDataHistoryPmParameter": pmDataHistoryPmParameter,
       "pmDataHistoryPmValue": pmDataHistoryPmValue,
       "pmDataHistoryPmUnit": pmDataHistoryPmUnit,
       "pmDataHistoryValidity": pmDataHistoryValidity,
       "pmThresholdsValue": pmThresholdsValue,
       "pmThresholdsValueTable": pmThresholdsValueTable,
       "pmThresholdsValueEntry": pmThresholdsValueEntry,
       "pmThresholdsValuePmParameter": pmThresholdsValuePmParameter,
       "pmThresholdsValuePmHighThreshold": pmThresholdsValuePmHighThreshold,
       "pmThresholdsValuePmLowThreshold": pmThresholdsValuePmLowThreshold,
       "pmThresholdsValuePmUnit": pmThresholdsValuePmUnit,
       "networking": networking,
       "networkingInfo": networkingInfo,
       "networkingSourceAddressSelectMode": networkingSourceAddressSelectMode,
       "interface": interface,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceIfName": interfaceIfName,
       "interfaceIfDescription": interfaceIfDescription,
       "interfaceIfType": interfaceIfType,
       "interfaceAdminStatus": interfaceAdminStatus,
       "interfaceOperStatus": interfaceOperStatus,
       "interfaceAvailStatus": interfaceAvailStatus,
       "interfaceAliasName": interfaceAliasName,
       "ethernet": ethernet,
       "ethernetTable": ethernetTable,
       "ethernetEntry": ethernetEntry,
       "ethernetAutoNegotiation": ethernetAutoNegotiation,
       "ethernetDuplexMode": ethernetDuplexMode,
       "ethernetOperationalDuplexMode": ethernetOperationalDuplexMode,
       "ethernetRate": ethernetRate,
       "ethernetOperationalEthernetRate": ethernetOperationalEthernetRate,
       "ethernetFlowControl": ethernetFlowControl,
       "ethernetOperationalFlowControl": ethernetOperationalFlowControl,
       "ethernetMacAddress": ethernetMacAddress,
       "ethernetAliasName": ethernetAliasName,
       "ppp": ppp,
       "pppTable": pppTable,
       "pppEntry": pppEntry,
       "pppType": pppType,
       "pppPfRef": pppPfRef,
       "pppResourceRef": pppResourceRef,
       "pppAliasName": pppAliasName,
       "ipv4": ipv4,
       "ipv4Table": ipv4Table,
       "ipv4Entry": ipv4Entry,
       "ipv4Forwarding": ipv4Forwarding,
       "ipv4Mtu": ipv4Mtu,
       "ipv4AddressAssignmentMethod": ipv4AddressAssignmentMethod,
       "ipAddress": ipAddress,
       "ipAddressTable": ipAddressTable,
       "ipAddressEntry": ipAddressEntry,
       "ipAddressIp": ipAddressIp,
       "ipAddressOrigin": ipAddressOrigin,
       "ipAddressPrefixLength": ipAddressPrefixLength,
       "ipUnnumbered": ipUnnumbered,
       "ipUnnumberedTable": ipUnnumberedTable,
       "ipUnnumberedEntry": ipUnnumberedEntry,
       "ipUnnumberedUnnumEnabled": ipUnnumberedUnnumEnabled,
       "ipUnnumberedParentInterface": ipUnnumberedParentInterface,
       "routingProtocol": routingProtocol,
       "routingProtocolTable": routingProtocolTable,
       "routingProtocolEntry": routingProtocolEntry,
       "routingProtocolRtpType": routingProtocolRtpType,
       "routingProtocolRtpName": routingProtocolRtpName,
       "routingProtocolDescription": routingProtocolDescription,
       "staticRoute": staticRoute,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteDestinationPrefix": staticRouteDestinationPrefix,
       "staticRouteDescription": staticRouteDescription,
       "staticRouteAdvertised": staticRouteAdvertised,
       "nextHop": nextHop,
       "nextHopTable": nextHopTable,
       "nextHopEntry": nextHopEntry,
       "nextHopIndex": nextHopIndex,
       "nextHopOutgoingInterface": nextHopOutgoingInterface,
       "nextHopAddress": nextHopAddress,
       "nextHopMetric": nextHopMetric,
       "ospf": ospf,
       "ospfTable": ospfTable,
       "ospfEntry": ospfEntry,
       "ospfRouterId": ospfRouterId,
       "ospfDescription": ospfDescription,
       "ospfAsbr": ospfAsbr,
       "ospfAdminStatus": ospfAdminStatus,
       "ospfOperStatus": ospfOperStatus,
       "ospfAliasName": ospfAliasName,
       "ospfArea": ospfArea,
       "ospfAreaTable": ospfAreaTable,
       "ospfAreaEntry": ospfAreaEntry,
       "ospfAreaId": ospfAreaId,
       "ospfAreaAdminStatus": ospfAreaAdminStatus,
       "ospfAreaOperStatus": ospfAreaOperStatus,
       "ospfAreaAliasName": ospfAreaAliasName,
       "ospfAreaType": ospfAreaType,
       "ospfInterface": ospfInterface,
       "ospfInterfaceTable": ospfInterfaceTable,
       "ospfInterfaceEntry": ospfInterfaceEntry,
       "ospfInterfaceOspfIfName": ospfInterfaceOspfIfName,
       "ospfInterfaceOspfLinkpf": ospfInterfaceOspfLinkpf,
       "ospfInterfaceOspfCost": ospfInterfaceOspfCost,
       "ospfInterfaceOspfIfRouting": ospfInterfaceOspfIfRouting,
       "ospfInterfaceOspfNetworkType": ospfInterfaceOspfNetworkType,
       "ospfAdjacency": ospfAdjacency,
       "ospfAdjacencyTable": ospfAdjacencyTable,
       "ospfAdjacencyEntry": ospfAdjacencyEntry,
       "ospfAdjacencyOspfNeighborAddress": ospfAdjacencyOspfNeighborAddress,
       "ospfAdjacencyNeighborRouterId": ospfAdjacencyNeighborRouterId,
       "ospfAdjacencyOspfAdjStatus": ospfAdjacencyOspfAdjStatus,
       "rib": rib,
       "ribTable": ribTable,
       "ribEntry": ribEntry,
       "ribName": ribName,
       "ribAddressFamily": ribAddressFamily,
       "ribDefaultRib": ribDefaultRib,
       "ribDescription": ribDescription,
       "route": route,
       "routeTable": routeTable,
       "routeEntry": routeEntry,
       "routeSourceProtocol": routeSourceProtocol,
       "routeDestinationPrefix": routeDestinationPrefix,
       "routeDescription": routeDescription,
       "routePreference": routePreference,
       "routeActive": routeActive,
       "profiles": profiles,
       "pppProfile": pppProfile,
       "pppProfileTable": pppProfileTable,
       "pppProfileEntry": pppProfileEntry,
       "pppProfilePppPfName": pppProfilePppPfName,
       "pppProfilePppFcsLength": pppProfilePppFcsLength,
       "pppProfilePppMru": pppProfilePppMru,
       "pppProfilePppRestartTimer": pppProfilePppRestartTimer,
       "pppProfilePppMaxFailure": pppProfilePppMaxFailure,
       "ospfLinkProfile": ospfLinkProfile,
       "ospfLinkProfileTable": ospfLinkProfileTable,
       "ospfLinkProfileEntry": ospfLinkProfileEntry,
       "ospfLinkProfileOspfLinkpfName": ospfLinkProfileOspfLinkpfName,
       "ospfLinkProfileHelloInterval": ospfLinkProfileHelloInterval,
       "ospfLinkProfileRouterDeadInterval": ospfLinkProfileRouterDeadInterval,
       "ospfLinkProfileRetransmissionInterval": ospfLinkProfileRetransmissionInterval,
       "oscx": oscx,
       "oscxTable": oscxTable,
       "oscxEntry": oscxEntry,
       "oscxChannel": oscxChannel,
       "oscxResourceRef": oscxResourceRef,
       "oscxAliasName": oscxAliasName,
       "security": security,
       "securityInfo": securityInfo,
       "securitySshPublicKey": securitySshPublicKey,
       "securitySshPublicKeyFingerprint": securitySshPublicKeyFingerprint,
       "securityPreLoginMessage": securityPreLoginMessage,
       "securityWarningMessage": securityWarningMessage,
       "securityAaaAuthenticationMethod": securityAaaAuthenticationMethod,
       "securitySystemFips": securitySystemFips,
       "securityHttpSupport": securityHttpSupport,
       "user": user,
       "userTable": userTable,
       "userEntry": userEntry,
       "userName": userName,
       "userPassword": userPassword,
       "userClass": userClass,
       "userMaxInvalidLogin": userMaxInvalidLogin,
       "userSuspensionTime": userSuspensionTime,
       "userTimeout": userTimeout,
       "userPasswordAgingInterval": userPasswordAgingInterval,
       "userPasswordExpirationDate": userPasswordExpirationDate,
       "userAdminStatus": userAdminStatus,
       "userStatus": userStatus,
       "userMaxSessions": userMaxSessions,
       "userLastLoginDate": userLastLoginDate,
       "userAaaType": userAaaType,
       "session": session,
       "sessionTable": sessionTable,
       "sessionEntry": sessionEntry,
       "sessionId": sessionId,
       "sessionUser": sessionUser,
       "sessionType": sessionType,
       "sessionProtocol": sessionProtocol,
       "sessionCreatedTime": sessionCreatedTime,
       "aaaServer": aaaServer,
       "aaaServerTable": aaaServerTable,
       "aaaServerEntry": aaaServerEntry,
       "aaaServerServerName": aaaServerServerName,
       "aaaServerServerPriority": aaaServerServerPriority,
       "aaaServerProtocolSupported": aaaServerProtocolSupported,
       "aaaServerServerIp": aaaServerServerIp,
       "aaaServerServerPort": aaaServerServerPort,
       "aaaServerSharedSecret": aaaServerSharedSecret,
       "aaaServerRoleSupported": aaaServerRoleSupported,
       "aaaServerAdminStatus": aaaServerAdminStatus,
       "aaaServerTimeOut": aaaServerTimeOut,
       "aaaServerRetry": aaaServerRetry,
       "keySyncSession": keySyncSession,
       "keySyncSessionTable": keySyncSessionTable,
       "keySyncSessionEntry": keySyncSessionEntry,
       "keySyncSessionId": keySyncSessionId,
       "keySyncSessionAdminStatus": keySyncSessionAdminStatus,
       "keySyncSessionSessionStatus": keySyncSessionSessionStatus,
       "keySyncSessionRemoteIp": keySyncSessionRemoteIp,
       "keySyncSessionRemotePort": keySyncSessionRemotePort,
       "keySyncSessionLocalIp": keySyncSessionLocalIp,
       "keySyncSessionLocalPort": keySyncSessionLocalPort,
       "keySyncSessionSourceAddressFrom": keySyncSessionSourceAddressFrom,
       "keySyncSessionConnectedTime": keySyncSessionConnectedTime,
       "keySyncSessionType": keySyncSessionType,
       "keySyncSessionAuthType": keySyncSessionAuthType,
       "keySyncSessionLocalCertificate": keySyncSessionLocalCertificate,
       "pskMap": pskMap,
       "pskMapTable": pskMapTable,
       "pskMapEntry": pskMapEntry,
       "pskMapPskIdentity": pskMapPskIdentity,
       "pskMapKey": pskMapKey,
       "pskMapPskStatus": pskMapPskStatus,
       "pskMapPskInfo": pskMapPskInfo,
       "pskMapWarningTimer": pskMapWarningTimer,
       "pskMapCriticalTimer": pskMapCriticalTimer,
       "pskMapTrafficOffTimer": pskMapTrafficOffTimer,
       "pskMapEffectiveTimestamp": pskMapEffectiveTimestamp,
       "key": key,
       "keyTable": keyTable,
       "keyEntry": keyEntry,
       "keyName": keyName,
       "keyAlgorithmIdentifier": keyAlgorithmIdentifier,
       "keyPublicKey": keyPublicKey,
       "certificate": certificate,
       "certificateTable": certificateTable,
       "certificateEntry": certificateEntry,
       "certificateName": certificateName,
       "certificateVersion": certificateVersion,
       "certificateSerialNumber": certificateSerialNumber,
       "certificateSignatureAlgorithm": certificateSignatureAlgorithm,
       "certificateIssuer": certificateIssuer,
       "certificateValidFrom": certificateValidFrom,
       "certificateValidTo": certificateValidTo,
       "certificateSubject": certificateSubject,
       "certificatePublicKeyAlgorithm": certificatePublicKeyAlgorithm,
       "trustedCertificateGroup": trustedCertificateGroup,
       "trustedCertificateGroupTable": trustedCertificateGroupTable,
       "trustedCertificateGroupEntry": trustedCertificateGroupEntry,
       "trustedCertificateGroupName": trustedCertificateGroupName,
       "trustedCertificate": trustedCertificate,
       "trustedCertificateTable": trustedCertificateTable,
       "trustedCertificateEntry": trustedCertificateEntry,
       "trustedCertificateName": trustedCertificateName,
       "trustedCertificateVersion": trustedCertificateVersion,
       "trustedCertificateSerialNumber": trustedCertificateSerialNumber,
       "trustedCertificateSignatureAlgorithm": trustedCertificateSignatureAlgorithm,
       "trustedCertificateIssuer": trustedCertificateIssuer,
       "trustedCertificateValidFrom": trustedCertificateValidFrom,
       "trustedCertificateValidTo": trustedCertificateValidTo,
       "trustedCertificateSubject": trustedCertificateSubject,
       "trustedCertificatePublicKeyAlgorithm": trustedCertificatePublicKeyAlgorithm,
       "nbi": nbi,
       "snmp": snmp,
       "snmpv3": snmpv3,
       "snmpv3Table": snmpv3Table,
       "snmpv3Entry": snmpv3Entry,
       "snmpv3UserSecLevel": snmpv3UserSecLevel,
       "snmpv3AuthProtocol": snmpv3AuthProtocol,
       "snmpv3AuthPassphrase": snmpv3AuthPassphrase,
       "snmpv3PrivProtocol": snmpv3PrivProtocol,
       "snmpv3PrivPassphrase": snmpv3PrivPassphrase,
       "snmpInfo": snmpInfo,
       "snmpEngineId": snmpEngineId,
       "snmpCommunity": snmpCommunity,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityCommunityString": snmpCommunityCommunityString,
       "snmpCommunityCommunityStringAccess": snmpCommunityCommunityStringAccess,
       "snmpTarget": snmpTarget,
       "snmpTargetTable": snmpTargetTable,
       "snmpTargetEntry": snmpTargetEntry,
       "snmpTargetSnmpVersion": snmpTargetSnmpVersion,
       "snmpTargetSnmpv3User": snmpTargetSnmpv3User,
       "snmpTargetTargetName": snmpTargetTargetName,
       "snmpTargetTargetIp": snmpTargetTargetIp,
       "snmpTargetTargetPort": snmpTargetTargetPort,
       "snmpTargetTargetTransport": snmpTargetTargetTransport,
       "snmpTargetTrapCommunityString": snmpTargetTrapCommunityString,
       "cli": cli,
       "cliConfig": cliConfig,
       "cliConfigTable": cliConfigTable,
       "cliConfigEntry": cliConfigEntry,
       "cliConfigCliLines": cliConfigCliLines,
       "cliConfigCliColumns": cliConfigCliColumns,
       "cliConfigMaxHistorySize": cliConfigMaxHistorySize,
       "cliConfigInteractiveMode": cliConfigInteractiveMode,
       "restconf": restconf,
       "restconfRestHttpSupport": restconfRestHttpSupport,
       "restconfRestHttpsSupport": restconfRestHttpsSupport,
       "restconfRestSessionTimeout": restconfRestSessionTimeout,
       "cliAlias": cliAlias,
       "cliAliasTable": cliAliasTable,
       "cliAliasEntry": cliAliasEntry,
       "cliAliasName": cliAliasName,
       "cliAliasValue": cliAliasValue,
       "cliScript": cliScript,
       "cliScriptTable": cliScriptTable,
       "cliScriptEntry": cliScriptEntry,
       "cliScriptScriptName": cliScriptScriptName,
       "cliScriptDescription": cliScriptDescription,
       "filesw": filesw,
       "softwareload": softwareload,
       "softwareloadTable": softwareloadTable,
       "softwareloadEntry": softwareloadEntry,
       "softwareloadSwloadId": softwareloadSwloadId,
       "softwareloadSwloadState": softwareloadSwloadState,
       "softwareloadSwloadVersion": softwareloadSwloadVersion,
       "softwareloadSwloadVendor": softwareloadSwloadVendor,
       "softwareloadSwloadProduct": softwareloadSwloadProduct,
       "softwareloadSwloadLabel": softwareloadSwloadLabel,
       "database": database,
       "databaseTable": databaseTable,
       "databaseEntry": databaseEntry,
       "databaseId": databaseId,
       "databaseState": databaseState,
       "databaseVersion": databaseVersion,
       "databaseVendor": databaseVendor,
       "databaseProduct": databaseProduct,
       "databaseBackupTime": databaseBackupTime,
       "fwVersionMap": fwVersionMap,
       "fwVersionMapTable": fwVersionMapTable,
       "fwVersionMapEntry": fwVersionMapEntry,
       "fwVersionMapDeviceName": fwVersionMapDeviceName,
       "fwVersionMapDeviceFwVersion": fwVersionMapDeviceFwVersion,
       "currentFwVersion": currentFwVersion,
       "currentFwVersionTable": currentFwVersionTable,
       "currentFwVersionEntry": currentFwVersionEntry,
       "currentFwVersionEquipmentEntity": currentFwVersionEquipmentEntity,
       "currentFwVersionFwEquipmentType": currentFwVersionFwEquipmentType,
       "currentFwVersionDeviceName": currentFwVersionDeviceName,
       "currentFwVersionDeviceFwVersion": currentFwVersionDeviceFwVersion,
       "currentFwVersionFwState": currentFwVersionFwState,
       "rollbackPoint": rollbackPoint,
       "rollbackPointTable": rollbackPointTable,
       "rollbackPointEntry": rollbackPointEntry,
       "rollbackPointId": rollbackPointId,
       "rollbackPointCreationTime": rollbackPointCreationTime,
       "rollbackPointCreationTrigger": rollbackPointCreationTrigger,
       "rollbackPointDescription": rollbackPointDescription,
       "rollbackPointType": rollbackPointType,
       "logServer": logServer,
       "logServerTable": logServerTable,
       "logServerEntry": logServerEntry,
       "logServerName": logServerName,
       "logServerIpAddress": logServerIpAddress,
       "logServerTransport": logServerTransport,
       "logServerPort": logServerPort,
       "logServerDestinationFacilityType": logServerDestinationFacilityType,
       "logServerDestinationFacility": logServerDestinationFacility,
       "logFacility": logFacility,
       "logFacilityTable": logFacilityTable,
       "logFacilityEntry": logFacilityEntry,
       "logFacilityLogSelectorFacility": logFacilityLogSelectorFacility,
       "logFacilityLogSelectorSeverity": logFacilityLogSelectorSeverity,
       "logFacilityCompareOp": logFacilityCompareOp,
       "timeManager": timeManager,
       "timeManagerInfo": timeManagerInfo,
       "timeManagerTimezone": timeManagerTimezone,
       "timeManagerCurrentTime": timeManagerCurrentTime,
       "timeManagerLastStartTime": timeManagerLastStartTime,
       "timeManagerUpTime": timeManagerUpTime,
       "timeManagerTimeSourceState": timeManagerTimeSourceState,
       "ntp": ntp,
       "ntpEnabled": ntpEnabled,
       "ntpCurrentTimeSource": ntpCurrentTimeSource,
       "ntpAssociation": ntpAssociation,
       "ntpAssociationTable": ntpAssociationTable,
       "ntpAssociationEntry": ntpAssociationEntry,
       "ntpAssociationSource": ntpAssociationSource,
       "ntpAssociationType": ntpAssociationType,
       "ntpAssociationPreferredNtpAssociation": ntpAssociationPreferredNtpAssociation,
       "ntpAssociationNtpAdminState": ntpAssociationNtpAdminState,
       "ntpAssociationStatus": ntpAssociationStatus,
       "ntpAssociationStatusTable": ntpAssociationStatusTable,
       "ntpAssociationStatusEntry": ntpAssociationStatusEntry,
       "ntpAssociationStatusNtpAssociationRefid": ntpAssociationStatusNtpAssociationRefid,
       "ntpAssociationStatusNtpStratum": ntpAssociationStatusNtpStratum,
       "ntpAssociationStatusNtpPollingInterval": ntpAssociationStatusNtpPollingInterval,
       "ntpAssociationStatusNtpPrecision": ntpAssociationStatusNtpPrecision,
       "ntpAssociationStatusNtpAssociationOffset": ntpAssociationStatusNtpAssociationOffset,
       "ntpAssociationStatusNtpAssociationReach": ntpAssociationStatusNtpAssociationReach,
       "ntpAssociationStatusNtpAssociationDelay": ntpAssociationStatusNtpAssociationDelay,
       "ntpAssociationStatusNtpAssociationDispersion": ntpAssociationStatusNtpAssociationDispersion,
       "ztc": ztc,
       "ztcInfo": ztcInfo,
       "ztcEnabled": ztcEnabled,
       "ztcStatus": ztcStatus,
       "common": common,
       "bitErrorRatePreFec": bitErrorRatePreFec,
       "bitErrorRatePreFecTable": bitErrorRatePreFecTable,
       "bitErrorRatePreFecEntry": bitErrorRatePreFecEntry,
       "bitErrorRatePreFecInstant": bitErrorRatePreFecInstant,
       "bitErrorRatePreFecAvg": bitErrorRatePreFecAvg,
       "bitErrorRatePreFecMin": bitErrorRatePreFecMin,
       "bitErrorRatePreFecMax": bitErrorRatePreFecMax,
       "bitErrorRatePostFec": bitErrorRatePostFec,
       "bitErrorRatePostFecTable": bitErrorRatePostFecTable,
       "bitErrorRatePostFecEntry": bitErrorRatePostFecEntry,
       "bitErrorRatePostFecInstant": bitErrorRatePostFecInstant,
       "bitErrorRatePostFecAvg": bitErrorRatePostFecAvg,
       "bitErrorRatePostFecMin": bitErrorRatePostFecMin,
       "bitErrorRatePostFecMax": bitErrorRatePostFecMax,
       "inUtilization": inUtilization,
       "inUtilizationTable": inUtilizationTable,
       "inUtilizationEntry": inUtilizationEntry,
       "inUtilizationInstant": inUtilizationInstant,
       "inUtilizationAvg": inUtilizationAvg,
       "inUtilizationMin": inUtilizationMin,
       "inUtilizationMax": inUtilizationMax,
       "outUtilization": outUtilization,
       "outUtilizationTable": outUtilizationTable,
       "outUtilizationEntry": outUtilizationEntry,
       "outUtilizationInstant": outUtilizationInstant,
       "outUtilizationAvg": outUtilizationAvg,
       "outUtilizationMin": outUtilizationMin,
       "outUtilizationMax": outUtilizationMax,
       "oduDelay": oduDelay,
       "oduDelayTable": oduDelayTable,
       "oduDelayEntry": oduDelayEntry,
       "oduDelayInstant": oduDelayInstant,
       "oduDelayAvg": oduDelayAvg,
       "oduDelayMin": oduDelayMin,
       "oduDelayMax": oduDelayMax,
       "inOpticalPower": inOpticalPower,
       "inOpticalPowerTable": inOpticalPowerTable,
       "inOpticalPowerEntry": inOpticalPowerEntry,
       "inOpticalPowerInstant": inOpticalPowerInstant,
       "inOpticalPowerAvg": inOpticalPowerAvg,
       "inOpticalPowerMin": inOpticalPowerMin,
       "inOpticalPowerMax": inOpticalPowerMax,
       "outOpticalPower": outOpticalPower,
       "outOpticalPowerTable": outOpticalPowerTable,
       "outOpticalPowerEntry": outOpticalPowerEntry,
       "outOpticalPowerInstant": outOpticalPowerInstant,
       "outOpticalPowerAvg": outOpticalPowerAvg,
       "outOpticalPowerMin": outOpticalPowerMin,
       "outOpticalPowerMax": outOpticalPowerMax,
       "differentialGroupDelay": differentialGroupDelay,
       "differentialGroupDelayTable": differentialGroupDelayTable,
       "differentialGroupDelayEntry": differentialGroupDelayEntry,
       "differentialGroupDelayInstant": differentialGroupDelayInstant,
       "differentialGroupDelayAvg": differentialGroupDelayAvg,
       "differentialGroupDelayMin": differentialGroupDelayMin,
       "differentialGroupDelayMax": differentialGroupDelayMax,
       "chromaticDispersion": chromaticDispersion,
       "chromaticDispersionTable": chromaticDispersionTable,
       "chromaticDispersionEntry": chromaticDispersionEntry,
       "chromaticDispersionInstant": chromaticDispersionInstant,
       "chromaticDispersionAvg": chromaticDispersionAvg,
       "chromaticDispersionMin": chromaticDispersionMin,
       "chromaticDispersionMax": chromaticDispersionMax,
       "osnr": osnr,
       "osnrTable": osnrTable,
       "osnrEntry": osnrEntry,
       "osnrInstant": osnrInstant,
       "osnrAvg": osnrAvg,
       "osnrMin": osnrMin,
       "osnrMax": osnrMax,
       "qFactor": qFactor,
       "qFactorTable": qFactorTable,
       "qFactorEntry": qFactorEntry,
       "qFactorInstant": qFactorInstant,
       "qFactorAvg": qFactorAvg,
       "qFactorMin": qFactorMin,
       "qFactorMax": qFactorMax,
       "polarizationDependentLoss": polarizationDependentLoss,
       "polarizationDependentLossTable": polarizationDependentLossTable,
       "polarizationDependentLossEntry": polarizationDependentLossEntry,
       "polarizationDependentLossInstant": polarizationDependentLossInstant,
       "polarizationDependentLossAvg": polarizationDependentLossAvg,
       "polarizationDependentLossMin": polarizationDependentLossMin,
       "polarizationDependentLossMax": polarizationDependentLossMax,
       "inOpticalFrequency": inOpticalFrequency,
       "inOpticalFrequencyTable": inOpticalFrequencyTable,
       "inOpticalFrequencyEntry": inOpticalFrequencyEntry,
       "inOpticalFrequencyInstant": inOpticalFrequencyInstant,
       "inOpticalFrequencyAvg": inOpticalFrequencyAvg,
       "inOpticalFrequencyMin": inOpticalFrequencyMin,
       "inOpticalFrequencyMax": inOpticalFrequencyMax,
       "outOpticalFrequency": outOpticalFrequency,
       "outOpticalFrequencyTable": outOpticalFrequencyTable,
       "outOpticalFrequencyEntry": outOpticalFrequencyEntry,
       "outOpticalFrequencyInstant": outOpticalFrequencyInstant,
       "outOpticalFrequencyAvg": outOpticalFrequencyAvg,
       "outOpticalFrequencyMin": outOpticalFrequencyMin,
       "outOpticalFrequencyMax": outOpticalFrequencyMax,
       "inOpticalPowerLaneHigh": inOpticalPowerLaneHigh,
       "inOpticalPowerLaneHighTable": inOpticalPowerLaneHighTable,
       "inOpticalPowerLaneHighEntry": inOpticalPowerLaneHighEntry,
       "inOpticalPowerLaneHighInstant": inOpticalPowerLaneHighInstant,
       "inOpticalPowerLaneHighAvg": inOpticalPowerLaneHighAvg,
       "inOpticalPowerLaneHighMin": inOpticalPowerLaneHighMin,
       "inOpticalPowerLaneHighMax": inOpticalPowerLaneHighMax,
       "inOpticalPowerLaneLow": inOpticalPowerLaneLow,
       "inOpticalPowerLaneLowTable": inOpticalPowerLaneLowTable,
       "inOpticalPowerLaneLowEntry": inOpticalPowerLaneLowEntry,
       "inOpticalPowerLaneLowInstant": inOpticalPowerLaneLowInstant,
       "inOpticalPowerLaneLowAvg": inOpticalPowerLaneLowAvg,
       "inOpticalPowerLaneLowMin": inOpticalPowerLaneLowMin,
       "inOpticalPowerLaneLowMax": inOpticalPowerLaneLowMax,
       "inOpticalPowerLaneTotal": inOpticalPowerLaneTotal,
       "inOpticalPowerLaneTotalTable": inOpticalPowerLaneTotalTable,
       "inOpticalPowerLaneTotalEntry": inOpticalPowerLaneTotalEntry,
       "inOpticalPowerLaneTotalInstant": inOpticalPowerLaneTotalInstant,
       "inOpticalPowerLaneTotalAvg": inOpticalPowerLaneTotalAvg,
       "inOpticalPowerLaneTotalMin": inOpticalPowerLaneTotalMin,
       "inOpticalPowerLaneTotalMax": inOpticalPowerLaneTotalMax,
       "outOpticalPowerLaneHigh": outOpticalPowerLaneHigh,
       "outOpticalPowerLaneHighTable": outOpticalPowerLaneHighTable,
       "outOpticalPowerLaneHighEntry": outOpticalPowerLaneHighEntry,
       "outOpticalPowerLaneHighInstant": outOpticalPowerLaneHighInstant,
       "outOpticalPowerLaneHighAvg": outOpticalPowerLaneHighAvg,
       "outOpticalPowerLaneHighMin": outOpticalPowerLaneHighMin,
       "outOpticalPowerLaneHighMax": outOpticalPowerLaneHighMax,
       "outOpticalPowerLaneLow": outOpticalPowerLaneLow,
       "outOpticalPowerLaneLowTable": outOpticalPowerLaneLowTable,
       "outOpticalPowerLaneLowEntry": outOpticalPowerLaneLowEntry,
       "outOpticalPowerLaneLowInstant": outOpticalPowerLaneLowInstant,
       "outOpticalPowerLaneLowAvg": outOpticalPowerLaneLowAvg,
       "outOpticalPowerLaneLowMin": outOpticalPowerLaneLowMin,
       "outOpticalPowerLaneLowMax": outOpticalPowerLaneLowMax,
       "outOpticalPowerLaneTotal": outOpticalPowerLaneTotal,
       "outOpticalPowerLaneTotalTable": outOpticalPowerLaneTotalTable,
       "outOpticalPowerLaneTotalEntry": outOpticalPowerLaneTotalEntry,
       "outOpticalPowerLaneTotalInstant": outOpticalPowerLaneTotalInstant,
       "outOpticalPowerLaneTotalAvg": outOpticalPowerLaneTotalAvg,
       "outOpticalPowerLaneTotalMin": outOpticalPowerLaneTotalMin,
       "outOpticalPowerLaneTotalMax": outOpticalPowerLaneTotalMax,
       "moduleTemperature": moduleTemperature,
       "moduleTemperatureTable": moduleTemperatureTable,
       "moduleTemperatureEntry": moduleTemperatureEntry,
       "moduleTemperatureInstant": moduleTemperatureInstant,
       "moduleTemperatureAvg": moduleTemperatureAvg,
       "moduleTemperatureMin": moduleTemperatureMin,
       "moduleTemperatureMax": moduleTemperatureMax,
       "inletTemperature": inletTemperature,
       "inletTemperatureTable": inletTemperatureTable,
       "inletTemperatureEntry": inletTemperatureEntry,
       "inletTemperatureInstant": inletTemperatureInstant,
       "inletTemperatureAvg": inletTemperatureAvg,
       "inletTemperatureMin": inletTemperatureMin,
       "inletTemperatureMax": inletTemperatureMax,
       "outletTemperature": outletTemperature,
       "outletTemperatureTable": outletTemperatureTable,
       "outletTemperatureEntry": outletTemperatureEntry,
       "outletTemperatureInstant": outletTemperatureInstant,
       "outletTemperatureAvg": outletTemperatureAvg,
       "outletTemperatureMin": outletTemperatureMin,
       "outletTemperatureMax": outletTemperatureMax}
)
