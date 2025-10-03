# SNMP MIB module (EXTREME-VC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-VC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:54 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

extremeVC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeVCLinkTable_Object = MibTable
extremeVCLinkTable = _ExtremeVCLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1)
)
if mibBuilder.loadTexts:
    extremeVCLinkTable.setStatus("deprecated")
_ExtremeVCLinkEntry_Object = MibTableRow
extremeVCLinkEntry = _ExtremeVCLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1)
)
extremeVCLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeVCLinkEntry.setStatus("deprecated")
_ExtremeVCLinkValid_Type = TruthValue
_ExtremeVCLinkValid_Object = MibTableColumn
extremeVCLinkValid = _ExtremeVCLinkValid_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 1),
    _ExtremeVCLinkValid_Type()
)
extremeVCLinkValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkValid.setStatus("deprecated")
_ExtremeVCLinkDeviceId_Type = Integer32
_ExtremeVCLinkDeviceId_Object = MibTableColumn
extremeVCLinkDeviceId = _ExtremeVCLinkDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 2),
    _ExtremeVCLinkDeviceId_Type()
)
extremeVCLinkDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkDeviceId.setStatus("deprecated")
_ExtremeVCLinkPortIndex_Type = Integer32
_ExtremeVCLinkPortIndex_Object = MibTableColumn
extremeVCLinkPortIndex = _ExtremeVCLinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 3),
    _ExtremeVCLinkPortIndex_Type()
)
extremeVCLinkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkPortIndex.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-VC-MIB",
    **{"extremeVC": extremeVC,
       "extremeVCLinkTable": extremeVCLinkTable,
       "extremeVCLinkEntry": extremeVCLinkEntry,
       "extremeVCLinkValid": extremeVCLinkValid,
       "extremeVCLinkDeviceId": extremeVCLinkDeviceId,
       "extremeVCLinkPortIndex": extremeVCLinkPortIndex}
)
