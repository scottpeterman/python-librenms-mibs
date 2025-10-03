# SNMP MIB module (SIAE-CARRIER-AGGRL1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-CARRIER-AGGRL1-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:40 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

carrierAggr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104)
)
if mibBuilder.loadTexts:
    carrierAggr.setRevisions(
        ("2016-08-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CarrierAggrMibVersion_Type = Integer32
_CarrierAggrMibVersion_Object = MibScalar
carrierAggrMibVersion = _CarrierAggrMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 1),
    _CarrierAggrMibVersion_Type()
)
carrierAggrMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierAggrMibVersion.setStatus("current")
_CarrierAggrSensorTable_Object = MibTable
carrierAggrSensorTable = _CarrierAggrSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2)
)
if mibBuilder.loadTexts:
    carrierAggrSensorTable.setStatus("current")
_CarrierAggrSensorEntry_Object = MibTableRow
carrierAggrSensorEntry = _CarrierAggrSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1)
)
carrierAggrSensorEntry.setIndexNames(
    (0, "SIAE-CARRIER-AGGRL1-MIB", "carrierAggrSensorIndex"),
)
if mibBuilder.loadTexts:
    carrierAggrSensorEntry.setStatus("current")


class _CarrierAggrSensorIndex_Type(Integer32):
    """Custom type carrierAggrSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CarrierAggrSensorIndex_Type.__name__ = "Integer32"
_CarrierAggrSensorIndex_Object = MibTableColumn
carrierAggrSensorIndex = _CarrierAggrSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 1),
    _CarrierAggrSensorIndex_Type()
)
carrierAggrSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierAggrSensorIndex.setStatus("current")
_CarrierAggrSensorRowstatus_Type = RowStatus
_CarrierAggrSensorRowstatus_Object = MibTableColumn
carrierAggrSensorRowstatus = _CarrierAggrSensorRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 2),
    _CarrierAggrSensorRowstatus_Type()
)
carrierAggrSensorRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrSensorRowstatus.setStatus("current")


class _CarrierAggrSensorAdminStatus_Type(Integer32):
    """Custom type carrierAggrSensorAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_CarrierAggrSensorAdminStatus_Type.__name__ = "Integer32"
_CarrierAggrSensorAdminStatus_Object = MibTableColumn
carrierAggrSensorAdminStatus = _CarrierAggrSensorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 3),
    _CarrierAggrSensorAdminStatus_Type()
)
carrierAggrSensorAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrSensorAdminStatus.setStatus("current")
_CarrierAggrSensorIfIndex_Type = InterfaceIndexOrZero
_CarrierAggrSensorIfIndex_Object = MibTableColumn
carrierAggrSensorIfIndex = _CarrierAggrSensorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 4),
    _CarrierAggrSensorIfIndex_Type()
)
carrierAggrSensorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrSensorIfIndex.setStatus("current")


class _CarrierAggrSensorHitlessCapability_Type(Bits):
    """Custom type carrierAggrSensorHitlessCapability based on Bits"""
    namedValues = NamedValues(
        ("hitlessAvailable", 0)
    )

_CarrierAggrSensorHitlessCapability_Type.__name__ = "Bits"
_CarrierAggrSensorHitlessCapability_Object = MibTableColumn
carrierAggrSensorHitlessCapability = _CarrierAggrSensorHitlessCapability_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 5),
    _CarrierAggrSensorHitlessCapability_Type()
)
carrierAggrSensorHitlessCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierAggrSensorHitlessCapability.setStatus("current")


class _CarrierAggrSensorHitlessBehaviour_Type(Integer32):
    """Custom type carrierAggrSensorHitlessBehaviour based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CarrierAggrSensorHitlessBehaviour_Type.__name__ = "Integer32"
_CarrierAggrSensorHitlessBehaviour_Object = MibTableColumn
carrierAggrSensorHitlessBehaviour = _CarrierAggrSensorHitlessBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 6),
    _CarrierAggrSensorHitlessBehaviour_Type()
)
carrierAggrSensorHitlessBehaviour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrSensorHitlessBehaviour.setStatus("current")


class _CarrierAggrSensorHitlessMode_Type(Integer32):
    """Custom type carrierAggrSensorHitlessMode based on Integer32"""
    defaultValue = 1

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


_CarrierAggrSensorHitlessMode_Type.__name__ = "Integer32"
_CarrierAggrSensorHitlessMode_Object = MibTableColumn
carrierAggrSensorHitlessMode = _CarrierAggrSensorHitlessMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 7),
    _CarrierAggrSensorHitlessMode_Type()
)
carrierAggrSensorHitlessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrSensorHitlessMode.setStatus("current")


class _CarrierAggrSensorHitlessProfile_Type(Integer32):
    """Custom type carrierAggrSensorHitlessProfile based on Integer32"""
    defaultValue = 1


_CarrierAggrSensorHitlessProfile_Type.__name__ = "Integer32"
_CarrierAggrSensorHitlessProfile_Object = MibTableColumn
carrierAggrSensorHitlessProfile = _CarrierAggrSensorHitlessProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 8),
    _CarrierAggrSensorHitlessProfile_Type()
)
carrierAggrSensorHitlessProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrSensorHitlessProfile.setStatus("current")


class _CarrierAggrSensorHitlessStatus_Type(Integer32):
    """Custom type carrierAggrSensorHitlessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("goodZone", 1),
          ("hitlessZone", 2),
          ("badZone", 3))
    )


_CarrierAggrSensorHitlessStatus_Type.__name__ = "Integer32"
_CarrierAggrSensorHitlessStatus_Object = MibTableColumn
carrierAggrSensorHitlessStatus = _CarrierAggrSensorHitlessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 9),
    _CarrierAggrSensorHitlessStatus_Type()
)
carrierAggrSensorHitlessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierAggrSensorHitlessStatus.setStatus("current")
_CarrierAggrActuatorTable_Object = MibTable
carrierAggrActuatorTable = _CarrierAggrActuatorTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3)
)
if mibBuilder.loadTexts:
    carrierAggrActuatorTable.setStatus("current")
_CarrierAggrActuatorEntry_Object = MibTableRow
carrierAggrActuatorEntry = _CarrierAggrActuatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1)
)
carrierAggrActuatorEntry.setIndexNames(
    (0, "SIAE-CARRIER-AGGRL1-MIB", "carrierAggrActuatorIndex"),
)
if mibBuilder.loadTexts:
    carrierAggrActuatorEntry.setStatus("current")


class _CarrierAggrActuatorIndex_Type(Integer32):
    """Custom type carrierAggrActuatorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CarrierAggrActuatorIndex_Type.__name__ = "Integer32"
_CarrierAggrActuatorIndex_Object = MibTableColumn
carrierAggrActuatorIndex = _CarrierAggrActuatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 1),
    _CarrierAggrActuatorIndex_Type()
)
carrierAggrActuatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierAggrActuatorIndex.setStatus("current")
_CarrierAggrActuatorRowStatus_Type = RowStatus
_CarrierAggrActuatorRowStatus_Object = MibTableColumn
carrierAggrActuatorRowStatus = _CarrierAggrActuatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 2),
    _CarrierAggrActuatorRowStatus_Type()
)
carrierAggrActuatorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrActuatorRowStatus.setStatus("current")


class _CarrierAggrActuatorAdminStatus_Type(Integer32):
    """Custom type carrierAggrActuatorAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_CarrierAggrActuatorAdminStatus_Type.__name__ = "Integer32"
_CarrierAggrActuatorAdminStatus_Object = MibTableColumn
carrierAggrActuatorAdminStatus = _CarrierAggrActuatorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 3),
    _CarrierAggrActuatorAdminStatus_Type()
)
carrierAggrActuatorAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrActuatorAdminStatus.setStatus("current")
_CarrierAggrActuatorIfIndex_Type = InterfaceIndexOrZero
_CarrierAggrActuatorIfIndex_Object = MibTableColumn
carrierAggrActuatorIfIndex = _CarrierAggrActuatorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 4),
    _CarrierAggrActuatorIfIndex_Type()
)
carrierAggrActuatorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrActuatorIfIndex.setStatus("current")
_CarrierAggrActuatorSensorIndex_Type = Integer32
_CarrierAggrActuatorSensorIndex_Object = MibTableColumn
carrierAggrActuatorSensorIndex = _CarrierAggrActuatorSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 5),
    _CarrierAggrActuatorSensorIndex_Type()
)
carrierAggrActuatorSensorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    carrierAggrActuatorSensorIndex.setStatus("current")
_CarrierAggrActuatorConcIpAddr_Type = IpAddress
_CarrierAggrActuatorConcIpAddr_Object = MibTableColumn
carrierAggrActuatorConcIpAddr = _CarrierAggrActuatorConcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 6),
    _CarrierAggrActuatorConcIpAddr_Type()
)
carrierAggrActuatorConcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierAggrActuatorConcIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-CARRIER-AGGRL1-MIB",
    **{"carrierAggr": carrierAggr,
       "carrierAggrMibVersion": carrierAggrMibVersion,
       "carrierAggrSensorTable": carrierAggrSensorTable,
       "carrierAggrSensorEntry": carrierAggrSensorEntry,
       "carrierAggrSensorIndex": carrierAggrSensorIndex,
       "carrierAggrSensorRowstatus": carrierAggrSensorRowstatus,
       "carrierAggrSensorAdminStatus": carrierAggrSensorAdminStatus,
       "carrierAggrSensorIfIndex": carrierAggrSensorIfIndex,
       "carrierAggrSensorHitlessCapability": carrierAggrSensorHitlessCapability,
       "carrierAggrSensorHitlessBehaviour": carrierAggrSensorHitlessBehaviour,
       "carrierAggrSensorHitlessMode": carrierAggrSensorHitlessMode,
       "carrierAggrSensorHitlessProfile": carrierAggrSensorHitlessProfile,
       "carrierAggrSensorHitlessStatus": carrierAggrSensorHitlessStatus,
       "carrierAggrActuatorTable": carrierAggrActuatorTable,
       "carrierAggrActuatorEntry": carrierAggrActuatorEntry,
       "carrierAggrActuatorIndex": carrierAggrActuatorIndex,
       "carrierAggrActuatorRowStatus": carrierAggrActuatorRowStatus,
       "carrierAggrActuatorAdminStatus": carrierAggrActuatorAdminStatus,
       "carrierAggrActuatorIfIndex": carrierAggrActuatorIfIndex,
       "carrierAggrActuatorSensorIndex": carrierAggrActuatorSensorIndex,
       "carrierAggrActuatorConcIpAddr": carrierAggrActuatorConcIpAddr}
)
