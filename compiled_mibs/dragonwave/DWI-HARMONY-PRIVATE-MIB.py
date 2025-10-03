# SNMP MIB module (DWI-HARMONY-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\DWI-HARMONY-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:29 2025
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

dragonwave = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7262)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Harmony_ObjectIdentity = ObjectIdentity
harmony = _Harmony_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4)
)
_Lite_ObjectIdentity = ObjectIdentity
lite = _Lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 1)
)
_HarmonyMultiRadio_ObjectIdentity = ObjectIdentity
harmonyMultiRadio = _HarmonyMultiRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 2)
)
_HarmonyFPH800_ObjectIdentity = ObjectIdentity
harmonyFPH800 = _HarmonyFPH800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 3)
)
_HarmonyFM_ObjectIdentity = ObjectIdentity
harmonyFM = _HarmonyFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 4)
)
_Mwr_ObjectIdentity = ObjectIdentity
mwr = _Mwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5)
)
_EquipmentCommon_ObjectIdentity = ObjectIdentity
equipmentCommon = _EquipmentCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 20)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 50)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DWI-HARMONY-PRIVATE-MIB",
    **{"dragonwave": dragonwave,
       "harmony": harmony,
       "lite": lite,
       "harmonyMultiRadio": harmonyMultiRadio,
       "harmonyFPH800": harmonyFPH800,
       "harmonyFM": harmonyFM,
       "mwr": mwr,
       "equipmentCommon": equipmentCommon,
       "switch": switch}
)
