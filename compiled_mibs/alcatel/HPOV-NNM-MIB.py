# SNMP MIB module (HPOV-NNM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alcatel\HPOV-NNM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:11 2025
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

hpOpenView = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 1)
)
if mibBuilder.loadTexts:
    hpOpenView.setRevisions(
        ("1996-07-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OVTextString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_OpenView_ObjectIdentity = ObjectIdentity
openView = _OpenView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17)
)
_HpOVNNMTraps_ObjectIdentity = ObjectIdentity
hpOVNNMTraps = _HpOVNNMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 1, 0)
)
_OpenViewTrapVars_ObjectIdentity = ObjectIdentity
openViewTrapVars = _OpenViewTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2)
)
_OpenViewSourceId_Type = Integer32
_OpenViewSourceId_Object = MibScalar
openViewSourceId = _OpenViewSourceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 1),
    _OpenViewSourceId_Type()
)
openViewSourceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewSourceId.setStatus("current")
_OpenViewSourceName_Type = OVTextString
_OpenViewSourceName_Object = MibScalar
openViewSourceName = _OpenViewSourceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 2),
    _OpenViewSourceName_Type()
)
openViewSourceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewSourceName.setStatus("current")
_OpenViewObjectId_Type = DisplayString
_OpenViewObjectId_Object = MibScalar
openViewObjectId = _OpenViewObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 3),
    _OpenViewObjectId_Type()
)
openViewObjectId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewObjectId.setStatus("current")
_OpenViewData_Type = OctetString
_OpenViewData_Object = MibScalar
openViewData = _OpenViewData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 4),
    _OpenViewData_Type()
)
openViewData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewData.setStatus("current")
_OpenViewSeverity_Type = OVTextString
_OpenViewSeverity_Object = MibScalar
openViewSeverity = _OpenViewSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 5),
    _OpenViewSeverity_Type()
)
openViewSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewSeverity.setStatus("current")
_OpenViewCategory_Type = OVTextString
_OpenViewCategory_Object = MibScalar
openViewCategory = _OpenViewCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 6),
    _OpenViewCategory_Type()
)
openViewCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewCategory.setStatus("current")
_OpenViewFilter_Type = DisplayString
_OpenViewFilter_Object = MibScalar
openViewFilter = _OpenViewFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 7),
    _OpenViewFilter_Type()
)
openViewFilter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewFilter.setStatus("current")
_OpenViewEntity_Type = OVTextString
_OpenViewEntity_Object = MibScalar
openViewEntity = _OpenViewEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 8),
    _OpenViewEntity_Type()
)
openViewEntity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewEntity.setStatus("current")
_OpenViewAddress_Type = DisplayString
_OpenViewAddress_Object = MibScalar
openViewAddress = _OpenViewAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 9),
    _OpenViewAddress_Type()
)
openViewAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewAddress.setStatus("current")
_OpenViewPid_Type = DisplayString
_OpenViewPid_Object = MibScalar
openViewPid = _OpenViewPid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 10),
    _OpenViewPid_Type()
)
openViewPid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewPid.setStatus("current")
_OpenViewCmipManagedObjectClass_Type = DisplayString
_OpenViewCmipManagedObjectClass_Object = MibScalar
openViewCmipManagedObjectClass = _OpenViewCmipManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 11),
    _OpenViewCmipManagedObjectClass_Type()
)
openViewCmipManagedObjectClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewCmipManagedObjectClass.setStatus("current")
_OpenViewCmipEventTime_Type = DisplayString
_OpenViewCmipEventTime_Object = MibScalar
openViewCmipEventTime = _OpenViewCmipEventTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 12),
    _OpenViewCmipEventTime_Type()
)
openViewCmipEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewCmipEventTime.setStatus("current")
_OpenViewCmipEventType_Type = DisplayString
_OpenViewCmipEventType_Object = MibScalar
openViewCmipEventType = _OpenViewCmipEventType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 13),
    _OpenViewCmipEventType_Type()
)
openViewCmipEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewCmipEventType.setStatus("current")
_OpenViewCmipEventInfo_Type = DisplayString
_OpenViewCmipEventInfo_Object = MibScalar
openViewCmipEventInfo = _OpenViewCmipEventInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 14),
    _OpenViewCmipEventInfo_Type()
)
openViewCmipEventInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewCmipEventInfo.setStatus("current")
_OpenViewCmipManagedObjectInstanceId_Type = DisplayString
_OpenViewCmipManagedObjectInstanceId_Object = MibScalar
openViewCmipManagedObjectInstanceId = _OpenViewCmipManagedObjectInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 15),
    _OpenViewCmipManagedObjectInstanceId_Type()
)
openViewCmipManagedObjectInstanceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewCmipManagedObjectInstanceId.setStatus("current")
_OpenViewEventUUID_Type = OctetString
_OpenViewEventUUID_Object = MibScalar
openViewEventUUID = _OpenViewEventUUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 16),
    _OpenViewEventUUID_Type()
)
openViewEventUUID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewEventUUID.setStatus("current")
_OpenViewEcsCorrelateEvUUID_Type = DisplayString
_OpenViewEcsCorrelateEvUUID_Object = MibScalar
openViewEcsCorrelateEvUUID = _OpenViewEcsCorrelateEvUUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 17),
    _OpenViewEcsCorrelateEvUUID_Type()
)
openViewEcsCorrelateEvUUID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewEcsCorrelateEvUUID.setStatus("current")
_OpenViewEcsNodeImportance_Type = DisplayString
_OpenViewEcsNodeImportance_Object = MibScalar
openViewEcsNodeImportance = _OpenViewEcsNodeImportance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 18),
    _OpenViewEcsNodeImportance_Type()
)
openViewEcsNodeImportance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openViewEcsNodeImportance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPOV-NNM-MIB",
    **{"OVTextString": OVTextString,
       "hp": hp,
       "nm": nm,
       "openView": openView,
       "hpOpenView": hpOpenView,
       "hpOVNNMTraps": hpOVNNMTraps,
       "openViewTrapVars": openViewTrapVars,
       "openViewSourceId": openViewSourceId,
       "openViewSourceName": openViewSourceName,
       "openViewObjectId": openViewObjectId,
       "openViewData": openViewData,
       "openViewSeverity": openViewSeverity,
       "openViewCategory": openViewCategory,
       "openViewFilter": openViewFilter,
       "openViewEntity": openViewEntity,
       "openViewAddress": openViewAddress,
       "openViewPid": openViewPid,
       "openViewCmipManagedObjectClass": openViewCmipManagedObjectClass,
       "openViewCmipEventTime": openViewCmipEventTime,
       "openViewCmipEventType": openViewCmipEventType,
       "openViewCmipEventInfo": openViewCmipEventInfo,
       "openViewCmipManagedObjectInstanceId": openViewCmipManagedObjectInstanceId,
       "openViewEventUUID": openViewEventUUID,
       "openViewEcsCorrelateEvUUID": openViewEcsCorrelateEvUUID,
       "openViewEcsNodeImportance": openViewEcsNodeImportance}
)
