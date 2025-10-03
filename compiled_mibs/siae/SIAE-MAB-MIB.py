# SNMP MIB module (SIAE-MAB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-MAB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:08 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mabMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93)
)
if mibBuilder.loadTexts:
    mabMib.setRevisions(
        ("2015-02-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MabBwCalculationMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("min", 2),
          ("max", 3))
    )



class MabPduCompliance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stdMcmCompliant", 1),
          ("extMcmCompliant", 2),
          ("ituG8013Compliant", 3))
    )



class MabSenderOption(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("enableAlways", 0),
          ("enableSignalFail", 1))
    )


# MIB Managed Objects in the order of their OIDs

_MabMibVersion_Type = Integer32
_MabMibVersion_Object = MibScalar
mabMibVersion = _MabMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 1),
    _MabMibVersion_Type()
)
mabMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mabMibVersion.setStatus("current")
_MabSensorTable_Object = MibTable
mabSensorTable = _MabSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2)
)
if mibBuilder.loadTexts:
    mabSensorTable.setStatus("current")
_MabSensorEntry_Object = MibTableRow
mabSensorEntry = _MabSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1)
)
mabSensorEntry.setIndexNames(
    (0, "SIAE-MAB-MIB", "mabSensorIndex"),
)
if mibBuilder.loadTexts:
    mabSensorEntry.setStatus("current")
_MabSensorIndex_Type = Integer32
_MabSensorIndex_Object = MibTableColumn
mabSensorIndex = _MabSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 1),
    _MabSensorIndex_Type()
)
mabSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mabSensorIndex.setStatus("current")
_MabSensorRowStatus_Type = RowStatus
_MabSensorRowStatus_Object = MibTableColumn
mabSensorRowStatus = _MabSensorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 2),
    _MabSensorRowStatus_Type()
)
mabSensorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorRowStatus.setStatus("current")


class _MabSensorAdminStatus_Type(Integer32):
    """Custom type mabSensorAdminStatus based on Integer32"""
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


_MabSensorAdminStatus_Type.__name__ = "Integer32"
_MabSensorAdminStatus_Object = MibTableColumn
mabSensorAdminStatus = _MabSensorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 3),
    _MabSensorAdminStatus_Type()
)
mabSensorAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorAdminStatus.setStatus("current")
_MabSensorIfIndex_Type = InterfaceIndex
_MabSensorIfIndex_Object = MibTableColumn
mabSensorIfIndex = _MabSensorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 4),
    _MabSensorIfIndex_Type()
)
mabSensorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorIfIndex.setStatus("current")
_MabSensorLinkId_Type = Integer32
_MabSensorLinkId_Object = MibTableColumn
mabSensorLinkId = _MabSensorLinkId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 5),
    _MabSensorLinkId_Type()
)
mabSensorLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorLinkId.setStatus("current")


class _MabSensorBwMode_Type(MabBwCalculationMethod):
    """Custom type mabSensorBwMode based on MabBwCalculationMethod"""
    defaultValue = 1


_MabSensorBwMode_Type.__name__ = "MabBwCalculationMethod"
_MabSensorBwMode_Object = MibTableColumn
mabSensorBwMode = _MabSensorBwMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 6),
    _MabSensorBwMode_Type()
)
mabSensorBwMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorBwMode.setStatus("current")


class _MabSensorHoldoffTime_Type(Integer32):
    """Custom type mabSensorHoldoffTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_MabSensorHoldoffTime_Type.__name__ = "Integer32"
_MabSensorHoldoffTime_Object = MibTableColumn
mabSensorHoldoffTime = _MabSensorHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 7),
    _MabSensorHoldoffTime_Type()
)
mabSensorHoldoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorHoldoffTime.setStatus("current")


class _MabSensorObservationTime_Type(Integer32):
    """Custom type mabSensorObservationTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(60, 60),
    )


_MabSensorObservationTime_Type.__name__ = "Integer32"
_MabSensorObservationTime_Object = MibTableColumn
mabSensorObservationTime = _MabSensorObservationTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 8),
    _MabSensorObservationTime_Type()
)
mabSensorObservationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorObservationTime.setStatus("current")


class _MabSensorFastTime_Type(Integer32):
    """Custom type mabSensorFastTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 59),
    )


_MabSensorFastTime_Type.__name__ = "Integer32"
_MabSensorFastTime_Object = MibTableColumn
mabSensorFastTime = _MabSensorFastTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 9),
    _MabSensorFastTime_Type()
)
mabSensorFastTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorFastTime.setStatus("current")


class _MabSensorFastCount_Type(Integer32):
    """Custom type mabSensorFastCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MabSensorFastCount_Type.__name__ = "Integer32"
_MabSensorFastCount_Object = MibTableColumn
mabSensorFastCount = _MabSensorFastCount_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 2, 1, 10),
    _MabSensorFastCount_Type()
)
mabSensorFastCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabSensorFastCount.setStatus("current")
_MabSensorStatusTable_Object = MibTable
mabSensorStatusTable = _MabSensorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3)
)
if mibBuilder.loadTexts:
    mabSensorStatusTable.setStatus("current")
_MabSensorStatusEntry_Object = MibTableRow
mabSensorStatusEntry = _MabSensorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1)
)
mabSensorStatusEntry.setIndexNames(
    (0, "SIAE-MAB-MIB", "mabSensorIndex"),
)
if mibBuilder.loadTexts:
    mabSensorStatusEntry.setStatus("current")
_MabSensorNominalBw_Type = Integer32
_MabSensorNominalBw_Object = MibTableColumn
mabSensorNominalBw = _MabSensorNominalBw_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1, 1),
    _MabSensorNominalBw_Type()
)
mabSensorNominalBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mabSensorNominalBw.setStatus("current")
_MabSensorCurrentBw_Type = Integer32
_MabSensorCurrentBw_Object = MibTableColumn
mabSensorCurrentBw = _MabSensorCurrentBw_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 3, 1, 2),
    _MabSensorCurrentBw_Type()
)
mabSensorCurrentBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mabSensorCurrentBw.setStatus("current")
_MabPduSenderTable_Object = MibTable
mabPduSenderTable = _MabPduSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4)
)
if mibBuilder.loadTexts:
    mabPduSenderTable.setStatus("current")
_MabPduSenderEntry_Object = MibTableRow
mabPduSenderEntry = _MabPduSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1)
)
mabPduSenderEntry.setIndexNames(
    (0, "SIAE-MAB-MIB", "mabPduSenderIndex"),
)
if mibBuilder.loadTexts:
    mabPduSenderEntry.setStatus("current")
_MabPduSenderIndex_Type = Integer32
_MabPduSenderIndex_Object = MibTableColumn
mabPduSenderIndex = _MabPduSenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 1),
    _MabPduSenderIndex_Type()
)
mabPduSenderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mabPduSenderIndex.setStatus("current")
_MabPduSenderRowStatus_Type = RowStatus
_MabPduSenderRowStatus_Object = MibTableColumn
mabPduSenderRowStatus = _MabPduSenderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 2),
    _MabPduSenderRowStatus_Type()
)
mabPduSenderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderRowStatus.setStatus("current")


class _MabPduSenderAdminStatus_Type(Integer32):
    """Custom type mabPduSenderAdminStatus based on Integer32"""
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


_MabPduSenderAdminStatus_Type.__name__ = "Integer32"
_MabPduSenderAdminStatus_Object = MibTableColumn
mabPduSenderAdminStatus = _MabPduSenderAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 3),
    _MabPduSenderAdminStatus_Type()
)
mabPduSenderAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderAdminStatus.setStatus("current")
_MabPduSenderIfIndex_Type = InterfaceIndex
_MabPduSenderIfIndex_Object = MibTableColumn
mabPduSenderIfIndex = _MabPduSenderIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 4),
    _MabPduSenderIfIndex_Type()
)
mabPduSenderIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderIfIndex.setStatus("current")
_MabPduSenderSensorIndex_Type = Integer32
_MabPduSenderSensorIndex_Object = MibTableColumn
mabPduSenderSensorIndex = _MabPduSenderSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 5),
    _MabPduSenderSensorIndex_Type()
)
mabPduSenderSensorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderSensorIndex.setStatus("current")


class _MabPduSenderVlanId_Type(Integer32):
    """Custom type mabPduSenderVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_MabPduSenderVlanId_Type.__name__ = "Integer32"
_MabPduSenderVlanId_Object = MibTableColumn
mabPduSenderVlanId = _MabPduSenderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 6),
    _MabPduSenderVlanId_Type()
)
mabPduSenderVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderVlanId.setStatus("current")


class _MabPduSenderPcp_Type(Integer32):
    """Custom type mabPduSenderPcp based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MabPduSenderPcp_Type.__name__ = "Integer32"
_MabPduSenderPcp_Object = MibTableColumn
mabPduSenderPcp = _MabPduSenderPcp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 7),
    _MabPduSenderPcp_Type()
)
mabPduSenderPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderPcp.setStatus("current")


class _MabPduSenderOamMaintLevel_Type(Integer32):
    """Custom type mabPduSenderOamMaintLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MabPduSenderOamMaintLevel_Type.__name__ = "Integer32"
_MabPduSenderOamMaintLevel_Object = MibTableColumn
mabPduSenderOamMaintLevel = _MabPduSenderOamMaintLevel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 8),
    _MabPduSenderOamMaintLevel_Type()
)
mabPduSenderOamMaintLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderOamMaintLevel.setStatus("current")


class _MabPduSenderDAType_Type(Integer32):
    """Custom type mabPduSenderDAType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicastDA", 1),
          ("unicastDA", 2))
    )


_MabPduSenderDAType_Type.__name__ = "Integer32"
_MabPduSenderDAType_Object = MibTableColumn
mabPduSenderDAType = _MabPduSenderDAType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 9),
    _MabPduSenderDAType_Type()
)
mabPduSenderDAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderDAType.setStatus("current")


class _MabPduSenderUnicastDA_Type(MacAddress):
    """Custom type mabPduSenderUnicastDA based on MacAddress"""
    defaultHexValue = "000000000000"


_MabPduSenderUnicastDA_Type.__name__ = "MacAddress"
_MabPduSenderUnicastDA_Object = MibTableColumn
mabPduSenderUnicastDA = _MabPduSenderUnicastDA_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 10),
    _MabPduSenderUnicastDA_Type()
)
mabPduSenderUnicastDA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderUnicastDA.setStatus("current")
_MabPduSenderOption_Type = MabSenderOption
_MabPduSenderOption_Object = MibTableColumn
mabPduSenderOption = _MabPduSenderOption_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 11),
    _MabPduSenderOption_Type()
)
mabPduSenderOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderOption.setStatus("current")


class _MabPduSenderPduCompliance_Type(MabPduCompliance):
    """Custom type mabPduSenderPduCompliance based on MabPduCompliance"""
    defaultValue = 1


_MabPduSenderPduCompliance_Type.__name__ = "MabPduCompliance"
_MabPduSenderPduCompliance_Object = MibTableColumn
mabPduSenderPduCompliance = _MabPduSenderPduCompliance_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 93, 4, 1, 12),
    _MabPduSenderPduCompliance_Type()
)
mabPduSenderPduCompliance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mabPduSenderPduCompliance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-MAB-MIB",
    **{"MabBwCalculationMethod": MabBwCalculationMethod,
       "MabPduCompliance": MabPduCompliance,
       "MabSenderOption": MabSenderOption,
       "mabMib": mabMib,
       "mabMibVersion": mabMibVersion,
       "mabSensorTable": mabSensorTable,
       "mabSensorEntry": mabSensorEntry,
       "mabSensorIndex": mabSensorIndex,
       "mabSensorRowStatus": mabSensorRowStatus,
       "mabSensorAdminStatus": mabSensorAdminStatus,
       "mabSensorIfIndex": mabSensorIfIndex,
       "mabSensorLinkId": mabSensorLinkId,
       "mabSensorBwMode": mabSensorBwMode,
       "mabSensorHoldoffTime": mabSensorHoldoffTime,
       "mabSensorObservationTime": mabSensorObservationTime,
       "mabSensorFastTime": mabSensorFastTime,
       "mabSensorFastCount": mabSensorFastCount,
       "mabSensorStatusTable": mabSensorStatusTable,
       "mabSensorStatusEntry": mabSensorStatusEntry,
       "mabSensorNominalBw": mabSensorNominalBw,
       "mabSensorCurrentBw": mabSensorCurrentBw,
       "mabPduSenderTable": mabPduSenderTable,
       "mabPduSenderEntry": mabPduSenderEntry,
       "mabPduSenderIndex": mabPduSenderIndex,
       "mabPduSenderRowStatus": mabPduSenderRowStatus,
       "mabPduSenderAdminStatus": mabPduSenderAdminStatus,
       "mabPduSenderIfIndex": mabPduSenderIfIndex,
       "mabPduSenderSensorIndex": mabPduSenderSensorIndex,
       "mabPduSenderVlanId": mabPduSenderVlanId,
       "mabPduSenderPcp": mabPduSenderPcp,
       "mabPduSenderOamMaintLevel": mabPduSenderOamMaintLevel,
       "mabPduSenderDAType": mabPduSenderDAType,
       "mabPduSenderUnicastDA": mabPduSenderUnicastDA,
       "mabPduSenderOption": mabPduSenderOption,
       "mabPduSenderPduCompliance": mabPduSenderPduCompliance}
)
