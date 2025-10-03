# SNMP MIB module (ZYXEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zyxel\ZYXEL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:50 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_Prestige_ObjectIdentity = ObjectIdentity
prestige = _Prestige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2)
)
_PrestigeCommon_ObjectIdentity = ObjectIdentity
prestigeCommon = _PrestigeCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1)
)
_P200Series_ObjectIdentity = ObjectIdentity
p200Series = _P200Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2)
)
_P300Series_ObjectIdentity = ObjectIdentity
p300Series = _P300Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3)
)
_P400Series_ObjectIdentity = ObjectIdentity
p400Series = _P400Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4)
)
_P500Series_ObjectIdentity = ObjectIdentity
p500Series = _P500Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5)
)
_P600Series_ObjectIdentity = ObjectIdentity
p600Series = _P600Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6)
)
_P641_ObjectIdentity = ObjectIdentity
p641 = _P641_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 1)
)
_P642_ObjectIdentity = ObjectIdentity
p642 = _P642_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 2)
)
_P643_ObjectIdentity = ObjectIdentity
p643 = _P643_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 3)
)
_P700Series_ObjectIdentity = ObjectIdentity
p700Series = _P700Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7)
)
_P794ra_ObjectIdentity = ObjectIdentity
p794ra = _P794ra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1)
)
_P794rb_ObjectIdentity = ObjectIdentity
p794rb = _P794rb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 2)
)
_P800Series_ObjectIdentity = ObjectIdentity
p800Series = _P800Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8)
)
_P900Series_ObjectIdentity = ObjectIdentity
p900Series = _P900Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 9)
)
_Rack_ObjectIdentity = ObjectIdentity
rack = _Rack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3)
)
_Dslam_ObjectIdentity = ObjectIdentity
dslam = _Dslam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 4)
)
_DslamCommon_ObjectIdentity = ObjectIdentity
dslamCommon = _DslamCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 4, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_AccessSwitchCommon_ObjectIdentity = ObjectIdentity
accessSwitchCommon = _AccessSwitchCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1)
)
_Aes100_ObjectIdentity = ObjectIdentity
aes100 = _Aes100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 2)
)
_Pes100_ObjectIdentity = ObjectIdentity
pes100 = _Pes100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 3)
)
_Ves1012_ObjectIdentity = ObjectIdentity
ves1012 = _Ves1012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 4)
)
_SesSeries_ObjectIdentity = ObjectIdentity
sesSeries = _SesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5)
)
_SesSeriesCommon_ObjectIdentity = ObjectIdentity
sesSeriesCommon = _SesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1)
)
_Sam1008_ObjectIdentity = ObjectIdentity
sam1008 = _Sam1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 2)
)
_Ses1024_ObjectIdentity = ObjectIdentity
ses1024 = _Ses1024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 3)
)
_Slc1024_ObjectIdentity = ObjectIdentity
slc1024 = _Slc1024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 4)
)
_Slc1224_22_ObjectIdentity = ObjectIdentity
slc1224_22 = _Slc1224_22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 5)
)
_Sam1216_22_ObjectIdentity = ObjectIdentity
sam1216_22 = _Sam1216_22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6)
)
_Ies708_22a_stuc_ObjectIdentity = ObjectIdentity
ies708_22a_stuc = _Ies708_22a_stuc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 7)
)
_Ies708_22a_stur_ObjectIdentity = ObjectIdentity
ies708_22a_stur = _Ies708_22a_stur_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 8)
)
_P1600_ObjectIdentity = ObjectIdentity
p1600 = _P1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 6)
)
_P1400_ObjectIdentity = ObjectIdentity
p1400 = _P1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 7)
)
_EsSeries_ObjectIdentity = ObjectIdentity
esSeries = _EsSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8)
)
_EsSeriesCommon_ObjectIdentity = ObjectIdentity
esSeriesCommon = _EsSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 1)
)
_Ees1024af_ObjectIdentity = ObjectIdentity
ees1024af = _Ees1024af_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2)
)
_Es2008_ObjectIdentity = ObjectIdentity
es2008 = _Es2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 3)
)
_Es2008_gtp_ObjectIdentity = ObjectIdentity
es2008_gtp = _Es2008_gtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 4)
)
_Es2008_sc_ObjectIdentity = ObjectIdentity
es2008_sc = _Es2008_sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 5)
)
_Es2008_sc30_ObjectIdentity = ObjectIdentity
es2008_sc30 = _Es2008_sc30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 6)
)
_Es3024_ObjectIdentity = ObjectIdentity
es3024 = _Es3024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 7)
)
_Es4024_ObjectIdentity = ObjectIdentity
es4024 = _Es4024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 8)
)
_Es2024_ObjectIdentity = ObjectIdentity
es2024 = _Es2024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 9)
)
_Gs3012_ObjectIdentity = ObjectIdentity
gs3012 = _Gs3012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 10)
)
_Gs3012f_ObjectIdentity = ObjectIdentity
gs3012f = _Gs3012f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 11)
)
_Es3124_ObjectIdentity = ObjectIdentity
es3124 = _Es3124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 12)
)
_Gs4024_ObjectIdentity = ObjectIdentity
gs4024 = _Gs4024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 13)
)
_Es3124pwr_ObjectIdentity = ObjectIdentity
es3124pwr = _Es3124pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14)
)
_Gs2024_ObjectIdentity = ObjectIdentity
gs2024 = _Gs2024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 15)
)
_Es2024a_ObjectIdentity = ObjectIdentity
es2024a = _Es2024a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 16)
)
_Es3148_ObjectIdentity = ObjectIdentity
es3148 = _Es3148_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 17)
)
_Es2108_ObjectIdentity = ObjectIdentity
es2108 = _Es2108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 18)
)
_Es2108g_ObjectIdentity = ObjectIdentity
es2108g = _Es2108g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19)
)
_Gs4012f_ObjectIdentity = ObjectIdentity
gs4012f = _Gs4012f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 20)
)
_Es2108pwr_ObjectIdentity = ObjectIdentity
es2108pwr = _Es2108pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 21)
)
_Es2108lc_ObjectIdentity = ObjectIdentity
es2108lc = _Es2108lc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 22)
)
_Es2048_ObjectIdentity = ObjectIdentity
es2048 = _Es2048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 23)
)
_Es4124_ObjectIdentity = ObjectIdentity
es4124 = _Es4124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 24)
)
_Es3124_4f_ObjectIdentity = ObjectIdentity
es3124_4f = _Es3124_4f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 26)
)
_Es2024pwr_ObjectIdentity = ObjectIdentity
es2024pwr = _Es2024pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 27)
)
_Es3724_ObjectIdentity = ObjectIdentity
es3724 = _Es3724_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 28)
)
_Es2108f_ObjectIdentity = ObjectIdentity
es2108f = _Es2108f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 29)
)
_Es2226_ObjectIdentity = ObjectIdentity
es2226 = _Es2226_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 30)
)
_Es3124f_ObjectIdentity = ObjectIdentity
es3124f = _Es3124f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 31)
)
_Es1528_ObjectIdentity = ObjectIdentity
es1528 = _Es1528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 32)
)
_Es1552_ObjectIdentity = ObjectIdentity
es1552 = _Es1552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 33)
)
_Ms7206_ObjectIdentity = ObjectIdentity
ms7206 = _Ms7206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 34)
)
_Gs2724_ObjectIdentity = ObjectIdentity
gs2724 = _Gs2724_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 35)
)
_Gs1524_ObjectIdentity = ObjectIdentity
gs1524 = _Gs1524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 36)
)
_Gs1548_ObjectIdentity = ObjectIdentity
gs1548 = _Gs1548_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 37)
)
_Es305_ObjectIdentity = ObjectIdentity
es305 = _Es305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 38)
)
_Xsg4528f_ObjectIdentity = ObjectIdentity
xsg4528f = _Xsg4528f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 39)
)
_Es3528_ObjectIdentity = ObjectIdentity
es3528 = _Es3528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 40)
)
_Es315_ObjectIdentity = ObjectIdentity
es315 = _Es315_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 41)
)
_Es315f_ObjectIdentity = ObjectIdentity
es315f = _Es315f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 42)
)
_Gs2726_ObjectIdentity = ObjectIdentity
gs2726 = _Gs2726_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 43)
)
_Gs2750_ObjectIdentity = ObjectIdentity
gs2750 = _Gs2750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 44)
)
_Mes3728_ObjectIdentity = ObjectIdentity
mes3728 = _Mes3728_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 45)
)
_Xgs4728f_ObjectIdentity = ObjectIdentity
xgs4728f = _Xgs4728f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 46)
)
_Mgs3712_ObjectIdentity = ObjectIdentity
mgs3712 = _Mgs3712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 47)
)
_Mgs3712f_ObjectIdentity = ObjectIdentity
mgs3712f = _Mgs3712f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 48)
)
_Es2105_ObjectIdentity = ObjectIdentity
es2105 = _Es2105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 49)
)
_Gs4012f_ncic_ObjectIdentity = ObjectIdentity
gs4012f_ncic = _Gs4012f_ncic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 50)
)
_Mes3528_ObjectIdentity = ObjectIdentity
mes3528 = _Mes3528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 51)
)
_Xgs2726_ObjectIdentity = ObjectIdentity
xgs2726 = _Xgs2726_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 52)
)
_Gs2200_48_ObjectIdentity = ObjectIdentity
gs2200_48 = _Gs2200_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 53)
)
_Aes100_1_ObjectIdentity = ObjectIdentity
aes100_1 = _Aes100_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 9)
)
_Pes1014_ObjectIdentity = ObjectIdentity
pes1014 = _Pes1014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 10)
)
_AesSeries_ObjectIdentity = ObjectIdentity
aesSeries = _AesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11)
)
_AesSeriesCommon_ObjectIdentity = ObjectIdentity
aesSeriesCommon = _AesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1)
)
_Aes1024_ObjectIdentity = ObjectIdentity
aes1024 = _Aes1024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 2)
)
_Alc1024_61_ObjectIdentity = ObjectIdentity
alc1024_61 = _Alc1024_61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 3)
)
_Aam1008_63_ObjectIdentity = ObjectIdentity
aam1008_63 = _Aam1008_63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 4)
)
_Alc1024_63_ObjectIdentity = ObjectIdentity
alc1024_63 = _Alc1024_63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 5)
)
_Aam1008_61_ObjectIdentity = ObjectIdentity
aam1008_61 = _Aam1008_61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 6)
)
_Alc1224_71_ObjectIdentity = ObjectIdentity
alc1224_71 = _Alc1224_71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 7)
)
_Ies1248_71_ObjectIdentity = ObjectIdentity
ies1248_71 = _Ies1248_71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 9)
)
_Ies1248_73_ObjectIdentity = ObjectIdentity
ies1248_73 = _Ies1248_73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 10)
)
_Aam1212_51_ObjectIdentity = ObjectIdentity
aam1212_51 = _Aam1212_51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 11)
)
_Aam1212_53_ObjectIdentity = ObjectIdentity
aam1212_53 = _Aam1212_53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 12)
)
_Ies1248_51_ObjectIdentity = ObjectIdentity
ies1248_51 = _Ies1248_51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 13)
)
_Ies1248_53_ObjectIdentity = ObjectIdentity
ies1248_53 = _Ies1248_53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 14)
)
_Alc1224_51_ObjectIdentity = ObjectIdentity
alc1224_51 = _Alc1224_51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 15)
)
_Alc1224_53_ObjectIdentity = ObjectIdentity
alc1224_53 = _Alc1224_53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 16)
)
_Ies1248_51v_ObjectIdentity = ObjectIdentity
ies1248_51v = _Ies1248_51v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 17)
)
_VesSeries_ObjectIdentity = ObjectIdentity
vesSeries = _VesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12)
)
_VesSeriesCommon_ObjectIdentity = ObjectIdentity
vesSeriesCommon = _VesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1)
)
_Ves1008_ObjectIdentity = ObjectIdentity
ves1008 = _Ves1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 2)
)
_Ves1024_ObjectIdentity = ObjectIdentity
ves1024 = _Ves1024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 4)
)
_Vlc1012_ObjectIdentity = ObjectIdentity
vlc1012 = _Vlc1012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 5)
)
_Ves1316_ObjectIdentity = ObjectIdentity
ves1316 = _Ves1316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 6)
)
_Ves1416_ObjectIdentity = ObjectIdentity
ves1416 = _Ves1416_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 7)
)
_Vlc1124_ObjectIdentity = ObjectIdentity
vlc1124 = _Vlc1124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 8)
)
_Ves1124_ObjectIdentity = ObjectIdentity
ves1124 = _Ves1124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 9)
)
_Ves1616f34_ObjectIdentity = ObjectIdentity
ves1616f34 = _Ves1616f34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 10)
)
_Ves1616f44_ObjectIdentity = ObjectIdentity
ves1616f44 = _Ves1616f44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 11)
)
_Ves1624f44_ObjectIdentity = ObjectIdentity
ves1624f44 = _Ves1624f44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 12)
)
_Ves1624fa44_ObjectIdentity = ObjectIdentity
ves1624fa44 = _Ves1624fa44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 13)
)
_Ves1616fa44_ObjectIdentity = ObjectIdentity
ves1616fa44 = _Ves1616fa44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 14)
)
_Ves1616fa34_co4_ObjectIdentity = ObjectIdentity
ves1616fa34_co4 = _Ves1616fa34_co4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 15)
)
_Ves1616fa35_co4_ObjectIdentity = ObjectIdentity
ves1616fa35_co4 = _Ves1616fa35_co4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 16)
)
_Ves1608fa34_ObjectIdentity = ObjectIdentity
ves1608fa34 = _Ves1608fa34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 17)
)
_Ves1608fa35_ObjectIdentity = ObjectIdentity
ves1608fa35 = _Ves1608fa35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 18)
)
_Ves1616fa54_ObjectIdentity = ObjectIdentity
ves1616fa54 = _Ves1616fa54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 19)
)
_Ves1624fa54_ObjectIdentity = ObjectIdentity
ves1624fa54 = _Ves1624fa54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 20)
)
_Ves1616fa55_ObjectIdentity = ObjectIdentity
ves1616fa55 = _Ves1616fa55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 21)
)
_Ves1624fa55_ObjectIdentity = ObjectIdentity
ves1624fa55 = _Ves1624fa55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 22)
)
_Ves1624ft_ObjectIdentity = ObjectIdentity
ves1624ft = _Ves1624ft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 23)
)
_Ves1624fa34_ObjectIdentity = ObjectIdentity
ves1624fa34 = _Ves1624fa34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 24)
)
_Ves1608fc54_ObjectIdentity = ObjectIdentity
ves1608fc54 = _Ves1608fc54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 25)
)
_Ves1616fc54_ObjectIdentity = ObjectIdentity
ves1616fc54 = _Ves1616fc54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 26)
)
_Ves1624ft54_ObjectIdentity = ObjectIdentity
ves1624ft54 = _Ves1624ft54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 27)
)
_Ves1624ftv54_ObjectIdentity = ObjectIdentity
ves1624ftv54 = _Ves1624ftv54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 28)
)
_Ves1616cta54_ObjectIdentity = ObjectIdentity
ves1616cta54 = _Ves1616cta54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 29)
)
_Ves1624cta54_ObjectIdentity = ObjectIdentity
ves1624cta54 = _Ves1624cta54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 30)
)
_Ves1608cea54_ObjectIdentity = ObjectIdentity
ves1608cea54 = _Ves1608cea54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 31)
)
_Ves1616cea54_ObjectIdentity = ObjectIdentity
ves1616cea54 = _Ves1616cea54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 32)
)
_Ves1616fe55a_ObjectIdentity = ObjectIdentity
ves1616fe55a = _Ves1616fe55a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 33)
)
_Ves1624ft55a_ObjectIdentity = ObjectIdentity
ves1624ft55a = _Ves1624ft55a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 34)
)
_Ves1616fb35_ObjectIdentity = ObjectIdentity
ves1616fb35 = _Ves1616fb35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 35)
)
_Ves1608pe35_ObjectIdentity = ObjectIdentity
ves1608pe35 = _Ves1608pe35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 36)
)
_Ves1616fe53a_ObjectIdentity = ObjectIdentity
ves1616fe53a = _Ves1616fe53a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 37)
)
_Ves1616ft54_ObjectIdentity = ObjectIdentity
ves1616ft54 = _Ves1616ft54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 38)
)
_Ves1616ctb54_ObjectIdentity = ObjectIdentity
ves1616ctb54 = _Ves1616ctb54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 39)
)
_Ves1624ctb54_ObjectIdentity = ObjectIdentity
ves1624ctb54 = _Ves1624ctb54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 40)
)
_Ves1624ftv55a_ObjectIdentity = ObjectIdentity
ves1624ftv55a = _Ves1624ftv55a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 41)
)
_Ves1608fe53a_ObjectIdentity = ObjectIdentity
ves1608fe53a = _Ves1608fe53a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 42)
)
_Ves1608fe57_ObjectIdentity = ObjectIdentity
ves1608fe57 = _Ves1608fe57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43)
)
_Ves1602fe57_ObjectIdentity = ObjectIdentity
ves1602fe57 = _Ves1602fe57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 44)
)
_Ves1724_58b_ObjectIdentity = ObjectIdentity
ves1724_58b = _Ves1724_58b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 45)
)
_Ves1724_56_ObjectIdentity = ObjectIdentity
ves1724_56 = _Ves1724_56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 46)
)
_Ves1724_56fanless_ObjectIdentity = ObjectIdentity
ves1724_56fanless = _Ves1724_56fanless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 47)
)
_Ves1724_55C_ObjectIdentity = ObjectIdentity
ves1724_55C = _Ves1724_55C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 48)
)
_Ves1724_58V_ObjectIdentity = ObjectIdentity
ves1724_58V = _Ves1724_58V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49)
)
_IesSeries_ObjectIdentity = ObjectIdentity
iesSeries = _IesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13)
)
_IesSeriesCommon_ObjectIdentity = ObjectIdentity
iesSeriesCommon = _IesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 1)
)
_Ies2000_ObjectIdentity = ObjectIdentity
ies2000 = _Ies2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 2)
)
_Ies3000_ObjectIdentity = ObjectIdentity
ies3000 = _Ies3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 3)
)
_Ies5000_ObjectIdentity = ObjectIdentity
ies5000 = _Ies5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 5)
)
_Ies5005_ObjectIdentity = ObjectIdentity
ies5005 = _Ies5005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 7)
)
_Ies6000_ObjectIdentity = ObjectIdentity
ies6000 = _Ies6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 8)
)
_Ies5006_ObjectIdentity = ObjectIdentity
ies5006 = _Ies5006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 9)
)
_Ies5106_ObjectIdentity = ObjectIdentity
ies5106 = _Ies5106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 10)
)
_Ies5112_ObjectIdentity = ObjectIdentity
ies5112 = _Ies5112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 11)
)
_Ies4005_ObjectIdentity = ObjectIdentity
ies4005 = _Ies4005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 12)
)
_Ies5206_ObjectIdentity = ObjectIdentity
ies5206 = _Ies5206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 13)
)
_Ies6100_ObjectIdentity = ObjectIdentity
ies6100 = _Ies6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 14)
)
_Ies4204_ObjectIdentity = ObjectIdentity
ies4204 = _Ies4204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 15)
)
_Ies5212_ObjectIdentity = ObjectIdentity
ies5212 = _Ies5212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 16)
)
_Ies4105_ObjectIdentity = ObjectIdentity
ies4105 = _Ies4105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 17)
)
_Ies6217_ObjectIdentity = ObjectIdentity
ies6217 = _Ies6217_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 18)
)
_AccessSwitchCommonATM_ObjectIdentity = ObjectIdentity
accessSwitchCommonATM = _AccessSwitchCommonATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14)
)
_PonSeries_ObjectIdentity = ObjectIdentity
ponSeries = _PonSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15)
)
_Olt1308_ObjectIdentity = ObjectIdentity
olt1308 = _Olt1308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 1)
)
_Lt20h_ObjectIdentity = ObjectIdentity
lt20h = _Lt20h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 2)
)
_Olt2300_12_ObjectIdentity = ObjectIdentity
olt2300_12 = _Olt2300_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 3)
)
_Olt1308s22_ObjectIdentity = ObjectIdentity
olt1308s22 = _Olt1308s22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 4)
)
_Olt2300v3_ObjectIdentity = ObjectIdentity
olt2300v3 = _Olt2300v3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 5)
)
_Eonu24240_ObjectIdentity = ObjectIdentity
eonu24240 = _Eonu24240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 6)
)
_Eonu16160_ObjectIdentity = ObjectIdentity
eonu16160 = _Eonu16160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 7)
)
_Eonu2400_ObjectIdentity = ObjectIdentity
eonu2400 = _Eonu2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 8)
)
_Eonu1600_ObjectIdentity = ObjectIdentity
eonu1600 = _Eonu1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 15, 9)
)
_VopSeries_ObjectIdentity = ObjectIdentity
vopSeries = _VopSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 16)
)
_VopSeriesCommon_ObjectIdentity = ObjectIdentity
vopSeriesCommon = _VopSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 16, 1)
)
_Vop1224_61_ObjectIdentity = ObjectIdentity
vop1224_61 = _Vop1224_61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 16, 2)
)
_GponSeries_ObjectIdentity = ObjectIdentity
gponSeries = _GponSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17)
)
_GponSeriesCommon_ObjectIdentity = ObjectIdentity
gponSeriesCommon = _GponSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 1)
)
_O_00240v_p_ObjectIdentity = ObjectIdentity
o_00240v_p = _O_00240v_p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 2)
)
_Olt2412_ObjectIdentity = ObjectIdentity
olt2412 = _Olt2412_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 17, 3)
)
_GesSeries_ObjectIdentity = ObjectIdentity
gesSeries = _GesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 18)
)
_GesSeriesCommon_ObjectIdentity = ObjectIdentity
gesSeriesCommon = _GesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 18, 1)
)
_Ges2104_ObjectIdentity = ObjectIdentity
ges2104 = _Ges2104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 18, 2)
)
_Ges1116_ObjectIdentity = ObjectIdentity
ges1116 = _Ges1116_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 18, 3)
)
_Zywall_ObjectIdentity = ObjectIdentity
zywall = _Zywall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6)
)
_ZywallCommon_ObjectIdentity = ObjectIdentity
zywallCommon = _ZywallCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 1)
)
_Zywall1_ObjectIdentity = ObjectIdentity
zywall1 = _Zywall1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 2)
)
_Zywall2_ObjectIdentity = ObjectIdentity
zywall2 = _Zywall2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 3)
)
_Zywall2w_ObjectIdentity = ObjectIdentity
zywall2w = _Zywall2w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 4)
)
_Zywall10_ObjectIdentity = ObjectIdentity
zywall10 = _Zywall10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 5)
)
_Zywall10ii_ObjectIdentity = ObjectIdentity
zywall10ii = _Zywall10ii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 6)
)
_Zywall10w_ObjectIdentity = ObjectIdentity
zywall10w = _Zywall10w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 7)
)
_Zywall50_ObjectIdentity = ObjectIdentity
zywall50 = _Zywall50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 8)
)
_Zywall100_ObjectIdentity = ObjectIdentity
zywall100 = _Zywall100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 9)
)
_Zywall200_ObjectIdentity = ObjectIdentity
zywall200 = _Zywall200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 10)
)
_Zywallidp10_ObjectIdentity = ObjectIdentity
zywallidp10 = _Zywallidp10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 11)
)
_Zywall5_ObjectIdentity = ObjectIdentity
zywall5 = _Zywall5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 12)
)
_Zywall30w_ObjectIdentity = ObjectIdentity
zywall30w = _Zywall30w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 13)
)
_Zywall35_ObjectIdentity = ObjectIdentity
zywall35 = _Zywall35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 14)
)
_Zywall70_ObjectIdentity = ObjectIdentity
zywall70 = _Zywall70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 15)
)
_Zywall1000_ObjectIdentity = ObjectIdentity
zywall1000 = _Zywall1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 16)
)
_ZywallCHT1_ObjectIdentity = ObjectIdentity
zywallCHT1 = _ZywallCHT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 17)
)
_ZywallM70_ObjectIdentity = ObjectIdentity
zywallM70 = _ZywallM70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 18)
)
_ZywallP1_ObjectIdentity = ObjectIdentity
zywallP1 = _ZywallP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 19)
)
_ZywallP2_ObjectIdentity = ObjectIdentity
zywallP2 = _ZywallP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 20)
)
_ZywallM110_ObjectIdentity = ObjectIdentity
zywallM110 = _ZywallM110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 21)
)
_ZywallZLDCommon_ObjectIdentity = ObjectIdentity
zywallZLDCommon = _ZywallZLDCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 6, 22)
)
_AtmEncryptor_ObjectIdentity = ObjectIdentity
atmEncryptor = _AtmEncryptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 7)
)
_ServiceGateway_ObjectIdentity = ObjectIdentity
serviceGateway = _ServiceGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 8)
)
_ServiceGWCommon_ObjectIdentity = ObjectIdentity
serviceGWCommon = _ServiceGWCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 8, 1)
)
_Vsg1000_ObjectIdentity = ObjectIdentity
vsg1000 = _Vsg1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 8, 2)
)
_Vsg1200_ObjectIdentity = ObjectIdentity
vsg1200 = _Vsg1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 8, 3)
)
_Vsg1200v2_ObjectIdentity = ObjectIdentity
vsg1200v2 = _Vsg1200v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 8, 4)
)
_ProWireless_ObjectIdentity = ObjectIdentity
proWireless = _ProWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9)
)
_WirelessController_ObjectIdentity = ObjectIdentity
wirelessController = _WirelessController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 10)
)
_Ipav_ObjectIdentity = ObjectIdentity
ipav = _Ipav_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 11)
)
_Wimax_ObjectIdentity = ObjectIdentity
wimax = _Wimax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 12)
)
_Ems_ObjectIdentity = ObjectIdentity
ems = _Ems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 13)
)
_NetAtlasEMS_ObjectIdentity = ObjectIdentity
netAtlasEMS = _NetAtlasEMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 13, 1)
)
_SmallCell_ObjectIdentity = ObjectIdentity
smallCell = _SmallCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 14)
)
_SmallCellCommon_ObjectIdentity = ObjectIdentity
smallCellCommon = _SmallCellCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 14, 1)
)
_LMT3313_ObjectIdentity = ObjectIdentity
LMT3313 = _LMT3313_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 14, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MIB",
    **{"zyxel": zyxel,
       "products": products,
       "prestige": prestige,
       "prestigeCommon": prestigeCommon,
       "p200Series": p200Series,
       "p300Series": p300Series,
       "p400Series": p400Series,
       "p500Series": p500Series,
       "p600Series": p600Series,
       "p641": p641,
       "p642": p642,
       "p643": p643,
       "p700Series": p700Series,
       "p794ra": p794ra,
       "p794rb": p794rb,
       "p800Series": p800Series,
       "p900Series": p900Series,
       "rack": rack,
       "dslam": dslam,
       "dslamCommon": dslamCommon,
       "accessSwitch": accessSwitch,
       "accessSwitchCommon": accessSwitchCommon,
       "aes100": aes100,
       "pes100": pes100,
       "ves1012": ves1012,
       "sesSeries": sesSeries,
       "sesSeriesCommon": sesSeriesCommon,
       "sam1008": sam1008,
       "ses1024": ses1024,
       "slc1024": slc1024,
       "slc1224-22": slc1224_22,
       "sam1216-22": sam1216_22,
       "ies708-22a-stuc": ies708_22a_stuc,
       "ies708-22a-stur": ies708_22a_stur,
       "p1600": p1600,
       "p1400": p1400,
       "esSeries": esSeries,
       "esSeriesCommon": esSeriesCommon,
       "ees1024af": ees1024af,
       "es2008": es2008,
       "es2008-gtp": es2008_gtp,
       "es2008-sc": es2008_sc,
       "es2008-sc30": es2008_sc30,
       "es3024": es3024,
       "es4024": es4024,
       "es2024": es2024,
       "gs3012": gs3012,
       "gs3012f": gs3012f,
       "es3124": es3124,
       "gs4024": gs4024,
       "es3124pwr": es3124pwr,
       "gs2024": gs2024,
       "es2024a": es2024a,
       "es3148": es3148,
       "es2108": es2108,
       "es2108g": es2108g,
       "gs4012f": gs4012f,
       "es2108pwr": es2108pwr,
       "es2108lc": es2108lc,
       "es2048": es2048,
       "es4124": es4124,
       "es3124-4f": es3124_4f,
       "es2024pwr": es2024pwr,
       "es3724": es3724,
       "es2108f": es2108f,
       "es2226": es2226,
       "es3124f": es3124f,
       "es1528": es1528,
       "es1552": es1552,
       "ms7206": ms7206,
       "gs2724": gs2724,
       "gs1524": gs1524,
       "gs1548": gs1548,
       "es305": es305,
       "xsg4528f": xsg4528f,
       "es3528": es3528,
       "es315": es315,
       "es315f": es315f,
       "gs2726": gs2726,
       "gs2750": gs2750,
       "mes3728": mes3728,
       "xgs4728f": xgs4728f,
       "mgs3712": mgs3712,
       "mgs3712f": mgs3712f,
       "es2105": es2105,
       "gs4012f-ncic": gs4012f_ncic,
       "mes3528": mes3528,
       "xgs2726": xgs2726,
       "gs2200-48": gs2200_48,
       "aes100-1": aes100_1,
       "pes1014": pes1014,
       "aesSeries": aesSeries,
       "aesSeriesCommon": aesSeriesCommon,
       "aes1024": aes1024,
       "alc1024-61": alc1024_61,
       "aam1008-63": aam1008_63,
       "alc1024-63": alc1024_63,
       "aam1008-61": aam1008_61,
       "alc1224-71": alc1224_71,
       "ies1248-71": ies1248_71,
       "ies1248-73": ies1248_73,
       "aam1212-51": aam1212_51,
       "aam1212-53": aam1212_53,
       "ies1248-51": ies1248_51,
       "ies1248-53": ies1248_53,
       "alc1224-51": alc1224_51,
       "alc1224-53": alc1224_53,
       "ies1248-51v": ies1248_51v,
       "vesSeries": vesSeries,
       "vesSeriesCommon": vesSeriesCommon,
       "ves1008": ves1008,
       "ves1024": ves1024,
       "vlc1012": vlc1012,
       "ves1316": ves1316,
       "ves1416": ves1416,
       "vlc1124": vlc1124,
       "ves1124": ves1124,
       "ves1616f34": ves1616f34,
       "ves1616f44": ves1616f44,
       "ves1624f44": ves1624f44,
       "ves1624fa44": ves1624fa44,
       "ves1616fa44": ves1616fa44,
       "ves1616fa34-co4": ves1616fa34_co4,
       "ves1616fa35-co4": ves1616fa35_co4,
       "ves1608fa34": ves1608fa34,
       "ves1608fa35": ves1608fa35,
       "ves1616fa54": ves1616fa54,
       "ves1624fa54": ves1624fa54,
       "ves1616fa55": ves1616fa55,
       "ves1624fa55": ves1624fa55,
       "ves1624ft": ves1624ft,
       "ves1624fa34": ves1624fa34,
       "ves1608fc54": ves1608fc54,
       "ves1616fc54": ves1616fc54,
       "ves1624ft54": ves1624ft54,
       "ves1624ftv54": ves1624ftv54,
       "ves1616cta54": ves1616cta54,
       "ves1624cta54": ves1624cta54,
       "ves1608cea54": ves1608cea54,
       "ves1616cea54": ves1616cea54,
       "ves1616fe55a": ves1616fe55a,
       "ves1624ft55a": ves1624ft55a,
       "ves1616fb35": ves1616fb35,
       "ves1608pe35": ves1608pe35,
       "ves1616fe53a": ves1616fe53a,
       "ves1616ft54": ves1616ft54,
       "ves1616ctb54": ves1616ctb54,
       "ves1624ctb54": ves1624ctb54,
       "ves1624ftv55a": ves1624ftv55a,
       "ves1608fe53a": ves1608fe53a,
       "ves1608fe57": ves1608fe57,
       "ves1602fe57": ves1602fe57,
       "ves1724-58b": ves1724_58b,
       "ves1724-56": ves1724_56,
       "ves1724-56fanless": ves1724_56fanless,
       "ves1724-55C": ves1724_55C,
       "ves1724-58V": ves1724_58V,
       "iesSeries": iesSeries,
       "iesSeriesCommon": iesSeriesCommon,
       "ies2000": ies2000,
       "ies3000": ies3000,
       "ies5000": ies5000,
       "ies5005": ies5005,
       "ies6000": ies6000,
       "ies5006": ies5006,
       "ies5106": ies5106,
       "ies5112": ies5112,
       "ies4005": ies4005,
       "ies5206": ies5206,
       "ies6100": ies6100,
       "ies4204": ies4204,
       "ies5212": ies5212,
       "ies4105": ies4105,
       "ies6217": ies6217,
       "accessSwitchCommonATM": accessSwitchCommonATM,
       "ponSeries": ponSeries,
       "olt1308": olt1308,
       "lt20h": lt20h,
       "olt2300-12": olt2300_12,
       "olt1308s22": olt1308s22,
       "olt2300v3": olt2300v3,
       "eonu24240": eonu24240,
       "eonu16160": eonu16160,
       "eonu2400": eonu2400,
       "eonu1600": eonu1600,
       "vopSeries": vopSeries,
       "vopSeriesCommon": vopSeriesCommon,
       "vop1224-61": vop1224_61,
       "gponSeries": gponSeries,
       "gponSeriesCommon": gponSeriesCommon,
       "o-00240v-p": o_00240v_p,
       "olt2412": olt2412,
       "gesSeries": gesSeries,
       "gesSeriesCommon": gesSeriesCommon,
       "ges2104": ges2104,
       "ges1116": ges1116,
       "zywall": zywall,
       "zywallCommon": zywallCommon,
       "zywall1": zywall1,
       "zywall2": zywall2,
       "zywall2w": zywall2w,
       "zywall10": zywall10,
       "zywall10ii": zywall10ii,
       "zywall10w": zywall10w,
       "zywall50": zywall50,
       "zywall100": zywall100,
       "zywall200": zywall200,
       "zywallidp10": zywallidp10,
       "zywall5": zywall5,
       "zywall30w": zywall30w,
       "zywall35": zywall35,
       "zywall70": zywall70,
       "zywall1000": zywall1000,
       "zywallCHT1": zywallCHT1,
       "zywallM70": zywallM70,
       "zywallP1": zywallP1,
       "zywallP2": zywallP2,
       "zywallM110": zywallM110,
       "zywallZLDCommon": zywallZLDCommon,
       "atmEncryptor": atmEncryptor,
       "serviceGateway": serviceGateway,
       "serviceGWCommon": serviceGWCommon,
       "vsg1000": vsg1000,
       "vsg1200": vsg1200,
       "vsg1200v2": vsg1200v2,
       "proWireless": proWireless,
       "wirelessController": wirelessController,
       "ipav": ipav,
       "wimax": wimax,
       "ems": ems,
       "netAtlasEMS": netAtlasEMS,
       "smallCell": smallCell,
       "smallCellCommon": smallCellCommon,
       "LMT3313": LMT3313}
)
