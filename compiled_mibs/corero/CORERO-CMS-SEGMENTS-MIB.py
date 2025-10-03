# SNMP MIB module (CORERO-CMS-SEGMENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\corero\CORERO-CMS-SEGMENTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:32 2025
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

(coreroCMSMIBCompliances,
 coreroCMSMIBGroups,
 coreroCMSMIBObjects) = mibBuilder.importSymbols(
    "CORERO-CMS-MIB",
    "coreroCMSMIBCompliances",
    "coreroCMSMIBGroups",
    "coreroCMSMIBObjects")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

segments = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4)
)
if mibBuilder.loadTexts:
    segments.setRevisions(
        ("2017-10-04 00:00",
         "2017-12-19 00:00",
         "2017-12-28 00:00",
         "2018-02-19 00:00",
         "2018-11-23 00:00",
         "2020-06-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SegmentTable_Object = MibTable
segmentTable = _SegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    segmentTable.setStatus("current")
_SegmentEntry_Object = MibTableRow
segmentEntry = _SegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1)
)
segmentEntry.setIndexNames(
    (0, "CORERO-CMS-SEGMENTS-MIB", "segmentIndex"),
)
if mibBuilder.loadTexts:
    segmentEntry.setStatus("current")


class _SegmentIndex_Type(Integer32):
    """Custom type segmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SegmentIndex_Type.__name__ = "Integer32"
_SegmentIndex_Object = MibTableColumn
segmentIndex = _SegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 1),
    _SegmentIndex_Type()
)
segmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentIndex.setStatus("current")
_SegmentDevice_Type = OctetString
_SegmentDevice_Object = MibTableColumn
segmentDevice = _SegmentDevice_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 2),
    _SegmentDevice_Type()
)
segmentDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentDevice.setStatus("current")
_SegmentId_Type = OctetString
_SegmentId_Object = MibTableColumn
segmentId = _SegmentId_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 3),
    _SegmentId_Type()
)
segmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentId.setStatus("current")
_SegmentName_Type = OctetString
_SegmentName_Object = MibTableColumn
segmentName = _SegmentName_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 4),
    _SegmentName_Type()
)
segmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentName.setStatus("current")
_SegmentDescription_Type = OctetString
_SegmentDescription_Object = MibTableColumn
segmentDescription = _SegmentDescription_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 5),
    _SegmentDescription_Type()
)
segmentDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentDescription.setStatus("current")


class _SegmentLinkStatePropagationAdminState_Type(Integer32):
    """Custom type segmentLinkStatePropagationAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SegmentLinkStatePropagationAdminState_Type.__name__ = "Integer32"
_SegmentLinkStatePropagationAdminState_Object = MibTableColumn
segmentLinkStatePropagationAdminState = _SegmentLinkStatePropagationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 6),
    _SegmentLinkStatePropagationAdminState_Type()
)
segmentLinkStatePropagationAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentLinkStatePropagationAdminState.setStatus("current")


class _SegmentLinkStatePropagationWaitTime_Type(Integer32):
    """Custom type segmentLinkStatePropagationWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_SegmentLinkStatePropagationWaitTime_Type.__name__ = "Integer32"
_SegmentLinkStatePropagationWaitTime_Object = MibTableColumn
segmentLinkStatePropagationWaitTime = _SegmentLinkStatePropagationWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 7),
    _SegmentLinkStatePropagationWaitTime_Type()
)
segmentLinkStatePropagationWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentLinkStatePropagationWaitTime.setStatus("current")


class _SegmentLinkStatePropagationRecoveryTimeout_Type(Integer32):
    """Custom type segmentLinkStatePropagationRecoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_SegmentLinkStatePropagationRecoveryTimeout_Type.__name__ = "Integer32"
_SegmentLinkStatePropagationRecoveryTimeout_Object = MibTableColumn
segmentLinkStatePropagationRecoveryTimeout = _SegmentLinkStatePropagationRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 8),
    _SegmentLinkStatePropagationRecoveryTimeout_Type()
)
segmentLinkStatePropagationRecoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentLinkStatePropagationRecoveryTimeout.setStatus("current")


class _SegmentConfiguredDefenseMode_Type(Integer32):
    """Custom type segmentConfiguredDefenseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 0),
          ("mitigate", 1),
          ("pass-through", 2),
          ("not-applicable", 10))
    )


_SegmentConfiguredDefenseMode_Type.__name__ = "Integer32"
_SegmentConfiguredDefenseMode_Object = MibTableColumn
segmentConfiguredDefenseMode = _SegmentConfiguredDefenseMode_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 9),
    _SegmentConfiguredDefenseMode_Type()
)
segmentConfiguredDefenseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentConfiguredDefenseMode.setStatus("current")
_SegmentNtdExternalInterface_Type = OctetString
_SegmentNtdExternalInterface_Object = MibTableColumn
segmentNtdExternalInterface = _SegmentNtdExternalInterface_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 10),
    _SegmentNtdExternalInterface_Type()
)
segmentNtdExternalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNtdExternalInterface.setStatus("current")


class _SegmentNtdExternalInterfaceStatus_Type(Integer32):
    """Custom type segmentNtdExternalInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("down-link-state-propagation", 2),
          ("disabled", 3),
          ("unknown", 4),
          ("unused", 5),
          ("partially-down", 6),
          ("down-remote-fault", 7),
          ("down-local-fault", 8))
    )


_SegmentNtdExternalInterfaceStatus_Type.__name__ = "Integer32"
_SegmentNtdExternalInterfaceStatus_Object = MibTableColumn
segmentNtdExternalInterfaceStatus = _SegmentNtdExternalInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 11),
    _SegmentNtdExternalInterfaceStatus_Type()
)
segmentNtdExternalInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNtdExternalInterfaceStatus.setStatus("current")
_SegmentNtdExternalInterfaceLinkSpeed_Type = Unsigned32
_SegmentNtdExternalInterfaceLinkSpeed_Object = MibTableColumn
segmentNtdExternalInterfaceLinkSpeed = _SegmentNtdExternalInterfaceLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 12),
    _SegmentNtdExternalInterfaceLinkSpeed_Type()
)
segmentNtdExternalInterfaceLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNtdExternalInterfaceLinkSpeed.setStatus("current")
_SegmentNtdInternalInterface_Type = OctetString
_SegmentNtdInternalInterface_Object = MibTableColumn
segmentNtdInternalInterface = _SegmentNtdInternalInterface_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 13),
    _SegmentNtdInternalInterface_Type()
)
segmentNtdInternalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNtdInternalInterface.setStatus("current")


class _SegmentNtdInternalInterfaceStatus_Type(Integer32):
    """Custom type segmentNtdInternalInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("down-link-state-propagation", 2),
          ("disabled", 3),
          ("unknown", 4),
          ("unused", 5),
          ("partially-down", 6),
          ("down-remote-fault", 7),
          ("down-local-fault", 8))
    )


_SegmentNtdInternalInterfaceStatus_Type.__name__ = "Integer32"
_SegmentNtdInternalInterfaceStatus_Object = MibTableColumn
segmentNtdInternalInterfaceStatus = _SegmentNtdInternalInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 14),
    _SegmentNtdInternalInterfaceStatus_Type()
)
segmentNtdInternalInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNtdInternalInterfaceStatus.setStatus("current")
_SegmentNtdInternalInterfaceLinkSpeed_Type = Unsigned32
_SegmentNtdInternalInterfaceLinkSpeed_Object = MibTableColumn
segmentNtdInternalInterfaceLinkSpeed = _SegmentNtdInternalInterfaceLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 15),
    _SegmentNtdInternalInterfaceLinkSpeed_Type()
)
segmentNtdInternalInterfaceLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNtdInternalInterfaceLinkSpeed.setStatus("current")
_SegmentNbaExternalInterface_Type = OctetString
_SegmentNbaExternalInterface_Object = MibTableColumn
segmentNbaExternalInterface = _SegmentNbaExternalInterface_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 16),
    _SegmentNbaExternalInterface_Type()
)
segmentNbaExternalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNbaExternalInterface.setStatus("current")


class _SegmentNbaExternalInterfaceStatus_Type(Integer32):
    """Custom type segmentNbaExternalInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("down-link-state-propagation", 2),
          ("disabled", 3),
          ("unknown", 4),
          ("unused", 5),
          ("partially-down", 6),
          ("down-remote-fault", 7),
          ("down-local-fault", 8))
    )


_SegmentNbaExternalInterfaceStatus_Type.__name__ = "Integer32"
_SegmentNbaExternalInterfaceStatus_Object = MibTableColumn
segmentNbaExternalInterfaceStatus = _SegmentNbaExternalInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 17),
    _SegmentNbaExternalInterfaceStatus_Type()
)
segmentNbaExternalInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNbaExternalInterfaceStatus.setStatus("current")
_SegmentNbaExternalInterfaceLinkSpeed_Type = Unsigned32
_SegmentNbaExternalInterfaceLinkSpeed_Object = MibTableColumn
segmentNbaExternalInterfaceLinkSpeed = _SegmentNbaExternalInterfaceLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 18),
    _SegmentNbaExternalInterfaceLinkSpeed_Type()
)
segmentNbaExternalInterfaceLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNbaExternalInterfaceLinkSpeed.setStatus("current")
_SegmentNbaInternalInterface_Type = OctetString
_SegmentNbaInternalInterface_Object = MibTableColumn
segmentNbaInternalInterface = _SegmentNbaInternalInterface_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 19),
    _SegmentNbaInternalInterface_Type()
)
segmentNbaInternalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNbaInternalInterface.setStatus("current")


class _SegmentNbaInternalInterfaceStatus_Type(Integer32):
    """Custom type segmentNbaInternalInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("down-link-state-propagation", 2),
          ("disabled", 3),
          ("unknown", 4),
          ("unused", 5),
          ("partially-down", 6),
          ("down-remote-fault", 7),
          ("down-local-fault", 8))
    )


_SegmentNbaInternalInterfaceStatus_Type.__name__ = "Integer32"
_SegmentNbaInternalInterfaceStatus_Object = MibTableColumn
segmentNbaInternalInterfaceStatus = _SegmentNbaInternalInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 20),
    _SegmentNbaInternalInterfaceStatus_Type()
)
segmentNbaInternalInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNbaInternalInterfaceStatus.setStatus("current")
_SegmentNbaInternalInterfaceLinkSpeed_Type = Unsigned32
_SegmentNbaInternalInterfaceLinkSpeed_Object = MibTableColumn
segmentNbaInternalInterfaceLinkSpeed = _SegmentNbaInternalInterfaceLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 21),
    _SegmentNbaInternalInterfaceLinkSpeed_Type()
)
segmentNbaInternalInterfaceLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentNbaInternalInterfaceLinkSpeed.setStatus("current")


class _SegmentCurrentDefenseMode_Type(Integer32):
    """Custom type segmentCurrentDefenseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 0),
          ("mitigate", 1),
          ("pass-through", 2),
          ("not-applicable", 10))
    )


_SegmentCurrentDefenseMode_Type.__name__ = "Integer32"
_SegmentCurrentDefenseMode_Object = MibTableColumn
segmentCurrentDefenseMode = _SegmentCurrentDefenseMode_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 22),
    _SegmentCurrentDefenseMode_Type()
)
segmentCurrentDefenseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentCurrentDefenseMode.setStatus("current")
_SegmentBypassDevice_Type = OctetString
_SegmentBypassDevice_Object = MibTableColumn
segmentBypassDevice = _SegmentBypassDevice_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 23),
    _SegmentBypassDevice_Type()
)
segmentBypassDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentBypassDevice.setStatus("current")


class _SegmentConfiguredBypassMode_Type(Integer32):
    """Custom type segmentConfiguredBypassMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("inline", 0),
          ("automatic", 1),
          ("physical-bypass", 2),
          ("switched-bypass", 3),
          ("monitor-tap", 4),
          ("not-applicable", 10))
    )


_SegmentConfiguredBypassMode_Type.__name__ = "Integer32"
_SegmentConfiguredBypassMode_Object = MibTableColumn
segmentConfiguredBypassMode = _SegmentConfiguredBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 24),
    _SegmentConfiguredBypassMode_Type()
)
segmentConfiguredBypassMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentConfiguredBypassMode.setStatus("current")


class _SegmentCurrentBypassMode_Type(Integer32):
    """Custom type segmentCurrentBypassMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("inline", 0),
          ("automatic", 1),
          ("physical-bypass", 2),
          ("switched-bypass", 3),
          ("monitor-tap", 4),
          ("not-applicable", 10))
    )


_SegmentCurrentBypassMode_Type.__name__ = "Integer32"
_SegmentCurrentBypassMode_Object = MibTableColumn
segmentCurrentBypassMode = _SegmentCurrentBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 25),
    _SegmentCurrentBypassMode_Type()
)
segmentCurrentBypassMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentCurrentBypassMode.setStatus("current")


class _SegmentCurrentBypassState_Type(Integer32):
    """Custom type segmentCurrentBypassState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("inline", 0),
          ("physical-bypass", 1),
          ("switched-bypass", 2),
          ("monitor-tap", 3),
          ("automatic-inline", 4),
          ("automatic-bypass", 5),
          ("not-applicable", 10))
    )


_SegmentCurrentBypassState_Type.__name__ = "Integer32"
_SegmentCurrentBypassState_Object = MibTableColumn
segmentCurrentBypassState = _SegmentCurrentBypassState_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 26),
    _SegmentCurrentBypassState_Type()
)
segmentCurrentBypassState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentCurrentBypassState.setStatus("current")


class _SegmentDefenseModeOverride_Type(Integer32):
    """Custom type segmentDefenseModeOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("segment", 1),
          ("device", 2),
          ("cluster", 3))
    )


_SegmentDefenseModeOverride_Type.__name__ = "Integer32"
_SegmentDefenseModeOverride_Object = MibTableColumn
segmentDefenseModeOverride = _SegmentDefenseModeOverride_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 27),
    _SegmentDefenseModeOverride_Type()
)
segmentDefenseModeOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentDefenseModeOverride.setStatus("current")


class _SegmentBypassModeOverride_Type(Integer32):
    """Custom type segmentBypassModeOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("segment", 1),
          ("device", 2),
          ("cluster", 3))
    )


_SegmentBypassModeOverride_Type.__name__ = "Integer32"
_SegmentBypassModeOverride_Object = MibTableColumn
segmentBypassModeOverride = _SegmentBypassModeOverride_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 4, 1, 1, 28),
    _SegmentBypassModeOverride_Type()
)
segmentBypassModeOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentBypassModeOverride.setStatus("current")

# Managed Objects groups

coreroSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 2, 4)
)
coreroSegmentGroup.setObjects(
      *(("CORERO-CMS-SEGMENTS-MIB", "segmentIndex"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentDevice"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentId"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentName"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentDescription"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentLinkStatePropagationAdminState"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentLinkStatePropagationWaitTime"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentLinkStatePropagationRecoveryTimeout"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentConfiguredDefenseMode"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNtdExternalInterface"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNtdExternalInterfaceStatus"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNtdExternalInterfaceLinkSpeed"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNtdInternalInterface"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNtdInternalInterfaceStatus"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNtdInternalInterfaceLinkSpeed"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNbaExternalInterface"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNbaExternalInterfaceStatus"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNbaExternalInterfaceLinkSpeed"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNbaInternalInterface"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNbaInternalInterfaceStatus"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentNbaInternalInterfaceLinkSpeed"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentCurrentDefenseMode"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentBypassDevice"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentConfiguredBypassMode"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentCurrentBypassMode"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentCurrentBypassState"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentDefenseModeOverride"),
        ("CORERO-CMS-SEGMENTS-MIB", "segmentBypassModeOverride"))
)
if mibBuilder.loadTexts:
    coreroSegmentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coreroCMSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 1, 4)
)
coreroCMSMIBCompliance.setObjects(
    ("CORERO-CMS-SEGMENTS-MIB", "coreroSegmentGroup")
)
if mibBuilder.loadTexts:
    coreroCMSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORERO-CMS-SEGMENTS-MIB",
    **{"segments": segments,
       "segmentTable": segmentTable,
       "segmentEntry": segmentEntry,
       "segmentIndex": segmentIndex,
       "segmentDevice": segmentDevice,
       "segmentId": segmentId,
       "segmentName": segmentName,
       "segmentDescription": segmentDescription,
       "segmentLinkStatePropagationAdminState": segmentLinkStatePropagationAdminState,
       "segmentLinkStatePropagationWaitTime": segmentLinkStatePropagationWaitTime,
       "segmentLinkStatePropagationRecoveryTimeout": segmentLinkStatePropagationRecoveryTimeout,
       "segmentConfiguredDefenseMode": segmentConfiguredDefenseMode,
       "segmentNtdExternalInterface": segmentNtdExternalInterface,
       "segmentNtdExternalInterfaceStatus": segmentNtdExternalInterfaceStatus,
       "segmentNtdExternalInterfaceLinkSpeed": segmentNtdExternalInterfaceLinkSpeed,
       "segmentNtdInternalInterface": segmentNtdInternalInterface,
       "segmentNtdInternalInterfaceStatus": segmentNtdInternalInterfaceStatus,
       "segmentNtdInternalInterfaceLinkSpeed": segmentNtdInternalInterfaceLinkSpeed,
       "segmentNbaExternalInterface": segmentNbaExternalInterface,
       "segmentNbaExternalInterfaceStatus": segmentNbaExternalInterfaceStatus,
       "segmentNbaExternalInterfaceLinkSpeed": segmentNbaExternalInterfaceLinkSpeed,
       "segmentNbaInternalInterface": segmentNbaInternalInterface,
       "segmentNbaInternalInterfaceStatus": segmentNbaInternalInterfaceStatus,
       "segmentNbaInternalInterfaceLinkSpeed": segmentNbaInternalInterfaceLinkSpeed,
       "segmentCurrentDefenseMode": segmentCurrentDefenseMode,
       "segmentBypassDevice": segmentBypassDevice,
       "segmentConfiguredBypassMode": segmentConfiguredBypassMode,
       "segmentCurrentBypassMode": segmentCurrentBypassMode,
       "segmentCurrentBypassState": segmentCurrentBypassState,
       "segmentDefenseModeOverride": segmentDefenseModeOverride,
       "segmentBypassModeOverride": segmentBypassModeOverride,
       "coreroCMSMIBCompliance": coreroCMSMIBCompliance,
       "coreroSegmentGroup": coreroSegmentGroup}
)
