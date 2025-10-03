# SNMP MIB module (ARUBA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\ARUBA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:42 2025
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
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

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

_Aruba_ObjectIdentity = ObjectIdentity
aruba = _Aruba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1)
)
_SwitchProducts_ObjectIdentity = ObjectIdentity
switchProducts = _SwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1)
)
_A5000_ObjectIdentity = ObjectIdentity
a5000 = _A5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 1)
)
_A2400_ObjectIdentity = ObjectIdentity
a2400 = _A2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 2)
)
_A800_ObjectIdentity = ObjectIdentity
a800 = _A800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 3)
)
_A6000_ObjectIdentity = ObjectIdentity
a6000 = _A6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 4)
)
_A2400E_ObjectIdentity = ObjectIdentity
a2400E = _A2400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 7)
)
_A800E_ObjectIdentity = ObjectIdentity
a800E = _A800E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 8)
)
_A804_ObjectIdentity = ObjectIdentity
a804 = _A804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 9)
)
_A200_ObjectIdentity = ObjectIdentity
a200 = _A200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 10)
)
_A2424_ObjectIdentity = ObjectIdentity
a2424 = _A2424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 11)
)
_A6000_SC3_ObjectIdentity = ObjectIdentity
a6000_SC3 = _A6000_SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 12)
)
_A3200_ObjectIdentity = ObjectIdentity
a3200 = _A3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 13)
)
_A3200_8_ObjectIdentity = ObjectIdentity
a3200_8 = _A3200_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 14)
)
_A3400_ObjectIdentity = ObjectIdentity
a3400 = _A3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 15)
)
_A3400_32_ObjectIdentity = ObjectIdentity
a3400_32 = _A3400_32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 16)
)
_A3600_ObjectIdentity = ObjectIdentity
a3600 = _A3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 17)
)
_A3600_64_ObjectIdentity = ObjectIdentity
a3600_64 = _A3600_64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 18)
)
_A650_ObjectIdentity = ObjectIdentity
a650 = _A650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 19)
)
_A651_ObjectIdentity = ObjectIdentity
a651 = _A651_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 20)
)
_Reserved1_ObjectIdentity = ObjectIdentity
reserved1 = _Reserved1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 21)
)
_Reserved2_ObjectIdentity = ObjectIdentity
reserved2 = _Reserved2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 22)
)
_A620_ObjectIdentity = ObjectIdentity
a620 = _A620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 23)
)
_S3500_24P_ObjectIdentity = ObjectIdentity
s3500_24P = _S3500_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 24)
)
_S3500_24T_ObjectIdentity = ObjectIdentity
s3500_24T = _S3500_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 25)
)
_S3500_48P_ObjectIdentity = ObjectIdentity
s3500_48P = _S3500_48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 26)
)
_S3500_48T_ObjectIdentity = ObjectIdentity
s3500_48T = _S3500_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 27)
)
_S2500_24P_ObjectIdentity = ObjectIdentity
s2500_24P = _S2500_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 28)
)
_S2500_24T_ObjectIdentity = ObjectIdentity
s2500_24T = _S2500_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 29)
)
_S2500_48P_ObjectIdentity = ObjectIdentity
s2500_48P = _S2500_48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 30)
)
_S2500_48T_ObjectIdentity = ObjectIdentity
s2500_48T = _S2500_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 31)
)
_A7210_ObjectIdentity = ObjectIdentity
a7210 = _A7210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 32)
)
_A7220_ObjectIdentity = ObjectIdentity
a7220 = _A7220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 33)
)
_A7240_ObjectIdentity = ObjectIdentity
a7240 = _A7240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 34)
)
_S3500_24F_ObjectIdentity = ObjectIdentity
s3500_24F = _S3500_24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 35)
)
_S1500_48P_ObjectIdentity = ObjectIdentity
s1500_48P = _S1500_48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 36)
)
_S1500_24P_ObjectIdentity = ObjectIdentity
s1500_24P = _S1500_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 37)
)
_S1500_12P_ObjectIdentity = ObjectIdentity
s1500_12P = _S1500_12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 38)
)
_A7005_ObjectIdentity = ObjectIdentity
a7005 = _A7005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 39)
)
_A7010_ObjectIdentity = ObjectIdentity
a7010 = _A7010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 40)
)
_A7030_ObjectIdentity = ObjectIdentity
a7030 = _A7030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 41)
)
_A7205_ObjectIdentity = ObjectIdentity
a7205 = _A7205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 42)
)
_A7024_ObjectIdentity = ObjectIdentity
a7024 = _A7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 43)
)
_A7215_ObjectIdentity = ObjectIdentity
a7215 = _A7215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 44)
)
_Vmc_tact_ObjectIdentity = ObjectIdentity
vmc_tact = _Vmc_tact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 45)
)
_Vmc_sp10k_ObjectIdentity = ObjectIdentity
vmc_sp10k = _Vmc_sp10k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 46)
)
_A7240xm_ObjectIdentity = ObjectIdentity
a7240xm = _A7240xm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 47)
)
_A7008_ObjectIdentity = ObjectIdentity
a7008 = _A7008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 48)
)
_Vmc_tact8_ObjectIdentity = ObjectIdentity
vmc_tact8 = _Vmc_tact8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 49)
)
_Mm_va_ObjectIdentity = ObjectIdentity
mm_va = _Mm_va_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 50)
)
_A7280_ObjectIdentity = ObjectIdentity
a7280 = _A7280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 51)
)
_Mc_va_ObjectIdentity = ObjectIdentity
mc_va = _Mc_va_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 52)
)
_Mm_hw_1K_ObjectIdentity = ObjectIdentity
mm_hw_1K = _Mm_hw_1K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 53)
)
_Mm_hw_5K_ObjectIdentity = ObjectIdentity
mm_hw_5K = _Mm_hw_5K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 54)
)
_Mm_hw_10K_ObjectIdentity = ObjectIdentity
mm_hw_10K = _Mm_hw_10K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 55)
)
_A9004_ObjectIdentity = ObjectIdentity
a9004 = _A9004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 56)
)
_A9012_ObjectIdentity = ObjectIdentity
a9012 = _A9012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 57)
)
_A9004_lte_ObjectIdentity = ObjectIdentity
a9004_lte = _A9004_lte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 58)
)
_AUndefined_ObjectIdentity = ObjectIdentity
aUndefined = _AUndefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 1, 9999)
)
_ApProducts_ObjectIdentity = ObjectIdentity
apProducts = _ApProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2)
)
_A50_ObjectIdentity = ObjectIdentity
a50 = _A50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 1)
)
_A52_ObjectIdentity = ObjectIdentity
a52 = _A52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 2)
)
_Ap60_ObjectIdentity = ObjectIdentity
ap60 = _Ap60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 3)
)
_Ap61_ObjectIdentity = ObjectIdentity
ap61 = _Ap61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 4)
)
_Ap70_ObjectIdentity = ObjectIdentity
ap70 = _Ap70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 5)
)
_WalljackAp61_ObjectIdentity = ObjectIdentity
walljackAp61 = _WalljackAp61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 6)
)
_A2E_ObjectIdentity = ObjectIdentity
a2E = _A2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 7)
)
_Ap1200_ObjectIdentity = ObjectIdentity
ap1200 = _Ap1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 8)
)
_Ap80s_ObjectIdentity = ObjectIdentity
ap80s = _Ap80s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 9)
)
_Ap80m_ObjectIdentity = ObjectIdentity
ap80m = _Ap80m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 10)
)
_Wg102_ObjectIdentity = ObjectIdentity
wg102 = _Wg102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 11)
)
_Ap40_ObjectIdentity = ObjectIdentity
ap40 = _Ap40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 12)
)
_Ap41_ObjectIdentity = ObjectIdentity
ap41 = _Ap41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 13)
)
_Ap65_ObjectIdentity = ObjectIdentity
ap65 = _Ap65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 14)
)
_ApMw1700_ObjectIdentity = ObjectIdentity
apMw1700 = _ApMw1700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 15)
)
_ApDuowj_ObjectIdentity = ObjectIdentity
apDuowj = _ApDuowj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 16)
)
_ApDuo_ObjectIdentity = ObjectIdentity
apDuo = _ApDuo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 17)
)
_Ap80MB_ObjectIdentity = ObjectIdentity
ap80MB = _Ap80MB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 18)
)
_Ap80SB_ObjectIdentity = ObjectIdentity
ap80SB = _Ap80SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 19)
)
_Ap85_ObjectIdentity = ObjectIdentity
ap85 = _Ap85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 20)
)
_Ap124_ObjectIdentity = ObjectIdentity
ap124 = _Ap124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 21)
)
_Ap125_ObjectIdentity = ObjectIdentity
ap125 = _Ap125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 22)
)
_Ap120_ObjectIdentity = ObjectIdentity
ap120 = _Ap120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 23)
)
_Ap121_ObjectIdentity = ObjectIdentity
ap121 = _Ap121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 24)
)
_Ap1250_ObjectIdentity = ObjectIdentity
ap1250 = _Ap1250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 25)
)
_Ap120abg_ObjectIdentity = ObjectIdentity
ap120abg = _Ap120abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 26)
)
_Ap121abg_ObjectIdentity = ObjectIdentity
ap121abg = _Ap121abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 27)
)
_Ap124abg_ObjectIdentity = ObjectIdentity
ap124abg = _Ap124abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 28)
)
_Ap125abg_ObjectIdentity = ObjectIdentity
ap125abg = _Ap125abg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 29)
)
_Rap5wn_ObjectIdentity = ObjectIdentity
rap5wn = _Rap5wn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 30)
)
_Rap5_ObjectIdentity = ObjectIdentity
rap5 = _Rap5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 31)
)
_Rap2wg_ObjectIdentity = ObjectIdentity
rap2wg = _Rap2wg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 32)
)
_Reserved4_ObjectIdentity = ObjectIdentity
reserved4 = _Reserved4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 33)
)
_Ap105_ObjectIdentity = ObjectIdentity
ap105 = _Ap105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 34)
)
_Ap65wb_ObjectIdentity = ObjectIdentity
ap65wb = _Ap65wb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 35)
)
_Ap651_ObjectIdentity = ObjectIdentity
ap651 = _Ap651_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 36)
)
_Reserved6_ObjectIdentity = ObjectIdentity
reserved6 = _Reserved6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 37)
)
_Ap60p_ObjectIdentity = ObjectIdentity
ap60p = _Ap60p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 38)
)
_Reserved7_ObjectIdentity = ObjectIdentity
reserved7 = _Reserved7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 39)
)
_Ap92_ObjectIdentity = ObjectIdentity
ap92 = _Ap92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 40)
)
_Ap93_ObjectIdentity = ObjectIdentity
ap93 = _Ap93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 41)
)
_Ap68_ObjectIdentity = ObjectIdentity
ap68 = _Ap68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 42)
)
_Ap68p_ObjectIdentity = ObjectIdentity
ap68p = _Ap68p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 43)
)
_Ap175p_ObjectIdentity = ObjectIdentity
ap175p = _Ap175p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 44)
)
_Ap175ac_ObjectIdentity = ObjectIdentity
ap175ac = _Ap175ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 45)
)
_Ap175dc_ObjectIdentity = ObjectIdentity
ap175dc = _Ap175dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 46)
)
_Ap134_ObjectIdentity = ObjectIdentity
ap134 = _Ap134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 47)
)
_Ap135_ObjectIdentity = ObjectIdentity
ap135 = _Ap135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 48)
)
_Reserved8_ObjectIdentity = ObjectIdentity
reserved8 = _Reserved8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 49)
)
_Ap93h_ObjectIdentity = ObjectIdentity
ap93h = _Ap93h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 50)
)
_Rap3wn_ObjectIdentity = ObjectIdentity
rap3wn = _Rap3wn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 51)
)
_Rap3wnp_ObjectIdentity = ObjectIdentity
rap3wnp = _Rap3wnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 52)
)
_Ap104_ObjectIdentity = ObjectIdentity
ap104 = _Ap104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 53)
)
_Rap155_ObjectIdentity = ObjectIdentity
rap155 = _Rap155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 54)
)
_Rap155p_ObjectIdentity = ObjectIdentity
rap155p = _Rap155p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 55)
)
_Rap108_ObjectIdentity = ObjectIdentity
rap108 = _Rap108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 56)
)
_Rap109_ObjectIdentity = ObjectIdentity
rap109 = _Rap109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 57)
)
_Ap224_ObjectIdentity = ObjectIdentity
ap224 = _Ap224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 58)
)
_Ap225_ObjectIdentity = ObjectIdentity
ap225 = _Ap225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 59)
)
_Ap114_ObjectIdentity = ObjectIdentity
ap114 = _Ap114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 60)
)
_Ap115_ObjectIdentity = ObjectIdentity
ap115 = _Ap115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 61)
)
_Rap109L_ObjectIdentity = ObjectIdentity
rap109L = _Rap109L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 62)
)
_Ap274_ObjectIdentity = ObjectIdentity
ap274 = _Ap274_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 63)
)
_Ap275_ObjectIdentity = ObjectIdentity
ap275 = _Ap275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 64)
)
_Ap214a_ObjectIdentity = ObjectIdentity
ap214a = _Ap214a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 65)
)
_Ap215a_ObjectIdentity = ObjectIdentity
ap215a = _Ap215a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 66)
)
_Ap204_ObjectIdentity = ObjectIdentity
ap204 = _Ap204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 67)
)
_Ap205_ObjectIdentity = ObjectIdentity
ap205 = _Ap205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 68)
)
_Ap103_ObjectIdentity = ObjectIdentity
ap103 = _Ap103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 69)
)
_Ap103H_ObjectIdentity = ObjectIdentity
ap103H = _Ap103H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 70)
)
_Iapvc_ObjectIdentity = ObjectIdentity
iapvc = _Iapvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 71)
)
_Ap277_ObjectIdentity = ObjectIdentity
ap277 = _Ap277_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 72)
)
_Ap214_ObjectIdentity = ObjectIdentity
ap214 = _Ap214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 73)
)
_Ap215_ObjectIdentity = ObjectIdentity
ap215 = _Ap215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 74)
)
_Ap228_ObjectIdentity = ObjectIdentity
ap228 = _Ap228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 75)
)
_Ap205H_ObjectIdentity = ObjectIdentity
ap205H = _Ap205H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 76)
)
_Ap324_ObjectIdentity = ObjectIdentity
ap324 = _Ap324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 77)
)
_Ap325_ObjectIdentity = ObjectIdentity
ap325 = _Ap325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 78)
)
_Ap334_ObjectIdentity = ObjectIdentity
ap334 = _Ap334_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 79)
)
_Ap335_ObjectIdentity = ObjectIdentity
ap335 = _Ap335_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 80)
)
_Ap314_ObjectIdentity = ObjectIdentity
ap314 = _Ap314_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 81)
)
_Ap315_ObjectIdentity = ObjectIdentity
ap315 = _Ap315_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 82)
)
_Apm210_ObjectIdentity = ObjectIdentity
apm210 = _Apm210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 83)
)
_Ap207_ObjectIdentity = ObjectIdentity
ap207 = _Ap207_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 84)
)
_Ap304_ObjectIdentity = ObjectIdentity
ap304 = _Ap304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 85)
)
_Ap305_ObjectIdentity = ObjectIdentity
ap305 = _Ap305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 86)
)
_Ap303h_ObjectIdentity = ObjectIdentity
ap303h = _Ap303h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 87)
)
_Ap365_ObjectIdentity = ObjectIdentity
ap365 = _Ap365_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 88)
)
_Ap367_ObjectIdentity = ObjectIdentity
ap367 = _Ap367_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 89)
)
_Ap203H_ObjectIdentity = ObjectIdentity
ap203H = _Ap203H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 90)
)
_Ap203R_ObjectIdentity = ObjectIdentity
ap203R = _Ap203R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 91)
)
_Ap203RP_ObjectIdentity = ObjectIdentity
ap203RP = _Ap203RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 92)
)
_Ap344_ObjectIdentity = ObjectIdentity
ap344 = _Ap344_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 93)
)
_Ap345_ObjectIdentity = ObjectIdentity
ap345 = _Ap345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 94)
)
_Ap374_ObjectIdentity = ObjectIdentity
ap374 = _Ap374_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 95)
)
_Ap375_ObjectIdentity = ObjectIdentity
ap375 = _Ap375_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 96)
)
_Ap377_ObjectIdentity = ObjectIdentity
ap377 = _Ap377_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 97)
)
_Ap318_ObjectIdentity = ObjectIdentity
ap318 = _Ap318_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 98)
)
_Ap303_ObjectIdentity = ObjectIdentity
ap303 = _Ap303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 99)
)
_Ap555_ObjectIdentity = ObjectIdentity
ap555 = _Ap555_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 100)
)
_Ap534_ObjectIdentity = ObjectIdentity
ap534 = _Ap534_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 101)
)
_Ap535_ObjectIdentity = ObjectIdentity
ap535 = _Ap535_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 102)
)
_Ap387_ObjectIdentity = ObjectIdentity
ap387 = _Ap387_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 104)
)
_Ap303P_ObjectIdentity = ObjectIdentity
ap303P = _Ap303P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 105)
)
_Ap514_ObjectIdentity = ObjectIdentity
ap514 = _Ap514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 106)
)
_Ap515_ObjectIdentity = ObjectIdentity
ap515 = _Ap515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 107)
)
_Ap544_ObjectIdentity = ObjectIdentity
ap544 = _Ap544_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 108)
)
_Ap545_ObjectIdentity = ObjectIdentity
ap545 = _Ap545_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 109)
)
_Ap504_ObjectIdentity = ObjectIdentity
ap504 = _Ap504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 110)
)
_Ap505_ObjectIdentity = ObjectIdentity
ap505 = _Ap505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 111)
)
_Ap505H_ObjectIdentity = ObjectIdentity
ap505H = _Ap505H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 112)
)
_Ap574_ObjectIdentity = ObjectIdentity
ap574 = _Ap574_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 113)
)
_Ap575_ObjectIdentity = ObjectIdentity
ap575 = _Ap575_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 114)
)
_Ap577_ObjectIdentity = ObjectIdentity
ap577 = _Ap577_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 115)
)
_Ap518_ObjectIdentity = ObjectIdentity
ap518 = _Ap518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 116)
)
_Ap503H_ObjectIdentity = ObjectIdentity
ap503H = _Ap503H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 117)
)
_Ap565_ObjectIdentity = ObjectIdentity
ap565 = _Ap565_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 118)
)
_Ap567_ObjectIdentity = ObjectIdentity
ap567 = _Ap567_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 119)
)
_Ap575EX_ObjectIdentity = ObjectIdentity
ap575EX = _Ap575EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 120)
)
_Ap577EX_ObjectIdentity = ObjectIdentity
ap577EX = _Ap577EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 121)
)
_Ap565EX_ObjectIdentity = ObjectIdentity
ap565EX = _Ap565EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 122)
)
_Ap567EX_ObjectIdentity = ObjectIdentity
ap567EX = _Ap567EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 123)
)
_Ap375ATEX_ObjectIdentity = ObjectIdentity
ap375ATEX = _Ap375ATEX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 124)
)
_ApUndefined_ObjectIdentity = ObjectIdentity
apUndefined = _ApUndefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 2, 9999)
)
_EmsProducts_ObjectIdentity = ObjectIdentity
emsProducts = _EmsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 3)
)
_PartnerProducts_ObjectIdentity = ObjectIdentity
partnerProducts = _PartnerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4)
)
_EcsE50_ObjectIdentity = ObjectIdentity
ecsE50 = _EcsE50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 1)
)
_EcsE100C_ObjectIdentity = ObjectIdentity
ecsE100C = _EcsE100C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 2)
)
_EcsE100A_ObjectIdentity = ObjectIdentity
ecsE100A = _EcsE100A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 3)
)
_EcsENSM_ObjectIdentity = ObjectIdentity
ecsENSM = _EcsENSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 4, 4)
)
_AmigopodProducts_ObjectIdentity = ObjectIdentity
amigopodProducts = _AmigopodProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 5)
)
_ClearpassProducts_ObjectIdentity = ObjectIdentity
clearpassProducts = _ClearpassProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6)
)
_Clearpass_ObjectIdentity = ObjectIdentity
clearpass = _Clearpass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1)
)
_ArubaEnterpriseMibModules_ObjectIdentity = ObjectIdentity
arubaEnterpriseMibModules = _ArubaEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1)
)
_ArubaMIBModules_ObjectIdentity = ObjectIdentity
arubaMIBModules = _ArubaMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2)
)
_WlsxEnterpriseMibModules_ObjectIdentity = ObjectIdentity
wlsxEnterpriseMibModules = _WlsxEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1)
)
_ArubaAp_ObjectIdentity = ObjectIdentity
arubaAp = _ArubaAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3)
)
_WlsrEnterpriseMibModules_ObjectIdentity = ObjectIdentity
wlsrEnterpriseMibModules = _WlsrEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1)
)
_WlsrOutDoorApMibModules_ObjectIdentity = ObjectIdentity
wlsrOutDoorApMibModules = _WlsrOutDoorApMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2)
)
_AiEnterpriseMibModules_ObjectIdentity = ObjectIdentity
aiEnterpriseMibModules = _AiEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3)
)
_ArubaEcs_ObjectIdentity = ObjectIdentity
arubaEcs = _ArubaEcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 4)
)
_ArubaMgmt_ObjectIdentity = ObjectIdentity
arubaMgmt = _ArubaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 3)
)
_ArubaPki_ObjectIdentity = ObjectIdentity
arubaPki = _ArubaPki_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 4)
)
if mibBuilder.loadTexts:
    arubaPki.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBA-MIB",
    **{"aruba": aruba,
       "products": products,
       "switchProducts": switchProducts,
       "a5000": a5000,
       "a2400": a2400,
       "a800": a800,
       "a6000": a6000,
       "a2400E": a2400E,
       "a800E": a800E,
       "a804": a804,
       "a200": a200,
       "a2424": a2424,
       "a6000-SC3": a6000_SC3,
       "a3200": a3200,
       "a3200-8": a3200_8,
       "a3400": a3400,
       "a3400-32": a3400_32,
       "a3600": a3600,
       "a3600-64": a3600_64,
       "a650": a650,
       "a651": a651,
       "reserved1": reserved1,
       "reserved2": reserved2,
       "a620": a620,
       "s3500-24P": s3500_24P,
       "s3500-24T": s3500_24T,
       "s3500-48P": s3500_48P,
       "s3500-48T": s3500_48T,
       "s2500-24P": s2500_24P,
       "s2500-24T": s2500_24T,
       "s2500-48P": s2500_48P,
       "s2500-48T": s2500_48T,
       "a7210": a7210,
       "a7220": a7220,
       "a7240": a7240,
       "s3500-24F": s3500_24F,
       "s1500-48P": s1500_48P,
       "s1500-24P": s1500_24P,
       "s1500-12P": s1500_12P,
       "a7005": a7005,
       "a7010": a7010,
       "a7030": a7030,
       "a7205": a7205,
       "a7024": a7024,
       "a7215": a7215,
       "vmc-tact": vmc_tact,
       "vmc-sp10k": vmc_sp10k,
       "a7240xm": a7240xm,
       "a7008": a7008,
       "vmc-tact8": vmc_tact8,
       "mm-va": mm_va,
       "a7280": a7280,
       "mc-va": mc_va,
       "mm-hw-1K": mm_hw_1K,
       "mm-hw-5K": mm_hw_5K,
       "mm-hw-10K": mm_hw_10K,
       "a9004": a9004,
       "a9012": a9012,
       "a9004-lte": a9004_lte,
       "aUndefined": aUndefined,
       "apProducts": apProducts,
       "a50": a50,
       "a52": a52,
       "ap60": ap60,
       "ap61": ap61,
       "ap70": ap70,
       "walljackAp61": walljackAp61,
       "a2E": a2E,
       "ap1200": ap1200,
       "ap80s": ap80s,
       "ap80m": ap80m,
       "wg102": wg102,
       "ap40": ap40,
       "ap41": ap41,
       "ap65": ap65,
       "apMw1700": apMw1700,
       "apDuowj": apDuowj,
       "apDuo": apDuo,
       "ap80MB": ap80MB,
       "ap80SB": ap80SB,
       "ap85": ap85,
       "ap124": ap124,
       "ap125": ap125,
       "ap120": ap120,
       "ap121": ap121,
       "ap1250": ap1250,
       "ap120abg": ap120abg,
       "ap121abg": ap121abg,
       "ap124abg": ap124abg,
       "ap125abg": ap125abg,
       "rap5wn": rap5wn,
       "rap5": rap5,
       "rap2wg": rap2wg,
       "reserved4": reserved4,
       "ap105": ap105,
       "ap65wb": ap65wb,
       "ap651": ap651,
       "reserved6": reserved6,
       "ap60p": ap60p,
       "reserved7": reserved7,
       "ap92": ap92,
       "ap93": ap93,
       "ap68": ap68,
       "ap68p": ap68p,
       "ap175p": ap175p,
       "ap175ac": ap175ac,
       "ap175dc": ap175dc,
       "ap134": ap134,
       "ap135": ap135,
       "reserved8": reserved8,
       "ap93h": ap93h,
       "rap3wn": rap3wn,
       "rap3wnp": rap3wnp,
       "ap104": ap104,
       "rap155": rap155,
       "rap155p": rap155p,
       "rap108": rap108,
       "rap109": rap109,
       "ap224": ap224,
       "ap225": ap225,
       "ap114": ap114,
       "ap115": ap115,
       "rap109L": rap109L,
       "ap274": ap274,
       "ap275": ap275,
       "ap214a": ap214a,
       "ap215a": ap215a,
       "ap204": ap204,
       "ap205": ap205,
       "ap103": ap103,
       "ap103H": ap103H,
       "iapvc": iapvc,
       "ap277": ap277,
       "ap214": ap214,
       "ap215": ap215,
       "ap228": ap228,
       "ap205H": ap205H,
       "ap324": ap324,
       "ap325": ap325,
       "ap334": ap334,
       "ap335": ap335,
       "ap314": ap314,
       "ap315": ap315,
       "apm210": apm210,
       "ap207": ap207,
       "ap304": ap304,
       "ap305": ap305,
       "ap303h": ap303h,
       "ap365": ap365,
       "ap367": ap367,
       "ap203H": ap203H,
       "ap203R": ap203R,
       "ap203RP": ap203RP,
       "ap344": ap344,
       "ap345": ap345,
       "ap374": ap374,
       "ap375": ap375,
       "ap377": ap377,
       "ap318": ap318,
       "ap303": ap303,
       "ap555": ap555,
       "ap534": ap534,
       "ap535": ap535,
       "ap387": ap387,
       "ap303P": ap303P,
       "ap514": ap514,
       "ap515": ap515,
       "ap544": ap544,
       "ap545": ap545,
       "ap504": ap504,
       "ap505": ap505,
       "ap505H": ap505H,
       "ap574": ap574,
       "ap575": ap575,
       "ap577": ap577,
       "ap518": ap518,
       "ap503H": ap503H,
       "ap565": ap565,
       "ap567": ap567,
       "ap575EX": ap575EX,
       "ap577EX": ap577EX,
       "ap565EX": ap565EX,
       "ap567EX": ap567EX,
       "ap375ATEX": ap375ATEX,
       "apUndefined": apUndefined,
       "emsProducts": emsProducts,
       "partnerProducts": partnerProducts,
       "ecsE50": ecsE50,
       "ecsE100C": ecsE100C,
       "ecsE100A": ecsE100A,
       "ecsENSM": ecsENSM,
       "amigopodProducts": amigopodProducts,
       "clearpassProducts": clearpassProducts,
       "clearpass": clearpass,
       "arubaEnterpriseMibModules": arubaEnterpriseMibModules,
       "common": common,
       "arubaMIBModules": arubaMIBModules,
       "switch": switch,
       "wlsxEnterpriseMibModules": wlsxEnterpriseMibModules,
       "arubaAp": arubaAp,
       "wlsrEnterpriseMibModules": wlsrEnterpriseMibModules,
       "wlsrOutDoorApMibModules": wlsrOutDoorApMibModules,
       "aiEnterpriseMibModules": aiEnterpriseMibModules,
       "arubaEcs": arubaEcs,
       "arubaMgmt": arubaMgmt,
       "arubaPki": arubaPki}
)
