# SNMP MIB module (DELL-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELL-REF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:53 2025
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

(dellLan,
 dellLanExtension) = mibBuilder.importSymbols(
    "Dell-Vendor-MIB",
    "dellLan",
    "dellLanExtension")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lvl7 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132)
)
if mibBuilder.loadTexts:
    lvl7.setRevisions(
        ("2018-12-27 00:00",
         "2013-04-12 00:00",
         "2013-03-27 00:00",
         "2011-04-14 00:00",
         "2003-11-21 00:00",
         "2003-02-06 12:00",
         "2013-07-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentPortMask(TextualConvention, OctetString):
    status = "current"
    displayHint = "255x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Dell6224Switch_ObjectIdentity = ObjectIdentity
dell6224Switch = _Dell6224Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3010)
)
_Dell6248Switch_ObjectIdentity = ObjectIdentity
dell6248Switch = _Dell6248Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3011)
)
_Dell6224PSwitch_ObjectIdentity = ObjectIdentity
dell6224PSwitch = _Dell6224PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3012)
)
_Dell6248PSwitch_ObjectIdentity = ObjectIdentity
dell6248PSwitch = _Dell6248PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3013)
)
_Dell6224FSwitch_ObjectIdentity = ObjectIdentity
dell6224FSwitch = _Dell6224FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3014)
)
_DellM6220Switch_ObjectIdentity = ObjectIdentity
dellM6220Switch = _DellM6220Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3015)
)
_DellM8024Switch_ObjectIdentity = ObjectIdentity
dellM8024Switch = _DellM8024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3022)
)
_Dell8024Switch_ObjectIdentity = ObjectIdentity
dell8024Switch = _Dell8024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3023)
)
_Dell8024FSwitch_ObjectIdentity = ObjectIdentity
dell8024FSwitch = _Dell8024FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3024)
)
_DellM6384Switch_ObjectIdentity = ObjectIdentity
dellM6384Switch = _DellM6384Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3025)
)
_Dell7024Switch_ObjectIdentity = ObjectIdentity
dell7024Switch = _Dell7024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3034)
)
_Dell7048Switch_ObjectIdentity = ObjectIdentity
dell7048Switch = _Dell7048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3035)
)
_Dell7024PSwitch_ObjectIdentity = ObjectIdentity
dell7024PSwitch = _Dell7024PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3036)
)
_Dell7048PSwitch_ObjectIdentity = ObjectIdentity
dell7048PSwitch = _Dell7048PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3037)
)
_Dell7024FSwitch_ObjectIdentity = ObjectIdentity
dell7024FSwitch = _Dell7024FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3038)
)
_Dell7048RSwitch_ObjectIdentity = ObjectIdentity
dell7048RSwitch = _Dell7048RSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3039)
)
_Dell7048RRASwitch_ObjectIdentity = ObjectIdentity
dell7048RRASwitch = _Dell7048RRASwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3040)
)
_DellM8024KSwitch_ObjectIdentity = ObjectIdentity
dellM8024KSwitch = _DellM8024KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3041)
)
_DellN4032Switch_ObjectIdentity = ObjectIdentity
dellN4032Switch = _DellN4032Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3042)
)
_DellN4032FSwitch_ObjectIdentity = ObjectIdentity
dellN4032FSwitch = _DellN4032FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3044)
)
_DellN4064Switch_ObjectIdentity = ObjectIdentity
dellN4064Switch = _DellN4064Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3045)
)
_DellN4064FSwitch_ObjectIdentity = ObjectIdentity
dellN4064FSwitch = _DellN4064FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3046)
)
_DellN2024Switch_ObjectIdentity = ObjectIdentity
dellN2024Switch = _DellN2024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3053)
)
_DellN2048Switch_ObjectIdentity = ObjectIdentity
dellN2048Switch = _DellN2048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3054)
)
_DellN2024PSwitch_ObjectIdentity = ObjectIdentity
dellN2024PSwitch = _DellN2024PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3055)
)
_DellN2048PSwitch_ObjectIdentity = ObjectIdentity
dellN2048PSwitch = _DellN2048PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3056)
)
_DellN3024Switch_ObjectIdentity = ObjectIdentity
dellN3024Switch = _DellN3024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3057)
)
_DellN3048Switch_ObjectIdentity = ObjectIdentity
dellN3048Switch = _DellN3048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3058)
)
_DellN3024PSwitch_ObjectIdentity = ObjectIdentity
dellN3024PSwitch = _DellN3024PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3059)
)
_DellN3048PSwitch_ObjectIdentity = ObjectIdentity
dellN3048PSwitch = _DellN3048PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3060)
)
_DellN3024FSwitch_ObjectIdentity = ObjectIdentity
dellN3024FSwitch = _DellN3024FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3061)
)
_DellN1524Switch_ObjectIdentity = ObjectIdentity
dellN1524Switch = _DellN1524Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3063)
)
_DellN1524PSwitch_ObjectIdentity = ObjectIdentity
dellN1524PSwitch = _DellN1524PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3064)
)
_DellN1548Switch_ObjectIdentity = ObjectIdentity
dellN1548Switch = _DellN1548Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3065)
)
_DellN1548PSwitch_ObjectIdentity = ObjectIdentity
dellN1548PSwitch = _DellN1548PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3066)
)
_DellN3132PXSwitch_ObjectIdentity = ObjectIdentity
dellN3132PXSwitch = _DellN3132PXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3076)
)
_DellN2128PXSwitch_ObjectIdentity = ObjectIdentity
dellN2128PXSwitch = _DellN2128PXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3077)
)
_DellN1108T_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1108T_ONSwitch = _DellN1108T_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3078)
)
_DellN1108P_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1108P_ONSwitch = _DellN1108P_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3079)
)
_DellN1124T_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1124T_ONSwitch = _DellN1124T_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3080)
)
_DellN1124P_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1124P_ONSwitch = _DellN1124P_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3081)
)
_DellN1148T_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1148T_ONSwitch = _DellN1148T_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3082)
)
_DellN1148P_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1148P_ONSwitch = _DellN1148P_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3083)
)
_DellN3048EP_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3048EP_ONSwitch = _DellN3048EP_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3084)
)
_DellN3048ET_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3048ET_ONSwitch = _DellN3048ET_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3085)
)
_DellN3024EP_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3024EP_ONSwitch = _DellN3024EP_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3086)
)
_DellN3024EF_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3024EF_ONSwitch = _DellN3024EF_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3087)
)
_DellN3024ET_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3024ET_ONSwitch = _DellN3024ET_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3088)
)
_DellN1608X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1608X_ONSwitch = _DellN1608X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3089)
)
_DellN1608PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1608PX_ONSwitch = _DellN1608PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3090)
)
_DellN1616X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1616X_ONSwitch = _DellN1616X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3091)
)
_DellN1616PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1616PX_ONSwitch = _DellN1616PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3092)
)
_DellN1624X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1624X_ONSwitch = _DellN1624X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3093)
)
_DellN1624PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1624PX_ONSwitch = _DellN1624PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3094)
)
_DellN1648X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1648X_ONSwitch = _DellN1648X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3095)
)
_DellN1648PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1648PX_ONSwitch = _DellN1648PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3096)
)
_DellN2224X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN2224X_ONSwitch = _DellN2224X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3097)
)
_DellN2224PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellN2224PX_ONSwitch = _DellN2224PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3098)
)
_DellN2248X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN2248X_ONSwitch = _DellN2248X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3099)
)
_DellN2248PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellN2248PX_ONSwitch = _DellN2248PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3100)
)
_DellNN3208PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellNN3208PX_ONSwitch = _DellNN3208PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3104)
)
_DellN3224X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3224X_ONSwitch = _DellN3224X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3105)
)
_DellN3224PX_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3224PX_ONSwitch = _DellN3224PX_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3106)
)
_DellN3248X_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3248X_ONSwitch = _DellN3248X_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3107)
)
_DellN3248PXE_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3248PXE_ONSwitch = _DellN3248PXE_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3109)
)
_DellN3224T_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3224T_ONSwitch = _DellN3224T_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3110)
)
_DellN3224F_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3224F_ONSwitch = _DellN3224F_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3111)
)
_DellN3224P_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3224P_ONSwitch = _DellN3224P_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3112)
)
_DellN3248TE_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3248TE_ONSwitch = _DellN3248TE_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3113)
)
_DellN3248P_ONSwitch_ObjectIdentity = ObjectIdentity
dellN3248P_ONSwitch = _DellN3248P_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3114)
)
_DellN1108EP_ONSwitch_ObjectIdentity = ObjectIdentity
dellN1108EP_ONSwitch = _DellN1108EP_ONSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3115)
)
_Lvl7Products_ObjectIdentity = ObjectIdentity
lvl7Products = _Lvl7Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1)
)
_DnOS_ObjectIdentity = ObjectIdentity
dnOS = _DnOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-REF-MIB",
    **{"AgentPortMask": AgentPortMask,
       "dell6224Switch": dell6224Switch,
       "dell6248Switch": dell6248Switch,
       "dell6224PSwitch": dell6224PSwitch,
       "dell6248PSwitch": dell6248PSwitch,
       "dell6224FSwitch": dell6224FSwitch,
       "dellM6220Switch": dellM6220Switch,
       "dellM8024Switch": dellM8024Switch,
       "dell8024Switch": dell8024Switch,
       "dell8024FSwitch": dell8024FSwitch,
       "dellM6384Switch": dellM6384Switch,
       "dell7024Switch": dell7024Switch,
       "dell7048Switch": dell7048Switch,
       "dell7024PSwitch": dell7024PSwitch,
       "dell7048PSwitch": dell7048PSwitch,
       "dell7024FSwitch": dell7024FSwitch,
       "dell7048RSwitch": dell7048RSwitch,
       "dell7048RRASwitch": dell7048RRASwitch,
       "dellM8024KSwitch": dellM8024KSwitch,
       "dellN4032Switch": dellN4032Switch,
       "dellN4032FSwitch": dellN4032FSwitch,
       "dellN4064Switch": dellN4064Switch,
       "dellN4064FSwitch": dellN4064FSwitch,
       "dellN2024Switch": dellN2024Switch,
       "dellN2048Switch": dellN2048Switch,
       "dellN2024PSwitch": dellN2024PSwitch,
       "dellN2048PSwitch": dellN2048PSwitch,
       "dellN3024Switch": dellN3024Switch,
       "dellN3048Switch": dellN3048Switch,
       "dellN3024PSwitch": dellN3024PSwitch,
       "dellN3048PSwitch": dellN3048PSwitch,
       "dellN3024FSwitch": dellN3024FSwitch,
       "dellN1524Switch": dellN1524Switch,
       "dellN1524PSwitch": dellN1524PSwitch,
       "dellN1548Switch": dellN1548Switch,
       "dellN1548PSwitch": dellN1548PSwitch,
       "dellN3132PXSwitch": dellN3132PXSwitch,
       "dellN2128PXSwitch": dellN2128PXSwitch,
       "dellN1108T-ONSwitch": dellN1108T_ONSwitch,
       "dellN1108P-ONSwitch": dellN1108P_ONSwitch,
       "dellN1124T-ONSwitch": dellN1124T_ONSwitch,
       "dellN1124P-ONSwitch": dellN1124P_ONSwitch,
       "dellN1148T-ONSwitch": dellN1148T_ONSwitch,
       "dellN1148P-ONSwitch": dellN1148P_ONSwitch,
       "dellN3048EP-ONSwitch": dellN3048EP_ONSwitch,
       "dellN3048ET-ONSwitch": dellN3048ET_ONSwitch,
       "dellN3024EP-ONSwitch": dellN3024EP_ONSwitch,
       "dellN3024EF-ONSwitch": dellN3024EF_ONSwitch,
       "dellN3024ET-ONSwitch": dellN3024ET_ONSwitch,
       "dellN1608X-ONSwitch": dellN1608X_ONSwitch,
       "dellN1608PX-ONSwitch": dellN1608PX_ONSwitch,
       "dellN1616X-ONSwitch": dellN1616X_ONSwitch,
       "dellN1616PX-ONSwitch": dellN1616PX_ONSwitch,
       "dellN1624X-ONSwitch": dellN1624X_ONSwitch,
       "dellN1624PX-ONSwitch": dellN1624PX_ONSwitch,
       "dellN1648X-ONSwitch": dellN1648X_ONSwitch,
       "dellN1648PX-ONSwitch": dellN1648PX_ONSwitch,
       "dellN2224X-ONSwitch": dellN2224X_ONSwitch,
       "dellN2224PX-ONSwitch": dellN2224PX_ONSwitch,
       "dellN2248X-ONSwitch": dellN2248X_ONSwitch,
       "dellN2248PX-ONSwitch": dellN2248PX_ONSwitch,
       "dellNN3208PX-ONSwitch": dellNN3208PX_ONSwitch,
       "dellN3224X-ONSwitch": dellN3224X_ONSwitch,
       "dellN3224PX-ONSwitch": dellN3224PX_ONSwitch,
       "dellN3248X-ONSwitch": dellN3248X_ONSwitch,
       "dellN3248PXE-ONSwitch": dellN3248PXE_ONSwitch,
       "dellN3224T-ONSwitch": dellN3224T_ONSwitch,
       "dellN3224F-ONSwitch": dellN3224F_ONSwitch,
       "dellN3224P-ONSwitch": dellN3224P_ONSwitch,
       "dellN3248TE-ONSwitch": dellN3248TE_ONSwitch,
       "dellN3248P-ONSwitch": dellN3248P_ONSwitch,
       "dellN1108EP-ONSwitch": dellN1108EP_ONSwitch,
       "lvl7": lvl7,
       "lvl7Products": lvl7Products,
       "dnOS": dnOS}
)
