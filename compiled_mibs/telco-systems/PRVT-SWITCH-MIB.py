# SNMP MIB module (PRVT-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SWITCH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:46 2025
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

(ifAdminStatus,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus")

(privateVendorOID,) = mibBuilder.importSymbols(
    "PRIV-VENDORDEF-MIB",
    "privateVendorOID")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtSwitchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100)
)
if mibBuilder.loadTexts:
    prvtSwitchMib.setRevisions(
        ("2009-06-22 00:00",
         "2009-04-14 00:00",
         "2009-03-08 00:00",
         "2009-02-20 00:00",
         "2009-01-12 00:00",
         "2008-09-25 00:00",
         "2008-03-28 00:00",
         "2008-02-28 00:00",
         "2007-12-28 00:00",
         "2007-12-12 00:00",
         "2007-09-26 00:00",
         "2007-04-24 00:00",
         "2007-02-06 00:00",
         "2006-10-25 00:00",
         "2006-07-02 00:00",
         "2006-06-14 00:00",
         "2006-04-20 00:00",
         "2006-02-10 00:00",
         "2006-02-02 00:00",
         "2005-12-22 00:00",
         "2005-12-08 00:00",
         "2005-10-03 00:00",
         "2005-09-26 00:00",
         "2005-09-07 00:00",
         "2005-07-20 00:00",
         "2005-07-08 00:00",
         "2005-03-07 00:00",
         "2005-02-16 00:00",
         "2005-02-01 00:00",
         "2004-06-29 00:00",
         "2004-05-03 00:00",
         "2004-03-03 00:00",
         "2004-02-03 00:00",
         "2003-11-18 00:00",
         "2003-10-16 00:00",
         "2003-09-09 00:00",
         "2003-07-02 00:00",
         "2003-05-06 00:00",
         "2002-12-12 00:00",
         "2002-12-01 00:00",
         "2002-11-21 00:00",
         "2002-11-17 00:00",
         "2002-09-09 00:00",
         "2002-04-10 00:00",
         "2001-08-14 00:00",
         "2001-07-22 00:00",
         "2001-07-15 00:00",
         "2001-05-17 00:00",
         "2001-05-15 00:00",
         "2001-04-19 00:00",
         "2001-04-15 00:00",
         "2000-06-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnitIndex(TextualConvention, Integer32):
    status = "current"
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
        *(("master", 1),
          ("slave1", 2),
          ("slave2", 3),
          ("slave3", 4),
          ("slave4", 5))
    )



class ModuleHwType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              112)
        )
    )
    namedValues = NamedValues(
        *(("uninstalled", 1),
          ("stacking", 2),
          ("m100BaseTx", 3),
          ("m100BaseFxVF45", 4),
          ("m1000BaseSxSCMM850", 6),
          ("m1000BaseLxSC1300", 7),
          ("m1000BaseSCSMLDA", 8),
          ("m1000BaseSCSMLDB", 9),
          ("m1000BaseSxVF45MM850", 10),
          ("m1000BaseLxVF451300", 11),
          ("m1000BaseSxMTRJMM", 12),
          ("m1000BaseLxMTRJ1300", 13),
          ("m10BaseFlVF45", 14),
          ("m10BaseFlVF45X4Ports", 15),
          ("m100BaseFxSCMM", 16),
          ("m100BaseFxSCSM", 17),
          ("m100BaseFxSCSM2Port", 18),
          ("m100BaseFxSCSMLD", 19),
          ("m100BaseFxSCSMLD2Port", 20),
          ("m100BaseFxMTRJMM", 21),
          ("m100BaseFxMTRJSM", 22),
          ("mDUAL-SFP", 23),
          ("mDUAL-SFP-installed", 24),
          ("m1000BaseTx", 25),
          ("m1000BaseCx", 26),
          ("mVDSLNT", 30),
          ("mVDSLLT", 31),
          ("mVDSLNTand100BaseTX", 32),
          ("mVDSLLTand100BaseTX", 33),
          ("mVDSLLT24Port", 34),
          ("mLayer31000BaseSXSCMM", 35),
          ("mLayer31000BaseLXSCSM", 36),
          ("mLayer31000BaseSXSFFMM", 37),
          ("mLayer31000BaseLXSFFSM", 38),
          ("mLayer3100BaseFXSCMM2Port", 39),
          ("mLayer3100BaseFXSCSM2Port", 40),
          ("mLayer3100BaseFXSCMM4Port", 41),
          ("mLayer3100BaseFXSCSM4Port", 42),
          ("mLayer3100BaseFXSFFMM", 43),
          ("mLayer3100BaseFXSFFSM", 44),
          ("mLayer3100BaseTX", 45),
          ("m1000BaseGBIC-installed", 46),
          ("m1000BaseGBIC-not-installed", 47),
          ("mLayer31000BaseSX-GIBIC", 48),
          ("mLayer31000BaseLX-GIBIC", 49),
          ("mLayer31000BaseCX-GIBIC", 50),
          ("mLayer31000BaseT-GIBIC", 51),
          ("mLayer3100BaseSMLCL-GIBIC", 52),
          ("mLayer3100BaseM5o6SNI-GIBIC", 53),
          ("mLayer31000BasePOSMM", 54),
          ("mLayer31000BasePOSSM", 55),
          ("mLayer3100BaseFXSFFMM20Port", 56),
          ("mLayer3100BaseFXSFFSM20Port", 57),
          ("mLayer3100BaseFXSFFMM5Port", 58),
          ("mLayer3100BaseFXSFFSM5Port", 59),
          ("mDS3ATM", 60),
          ("mDS1MLP", 61),
          ("mMLPmother", 62),
          ("m1000BaseSFP-installed", 63),
          ("mLayer31000BaseSX-SFP", 65),
          ("mLayer31000BaseLX-SFP", 66),
          ("mLayer31000BaseCX-SFP", 67),
          ("mLayer31000BaseT-SFP", 68),
          ("mLayer3100BaseSMLCL-SFP", 69),
          ("mLayer3100BaseM5o6SNI-SFP", 70),
          ("m100BaseGBIC-not-installed", 71),
          ("mLayer310GBaseSR-XFP", 72),
          ("mLayer310GBaseLR-XFP", 73),
          ("mLayer310GBaseER-XFP", 74),
          ("mLayer310GBaseSW-XFP", 75),
          ("mLayer310GBaseLW-XFP", 76),
          ("mLayer310GBaseEW-XFP", 77),
          ("mLayer310GBase-XFP", 78),
          ("m10000BaseMEDIA-not-installed", 79),
          ("mCpmCard", 80),
          ("mLayer310GBaseLRW-XFP", 81),
          ("mLayer310GBaseERW-XFP", 82),
          ("mLayer31000BaseX-SFP", 83),
          ("mCES", 84),
          ("mLayer3100BaseFX-SFP", 85),
          ("mCES-4TDM", 86),
          ("mLayer31000BaseLX-BD-SFP", 87),
          ("mMiRIC-E1", 88),
          ("mMiRIC-E3", 89),
          ("mMiRIC-T1", 90),
          ("mMiRIC-T3", 91),
          ("mLayer31000BaseSFP-Unknown", 92),
          ("m10000BaseXFP-Unknown", 93),
          ("xAUI-1G-10G", 94),
          ("mLayer3-10-1000BaseT", 95),
          ("mLayer310GBaseSMSR-XFP", 96),
          ("mLayer310GBaseSMLR-XFP", 97),
          ("mLayer310GBaseSMER-XFP", 98),
          ("mLayer310GBaseSMSW-XFP", 99),
          ("mLayer310GBaseSMLW-XFP", 101),
          ("mLayer310GBaseSMEW-XFP", 102),
          ("mLayer310GBaseSMSRW-XFP", 103),
          ("mLayer310GBaseSMLRW-XFP", 104),
          ("mLayer310GBaseSMERW-XFP", 105),
          ("mLayer310GBaseCpPgt-XFP", 106),
          ("mLayer310GBaseSMZR-XFP", 107),
          ("mLayer31000BaseZX-SFP", 108),
          ("mLayer310GBaseSMZX-XFP", 109),
          ("mLayer310GBaseSMEX-XFP", 110),
          ("mLayer31000BaseT-WithoutAN-SFP", 111),
          ("mLayer3100BaseLX-BD-SFP", 112))
    )



class Series(TextualConvention, Integer32):
    status = "current"
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
        *(("notExist", 1),
          ("e-series", 2),
          ("g-series", 3),
          ("t-series", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Prvt_products_ObjectIdentity = ObjectIdentity
prvt_products = _Prvt_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1)
)
_Rptr_ObjectIdentity = ObjectIdentity
rptr = _Rptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 1)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 2)
)
_Trclam_ObjectIdentity = ObjectIdentity
trclam = _Trclam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 3)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 4)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5)
)
_Bsw_ObjectIdentity = ObjectIdentity
bsw = _Bsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1)
)
_Tps_ObjectIdentity = ObjectIdentity
tps = _Tps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2)
)
_Tpf_ObjectIdentity = ObjectIdentity
tpf = _Tpf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 3)
)
_Titan_ObjectIdentity = ObjectIdentity
titan = _Titan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 5)
)
_Titant5_ObjectIdentity = ObjectIdentity
titant5 = _Titant5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 7)
)
_EdgeLinkT4_ObjectIdentity = ObjectIdentity
edgeLinkT4 = _EdgeLinkT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 15)
)
_EdgeLinkT5_ObjectIdentity = ObjectIdentity
edgeLinkT5 = _EdgeLinkT5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 17)
)
_TitanPro_ObjectIdentity = ObjectIdentity
titanPro = _TitanPro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 20)
)
_PrvtSwitchNotifications_ObjectIdentity = ObjectIdentity
prvtSwitchNotifications = _PrvtSwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1)
)
_SysProductsOids_ObjectIdentity = ObjectIdentity
sysProductsOids = _SysProductsOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1)
)
_T4Router_ObjectIdentity = ObjectIdentity
t4Router = _T4Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1)
)
_T5Router_ObjectIdentity = ObjectIdentity
t5Router = _T5Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 2)
)
_T5ProRouter_ObjectIdentity = ObjectIdentity
t5ProRouter = _T5ProRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 3)
)
_T6Router_ObjectIdentity = ObjectIdentity
t6Router = _T6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 4)
)
_T5c_48TRouter_ObjectIdentity = ObjectIdentity
t5c_48TRouter = _T5c_48TRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 5)
)
_T5RNRouter_ObjectIdentity = ObjectIdentity
t5RNRouter = _T5RNRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 6)
)
_T5c_24TRouter_ObjectIdentity = ObjectIdentity
t5c_24TRouter = _T5c_24TRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 7)
)
_As9205_ObjectIdentity = ObjectIdentity
as9205 = _As9205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 7, 1)
)
_T5c_24MRouter_ObjectIdentity = ObjectIdentity
t5c_24MRouter = _T5c_24MRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 8)
)
_T5c_24FRouter_ObjectIdentity = ObjectIdentity
t5c_24FRouter = _T5c_24FRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 9)
)
_As9205_F_ObjectIdentity = ObjectIdentity
as9205_F = _As9205_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 9, 1)
)
_T5c_24GRouter_ObjectIdentity = ObjectIdentity
t5c_24GRouter = _T5c_24GRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 10)
)
_T5c_24GTRouter_ObjectIdentity = ObjectIdentity
t5c_24GTRouter = _T5c_24GTRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 11)
)
_T6pro_lc_20G_ObjectIdentity = ObjectIdentity
t6pro_lc_20G = _T6pro_lc_20G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 13)
)
_T6pro_cpm_ObjectIdentity = ObjectIdentity
t6pro_cpm = _T6pro_cpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 14)
)
_Compact_ObjectIdentity = ObjectIdentity
compact = _Compact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 14, 1)
)
_Classic_ObjectIdentity = ObjectIdentity
classic = _Classic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 14, 2)
)
_TMetro_ObjectIdentity = ObjectIdentity
tMetro = _TMetro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 16)
)
_Alcatel_7250_ObjectIdentity = ObjectIdentity
alcatel_7250 = _Alcatel_7250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 16, 1)
)
_TMarc_ObjectIdentity = ObjectIdentity
tMarc = _TMarc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17)
)
_TMarc_250_ObjectIdentity = ObjectIdentity
tMarc_250 = _TMarc_250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 1)
)
_Dm9225_ObjectIdentity = ObjectIdentity
dm9225 = _Dm9225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 1, 1)
)
_TMarc_254_ObjectIdentity = ObjectIdentity
tMarc_254 = _TMarc_254_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 2)
)
_Dm9225_E_ObjectIdentity = ObjectIdentity
dm9225_E = _Dm9225_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 2, 1)
)
_TMarc_254h_ObjectIdentity = ObjectIdentity
tMarc_254h = _TMarc_254h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 3)
)
_TMarc_340_ObjectIdentity = ObjectIdentity
tMarc_340 = _TMarc_340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 10)
)
_Dm9234_ObjectIdentity = ObjectIdentity
dm9234 = _Dm9234_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 10, 1)
)
_TMarc_380_ObjectIdentity = ObjectIdentity
tMarc_380 = _TMarc_380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 11)
)
_TMarc_280_ObjectIdentity = ObjectIdentity
tMarc_280 = _TMarc_280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 17, 20)
)
_AHUB1_A_ObjectIdentity = ObjectIdentity
aHUB1_A = _AHUB1_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 18)
)
_BI_Ethernet_ObjectIdentity = ObjectIdentity
bI_Ethernet = _BI_Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 18, 1)
)
_FI_Ethernet_ObjectIdentity = ObjectIdentity
fI_Ethernet = _FI_Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 18, 2)
)
_TMetro_ES_ObjectIdentity = ObjectIdentity
tMetro_ES = _TMetro_ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 19)
)
_Alcatel_7250_ES_ObjectIdentity = ObjectIdentity
alcatel_7250_ES = _Alcatel_7250_ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 19, 1)
)
_Alcatel_7250_ESA_ObjectIdentity = ObjectIdentity
alcatel_7250_ESA = _Alcatel_7250_ESA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 19, 2)
)
_TMetro_ESA_ObjectIdentity = ObjectIdentity
tMetro_ESA = _TMetro_ESA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 19, 3)
)
_As9220_ObjectIdentity = ObjectIdentity
as9220 = _As9220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 19, 10)
)
_TMetro_200S_ObjectIdentity = ObjectIdentity
tMetro_200S = _TMetro_200S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 19, 11)
)
_TMarc_E_ObjectIdentity = ObjectIdentity
tMarc_E = _TMarc_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 20)
)
_TMarc_340_E_ObjectIdentity = ObjectIdentity
tMarc_340_E = _TMarc_340_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 20, 1)
)
_TMarc_380_E_ObjectIdentity = ObjectIdentity
tMarc_380_E = _TMarc_380_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 20, 2)
)
_TMarc_EW_ObjectIdentity = ObjectIdentity
tMarc_EW = _TMarc_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 21)
)
_TMarc_340_EW_ObjectIdentity = ObjectIdentity
tMarc_340_EW = _TMarc_340_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 21, 1)
)
_TMarc_380_EW_ObjectIdentity = ObjectIdentity
tMarc_380_EW = _TMarc_380_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 21, 2)
)
_TMarc_WDB_ObjectIdentity = ObjectIdentity
tMarc_WDB = _TMarc_WDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 22)
)
_TMarc_340WD_B_ObjectIdentity = ObjectIdentity
tMarc_340WD_B = _TMarc_340WD_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 22, 1)
)
_TMarc_WD_ObjectIdentity = ObjectIdentity
tMarc_WD = _TMarc_WD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 23)
)
_TMarc_340WD_ObjectIdentity = ObjectIdentity
tMarc_340WD = _TMarc_340WD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 23, 1)
)
_TMarc_F_ObjectIdentity = ObjectIdentity
tMarc_F = _TMarc_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 24)
)
_TMarc_340_F_ObjectIdentity = ObjectIdentity
tMarc_340_F = _TMarc_340_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 24, 1)
)
_T5c_XG_ObjectIdentity = ObjectIdentity
t5c_XG = _T5c_XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 27)
)
_As9215_ObjectIdentity = ObjectIdentity
as9215 = _As9215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 27, 1)
)
_T5c_ObjectIdentity = ObjectIdentity
t5c = _T5c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 100)
)
_T5cgt_ObjectIdentity = ObjectIdentity
t5cgt = _T5cgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 222)
)
_T5g_ObjectIdentity = ObjectIdentity
t5g = _T5g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 333)
)
_V24s_ObjectIdentity = ObjectIdentity
v24s = _V24s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 444)
)
_EdgeGate281_ObjectIdentity = ObjectIdentity
edgeGate281 = _EdgeGate281_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1000)
)
_EdgeGate281SYS_ObjectIdentity = ObjectIdentity
edgeGate281SYS = _EdgeGate281SYS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1001)
)
_EdgeGate231_ObjectIdentity = ObjectIdentity
edgeGate231 = _EdgeGate231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1010)
)
_EdgeGate282_ObjectIdentity = ObjectIdentity
edgeGate282 = _EdgeGate282_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1020)
)
_EdgeGate282S_ObjectIdentity = ObjectIdentity
edgeGate282S = _EdgeGate282S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1021)
)
_EdgeGate482S_ObjectIdentity = ObjectIdentity
edgeGate482S = _EdgeGate482S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1022)
)
_EdgeGate483S_ObjectIdentity = ObjectIdentity
edgeGate483S = _EdgeGate483S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1023)
)
_EdgeGate483D_ObjectIdentity = ObjectIdentity
edgeGate483D = _EdgeGate483D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1024)
)
_EdgeGate201_ObjectIdentity = ObjectIdentity
edgeGate201 = _EdgeGate201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1031)
)
_EdgeGate232_ObjectIdentity = ObjectIdentity
edgeGate232 = _EdgeGate232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1041)
)
_Ac500_ObjectIdentity = ObjectIdentity
ac500 = _Ac500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1050)
)
_Ac505_ObjectIdentity = ObjectIdentity
ac505 = _Ac505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1050, 1)
)
_Ac512_ObjectIdentity = ObjectIdentity
ac512 = _Ac512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1050, 2)
)
_Ac524_ObjectIdentity = ObjectIdentity
ac524 = _Ac524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 1, 1050, 3)
)
_SysIntf_ObjectIdentity = ObjectIdentity
sysIntf = _SysIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 2)
)
_SysIntfTable_Object = MibTable
sysIntfTable = _SysIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysIntfTable.setStatus("current")
_SysIntfEntry_Object = MibTableRow
sysIntfEntry = _SysIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 2, 1, 1)
)
sysIntfEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "sysStackNo"),
    (0, "PRVT-SWITCH-MIB", "sysSlotNo"),
)
if mibBuilder.loadTexts:
    sysIntfEntry.setStatus("current")
_SysStackNo_Type = UnitIndex
_SysStackNo_Object = MibTableColumn
sysStackNo = _SysStackNo_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 2, 1, 1, 1),
    _SysStackNo_Type()
)
sysStackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStackNo.setStatus("current")


class _SysSlotNo_Type(Integer32):
    """Custom type sysSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SysSlotNo_Type.__name__ = "Integer32"
_SysSlotNo_Object = MibTableColumn
sysSlotNo = _SysSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 2, 1, 1, 2),
    _SysSlotNo_Type()
)
sysSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSlotNo.setStatus("current")


class _SysIntfUnitExist_Type(Integer32):
    """Custom type sysIntfUnitExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uninstalled", 1),
          ("installed", 2))
    )


_SysIntfUnitExist_Type.__name__ = "Integer32"
_SysIntfUnitExist_Object = MibTableColumn
sysIntfUnitExist = _SysIntfUnitExist_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 2, 1, 1, 3),
    _SysIntfUnitExist_Type()
)
sysIntfUnitExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIntfUnitExist.setStatus("current")
_SysIntfModule_Type = ModuleHwType
_SysIntfModule_Object = MibTableColumn
sysIntfModule = _SysIntfModule_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 2, 1, 1, 4),
    _SysIntfModule_Type()
)
sysIntfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIntfModule.setStatus("current")
_SysManufacturing_ObjectIdentity = ObjectIdentity
sysManufacturing = _SysManufacturing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3)
)
_SysSerialNumber_Type = DisplayString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3, 1),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")
_SysSwitchModel_Type = DisplayString
_SysSwitchModel_Object = MibScalar
sysSwitchModel = _SysSwitchModel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3, 2),
    _SysSwitchModel_Type()
)
sysSwitchModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwitchModel.setStatus("current")
_SysAssemblyNumber_Type = DisplayString
_SysAssemblyNumber_Object = MibScalar
sysAssemblyNumber = _SysAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3, 3),
    _SysAssemblyNumber_Type()
)
sysAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAssemblyNumber.setStatus("current")
_SysPartNumber_Type = DisplayString
_SysPartNumber_Object = MibScalar
sysPartNumber = _SysPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3, 4),
    _SysPartNumber_Type()
)
sysPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPartNumber.setStatus("current")
_SysCLEI_Type = DisplayString
_SysCLEI_Object = MibScalar
sysCLEI = _SysCLEI_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3, 5),
    _SysCLEI_Type()
)
sysCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCLEI.setStatus("current")
_SysHwRevision_Type = DisplayString
_SysHwRevision_Object = MibScalar
sysHwRevision = _SysHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3, 6),
    _SysHwRevision_Type()
)
sysHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwRevision.setStatus("current")
_SysManufacturingDate_Type = DisplayString
_SysManufacturingDate_Object = MibScalar
sysManufacturingDate = _SysManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 3, 7),
    _SysManufacturingDate_Type()
)
sysManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysManufacturingDate.setStatus("current")
_SysSwitchingHW_ObjectIdentity = ObjectIdentity
sysSwitchingHW = _SysSwitchingHW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 4)
)
_SysSwitchSeries_Type = Series
_SysSwitchSeries_Object = MibScalar
sysSwitchSeries = _SysSwitchSeries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 1, 4, 1),
    _SysSwitchSeries_Type()
)
sysSwitchSeries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwitchSeries.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2)
)
_ConfigL2_ObjectIdentity = ObjectIdentity
configL2 = _ConfigL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2)
)


class _ConfigL2SpanOnOff_Type(Integer32):
    """Custom type configL2SpanOnOff based on Integer32"""
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
        *(("enableSTP", 1),
          ("disable", 2),
          ("enableRSTP", 3),
          ("enablePVST", 4),
          ("enableMST", 5))
    )


_ConfigL2SpanOnOff_Type.__name__ = "Integer32"
_ConfigL2SpanOnOff_Object = MibScalar
configL2SpanOnOff = _ConfigL2SpanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 1),
    _ConfigL2SpanOnOff_Type()
)
configL2SpanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2SpanOnOff.setStatus("current")
_ConfigL2IfaceTable_Object = MibTable
configL2IfaceTable = _ConfigL2IfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2)
)
if mibBuilder.loadTexts:
    configL2IfaceTable.setStatus("current")
_ConfigL2IfaceEntry_Object = MibTableRow
configL2IfaceEntry = _ConfigL2IfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1)
)
configL2IfaceEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "configL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "configL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "configL2IfacePort"),
)
if mibBuilder.loadTexts:
    configL2IfaceEntry.setStatus("current")


class _ConfigL2IfaceUnit_Type(Integer32):
    """Custom type configL2IfaceUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ConfigL2IfaceUnit_Type.__name__ = "Integer32"
_ConfigL2IfaceUnit_Object = MibTableColumn
configL2IfaceUnit = _ConfigL2IfaceUnit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 1),
    _ConfigL2IfaceUnit_Type()
)
configL2IfaceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configL2IfaceUnit.setStatus("current")


class _ConfigL2IfaceSlot_Type(Integer32):
    """Custom type configL2IfaceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ConfigL2IfaceSlot_Type.__name__ = "Integer32"
_ConfigL2IfaceSlot_Object = MibTableColumn
configL2IfaceSlot = _ConfigL2IfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 2),
    _ConfigL2IfaceSlot_Type()
)
configL2IfaceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configL2IfaceSlot.setStatus("current")


class _ConfigL2IfacePort_Type(Integer32):
    """Custom type configL2IfacePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ConfigL2IfacePort_Type.__name__ = "Integer32"
_ConfigL2IfacePort_Object = MibTableColumn
configL2IfacePort = _ConfigL2IfacePort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 3),
    _ConfigL2IfacePort_Type()
)
configL2IfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configL2IfacePort.setStatus("current")


class _ConfigL2IfaceName_Type(DisplayString):
    """Custom type configL2IfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigL2IfaceName_Type.__name__ = "DisplayString"
_ConfigL2IfaceName_Object = MibTableColumn
configL2IfaceName = _ConfigL2IfaceName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 4),
    _ConfigL2IfaceName_Type()
)
configL2IfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceName.setStatus("current")


class _ConfigL2IfaceEnable_Type(Integer32):
    """Custom type configL2IfaceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConfigL2IfaceEnable_Type.__name__ = "Integer32"
_ConfigL2IfaceEnable_Object = MibTableColumn
configL2IfaceEnable = _ConfigL2IfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 5),
    _ConfigL2IfaceEnable_Type()
)
configL2IfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceEnable.setStatus("current")


class _ConfigL2IfaceSTPEnable_Type(Integer32):
    """Custom type configL2IfaceSTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConfigL2IfaceSTPEnable_Type.__name__ = "Integer32"
_ConfigL2IfaceSTPEnable_Object = MibTableColumn
configL2IfaceSTPEnable = _ConfigL2IfaceSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 6),
    _ConfigL2IfaceSTPEnable_Type()
)
configL2IfaceSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceSTPEnable.setStatus("current")


class _ConfigL2IfaceDuplexSpeedSet_Type(Integer32):
    """Custom type configL2IfaceDuplexSpeedSet based on Integer32"""
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
              16,
              99)
        )
    )
    namedValues = NamedValues(
        *(("autonegotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("half-1000", 6),
          ("full-1000", 7),
          ("pos-155", 8),
          ("pos-622", 9),
          ("full-10000", 10),
          ("half-auto", 11),
          ("full-auto", 12),
          ("auto-10", 13),
          ("auto-100", 14),
          ("auto-1000", 16),
          ("illegal", 99))
    )


_ConfigL2IfaceDuplexSpeedSet_Type.__name__ = "Integer32"
_ConfigL2IfaceDuplexSpeedSet_Object = MibTableColumn
configL2IfaceDuplexSpeedSet = _ConfigL2IfaceDuplexSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 7),
    _ConfigL2IfaceDuplexSpeedSet_Type()
)
configL2IfaceDuplexSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceDuplexSpeedSet.setStatus("obsolete")


class _ConfigL2IfaceFlow_Type(Integer32):
    """Custom type configL2IfaceFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autonegotiate", 1),
          ("flowon", 2),
          ("flowoff", 3))
    )


_ConfigL2IfaceFlow_Type.__name__ = "Integer32"
_ConfigL2IfaceFlow_Object = MibTableColumn
configL2IfaceFlow = _ConfigL2IfaceFlow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 8),
    _ConfigL2IfaceFlow_Type()
)
configL2IfaceFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceFlow.setStatus("current")


class _ConfigL2IfaceBackpressure_Type(Integer32):
    """Custom type configL2IfaceBackpressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("backpressureon", 1),
          ("backpressureoff", 2),
          ("illegal", 99))
    )


_ConfigL2IfaceBackpressure_Type.__name__ = "Integer32"
_ConfigL2IfaceBackpressure_Object = MibTableColumn
configL2IfaceBackpressure = _ConfigL2IfaceBackpressure_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 9),
    _ConfigL2IfaceBackpressure_Type()
)
configL2IfaceBackpressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceBackpressure.setStatus("current")


class _ConfigL2IfaceResetCounters_Type(Integer32):
    """Custom type configL2IfaceResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_ConfigL2IfaceResetCounters_Type.__name__ = "Integer32"
_ConfigL2IfaceResetCounters_Object = MibTableColumn
configL2IfaceResetCounters = _ConfigL2IfaceResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 10),
    _ConfigL2IfaceResetCounters_Type()
)
configL2IfaceResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceResetCounters.setStatus("current")


class _ConfigL2IfaceDefaultVID_Type(Integer32):
    """Custom type configL2IfaceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ConfigL2IfaceDefaultVID_Type.__name__ = "Integer32"
_ConfigL2IfaceDefaultVID_Object = MibTableColumn
configL2IfaceDefaultVID = _ConfigL2IfaceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 11),
    _ConfigL2IfaceDefaultVID_Type()
)
configL2IfaceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceDefaultVID.setStatus("current")


class _ConfigL2IfaceSnifferIfIndex_Type(Integer32):
    """Custom type configL2IfaceSnifferIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConfigL2IfaceSnifferIfIndex_Type.__name__ = "Integer32"
_ConfigL2IfaceSnifferIfIndex_Object = MibTableColumn
configL2IfaceSnifferIfIndex = _ConfigL2IfaceSnifferIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 12),
    _ConfigL2IfaceSnifferIfIndex_Type()
)
configL2IfaceSnifferIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceSnifferIfIndex.setStatus("current")
_ConfigL2TopologyChangeDetection_Type = TruthValue
_ConfigL2TopologyChangeDetection_Object = MibTableColumn
configL2TopologyChangeDetection = _ConfigL2TopologyChangeDetection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 13),
    _ConfigL2TopologyChangeDetection_Type()
)
configL2TopologyChangeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2TopologyChangeDetection.setStatus("current")


class _ConfigL2IfaceDuplexModeSet_Type(Integer32):
    """Custom type configL2IfaceDuplexModeSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("full", 2),
          ("half", 3))
    )


_ConfigL2IfaceDuplexModeSet_Type.__name__ = "Integer32"
_ConfigL2IfaceDuplexModeSet_Object = MibTableColumn
configL2IfaceDuplexModeSet = _ConfigL2IfaceDuplexModeSet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 14),
    _ConfigL2IfaceDuplexModeSet_Type()
)
configL2IfaceDuplexModeSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceDuplexModeSet.setStatus("current")


class _ConfigL2IfaceSpeedSet_Type(Integer32):
    """Custom type configL2IfaceSpeedSet based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("speed-10", 2),
          ("speed-100", 3),
          ("speed-1000", 4),
          ("speed-10000", 5),
          ("pos-155", 6),
          ("pos-622", 7),
          ("illegal", 99))
    )


_ConfigL2IfaceSpeedSet_Type.__name__ = "Integer32"
_ConfigL2IfaceSpeedSet_Object = MibTableColumn
configL2IfaceSpeedSet = _ConfigL2IfaceSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 15),
    _ConfigL2IfaceSpeedSet_Type()
)
configL2IfaceSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceSpeedSet.setStatus("current")


class _ConfigL2IfaceBroadcastRateLimit_Type(Integer32):
    """Custom type configL2IfaceBroadcastRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConfigL2IfaceBroadcastRateLimit_Type.__name__ = "Integer32"
_ConfigL2IfaceBroadcastRateLimit_Object = MibTableColumn
configL2IfaceBroadcastRateLimit = _ConfigL2IfaceBroadcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 16),
    _ConfigL2IfaceBroadcastRateLimit_Type()
)
configL2IfaceBroadcastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceBroadcastRateLimit.setStatus("current")


class _ConfigL2IfaceMulticastRateLimit_Type(Integer32):
    """Custom type configL2IfaceMulticastRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConfigL2IfaceMulticastRateLimit_Type.__name__ = "Integer32"
_ConfigL2IfaceMulticastRateLimit_Object = MibTableColumn
configL2IfaceMulticastRateLimit = _ConfigL2IfaceMulticastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 17),
    _ConfigL2IfaceMulticastRateLimit_Type()
)
configL2IfaceMulticastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceMulticastRateLimit.setStatus("current")


class _ConfigL2IfaceUnknownRateLimit_Type(Integer32):
    """Custom type configL2IfaceUnknownRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConfigL2IfaceUnknownRateLimit_Type.__name__ = "Integer32"
_ConfigL2IfaceUnknownRateLimit_Object = MibTableColumn
configL2IfaceUnknownRateLimit = _ConfigL2IfaceUnknownRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 18),
    _ConfigL2IfaceUnknownRateLimit_Type()
)
configL2IfaceUnknownRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceUnknownRateLimit.setStatus("current")


class _ConfigL2IfaceBroadcastBurstSize_Type(Integer32):
    """Custom type configL2IfaceBroadcastBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConfigL2IfaceBroadcastBurstSize_Type.__name__ = "Integer32"
_ConfigL2IfaceBroadcastBurstSize_Object = MibTableColumn
configL2IfaceBroadcastBurstSize = _ConfigL2IfaceBroadcastBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 19),
    _ConfigL2IfaceBroadcastBurstSize_Type()
)
configL2IfaceBroadcastBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceBroadcastBurstSize.setStatus("current")


class _ConfigL2IfaceMulticastBurstSize_Type(Integer32):
    """Custom type configL2IfaceMulticastBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConfigL2IfaceMulticastBurstSize_Type.__name__ = "Integer32"
_ConfigL2IfaceMulticastBurstSize_Object = MibTableColumn
configL2IfaceMulticastBurstSize = _ConfigL2IfaceMulticastBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 20),
    _ConfigL2IfaceMulticastBurstSize_Type()
)
configL2IfaceMulticastBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceMulticastBurstSize.setStatus("current")


class _ConfigL2IfaceUnknownBurstSize_Type(Integer32):
    """Custom type configL2IfaceUnknownBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConfigL2IfaceUnknownBurstSize_Type.__name__ = "Integer32"
_ConfigL2IfaceUnknownBurstSize_Object = MibTableColumn
configL2IfaceUnknownBurstSize = _ConfigL2IfaceUnknownBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 21),
    _ConfigL2IfaceUnknownBurstSize_Type()
)
configL2IfaceUnknownBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceUnknownBurstSize.setStatus("current")


class _ConfigL2IfaceMtu_Type(Integer32):
    """Custom type configL2IfaceMtu based on Integer32"""
    defaultValue = 1528

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9216),
    )


_ConfigL2IfaceMtu_Type.__name__ = "Integer32"
_ConfigL2IfaceMtu_Object = MibTableColumn
configL2IfaceMtu = _ConfigL2IfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 22),
    _ConfigL2IfaceMtu_Type()
)
configL2IfaceMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceMtu.setStatus("current")


class _ConfigL2IfaceAdminCrossOver_Type(Integer32):
    """Custom type configL2IfaceAdminCrossOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3),
          ("unsupported", 255))
    )


_ConfigL2IfaceAdminCrossOver_Type.__name__ = "Integer32"
_ConfigL2IfaceAdminCrossOver_Object = MibTableColumn
configL2IfaceAdminCrossOver = _ConfigL2IfaceAdminCrossOver_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 23),
    _ConfigL2IfaceAdminCrossOver_Type()
)
configL2IfaceAdminCrossOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceAdminCrossOver.setStatus("current")


class _ConfigL2IfaceRemoteFaultDetect_Type(Integer32):
    """Custom type configL2IfaceRemoteFaultDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableRemoteFaultDetect", 1),
          ("disableRemoteFaultDetect", 2))
    )


_ConfigL2IfaceRemoteFaultDetect_Type.__name__ = "Integer32"
_ConfigL2IfaceRemoteFaultDetect_Object = MibTableColumn
configL2IfaceRemoteFaultDetect = _ConfigL2IfaceRemoteFaultDetect_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 2, 2, 2, 1, 24),
    _ConfigL2IfaceRemoteFaultDetect_Type()
)
configL2IfaceRemoteFaultDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configL2IfaceRemoteFaultDetect.setStatus("current")
_Reports_ObjectIdentity = ObjectIdentity
reports = _Reports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3)
)
_ReportsL2_ObjectIdentity = ObjectIdentity
reportsL2 = _ReportsL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1)
)
_ReportsL2IfaceTable_Object = MibTable
reportsL2IfaceTable = _ReportsL2IfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1)
)
if mibBuilder.loadTexts:
    reportsL2IfaceTable.setStatus("current")
_ReportsL2IfaceEntry_Object = MibTableRow
reportsL2IfaceEntry = _ReportsL2IfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1)
)
reportsL2IfaceEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"),
)
if mibBuilder.loadTexts:
    reportsL2IfaceEntry.setStatus("current")


class _ReportsL2IfaceUnit_Type(Integer32):
    """Custom type reportsL2IfaceUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ReportsL2IfaceUnit_Type.__name__ = "Integer32"
_ReportsL2IfaceUnit_Object = MibTableColumn
reportsL2IfaceUnit = _ReportsL2IfaceUnit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 1),
    _ReportsL2IfaceUnit_Type()
)
reportsL2IfaceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceUnit.setStatus("current")


class _ReportsL2IfaceSlot_Type(Integer32):
    """Custom type reportsL2IfaceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ReportsL2IfaceSlot_Type.__name__ = "Integer32"
_ReportsL2IfaceSlot_Object = MibTableColumn
reportsL2IfaceSlot = _ReportsL2IfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 2),
    _ReportsL2IfaceSlot_Type()
)
reportsL2IfaceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceSlot.setStatus("current")


class _ReportsL2IfacePort_Type(Integer32):
    """Custom type reportsL2IfacePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ReportsL2IfacePort_Type.__name__ = "Integer32"
_ReportsL2IfacePort_Object = MibTableColumn
reportsL2IfacePort = _ReportsL2IfacePort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 3),
    _ReportsL2IfacePort_Type()
)
reportsL2IfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfacePort.setStatus("current")


class _ReportsL2IfaceBridgeIndex_Type(Integer32):
    """Custom type reportsL2IfaceBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ReportsL2IfaceBridgeIndex_Type.__name__ = "Integer32"
_ReportsL2IfaceBridgeIndex_Object = MibTableColumn
reportsL2IfaceBridgeIndex = _ReportsL2IfaceBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 4),
    _ReportsL2IfaceBridgeIndex_Type()
)
reportsL2IfaceBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceBridgeIndex.setStatus("current")


class _ReportsL2IfaceType_Type(Integer32):
    """Custom type reportsL2IfaceType based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("regular1822", 2),
          ("hdh1822", 3),
          ("ddn-x25", 4),
          ("rfc877-x25", 5),
          ("ethernet-csmacd", 6),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("starLan", 11),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("hyperchannel", 14),
          ("fddi", 15),
          ("lapb", 16),
          ("sdlc", 17),
          ("ds1", 18),
          ("e1", 19),
          ("basicISDN", 20),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("ppp", 23),
          ("softwareLoopback", 24),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("nsip", 27),
          ("slip", 28),
          ("ultra", 29),
          ("ds3", 30),
          ("sip", 31),
          ("frame-relay", 32))
    )


_ReportsL2IfaceType_Type.__name__ = "Integer32"
_ReportsL2IfaceType_Object = MibTableColumn
reportsL2IfaceType = _ReportsL2IfaceType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 5),
    _ReportsL2IfaceType_Type()
)
reportsL2IfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceType.setStatus("current")


class _ReportsL2IfaceLink_Type(Integer32):
    """Custom type reportsL2IfaceLink based on Integer32"""
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


_ReportsL2IfaceLink_Type.__name__ = "Integer32"
_ReportsL2IfaceLink_Object = MibTableColumn
reportsL2IfaceLink = _ReportsL2IfaceLink_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 6),
    _ReportsL2IfaceLink_Type()
)
reportsL2IfaceLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceLink.setStatus("current")


class _ReportsL2IfaceDuplexSpeedGet_Type(Integer32):
    """Custom type reportsL2IfaceDuplexSpeedGet based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("half-1000", 6),
          ("full-1000", 7),
          ("pos-155", 8),
          ("pos-622", 9),
          ("full-10000", 10),
          ("illegal", 99))
    )


_ReportsL2IfaceDuplexSpeedGet_Type.__name__ = "Integer32"
_ReportsL2IfaceDuplexSpeedGet_Object = MibTableColumn
reportsL2IfaceDuplexSpeedGet = _ReportsL2IfaceDuplexSpeedGet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 7),
    _ReportsL2IfaceDuplexSpeedGet_Type()
)
reportsL2IfaceDuplexSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceDuplexSpeedGet.setStatus("current")
_ReportsL2IfaceTXOctetsNoErr_Type = Counter32
_ReportsL2IfaceTXOctetsNoErr_Object = MibTableColumn
reportsL2IfaceTXOctetsNoErr = _ReportsL2IfaceTXOctetsNoErr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 8),
    _ReportsL2IfaceTXOctetsNoErr_Type()
)
reportsL2IfaceTXOctetsNoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceTXOctetsNoErr.setStatus("current")
_ReportsL2IfaceTXPacketsNoErr_Type = Counter32
_ReportsL2IfaceTXPacketsNoErr_Object = MibTableColumn
reportsL2IfaceTXPacketsNoErr = _ReportsL2IfaceTXPacketsNoErr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 9),
    _ReportsL2IfaceTXPacketsNoErr_Type()
)
reportsL2IfaceTXPacketsNoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceTXPacketsNoErr.setStatus("current")
_ReportsL2IfaceRXOctetsNoErr_Type = Counter32
_ReportsL2IfaceRXOctetsNoErr_Object = MibTableColumn
reportsL2IfaceRXOctetsNoErr = _ReportsL2IfaceRXOctetsNoErr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 10),
    _ReportsL2IfaceRXOctetsNoErr_Type()
)
reportsL2IfaceRXOctetsNoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceRXOctetsNoErr.setStatus("current")
_ReportsL2IfaceRXPacketsNoErr_Type = Counter32
_ReportsL2IfaceRXPacketsNoErr_Object = MibTableColumn
reportsL2IfaceRXPacketsNoErr = _ReportsL2IfaceRXPacketsNoErr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 11),
    _ReportsL2IfaceRXPacketsNoErr_Type()
)
reportsL2IfaceRXPacketsNoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceRXPacketsNoErr.setStatus("current")
_ReportsL2IfaceIfInOctets_Type = Counter32
_ReportsL2IfaceIfInOctets_Object = MibTableColumn
reportsL2IfaceIfInOctets = _ReportsL2IfaceIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 12),
    _ReportsL2IfaceIfInOctets_Type()
)
reportsL2IfaceIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfInOctets.setStatus("current")
_ReportsL2IfaceIfInUcastPkts_Type = Counter32
_ReportsL2IfaceIfInUcastPkts_Object = MibTableColumn
reportsL2IfaceIfInUcastPkts = _ReportsL2IfaceIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 13),
    _ReportsL2IfaceIfInUcastPkts_Type()
)
reportsL2IfaceIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfInUcastPkts.setStatus("current")
_ReportsL2IfaceIfInNUcastPkts_Type = Counter32
_ReportsL2IfaceIfInNUcastPkts_Object = MibTableColumn
reportsL2IfaceIfInNUcastPkts = _ReportsL2IfaceIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 14),
    _ReportsL2IfaceIfInNUcastPkts_Type()
)
reportsL2IfaceIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfInNUcastPkts.setStatus("current")
_ReportsL2IfaceIfInDiscards_Type = Counter32
_ReportsL2IfaceIfInDiscards_Object = MibTableColumn
reportsL2IfaceIfInDiscards = _ReportsL2IfaceIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 15),
    _ReportsL2IfaceIfInDiscards_Type()
)
reportsL2IfaceIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfInDiscards.setStatus("current")
_ReportsL2IfaceIfInErrors_Type = Counter32
_ReportsL2IfaceIfInErrors_Object = MibTableColumn
reportsL2IfaceIfInErrors = _ReportsL2IfaceIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 16),
    _ReportsL2IfaceIfInErrors_Type()
)
reportsL2IfaceIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfInErrors.setStatus("current")
_ReportsL2IfaceIfInUnknownProtos_Type = Counter32
_ReportsL2IfaceIfInUnknownProtos_Object = MibTableColumn
reportsL2IfaceIfInUnknownProtos = _ReportsL2IfaceIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 17),
    _ReportsL2IfaceIfInUnknownProtos_Type()
)
reportsL2IfaceIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfInUnknownProtos.setStatus("current")
_ReportsL2IfaceIfOutOctets_Type = Counter32
_ReportsL2IfaceIfOutOctets_Object = MibTableColumn
reportsL2IfaceIfOutOctets = _ReportsL2IfaceIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 18),
    _ReportsL2IfaceIfOutOctets_Type()
)
reportsL2IfaceIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfOutOctets.setStatus("current")
_ReportsL2IfaceIfOutUcastPkts_Type = Counter32
_ReportsL2IfaceIfOutUcastPkts_Object = MibTableColumn
reportsL2IfaceIfOutUcastPkts = _ReportsL2IfaceIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 19),
    _ReportsL2IfaceIfOutUcastPkts_Type()
)
reportsL2IfaceIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfOutUcastPkts.setStatus("current")
_ReportsL2IfaceIfOutNUcastPkts_Type = Counter32
_ReportsL2IfaceIfOutNUcastPkts_Object = MibTableColumn
reportsL2IfaceIfOutNUcastPkts = _ReportsL2IfaceIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 20),
    _ReportsL2IfaceIfOutNUcastPkts_Type()
)
reportsL2IfaceIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfOutNUcastPkts.setStatus("current")
_ReportsL2IfaceIfOutDiscards_Type = Counter32
_ReportsL2IfaceIfOutDiscards_Object = MibTableColumn
reportsL2IfaceIfOutDiscards = _ReportsL2IfaceIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 21),
    _ReportsL2IfaceIfOutDiscards_Type()
)
reportsL2IfaceIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfOutDiscards.setStatus("current")
_ReportsL2IfaceIfOutErrors_Type = Counter32
_ReportsL2IfaceIfOutErrors_Object = MibTableColumn
reportsL2IfaceIfOutErrors = _ReportsL2IfaceIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 22),
    _ReportsL2IfaceIfOutErrors_Type()
)
reportsL2IfaceIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceIfOutErrors.setStatus("current")
_ReportsL2IfaceStatsDropEvents_Type = Counter32
_ReportsL2IfaceStatsDropEvents_Object = MibTableColumn
reportsL2IfaceStatsDropEvents = _ReportsL2IfaceStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 23),
    _ReportsL2IfaceStatsDropEvents_Type()
)
reportsL2IfaceStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsDropEvents.setStatus("current")
_ReportsL2IfaceStatsOctets_Type = Counter32
_ReportsL2IfaceStatsOctets_Object = MibTableColumn
reportsL2IfaceStatsOctets = _ReportsL2IfaceStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 24),
    _ReportsL2IfaceStatsOctets_Type()
)
reportsL2IfaceStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsOctets.setStatus("current")
_ReportsL2IfaceStatsPkts_Type = Counter32
_ReportsL2IfaceStatsPkts_Object = MibTableColumn
reportsL2IfaceStatsPkts = _ReportsL2IfaceStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 25),
    _ReportsL2IfaceStatsPkts_Type()
)
reportsL2IfaceStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsPkts.setStatus("current")
_ReportsL2IfaceStatsBroadcastPkts_Type = Counter32
_ReportsL2IfaceStatsBroadcastPkts_Object = MibTableColumn
reportsL2IfaceStatsBroadcastPkts = _ReportsL2IfaceStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 26),
    _ReportsL2IfaceStatsBroadcastPkts_Type()
)
reportsL2IfaceStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsBroadcastPkts.setStatus("current")
_ReportsL2IfaceStatsMulticastPkts_Type = Counter32
_ReportsL2IfaceStatsMulticastPkts_Object = MibTableColumn
reportsL2IfaceStatsMulticastPkts = _ReportsL2IfaceStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 27),
    _ReportsL2IfaceStatsMulticastPkts_Type()
)
reportsL2IfaceStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsMulticastPkts.setStatus("current")
_ReportsL2IfaceStatsCRCAlignErrors_Type = Counter32
_ReportsL2IfaceStatsCRCAlignErrors_Object = MibTableColumn
reportsL2IfaceStatsCRCAlignErrors = _ReportsL2IfaceStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 28),
    _ReportsL2IfaceStatsCRCAlignErrors_Type()
)
reportsL2IfaceStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsCRCAlignErrors.setStatus("current")
_ReportsL2IfaceStatsUndersizePkts_Type = Counter32
_ReportsL2IfaceStatsUndersizePkts_Object = MibTableColumn
reportsL2IfaceStatsUndersizePkts = _ReportsL2IfaceStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 29),
    _ReportsL2IfaceStatsUndersizePkts_Type()
)
reportsL2IfaceStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsUndersizePkts.setStatus("current")
_ReportsL2IfaceStatsOversizePkts_Type = Counter32
_ReportsL2IfaceStatsOversizePkts_Object = MibTableColumn
reportsL2IfaceStatsOversizePkts = _ReportsL2IfaceStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 30),
    _ReportsL2IfaceStatsOversizePkts_Type()
)
reportsL2IfaceStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsOversizePkts.setStatus("current")
_ReportsL2IfaceStatsFragments_Type = Counter32
_ReportsL2IfaceStatsFragments_Object = MibTableColumn
reportsL2IfaceStatsFragments = _ReportsL2IfaceStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 31),
    _ReportsL2IfaceStatsFragments_Type()
)
reportsL2IfaceStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsFragments.setStatus("current")
_ReportsL2IfaceStatsJabbers_Type = Counter32
_ReportsL2IfaceStatsJabbers_Object = MibTableColumn
reportsL2IfaceStatsJabbers = _ReportsL2IfaceStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 32),
    _ReportsL2IfaceStatsJabbers_Type()
)
reportsL2IfaceStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsJabbers.setStatus("current")
_ReportsL2IfaceStatsCollisions_Type = Counter32
_ReportsL2IfaceStatsCollisions_Object = MibTableColumn
reportsL2IfaceStatsCollisions = _ReportsL2IfaceStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 33),
    _ReportsL2IfaceStatsCollisions_Type()
)
reportsL2IfaceStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsCollisions.setStatus("current")
_ReportsL2IfaceStatsPkts64Octets_Type = Counter32
_ReportsL2IfaceStatsPkts64Octets_Object = MibTableColumn
reportsL2IfaceStatsPkts64Octets = _ReportsL2IfaceStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 34),
    _ReportsL2IfaceStatsPkts64Octets_Type()
)
reportsL2IfaceStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsPkts64Octets.setStatus("current")
_ReportsL2IfaceStatsPkts65to127Octets_Type = Counter32
_ReportsL2IfaceStatsPkts65to127Octets_Object = MibTableColumn
reportsL2IfaceStatsPkts65to127Octets = _ReportsL2IfaceStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 35),
    _ReportsL2IfaceStatsPkts65to127Octets_Type()
)
reportsL2IfaceStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsPkts65to127Octets.setStatus("current")
_ReportsL2IfaceStatsPkts128to255Octets_Type = Counter32
_ReportsL2IfaceStatsPkts128to255Octets_Object = MibTableColumn
reportsL2IfaceStatsPkts128to255Octets = _ReportsL2IfaceStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 36),
    _ReportsL2IfaceStatsPkts128to255Octets_Type()
)
reportsL2IfaceStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsPkts128to255Octets.setStatus("current")
_ReportsL2IfaceStatsPkts256to511Octets_Type = Counter32
_ReportsL2IfaceStatsPkts256to511Octets_Object = MibTableColumn
reportsL2IfaceStatsPkts256to511Octets = _ReportsL2IfaceStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 37),
    _ReportsL2IfaceStatsPkts256to511Octets_Type()
)
reportsL2IfaceStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsPkts256to511Octets.setStatus("current")
_ReportsL2IfaceStatsPkts512to1023Octets_Type = Counter32
_ReportsL2IfaceStatsPkts512to1023Octets_Object = MibTableColumn
reportsL2IfaceStatsPkts512to1023Octets = _ReportsL2IfaceStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 38),
    _ReportsL2IfaceStatsPkts512to1023Octets_Type()
)
reportsL2IfaceStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsPkts512to1023Octets.setStatus("current")
_ReportsL2IfaceStatsPkts1024to1518Octets_Type = Counter32
_ReportsL2IfaceStatsPkts1024to1518Octets_Object = MibTableColumn
reportsL2IfaceStatsPkts1024to1518Octets = _ReportsL2IfaceStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 39),
    _ReportsL2IfaceStatsPkts1024to1518Octets_Type()
)
reportsL2IfaceStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceStatsPkts1024to1518Octets.setStatus("current")


class _ReportsL2IfaceFlow_Type(Integer32):
    """Custom type reportsL2IfaceFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("flowon", 2),
          ("flowoff", 3))
    )


_ReportsL2IfaceFlow_Type.__name__ = "Integer32"
_ReportsL2IfaceFlow_Object = MibTableColumn
reportsL2IfaceFlow = _ReportsL2IfaceFlow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 40),
    _ReportsL2IfaceFlow_Type()
)
reportsL2IfaceFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceFlow.setStatus("current")
_ReportsL2IfaceHWType_Type = ModuleHwType
_ReportsL2IfaceHWType_Object = MibTableColumn
reportsL2IfaceHWType = _ReportsL2IfaceHWType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 41),
    _ReportsL2IfaceHWType_Type()
)
reportsL2IfaceHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceHWType.setStatus("current")
_ReportsL2IfaceActiveJackIndex_Type = Integer32
_ReportsL2IfaceActiveJackIndex_Object = MibTableColumn
reportsL2IfaceActiveJackIndex = _ReportsL2IfaceActiveJackIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 1, 1, 1, 42),
    _ReportsL2IfaceActiveJackIndex_Type()
)
reportsL2IfaceActiveJackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsL2IfaceActiveJackIndex.setStatus("current")
_ReportsHardware_ObjectIdentity = ObjectIdentity
reportsHardware = _ReportsHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2)
)


class _ReportsHardwarePSStatus_Type(OctetString):
    """Custom type reportsHardwarePSStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ReportsHardwarePSStatus_Type.__name__ = "OctetString"
_ReportsHardwarePSStatus_Object = MibScalar
reportsHardwarePSStatus = _ReportsHardwarePSStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2, 1),
    _ReportsHardwarePSStatus_Type()
)
reportsHardwarePSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsHardwarePSStatus.setStatus("current")


class _ReportsHardwareFanStatus_Type(OctetString):
    """Custom type reportsHardwareFanStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ReportsHardwareFanStatus_Type.__name__ = "OctetString"
_ReportsHardwareFanStatus_Object = MibScalar
reportsHardwareFanStatus = _ReportsHardwareFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2, 2),
    _ReportsHardwareFanStatus_Type()
)
reportsHardwareFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsHardwareFanStatus.setStatus("current")
_ReportsHardwareTemperature_Type = Integer32
_ReportsHardwareTemperature_Object = MibScalar
reportsHardwareTemperature = _ReportsHardwareTemperature_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2, 3),
    _ReportsHardwareTemperature_Type()
)
reportsHardwareTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsHardwareTemperature.setStatus("current")


class _ReportsHardwarePSVoltage_Type(OctetString):
    """Custom type reportsHardwarePSVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ReportsHardwarePSVoltage_Type.__name__ = "OctetString"
_ReportsHardwarePSVoltage_Object = MibScalar
reportsHardwarePSVoltage = _ReportsHardwarePSVoltage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2, 4),
    _ReportsHardwarePSVoltage_Type()
)
reportsHardwarePSVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsHardwarePSVoltage.setStatus("current")


class _ReportsHardwareTemperatureScale_Type(Integer32):
    """Custom type reportsHardwareTemperatureScale based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_ReportsHardwareTemperatureScale_Type.__name__ = "Integer32"
_ReportsHardwareTemperatureScale_Object = MibScalar
reportsHardwareTemperatureScale = _ReportsHardwareTemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2, 5),
    _ReportsHardwareTemperatureScale_Type()
)
reportsHardwareTemperatureScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reportsHardwareTemperatureScale.setStatus("current")


class _ReportsHardwareTemperatureHighLimit_Type(Integer32):
    """Custom type reportsHardwareTemperatureHighLimit based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 70),
    )


_ReportsHardwareTemperatureHighLimit_Type.__name__ = "Integer32"
_ReportsHardwareTemperatureHighLimit_Object = MibScalar
reportsHardwareTemperatureHighLimit = _ReportsHardwareTemperatureHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2, 6),
    _ReportsHardwareTemperatureHighLimit_Type()
)
reportsHardwareTemperatureHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reportsHardwareTemperatureHighLimit.setStatus("current")


class _ReportsHardwareDoorStatus_Type(Integer32):
    """Custom type reportsHardwareDoorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ReportsHardwareDoorStatus_Type.__name__ = "Integer32"
_ReportsHardwareDoorStatus_Object = MibScalar
reportsHardwareDoorStatus = _ReportsHardwareDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 2, 7),
    _ReportsHardwareDoorStatus_Type()
)
reportsHardwareDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsHardwareDoorStatus.setStatus("current")
_ReportsIfJack_ObjectIdentity = ObjectIdentity
reportsIfJack = _ReportsIfJack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 3)
)
_ReportsIfJackTable_Object = MibTable
reportsIfJackTable = _ReportsIfJackTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 3, 2)
)
if mibBuilder.loadTexts:
    reportsIfJackTable.setStatus("current")
_ReportsIfJackEntry_Object = MibTableRow
reportsIfJackEntry = _ReportsIfJackEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 3, 2, 1)
)
reportsIfJackEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"),
    (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"),
)
if mibBuilder.loadTexts:
    reportsIfJackEntry.setStatus("current")


class _ReportsIfJackIndex_Type(Integer32):
    """Custom type reportsIfJackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ReportsIfJackIndex_Type.__name__ = "Integer32"
_ReportsIfJackIndex_Object = MibTableColumn
reportsIfJackIndex = _ReportsIfJackIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 3, 2, 1, 1),
    _ReportsIfJackIndex_Type()
)
reportsIfJackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reportsIfJackIndex.setStatus("current")
_ReportsIfJackType_Type = ModuleHwType
_ReportsIfJackType_Object = MibTableColumn
reportsIfJackType = _ReportsIfJackType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 3, 3, 2, 1, 2),
    _ReportsIfJackType_Type()
)
reportsIfJackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportsIfJackType.setStatus("current")
_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 4)
)
_Commands_ObjectIdentity = ObjectIdentity
commands = _Commands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 5)
)
_PrvtSwitchConformance_ObjectIdentity = ObjectIdentity
prvtSwitchConformance = _PrvtSwitchConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 6)
)
_PrvtSwitchMIBGroups_ObjectIdentity = ObjectIdentity
prvtSwitchMIBGroups = _PrvtSwitchMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 6, 2)
)
_Acs25L4282_ObjectIdentity = ObjectIdentity
acs25L4282 = _Acs25L4282_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 500)
)
_Acs25L4282t5_ObjectIdentity = ObjectIdentity
acs25L4282t5 = _Acs25L4282t5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 502)
)
_Vol5000_ObjectIdentity = ObjectIdentity
vol5000 = _Vol5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 996)
)
_Vol4000_ObjectIdentity = ObjectIdentity
vol4000 = _Vol4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 998)
)
_Vol0215_ObjectIdentity = ObjectIdentity
vol0215 = _Vol0215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 999)
)
_IpSwitch_ObjectIdentity = ObjectIdentity
ipSwitch = _IpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6)
)
_Prvt_mgmt_ObjectIdentity = ObjectIdentity
prvt_mgmt = _Prvt_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 2)
)

# Managed Objects groups


# Notification objects

cpuTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 1)
)
cpuTemperatureExceeded.setObjects(
    ("PRVT-SWITCH-MIB", "reportsHardwareTemperature")
)
if mibBuilder.loadTexts:
    cpuTemperatureExceeded.setStatus(
        "current"
    )

powerSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 2)
)
powerSupplyStatusChange.setObjects(
    ("PRVT-SWITCH-MIB", "reportsHardwarePSStatus")
)
if mibBuilder.loadTexts:
    powerSupplyStatusChange.setStatus(
        "current"
    )

fanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 3)
)
fanStatusChange.setObjects(
    ("PRVT-SWITCH-MIB", "reportsHardwareFanStatus")
)
if mibBuilder.loadTexts:
    fanStatusChange.setStatus(
        "current"
    )

portSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 4)
)
portSecurityViolation.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portSecurityViolation.setStatus(
        "current"
    )

portRedundantLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 5)
)
portRedundantLinkChange.setObjects(
      *(("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("PRVT-SWITCH-MIB", "reportsL2IfaceLink"))
)
if mibBuilder.loadTexts:
    portRedundantLinkChange.setStatus(
        "current"
    )

sysIntfModuleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 6)
)
sysIntfModuleChange.setObjects(
    ("PRVT-SWITCH-MIB", "sysIntfModule")
)
if mibBuilder.loadTexts:
    sysIntfModuleChange.setStatus(
        "current"
    )

prvtLogNotifyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 7)
)
if mibBuilder.loadTexts:
    prvtLogNotifyFull.setStatus(
        "current"
    )

doorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 0, 8)
)
doorStatusChange.setObjects(
    ("PRVT-SWITCH-MIB", "reportsHardwareDoorStatus")
)
if mibBuilder.loadTexts:
    doorStatusChange.setStatus(
        "current"
    )


# Notifications groups

prvtSwitchNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 100, 6, 2, 3)
)
prvtSwitchNotificationGroup.setObjects(
      *(("PRVT-SWITCH-MIB", "cpuTemperatureExceeded"),
        ("PRVT-SWITCH-MIB", "powerSupplyStatusChange"),
        ("PRVT-SWITCH-MIB", "fanStatusChange"),
        ("PRVT-SWITCH-MIB", "portSecurityViolation"),
        ("PRVT-SWITCH-MIB", "portRedundantLinkChange"),
        ("PRVT-SWITCH-MIB", "sysIntfModuleChange"),
        ("PRVT-SWITCH-MIB", "doorStatusChange"))
)
if mibBuilder.loadTexts:
    prvtSwitchNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SWITCH-MIB",
    **{"UnitIndex": UnitIndex,
       "ModuleHwType": ModuleHwType,
       "Series": Series,
       "prvt-products": prvt_products,
       "rptr": rptr,
       "bridge": bridge,
       "trclam": trclam,
       "router": router,
       "switch": switch,
       "bsw": bsw,
       "tps": tps,
       "tpf": tpf,
       "titan": titan,
       "titant5": titant5,
       "edgeLinkT4": edgeLinkT4,
       "edgeLinkT5": edgeLinkT5,
       "titanPro": titanPro,
       "prvtSwitchMib": prvtSwitchMib,
       "prvtSwitchNotifications": prvtSwitchNotifications,
       "cpuTemperatureExceeded": cpuTemperatureExceeded,
       "powerSupplyStatusChange": powerSupplyStatusChange,
       "fanStatusChange": fanStatusChange,
       "portSecurityViolation": portSecurityViolation,
       "portRedundantLinkChange": portRedundantLinkChange,
       "sysIntfModuleChange": sysIntfModuleChange,
       "prvtLogNotifyFull": prvtLogNotifyFull,
       "doorStatusChange": doorStatusChange,
       "sys": sys,
       "sysProductsOids": sysProductsOids,
       "t4Router": t4Router,
       "t5Router": t5Router,
       "t5ProRouter": t5ProRouter,
       "t6Router": t6Router,
       "t5c-48TRouter": t5c_48TRouter,
       "t5RNRouter": t5RNRouter,
       "t5c-24TRouter": t5c_24TRouter,
       "as9205": as9205,
       "t5c-24MRouter": t5c_24MRouter,
       "t5c-24FRouter": t5c_24FRouter,
       "as9205-F": as9205_F,
       "t5c-24GRouter": t5c_24GRouter,
       "t5c-24GTRouter": t5c_24GTRouter,
       "t6pro-lc-20G": t6pro_lc_20G,
       "t6pro-cpm": t6pro_cpm,
       "compact": compact,
       "classic": classic,
       "tMetro": tMetro,
       "alcatel-7250": alcatel_7250,
       "tMarc": tMarc,
       "tMarc-250": tMarc_250,
       "dm9225": dm9225,
       "tMarc-254": tMarc_254,
       "dm9225-E": dm9225_E,
       "tMarc-254h": tMarc_254h,
       "tMarc-340": tMarc_340,
       "dm9234": dm9234,
       "tMarc-380": tMarc_380,
       "tMarc-280": tMarc_280,
       "aHUB1-A": aHUB1_A,
       "bI-Ethernet": bI_Ethernet,
       "fI-Ethernet": fI_Ethernet,
       "tMetro-ES": tMetro_ES,
       "alcatel-7250-ES": alcatel_7250_ES,
       "alcatel-7250-ESA": alcatel_7250_ESA,
       "tMetro-ESA": tMetro_ESA,
       "as9220": as9220,
       "tMetro-200S": tMetro_200S,
       "tMarc-E": tMarc_E,
       "tMarc-340-E": tMarc_340_E,
       "tMarc-380-E": tMarc_380_E,
       "tMarc-EW": tMarc_EW,
       "tMarc-340-EW": tMarc_340_EW,
       "tMarc-380-EW": tMarc_380_EW,
       "tMarc-WDB": tMarc_WDB,
       "tMarc-340WD-B": tMarc_340WD_B,
       "tMarc-WD": tMarc_WD,
       "tMarc-340WD": tMarc_340WD,
       "tMarc-F": tMarc_F,
       "tMarc-340-F": tMarc_340_F,
       "t5c-XG": t5c_XG,
       "as9215": as9215,
       "t5c": t5c,
       "t5cgt": t5cgt,
       "t5g": t5g,
       "v24s": v24s,
       "edgeGate281": edgeGate281,
       "edgeGate281SYS": edgeGate281SYS,
       "edgeGate231": edgeGate231,
       "edgeGate282": edgeGate282,
       "edgeGate282S": edgeGate282S,
       "edgeGate482S": edgeGate482S,
       "edgeGate483S": edgeGate483S,
       "edgeGate483D": edgeGate483D,
       "edgeGate201": edgeGate201,
       "edgeGate232": edgeGate232,
       "ac500": ac500,
       "ac505": ac505,
       "ac512": ac512,
       "ac524": ac524,
       "sysIntf": sysIntf,
       "sysIntfTable": sysIntfTable,
       "sysIntfEntry": sysIntfEntry,
       "sysStackNo": sysStackNo,
       "sysSlotNo": sysSlotNo,
       "sysIntfUnitExist": sysIntfUnitExist,
       "sysIntfModule": sysIntfModule,
       "sysManufacturing": sysManufacturing,
       "sysSerialNumber": sysSerialNumber,
       "sysSwitchModel": sysSwitchModel,
       "sysAssemblyNumber": sysAssemblyNumber,
       "sysPartNumber": sysPartNumber,
       "sysCLEI": sysCLEI,
       "sysHwRevision": sysHwRevision,
       "sysManufacturingDate": sysManufacturingDate,
       "sysSwitchingHW": sysSwitchingHW,
       "sysSwitchSeries": sysSwitchSeries,
       "config": config,
       "configL2": configL2,
       "configL2SpanOnOff": configL2SpanOnOff,
       "configL2IfaceTable": configL2IfaceTable,
       "configL2IfaceEntry": configL2IfaceEntry,
       "configL2IfaceUnit": configL2IfaceUnit,
       "configL2IfaceSlot": configL2IfaceSlot,
       "configL2IfacePort": configL2IfacePort,
       "configL2IfaceName": configL2IfaceName,
       "configL2IfaceEnable": configL2IfaceEnable,
       "configL2IfaceSTPEnable": configL2IfaceSTPEnable,
       "configL2IfaceDuplexSpeedSet": configL2IfaceDuplexSpeedSet,
       "configL2IfaceFlow": configL2IfaceFlow,
       "configL2IfaceBackpressure": configL2IfaceBackpressure,
       "configL2IfaceResetCounters": configL2IfaceResetCounters,
       "configL2IfaceDefaultVID": configL2IfaceDefaultVID,
       "configL2IfaceSnifferIfIndex": configL2IfaceSnifferIfIndex,
       "configL2TopologyChangeDetection": configL2TopologyChangeDetection,
       "configL2IfaceDuplexModeSet": configL2IfaceDuplexModeSet,
       "configL2IfaceSpeedSet": configL2IfaceSpeedSet,
       "configL2IfaceBroadcastRateLimit": configL2IfaceBroadcastRateLimit,
       "configL2IfaceMulticastRateLimit": configL2IfaceMulticastRateLimit,
       "configL2IfaceUnknownRateLimit": configL2IfaceUnknownRateLimit,
       "configL2IfaceBroadcastBurstSize": configL2IfaceBroadcastBurstSize,
       "configL2IfaceMulticastBurstSize": configL2IfaceMulticastBurstSize,
       "configL2IfaceUnknownBurstSize": configL2IfaceUnknownBurstSize,
       "configL2IfaceMtu": configL2IfaceMtu,
       "configL2IfaceAdminCrossOver": configL2IfaceAdminCrossOver,
       "configL2IfaceRemoteFaultDetect": configL2IfaceRemoteFaultDetect,
       "reports": reports,
       "reportsL2": reportsL2,
       "reportsL2IfaceTable": reportsL2IfaceTable,
       "reportsL2IfaceEntry": reportsL2IfaceEntry,
       "reportsL2IfaceUnit": reportsL2IfaceUnit,
       "reportsL2IfaceSlot": reportsL2IfaceSlot,
       "reportsL2IfacePort": reportsL2IfacePort,
       "reportsL2IfaceBridgeIndex": reportsL2IfaceBridgeIndex,
       "reportsL2IfaceType": reportsL2IfaceType,
       "reportsL2IfaceLink": reportsL2IfaceLink,
       "reportsL2IfaceDuplexSpeedGet": reportsL2IfaceDuplexSpeedGet,
       "reportsL2IfaceTXOctetsNoErr": reportsL2IfaceTXOctetsNoErr,
       "reportsL2IfaceTXPacketsNoErr": reportsL2IfaceTXPacketsNoErr,
       "reportsL2IfaceRXOctetsNoErr": reportsL2IfaceRXOctetsNoErr,
       "reportsL2IfaceRXPacketsNoErr": reportsL2IfaceRXPacketsNoErr,
       "reportsL2IfaceIfInOctets": reportsL2IfaceIfInOctets,
       "reportsL2IfaceIfInUcastPkts": reportsL2IfaceIfInUcastPkts,
       "reportsL2IfaceIfInNUcastPkts": reportsL2IfaceIfInNUcastPkts,
       "reportsL2IfaceIfInDiscards": reportsL2IfaceIfInDiscards,
       "reportsL2IfaceIfInErrors": reportsL2IfaceIfInErrors,
       "reportsL2IfaceIfInUnknownProtos": reportsL2IfaceIfInUnknownProtos,
       "reportsL2IfaceIfOutOctets": reportsL2IfaceIfOutOctets,
       "reportsL2IfaceIfOutUcastPkts": reportsL2IfaceIfOutUcastPkts,
       "reportsL2IfaceIfOutNUcastPkts": reportsL2IfaceIfOutNUcastPkts,
       "reportsL2IfaceIfOutDiscards": reportsL2IfaceIfOutDiscards,
       "reportsL2IfaceIfOutErrors": reportsL2IfaceIfOutErrors,
       "reportsL2IfaceStatsDropEvents": reportsL2IfaceStatsDropEvents,
       "reportsL2IfaceStatsOctets": reportsL2IfaceStatsOctets,
       "reportsL2IfaceStatsPkts": reportsL2IfaceStatsPkts,
       "reportsL2IfaceStatsBroadcastPkts": reportsL2IfaceStatsBroadcastPkts,
       "reportsL2IfaceStatsMulticastPkts": reportsL2IfaceStatsMulticastPkts,
       "reportsL2IfaceStatsCRCAlignErrors": reportsL2IfaceStatsCRCAlignErrors,
       "reportsL2IfaceStatsUndersizePkts": reportsL2IfaceStatsUndersizePkts,
       "reportsL2IfaceStatsOversizePkts": reportsL2IfaceStatsOversizePkts,
       "reportsL2IfaceStatsFragments": reportsL2IfaceStatsFragments,
       "reportsL2IfaceStatsJabbers": reportsL2IfaceStatsJabbers,
       "reportsL2IfaceStatsCollisions": reportsL2IfaceStatsCollisions,
       "reportsL2IfaceStatsPkts64Octets": reportsL2IfaceStatsPkts64Octets,
       "reportsL2IfaceStatsPkts65to127Octets": reportsL2IfaceStatsPkts65to127Octets,
       "reportsL2IfaceStatsPkts128to255Octets": reportsL2IfaceStatsPkts128to255Octets,
       "reportsL2IfaceStatsPkts256to511Octets": reportsL2IfaceStatsPkts256to511Octets,
       "reportsL2IfaceStatsPkts512to1023Octets": reportsL2IfaceStatsPkts512to1023Octets,
       "reportsL2IfaceStatsPkts1024to1518Octets": reportsL2IfaceStatsPkts1024to1518Octets,
       "reportsL2IfaceFlow": reportsL2IfaceFlow,
       "reportsL2IfaceHWType": reportsL2IfaceHWType,
       "reportsL2IfaceActiveJackIndex": reportsL2IfaceActiveJackIndex,
       "reportsHardware": reportsHardware,
       "reportsHardwarePSStatus": reportsHardwarePSStatus,
       "reportsHardwareFanStatus": reportsHardwareFanStatus,
       "reportsHardwareTemperature": reportsHardwareTemperature,
       "reportsHardwarePSVoltage": reportsHardwarePSVoltage,
       "reportsHardwareTemperatureScale": reportsHardwareTemperatureScale,
       "reportsHardwareTemperatureHighLimit": reportsHardwareTemperatureHighLimit,
       "reportsHardwareDoorStatus": reportsHardwareDoorStatus,
       "reportsIfJack": reportsIfJack,
       "reportsIfJackTable": reportsIfJackTable,
       "reportsIfJackEntry": reportsIfJackEntry,
       "reportsIfJackIndex": reportsIfJackIndex,
       "reportsIfJackType": reportsIfJackType,
       "test": test,
       "commands": commands,
       "prvtSwitchConformance": prvtSwitchConformance,
       "prvtSwitchMIBGroups": prvtSwitchMIBGroups,
       "prvtSwitchNotificationGroup": prvtSwitchNotificationGroup,
       "acs25L4282": acs25L4282,
       "acs25L4282t5": acs25L4282t5,
       "vol5000": vol5000,
       "vol4000": vol4000,
       "vol0215": vol0215,
       "ipSwitch": ipSwitch,
       "prvt-mgmt": prvt_mgmt}
)
