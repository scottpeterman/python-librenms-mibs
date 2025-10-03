# SNMP MIB module (UBQS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:29 2025
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

(ubqsProducts,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubqsProducts")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_E7508_ObjectIdentity = ObjectIdentity
e7508 = _E7508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 65)
)
_U9264H_EPON_ObjectIdentity = ObjectIdentity
u9264H_EPON = _U9264H_EPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 69)
)
_Cs3400_ObjectIdentity = ObjectIdentity
cs3400 = _Cs3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 73)
)
_U9264H_GPON_ObjectIdentity = ObjectIdentity
u9264H_GPON = _U9264H_GPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 92)
)
_U9016B_EPON_ObjectIdentity = ObjectIdentity
u9016B_EPON = _U9016B_EPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 93)
)
_U9016B_GPON_ObjectIdentity = ObjectIdentity
u9016B_GPON = _U9016B_GPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 94)
)
_E5224C_ObjectIdentity = ObjectIdentity
e5224C = _E5224C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 95)
)
_E5224D_ObjectIdentity = ObjectIdentity
e5224D = _E5224D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 100)
)
_E3224C_ObjectIdentity = ObjectIdentity
e3224C = _E3224C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 101)
)
_E3224D_ObjectIdentity = ObjectIdentity
e3224D = _E3224D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 102)
)
_E6100_ObjectIdentity = ObjectIdentity
e6100 = _E6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 103)
)
_E5002G_ObjectIdentity = ObjectIdentity
e5002G = _E5002G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 105)
)
_E7505_ObjectIdentity = ObjectIdentity
e7505 = _E7505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 108)
)
_U9764H_GPON_ObjectIdentity = ObjectIdentity
u9764H_GPON = _U9764H_GPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 112)
)
_E5224CP_ObjectIdentity = ObjectIdentity
e5224CP = _E5224CP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 115)
)
_U9500h_ObjectIdentity = ObjectIdentity
u9500h = _U9500h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 117)
)
_Ce7010_ObjectIdentity = ObjectIdentity
ce7010 = _Ce7010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 118)
)
_UCrown6020_ObjectIdentity = ObjectIdentity
uCrown6020 = _UCrown6020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 128)
)
_U9008B_ObjectIdentity = ObjectIdentity
U9008B = _U9008B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 129)
)
_UHon1010_ObjectIdentity = ObjectIdentity
uHon1010 = _UHon1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 130)
)
_E6300_ObjectIdentity = ObjectIdentity
e6300 = _E6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 133)
)
_USafe4010_ObjectIdentity = ObjectIdentity
uSafe4010 = _USafe4010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 134)
)
_IES4028GP_ObjectIdentity = ObjectIdentity
iES4028GP = _IES4028GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 135)
)
_IES4028XP_ObjectIdentity = ObjectIdentity
iES4028XP = _IES4028XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 136)
)
_UCrown5010_48T_ObjectIdentity = ObjectIdentity
uCrown5010_48T = _UCrown5010_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 140)
)
_UCrown5010_48S_ObjectIdentity = ObjectIdentity
uCrown5010_48S = _UCrown5010_48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1, 141)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-PRODUCTS-MIB",
    **{"e7508": e7508,
       "u9264H_EPON": u9264H_EPON,
       "cs3400": cs3400,
       "u9264H_GPON": u9264H_GPON,
       "u9016B_EPON": u9016B_EPON,
       "u9016B_GPON": u9016B_GPON,
       "e5224C": e5224C,
       "e5224D": e5224D,
       "e3224C": e3224C,
       "e3224D": e3224D,
       "e6100": e6100,
       "e5002G": e5002G,
       "e7505": e7505,
       "u9764H_GPON": u9764H_GPON,
       "e5224CP": e5224CP,
       "u9500h": u9500h,
       "ce7010": ce7010,
       "uCrown6020": uCrown6020,
       "U9008B": U9008B,
       "uHon1010": uHon1010,
       "e6300": e6300,
       "uSafe4010": uSafe4010,
       "iES4028GP": iES4028GP,
       "iES4028XP": iES4028XP,
       "uCrown5010_48T": uCrown5010_48T,
       "uCrown5010_48S": uCrown5010_48S}
)
