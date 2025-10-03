# SNMP MIB module (CT-FASTPATH-PROTECTED-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CT-FASTPATH-PROTECTED-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:13 2025
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

(ctFastPathProtectedPortMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFastPathProtectedPortMib")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

ctFastPathProtectedPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1)
)
if mibBuilder.loadTexts:
    ctFastPathProtectedPortMIB.setRevisions(
        ("2006-03-06 15:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtAgentSwitchConfigGroup_ObjectIdentity = ObjectIdentity
ctAgentSwitchConfigGroup = _CtAgentSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1)
)
_CtAgentSwitchProtectedPortConfigGroup_ObjectIdentity = ObjectIdentity
ctAgentSwitchProtectedPortConfigGroup = _CtAgentSwitchProtectedPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18)
)
_CtAgentSwitchProtectedPortTable_Object = MibTable
ctAgentSwitchProtectedPortTable = _CtAgentSwitchProtectedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    ctAgentSwitchProtectedPortTable.setStatus("current")
_CtAgentSwitchProtectedPortEntry_Object = MibTableRow
ctAgentSwitchProtectedPortEntry = _CtAgentSwitchProtectedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1)
)
ctAgentSwitchProtectedPortEntry.setIndexNames(
    (0, "CT-FASTPATH-PROTECTED-PORT-MIB", "ctAgentSwitchProtectedPortGroupId"),
)
if mibBuilder.loadTexts:
    ctAgentSwitchProtectedPortEntry.setStatus("current")
_CtAgentSwitchProtectedPortGroupId_Type = Integer32
_CtAgentSwitchProtectedPortGroupId_Object = MibTableColumn
ctAgentSwitchProtectedPortGroupId = _CtAgentSwitchProtectedPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 1),
    _CtAgentSwitchProtectedPortGroupId_Type()
)
ctAgentSwitchProtectedPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctAgentSwitchProtectedPortGroupId.setStatus("current")


class _CtAgentSwitchProtectedPortGroupName_Type(DisplayString):
    """Custom type ctAgentSwitchProtectedPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CtAgentSwitchProtectedPortGroupName_Type.__name__ = "DisplayString"
_CtAgentSwitchProtectedPortGroupName_Object = MibTableColumn
ctAgentSwitchProtectedPortGroupName = _CtAgentSwitchProtectedPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 2),
    _CtAgentSwitchProtectedPortGroupName_Type()
)
ctAgentSwitchProtectedPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentSwitchProtectedPortGroupName.setStatus("current")
_CtAgentSwitchProtectedPortPortList_Type = PortList
_CtAgentSwitchProtectedPortPortList_Object = MibTableColumn
ctAgentSwitchProtectedPortPortList = _CtAgentSwitchProtectedPortPortList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33, 1, 1, 18, 1, 1, 3),
    _CtAgentSwitchProtectedPortPortList_Type()
)
ctAgentSwitchProtectedPortPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentSwitchProtectedPortPortList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-FASTPATH-PROTECTED-PORT-MIB",
    **{"ctFastPathProtectedPortMIB": ctFastPathProtectedPortMIB,
       "ctAgentSwitchConfigGroup": ctAgentSwitchConfigGroup,
       "ctAgentSwitchProtectedPortConfigGroup": ctAgentSwitchProtectedPortConfigGroup,
       "ctAgentSwitchProtectedPortTable": ctAgentSwitchProtectedPortTable,
       "ctAgentSwitchProtectedPortEntry": ctAgentSwitchProtectedPortEntry,
       "ctAgentSwitchProtectedPortGroupId": ctAgentSwitchProtectedPortGroupId,
       "ctAgentSwitchProtectedPortGroupName": ctAgentSwitchProtectedPortGroupName,
       "ctAgentSwitchProtectedPortPortList": ctAgentSwitchProtectedPortPortList}
)
