# SNMP MIB module (RUCKUS-UNLEASHED-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-UNLEASHED-WLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:58 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusUnleashedWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusUnleashedWLANModule")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusUnleashedWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusUnleashedWLANObjects_ObjectIdentity = ObjectIdentity
ruckusUnleashedWLANObjects = _RuckusUnleashedWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1)
)
_RuckusUnleashedWLANInfo_ObjectIdentity = ObjectIdentity
ruckusUnleashedWLANInfo = _RuckusUnleashedWLANInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 1)
)
_RuckusUnleashedWLANAPInfo_ObjectIdentity = ObjectIdentity
ruckusUnleashedWLANAPInfo = _RuckusUnleashedWLANAPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2)
)
_RuckusUnleashedWLANAPEthStatusTable_Object = MibTable
ruckusUnleashedWLANAPEthStatusTable = _RuckusUnleashedWLANAPEthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthStatusTable.setStatus("current")
_RuckusUnleashedWLANAPEthStatusEntry_Object = MibTableRow
ruckusUnleashedWLANAPEthStatusEntry = _RuckusUnleashedWLANAPEthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1)
)
ruckusUnleashedWLANAPEthStatusEntry.setIndexNames(
    (0, "RUCKUS-UNLEASHED-WLAN-MIB", "ruckusUnleashedWLANAPMacAddress"),
    (0, "RUCKUS-UNLEASHED-WLAN-MIB", "ruckusUnleashedWLANAPEthPortId"),
)
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthStatusEntry.setStatus("current")
_RuckusUnleashedWLANAPMacAddress_Type = MacAddress
_RuckusUnleashedWLANAPMacAddress_Object = MibTableColumn
ruckusUnleashedWLANAPMacAddress = _RuckusUnleashedWLANAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1, 1),
    _RuckusUnleashedWLANAPMacAddress_Type()
)
ruckusUnleashedWLANAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPMacAddress.setStatus("current")
_RuckusUnleashedWLANAPEthPortId_Type = Integer32
_RuckusUnleashedWLANAPEthPortId_Object = MibTableColumn
ruckusUnleashedWLANAPEthPortId = _RuckusUnleashedWLANAPEthPortId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1, 2),
    _RuckusUnleashedWLANAPEthPortId_Type()
)
ruckusUnleashedWLANAPEthPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthPortId.setStatus("current")
_RuckusUnleashedWLANAPEthIfname_Type = OctetString
_RuckusUnleashedWLANAPEthIfname_Object = MibTableColumn
ruckusUnleashedWLANAPEthIfname = _RuckusUnleashedWLANAPEthIfname_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1, 5),
    _RuckusUnleashedWLANAPEthIfname_Type()
)
ruckusUnleashedWLANAPEthIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthIfname.setStatus("current")


class _RuckusUnleashedWLANAPEthPhyStatus_Type(Integer32):
    """Custom type ruckusUnleashedWLANAPEthPhyStatus based on Integer32"""
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


_RuckusUnleashedWLANAPEthPhyStatus_Type.__name__ = "Integer32"
_RuckusUnleashedWLANAPEthPhyStatus_Object = MibTableColumn
ruckusUnleashedWLANAPEthPhyStatus = _RuckusUnleashedWLANAPEthPhyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1, 8),
    _RuckusUnleashedWLANAPEthPhyStatus_Type()
)
ruckusUnleashedWLANAPEthPhyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthPhyStatus.setStatus("current")
_RuckusUnleashedWLANAPEthPhyIfSpeed_Type = Integer32
_RuckusUnleashedWLANAPEthPhyIfSpeed_Object = MibTableColumn
ruckusUnleashedWLANAPEthPhyIfSpeed = _RuckusUnleashedWLANAPEthPhyIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1, 9),
    _RuckusUnleashedWLANAPEthPhyIfSpeed_Type()
)
ruckusUnleashedWLANAPEthPhyIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthPhyIfSpeed.setStatus("current")


class _RuckusUnleashedWLANAPEthPhyLinkStatus_Type(Integer32):
    """Custom type ruckusUnleashedWLANAPEthPhyLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_RuckusUnleashedWLANAPEthPhyLinkStatus_Type.__name__ = "Integer32"
_RuckusUnleashedWLANAPEthPhyLinkStatus_Object = MibTableColumn
ruckusUnleashedWLANAPEthPhyLinkStatus = _RuckusUnleashedWLANAPEthPhyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1, 10),
    _RuckusUnleashedWLANAPEthPhyLinkStatus_Type()
)
ruckusUnleashedWLANAPEthPhyLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthPhyLinkStatus.setStatus("current")
_RuckusUnleashedWLANAPEthLabel_Type = OctetString
_RuckusUnleashedWLANAPEthLabel_Object = MibTableColumn
ruckusUnleashedWLANAPEthLabel = _RuckusUnleashedWLANAPEthLabel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2, 1, 1, 2, 8, 1, 11),
    _RuckusUnleashedWLANAPEthLabel_Type()
)
ruckusUnleashedWLANAPEthLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedWLANAPEthLabel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-UNLEASHED-WLAN-MIB",
    **{"ruckusUnleashedWLANMIB": ruckusUnleashedWLANMIB,
       "ruckusUnleashedWLANObjects": ruckusUnleashedWLANObjects,
       "ruckusUnleashedWLANInfo": ruckusUnleashedWLANInfo,
       "ruckusUnleashedWLANAPInfo": ruckusUnleashedWLANAPInfo,
       "ruckusUnleashedWLANAPEthStatusTable": ruckusUnleashedWLANAPEthStatusTable,
       "ruckusUnleashedWLANAPEthStatusEntry": ruckusUnleashedWLANAPEthStatusEntry,
       "ruckusUnleashedWLANAPMacAddress": ruckusUnleashedWLANAPMacAddress,
       "ruckusUnleashedWLANAPEthPortId": ruckusUnleashedWLANAPEthPortId,
       "ruckusUnleashedWLANAPEthIfname": ruckusUnleashedWLANAPEthIfname,
       "ruckusUnleashedWLANAPEthPhyStatus": ruckusUnleashedWLANAPEthPhyStatus,
       "ruckusUnleashedWLANAPEthPhyIfSpeed": ruckusUnleashedWLANAPEthPhyIfSpeed,
       "ruckusUnleashedWLANAPEthPhyLinkStatus": ruckusUnleashedWLANAPEthPhyLinkStatus,
       "ruckusUnleashedWLANAPEthLabel": ruckusUnleashedWLANAPEthLabel}
)
