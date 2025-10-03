# SNMP MIB module (TROPIC-GENERIC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-GENERIC-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:29 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnGenericNotificationMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnGenericNotificationMIB",
    "tnSystemModules")

(TnCondition,
 TnEntityType,
 TnTrapCategory) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCondition",
    "TnEntityType",
    "TnTrapCategory")


# MODULE-IDENTITY

tnGenericNotificationMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnGenericNotificationMibModule.setRevisions(
        ("2023-01-20 00:00",
         "2022-12-23 00:00",
         "2022-11-04 00:00",
         "2022-10-24 00:00",
         "2022-10-12 00:00",
         "2021-08-13 12:00",
         "2021-06-25 12:00",
         "2021-05-07 12:00",
         "2020-11-08 12:00",
         "2020-10-23 12:00",
         "2020-03-06 12:00",
         "2020-02-28 12:00",
         "2019-09-04 12:00",
         "2018-03-19 12:00",
         "2018-02-23 12:00",
         "2017-11-24 12:00",
         "2017-09-25 12:00",
         "2017-09-22 12:00",
         "2017-09-15 12:00",
         "2017-08-18 12:00",
         "2017-07-07 12:00",
         "2017-03-06 12:00",
         "2017-02-06 12:00",
         "2016-12-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicGenericTrapObjectValueType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8))
    )



# MIB Managed Objects in the order of their OIDs

_TnGenericTrapBuffer_ObjectIdentity = ObjectIdentity
tnGenericTrapBuffer = _TnGenericTrapBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1)
)
_TnGenericTrapBufferObjects_ObjectIdentity = ObjectIdentity
tnGenericTrapBufferObjects = _TnGenericTrapBufferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1)
)
_TnGenericTrapBufferTable_Object = MibTable
tnGenericTrapBufferTable = _TnGenericTrapBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnGenericTrapBufferTable.setStatus("current")
_TnGenericTrapBufferEntry_Object = MibTableRow
tnGenericTrapBufferEntry = _TnGenericTrapBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1)
)
tnGenericTrapBufferEntry.setIndexNames(
    (0, "TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapNumber"),
)
if mibBuilder.loadTexts:
    tnGenericTrapBufferEntry.setStatus("current")


class _TnGenericTrapNumber_Type(Unsigned32):
    """Custom type tnGenericTrapNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericTrapNumber_Type.__name__ = "Unsigned32"
_TnGenericTrapNumber_Object = MibTableColumn
tnGenericTrapNumber = _TnGenericTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 1),
    _TnGenericTrapNumber_Type()
)
tnGenericTrapNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGenericTrapNumber.setStatus("current")
_TnGenericTrapType_Type = ObjectIdentifier
_TnGenericTrapType_Object = MibTableColumn
tnGenericTrapType = _TnGenericTrapType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 2),
    _TnGenericTrapType_Type()
)
tnGenericTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapType.setStatus("current")
_TnGenericTrapObject_Type = ObjectIdentifier
_TnGenericTrapObject_Object = MibTableColumn
tnGenericTrapObject = _TnGenericTrapObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 3),
    _TnGenericTrapObject_Type()
)
tnGenericTrapObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObject.setStatus("current")
_TnGenericTrapObjectInstance_Type = SnmpAdminString
_TnGenericTrapObjectInstance_Object = MibTableColumn
tnGenericTrapObjectInstance = _TnGenericTrapObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 4),
    _TnGenericTrapObjectInstance_Type()
)
tnGenericTrapObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectInstance.setStatus("current")
_TnGenericTrapTime_Type = Unsigned32
_TnGenericTrapTime_Object = MibTableColumn
tnGenericTrapTime = _TnGenericTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 5),
    _TnGenericTrapTime_Type()
)
tnGenericTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapTime.setStatus("current")
_TnGenericTrapCategory_Type = TnTrapCategory
_TnGenericTrapCategory_Object = MibTableColumn
tnGenericTrapCategory = _TnGenericTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 6),
    _TnGenericTrapCategory_Type()
)
tnGenericTrapCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapCategory.setStatus("current")


class _TnGenericTrapDescr_Type(SnmpAdminString):
    """Custom type tnGenericTrapDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericTrapDescr_Type.__name__ = "SnmpAdminString"
_TnGenericTrapDescr_Object = MibTableColumn
tnGenericTrapDescr = _TnGenericTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 7),
    _TnGenericTrapDescr_Type()
)
tnGenericTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapDescr.setStatus("current")


class _TnGenericTrapData_Type(SnmpAdminString):
    """Custom type tnGenericTrapData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGenericTrapData_Type.__name__ = "SnmpAdminString"
_TnGenericTrapData_Object = MibTableColumn
tnGenericTrapData = _TnGenericTrapData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 8),
    _TnGenericTrapData_Type()
)
tnGenericTrapData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapData.setStatus("current")
_TnGenericTrapServiceAffecting_Type = TruthValue
_TnGenericTrapServiceAffecting_Object = MibTableColumn
tnGenericTrapServiceAffecting = _TnGenericTrapServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 9),
    _TnGenericTrapServiceAffecting_Type()
)
tnGenericTrapServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapServiceAffecting.setStatus("current")
_TnGenericTrapCondition_Type = TnCondition
_TnGenericTrapCondition_Object = MibTableColumn
tnGenericTrapCondition = _TnGenericTrapCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 10),
    _TnGenericTrapCondition_Type()
)
tnGenericTrapCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapCondition.setStatus("current")
_TnGenericTrapObjectValueType_Type = TropicGenericTrapObjectValueType
_TnGenericTrapObjectValueType_Object = MibTableColumn
tnGenericTrapObjectValueType = _TnGenericTrapObjectValueType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 11),
    _TnGenericTrapObjectValueType_Type()
)
tnGenericTrapObjectValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectValueType.setStatus("current")
_TnGenericTrapObjectCounter32Val_Type = Counter32
_TnGenericTrapObjectCounter32Val_Object = MibTableColumn
tnGenericTrapObjectCounter32Val = _TnGenericTrapObjectCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 12),
    _TnGenericTrapObjectCounter32Val_Type()
)
tnGenericTrapObjectCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectCounter32Val.setStatus("current")
_TnGenericTrapObjectUnsigned32Val_Type = Unsigned32
_TnGenericTrapObjectUnsigned32Val_Object = MibTableColumn
tnGenericTrapObjectUnsigned32Val = _TnGenericTrapObjectUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 13),
    _TnGenericTrapObjectUnsigned32Val_Type()
)
tnGenericTrapObjectUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectUnsigned32Val.setStatus("current")
_TnGenericTrapObjectTimeTicksVal_Type = TimeTicks
_TnGenericTrapObjectTimeTicksVal_Object = MibTableColumn
tnGenericTrapObjectTimeTicksVal = _TnGenericTrapObjectTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 14),
    _TnGenericTrapObjectTimeTicksVal_Type()
)
tnGenericTrapObjectTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectTimeTicksVal.setStatus("current")
_TnGenericTrapObjectInteger32Val_Type = Integer32
_TnGenericTrapObjectInteger32Val_Object = MibTableColumn
tnGenericTrapObjectInteger32Val = _TnGenericTrapObjectInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 15),
    _TnGenericTrapObjectInteger32Val_Type()
)
tnGenericTrapObjectInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectInteger32Val.setStatus("current")
_TnGenericTrapObjectOctetStringVal_Type = OctetString
_TnGenericTrapObjectOctetStringVal_Object = MibTableColumn
tnGenericTrapObjectOctetStringVal = _TnGenericTrapObjectOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 16),
    _TnGenericTrapObjectOctetStringVal_Type()
)
tnGenericTrapObjectOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectOctetStringVal.setStatus("current")
_TnGenericTrapObjectIpAddressVal_Type = IpAddress
_TnGenericTrapObjectIpAddressVal_Object = MibTableColumn
tnGenericTrapObjectIpAddressVal = _TnGenericTrapObjectIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 17),
    _TnGenericTrapObjectIpAddressVal_Type()
)
tnGenericTrapObjectIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectIpAddressVal.setStatus("current")
_TnGenericTrapObjectOidVal_Type = ObjectIdentifier
_TnGenericTrapObjectOidVal_Object = MibTableColumn
tnGenericTrapObjectOidVal = _TnGenericTrapObjectOidVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 18),
    _TnGenericTrapObjectOidVal_Type()
)
tnGenericTrapObjectOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectOidVal.setStatus("current")
_TnGenericTrapObjectCounter64Val_Type = Counter64
_TnGenericTrapObjectCounter64Val_Object = MibTableColumn
tnGenericTrapObjectCounter64Val = _TnGenericTrapObjectCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 19),
    _TnGenericTrapObjectCounter64Val_Type()
)
tnGenericTrapObjectCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapObjectCounter64Val.setStatus("current")
_TnGenericTrapDateAndTime_Type = DateAndTime
_TnGenericTrapDateAndTime_Object = MibTableColumn
tnGenericTrapDateAndTime = _TnGenericTrapDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 20),
    _TnGenericTrapDateAndTime_Type()
)
tnGenericTrapDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapDateAndTime.setStatus("current")
_TnGenericTrapConfigurationChangeCounter_Type = Unsigned32
_TnGenericTrapConfigurationChangeCounter_Object = MibTableColumn
tnGenericTrapConfigurationChangeCounter = _TnGenericTrapConfigurationChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 21),
    _TnGenericTrapConfigurationChangeCounter_Type()
)
tnGenericTrapConfigurationChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapConfigurationChangeCounter.setStatus("current")
_TnGenericTrapEntityType_Type = TnEntityType
_TnGenericTrapEntityType_Object = MibTableColumn
tnGenericTrapEntityType = _TnGenericTrapEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 1, 1, 22),
    _TnGenericTrapEntityType_Type()
)
tnGenericTrapEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericTrapEntityType.setStatus("current")


class _TnGenericLastIssuedTrapNumber_Type(Unsigned32):
    """Custom type tnGenericLastIssuedTrapNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnGenericLastIssuedTrapNumber_Type.__name__ = "Unsigned32"
_TnGenericLastIssuedTrapNumber_Object = MibScalar
tnGenericLastIssuedTrapNumber = _TnGenericLastIssuedTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 2),
    _TnGenericLastIssuedTrapNumber_Type()
)
tnGenericLastIssuedTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGenericLastIssuedTrapNumber.setStatus("current")
_TnGenericTrapNumberResetToBeHandled_Type = TruthValue
_TnGenericTrapNumberResetToBeHandled_Object = MibScalar
tnGenericTrapNumberResetToBeHandled = _TnGenericTrapNumberResetToBeHandled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 1, 3),
    _TnGenericTrapNumberResetToBeHandled_Type()
)
tnGenericTrapNumberResetToBeHandled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnGenericTrapNumberResetToBeHandled.setStatus("current")
_TnGenericTrapBufferConformance_ObjectIdentity = ObjectIdentity
tnGenericTrapBufferConformance = _TnGenericTrapBufferConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 2)
)
_TnGenericTrapBufferCompliances_ObjectIdentity = ObjectIdentity
tnGenericTrapBufferCompliances = _TnGenericTrapBufferCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 2, 1)
)
_TnGenericTrapBufferGroups_ObjectIdentity = ObjectIdentity
tnGenericTrapBufferGroups = _TnGenericTrapBufferGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 2, 2)
)
_TnGenericTrap_ObjectIdentity = ObjectIdentity
tnGenericTrap = _TnGenericTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2)
)
_TnGenericTrapNotifs_ObjectIdentity = ObjectIdentity
tnGenericTrapNotifs = _TnGenericTrapNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 0)
)
_TnGenericTrapObjects_ObjectIdentity = ObjectIdentity
tnGenericTrapObjects = _TnGenericTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 1)
)
_TnGenericTrapSeqNumber_Type = Unsigned32
_TnGenericTrapSeqNumber_Object = MibScalar
tnGenericTrapSeqNumber = _TnGenericTrapSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 1, 1),
    _TnGenericTrapSeqNumber_Type()
)
tnGenericTrapSeqNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnGenericTrapSeqNumber.setStatus("current")


class _TnGenericTrapOthOdukApsAction_Type(Integer32):
    """Custom type tnGenericTrapOthOdukApsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2),
          ("update", 3),
          ("convertToProt", 4),
          ("convertToUnprot", 5),
          ("noCommand", 6),
          ("convertToUnprotFroming", 7))
    )


_TnGenericTrapOthOdukApsAction_Type.__name__ = "Integer32"
_TnGenericTrapOthOdukApsAction_Object = MibScalar
tnGenericTrapOthOdukApsAction = _TnGenericTrapOthOdukApsAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 1, 2),
    _TnGenericTrapOthOdukApsAction_Type()
)
tnGenericTrapOthOdukApsAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnGenericTrapOthOdukApsAction.setStatus("current")
_TnGenericTrapOthOdukApsFromedIfIndex_Type = Integer32
_TnGenericTrapOthOdukApsFromedIfIndex_Object = MibScalar
tnGenericTrapOthOdukApsFromedIfIndex = _TnGenericTrapOthOdukApsFromedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 1, 3),
    _TnGenericTrapOthOdukApsFromedIfIndex_Type()
)
tnGenericTrapOthOdukApsFromedIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnGenericTrapOthOdukApsFromedIfIndex.setStatus("current")
_TnGenericTrapOthOdukApsFromedIfIndexLo_Type = Integer32
_TnGenericTrapOthOdukApsFromedIfIndexLo_Object = MibScalar
tnGenericTrapOthOdukApsFromedIfIndexLo = _TnGenericTrapOthOdukApsFromedIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 1, 4),
    _TnGenericTrapOthOdukApsFromedIfIndexLo_Type()
)
tnGenericTrapOthOdukApsFromedIfIndexLo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnGenericTrapOthOdukApsFromedIfIndexLo.setStatus("current")
_TnGenericTrapOthOdukApsFromingIfIndex_Type = Integer32
_TnGenericTrapOthOdukApsFromingIfIndex_Object = MibScalar
tnGenericTrapOthOdukApsFromingIfIndex = _TnGenericTrapOthOdukApsFromingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 1, 5),
    _TnGenericTrapOthOdukApsFromingIfIndex_Type()
)
tnGenericTrapOthOdukApsFromingIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnGenericTrapOthOdukApsFromingIfIndex.setStatus("current")
_TnGenericTrapOthOdukApsFromingIfIndexLo_Type = Integer32
_TnGenericTrapOthOdukApsFromingIfIndexLo_Object = MibScalar
tnGenericTrapOthOdukApsFromingIfIndexLo = _TnGenericTrapOthOdukApsFromingIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 1, 6),
    _TnGenericTrapOthOdukApsFromingIfIndexLo_Type()
)
tnGenericTrapOthOdukApsFromingIfIndexLo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnGenericTrapOthOdukApsFromingIfIndexLo.setStatus("current")
_TnGenericTrapConformance_ObjectIdentity = ObjectIdentity
tnGenericTrapConformance = _TnGenericTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2)
)
_TnGenericTrapCompliances_ObjectIdentity = ObjectIdentity
tnGenericTrapCompliances = _TnGenericTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2, 1)
)
_TnGenericTrapGroups_ObjectIdentity = ObjectIdentity
tnGenericTrapGroups = _TnGenericTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2, 2)
)
_TnGenericAlarm_ObjectIdentity = ObjectIdentity
tnGenericAlarm = _TnGenericAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3)
)
_TnGenericAlarmNotifs_ObjectIdentity = ObjectIdentity
tnGenericAlarmNotifs = _TnGenericAlarmNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0)
)
_TnGenericAlarmConformance_ObjectIdentity = ObjectIdentity
tnGenericAlarmConformance = _TnGenericAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 2)
)
_TnGenericAlarmCompliances_ObjectIdentity = ObjectIdentity
tnGenericAlarmCompliances = _TnGenericAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 2, 1)
)
_TnGenericAlarmGroups_ObjectIdentity = ObjectIdentity
tnGenericAlarmGroups = _TnGenericAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 2, 2)
)
_TnGenericEvent_ObjectIdentity = ObjectIdentity
tnGenericEvent = _TnGenericEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4)
)
_TnGenericEventNotifs_ObjectIdentity = ObjectIdentity
tnGenericEventNotifs = _TnGenericEventNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0)
)
_TnGenericEventConformance_ObjectIdentity = ObjectIdentity
tnGenericEventConformance = _TnGenericEventConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 2)
)
_TnGenericEventCompliances_ObjectIdentity = ObjectIdentity
tnGenericEventCompliances = _TnGenericEventCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 2, 1)
)
_TnGenericEventGroups_ObjectIdentity = ObjectIdentity
tnGenericEventGroups = _TnGenericEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 2, 2)
)
_TnGenericScalar_ObjectIdentity = ObjectIdentity
tnGenericScalar = _TnGenericScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5)
)
_TnGenericScalarNotifs_ObjectIdentity = ObjectIdentity
tnGenericScalarNotifs = _TnGenericScalarNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5, 0)
)
_TnGenericScalarConformance_ObjectIdentity = ObjectIdentity
tnGenericScalarConformance = _TnGenericScalarConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5, 2)
)
_TnGenericScalarCompliances_ObjectIdentity = ObjectIdentity
tnGenericScalarCompliances = _TnGenericScalarCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5, 2, 1)
)
_TnGenericScalarGroups_ObjectIdentity = ObjectIdentity
tnGenericScalarGroups = _TnGenericScalarGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5, 2, 2)
)
_TnGenericInterface_ObjectIdentity = ObjectIdentity
tnGenericInterface = _TnGenericInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6)
)
_TnGenericInterfaceNotifs_ObjectIdentity = ObjectIdentity
tnGenericInterfaceNotifs = _TnGenericInterfaceNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 0)
)
_TnGenericInterfaceConformance_ObjectIdentity = ObjectIdentity
tnGenericInterfaceConformance = _TnGenericInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 2)
)
_TnGenericInterfaceCompliances_ObjectIdentity = ObjectIdentity
tnGenericInterfaceCompliances = _TnGenericInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 2, 1)
)
_TnGenericInterfaceGroups_ObjectIdentity = ObjectIdentity
tnGenericInterfaceGroups = _TnGenericInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 2, 2)
)
_TnGenericOptIf_ObjectIdentity = ObjectIdentity
tnGenericOptIf = _TnGenericOptIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7)
)
_TnGenericOptIfNotifs_ObjectIdentity = ObjectIdentity
tnGenericOptIfNotifs = _TnGenericOptIfNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7, 0)
)
_TnGenericOptIfConformance_ObjectIdentity = ObjectIdentity
tnGenericOptIfConformance = _TnGenericOptIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7, 2)
)
_TnGenericOptIfCompliances_ObjectIdentity = ObjectIdentity
tnGenericOptIfCompliances = _TnGenericOptIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7, 2, 1)
)
_TnGenericOptIfGroups_ObjectIdentity = ObjectIdentity
tnGenericOptIfGroups = _TnGenericOptIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7, 2, 2)
)
_TnGenericTnAccessPort_ObjectIdentity = ObjectIdentity
tnGenericTnAccessPort = _TnGenericTnAccessPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8)
)
_TnGenericTnAccessPortNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnAccessPortNotifs = _TnGenericTnAccessPortNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 0)
)
_TnGenericTnAccessPortConformance_ObjectIdentity = ObjectIdentity
tnGenericTnAccessPortConformance = _TnGenericTnAccessPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 2)
)
_TnGenericTnAccessPortCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnAccessPortCompliances = _TnGenericTnAccessPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 2, 1)
)
_TnGenericTnAccessPortGroups_ObjectIdentity = ObjectIdentity
tnGenericTnAccessPortGroups = _TnGenericTnAccessPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 2, 2)
)
_TnGenericTnOpticalPort_ObjectIdentity = ObjectIdentity
tnGenericTnOpticalPort = _TnGenericTnOpticalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9)
)
_TnGenericTnOpticalPortNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnOpticalPortNotifs = _TnGenericTnOpticalPortNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 0)
)
_TnGenericTnOpticalPortConformance_ObjectIdentity = ObjectIdentity
tnGenericTnOpticalPortConformance = _TnGenericTnOpticalPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 2)
)
_TnGenericTnOpticalPortCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnOpticalPortCompliances = _TnGenericTnOpticalPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 2, 1)
)
_TnGenericTnOpticalPortGroups_ObjectIdentity = ObjectIdentity
tnGenericTnOpticalPortGroups = _TnGenericTnOpticalPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 2, 2)
)
_TnGenericTnOtuOdu_ObjectIdentity = ObjectIdentity
tnGenericTnOtuOdu = _TnGenericTnOtuOdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10)
)
_TnGenericTnOtuOduNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnOtuOduNotifs = _TnGenericTnOtuOduNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10, 0)
)
_TnGenericTnOtuOduConformance_ObjectIdentity = ObjectIdentity
tnGenericTnOtuOduConformance = _TnGenericTnOtuOduConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10, 2)
)
_TnGenericTnOtuOduCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnOtuOduCompliances = _TnGenericTnOtuOduCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10, 2, 1)
)
_TnGenericTnOtuOduGroups_ObjectIdentity = ObjectIdentity
tnGenericTnOtuOduGroups = _TnGenericTnOtuOduGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10, 2, 2)
)
_TnGenericTnOth_ObjectIdentity = ObjectIdentity
tnGenericTnOth = _TnGenericTnOth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11)
)
_TnGenericTnOthNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnOthNotifs = _TnGenericTnOthNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0)
)
_TnGenericTnOthConformance_ObjectIdentity = ObjectIdentity
tnGenericTnOthConformance = _TnGenericTnOthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 2)
)
_TnGenericTnOthCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnOthCompliances = _TnGenericTnOthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 2, 1)
)
_TnGenericTnOthGroups_ObjectIdentity = ObjectIdentity
tnGenericTnOthGroups = _TnGenericTnOthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 2, 2)
)
_TnGenericTnL1Service_ObjectIdentity = ObjectIdentity
tnGenericTnL1Service = _TnGenericTnL1Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12)
)
_TnGenericTnL1ServiceNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnL1ServiceNotifs = _TnGenericTnL1ServiceNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 0)
)
_TnGenericTnL1ServiceConformance_ObjectIdentity = ObjectIdentity
tnGenericTnL1ServiceConformance = _TnGenericTnL1ServiceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 2)
)
_TnGenericTnL1ServiceCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnL1ServiceCompliances = _TnGenericTnL1ServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 2, 1)
)
_TnGenericTnL1ServiceGroups_ObjectIdentity = ObjectIdentity
tnGenericTnL1ServiceGroups = _TnGenericTnL1ServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 2, 2)
)
_TnGenericTnStatistics_ObjectIdentity = ObjectIdentity
tnGenericTnStatistics = _TnGenericTnStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13)
)
_TnGenericTnStatisticsNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnStatisticsNotifs = _TnGenericTnStatisticsNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 0)
)
_TnGenericTnStatisticsConformance_ObjectIdentity = ObjectIdentity
tnGenericTnStatisticsConformance = _TnGenericTnStatisticsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 2)
)
_TnGenericTnStatisticsCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnStatisticsCompliances = _TnGenericTnStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 2, 1)
)
_TnGenericTnStatisticsGroups_ObjectIdentity = ObjectIdentity
tnGenericTnStatisticsGroups = _TnGenericTnStatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 2, 2)
)
_TnGenericTnLag_ObjectIdentity = ObjectIdentity
tnGenericTnLag = _TnGenericTnLag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14)
)
_TnGenericTnLagNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnLagNotifs = _TnGenericTnLagNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 0)
)
_TnGenericTnLagConformance_ObjectIdentity = ObjectIdentity
tnGenericTnLagConformance = _TnGenericTnLagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 2)
)
_TnGenericTnLagCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnLagCompliances = _TnGenericTnLagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 2, 1)
)
_TnGenericTnLagGroups_ObjectIdentity = ObjectIdentity
tnGenericTnLagGroups = _TnGenericTnLagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 2, 2)
)
_TnGenericTnPmon_ObjectIdentity = ObjectIdentity
tnGenericTnPmon = _TnGenericTnPmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15)
)
_TnGenericTnPmonNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnPmonNotifs = _TnGenericTnPmonNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 0)
)
_TnGenericTnPmonConformance_ObjectIdentity = ObjectIdentity
tnGenericTnPmonConformance = _TnGenericTnPmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 2)
)
_TnGenericTnPmonCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnPmonCompliances = _TnGenericTnPmonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 2, 1)
)
_TnGenericTnPmonGroups_ObjectIdentity = ObjectIdentity
tnGenericTnPmonGroups = _TnGenericTnPmonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 2, 2)
)
_TnGenericTnPort_ObjectIdentity = ObjectIdentity
tnGenericTnPort = _TnGenericTnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16)
)
_TnGenericTnPortNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnPortNotifs = _TnGenericTnPortNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16, 0)
)
_TnGenericTnPortConformance_ObjectIdentity = ObjectIdentity
tnGenericTnPortConformance = _TnGenericTnPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16, 2)
)
_TnGenericTnPortCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnPortCompliances = _TnGenericTnPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16, 2, 1)
)
_TnGenericTnPortGroups_ObjectIdentity = ObjectIdentity
tnGenericTnPortGroups = _TnGenericTnPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16, 2, 2)
)
_TnGenericDot1agCfm_ObjectIdentity = ObjectIdentity
tnGenericDot1agCfm = _TnGenericDot1agCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17)
)
_TnGenericDot1agCfmNotifs_ObjectIdentity = ObjectIdentity
tnGenericDot1agCfmNotifs = _TnGenericDot1agCfmNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0)
)
_TnGenericDot1agCfmConformance_ObjectIdentity = ObjectIdentity
tnGenericDot1agCfmConformance = _TnGenericDot1agCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 2)
)
_TnGenericDot1agCfmCompliances_ObjectIdentity = ObjectIdentity
tnGenericDot1agCfmCompliances = _TnGenericDot1agCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 2, 1)
)
_TnGenericDot1agCfmGroups_ObjectIdentity = ObjectIdentity
tnGenericDot1agCfmGroups = _TnGenericDot1agCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 2, 2)
)
_TnGenericTnDot1agCfm_ObjectIdentity = ObjectIdentity
tnGenericTnDot1agCfm = _TnGenericTnDot1agCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18)
)
_TnGenericTnDot1agCfmNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnDot1agCfmNotifs = _TnGenericTnDot1agCfmNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 0)
)
_TnGenericTnDot1agCfmConformance_ObjectIdentity = ObjectIdentity
tnGenericTnDot1agCfmConformance = _TnGenericTnDot1agCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 2)
)
_TnGenericTnDot1agCfmCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnDot1agCfmCompliances = _TnGenericTnDot1agCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 2, 1)
)
_TnGenericTnDot1agCfmGroups_ObjectIdentity = ObjectIdentity
tnGenericTnDot1agCfmGroups = _TnGenericTnDot1agCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 2, 2)
)
_TnGenericTnOamTest_ObjectIdentity = ObjectIdentity
tnGenericTnOamTest = _TnGenericTnOamTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19)
)
_TnGenericTnOamTestNotifs_ObjectIdentity = ObjectIdentity
tnGenericTnOamTestNotifs = _TnGenericTnOamTestNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 0)
)
_TnGenericTnOamTestConformance_ObjectIdentity = ObjectIdentity
tnGenericTnOamTestConformance = _TnGenericTnOamTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 2)
)
_TnGenericTnOamTestCompliances_ObjectIdentity = ObjectIdentity
tnGenericTnOamTestCompliances = _TnGenericTnOamTestCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 2, 1)
)
_TnGenericTnOamTestGroups_ObjectIdentity = ObjectIdentity
tnGenericTnOamTestGroups = _TnGenericTnOamTestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 2, 2)
)
_TnGenericRadius_ObjectIdentity = ObjectIdentity
tnGenericRadius = _TnGenericRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20)
)
_TnGenericRadiusNotifs_ObjectIdentity = ObjectIdentity
tnGenericRadiusNotifs = _TnGenericRadiusNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 0)
)
_TnGenericRadiusConformance_ObjectIdentity = ObjectIdentity
tnGenericRadiusConformance = _TnGenericRadiusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 2)
)
_TnGenericRadiusCompliances_ObjectIdentity = ObjectIdentity
tnGenericRadiusCompliances = _TnGenericRadiusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 2, 1)
)
_TnGenericRadiusGroups_ObjectIdentity = ObjectIdentity
tnGenericRadiusGroups = _TnGenericRadiusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 2, 2)
)
_TnGenericSyslog_ObjectIdentity = ObjectIdentity
tnGenericSyslog = _TnGenericSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21)
)
_TnGenericSyslogNotifs_ObjectIdentity = ObjectIdentity
tnGenericSyslogNotifs = _TnGenericSyslogNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 0)
)
_TnGenericSyslogConformance_ObjectIdentity = ObjectIdentity
tnGenericSyslogConformance = _TnGenericSyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 2)
)
_TnGenericSyslogCompliances_ObjectIdentity = ObjectIdentity
tnGenericSyslogCompliances = _TnGenericSyslogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 2, 1)
)
_TnGenericSyslogGroups_ObjectIdentity = ObjectIdentity
tnGenericSyslogGroups = _TnGenericSyslogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 2, 2)
)
_TnGenericTransferPMDiscovery_ObjectIdentity = ObjectIdentity
tnGenericTransferPMDiscovery = _TnGenericTransferPMDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22)
)
_TnGenericTransferPMDiscoveryNotifs_ObjectIdentity = ObjectIdentity
tnGenericTransferPMDiscoveryNotifs = _TnGenericTransferPMDiscoveryNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 0)
)
_TnGenericTransferPMDiscoveryConformance_ObjectIdentity = ObjectIdentity
tnGenericTransferPMDiscoveryConformance = _TnGenericTransferPMDiscoveryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 2)
)
_TnGenericTransferPMDiscoveryCompliances_ObjectIdentity = ObjectIdentity
tnGenericTransferPMDiscoveryCompliances = _TnGenericTransferPMDiscoveryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 2, 1)
)
_TnGenericTransferPMDiscoveryGroups_ObjectIdentity = ObjectIdentity
tnGenericTransferPMDiscoveryGroups = _TnGenericTransferPMDiscoveryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 2, 2)
)

# Managed Objects groups

tnGenericTrapBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 2, 2, 1)
)
tnGenericTrapBufferGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLastIssuedTrapNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapNumberResetToBeHandled"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTrapBufferGroup.setStatus("current")

tnGenericTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2, 2, 1)
)
tnGenericTrapGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsAction"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromedIfIndex"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromedIfIndexLo"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromingIfIndex"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromingIfIndexLo"))
)
if mibBuilder.loadTexts:
    tnGenericTrapGroup.setStatus("current")


# Notification objects

tnGenericConfigurationChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 0, 1)
)
tnGenericConfigurationChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericConfigurationChangeNotif.setStatus(
        "current"
    )

tnGenericStateChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 0, 2)
)
tnGenericStateChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericStateChangeNotif.setStatus(
        "current"
    )

tnGenericTreeUpdateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 0, 3)
)
tnGenericTreeUpdateNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTreeUpdateNotif.setStatus(
        "current"
    )

tnGenericBackwardDefectIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 1)
)
tnGenericBackwardDefectIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericBackwardDefectIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericBackwardDefectIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 2)
)
tnGenericBackwardDefectIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericBackwardDefectIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericOduBackwardDefectIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 3)
)
tnGenericOduBackwardDefectIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduBackwardDefectIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericOduBackwardDefectIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 4)
)
tnGenericOduBackwardDefectIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduBackwardDefectIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericTcmBackwardDefectIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 5)
)
tnGenericTcmBackwardDefectIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmBackwardDefectIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmBackwardDefectIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 6)
)
tnGenericTcmBackwardDefectIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmBackwardDefectIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericCommDownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 7)
)
tnGenericCommDownRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCommDownRaisedNotif.setStatus(
        "current"
    )

tnGenericCommDownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 8)
)
tnGenericCommDownClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCommDownClearedNotif.setStatus(
        "current"
    )

tnGenericSignalDegradeRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 9)
)
tnGenericSignalDegradeRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSignalDegradeRaisedNotif.setStatus(
        "current"
    )

tnGenericSignalDegradeClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 10)
)
tnGenericSignalDegradeClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSignalDegradeClearedNotif.setStatus(
        "current"
    )

tnGenericOduSignalDegradeRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 11)
)
tnGenericOduSignalDegradeRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduSignalDegradeRaisedNotif.setStatus(
        "current"
    )

tnGenericOduSignalDegradeClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 12)
)
tnGenericOduSignalDegradeClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduSignalDegradeClearedNotif.setStatus(
        "current"
    )

tnGenericTcmSignalDegradeRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 13)
)
tnGenericTcmSignalDegradeRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmSignalDegradeRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmSignalDegradeClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 14)
)
tnGenericTcmSignalDegradeClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmSignalDegradeClearedNotif.setStatus(
        "current"
    )

tnGenericBoardEqptRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 15)
)
tnGenericBoardEqptRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericBoardEqptRaisedNotif.setStatus(
        "current"
    )

tnGenericBoardEqptClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 16)
)
tnGenericBoardEqptClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericBoardEqptClearedNotif.setStatus(
        "current"
    )

tnGenericEqptPortRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 17)
)
tnGenericEqptPortRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericEqptPortRaisedNotif.setStatus(
        "current"
    )

tnGenericEqptPortClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 18)
)
tnGenericEqptPortClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericEqptPortClearedNotif.setStatus(
        "current"
    )

tnGenericIntTempHighRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 19)
)
tnGenericIntTempHighRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericIntTempHighRaisedNotif.setStatus(
        "current"
    )

tnGenericIntTempHighClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 20)
)
tnGenericIntTempHighClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericIntTempHighClearedNotif.setStatus(
        "current"
    )

tnGenericLockedIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 21)
)
tnGenericLockedIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLockedIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericLockedIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 22)
)
tnGenericLockedIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLockedIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericTcmLockedIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 23)
)
tnGenericTcmLockedIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmLockedIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmLockedIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 24)
)
tnGenericTcmLockedIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmLockedIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericDwLossOfFrameRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 25)
)
tnGenericDwLossOfFrameRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericDwLossOfFrameRaisedNotif.setStatus(
        "current"
    )

tnGenericDwLossOfFrameClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 26)
)
tnGenericDwLossOfFrameClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericDwLossOfFrameClearedNotif.setStatus(
        "current"
    )

tnGenericDwLossOfMultiFrameRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 27)
)
tnGenericDwLossOfMultiFrameRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericDwLossOfMultiFrameRaisedNotif.setStatus(
        "current"
    )

tnGenericDwLossOfMultiFrameClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 28)
)
tnGenericDwLossOfMultiFrameClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericDwLossOfMultiFrameClearedNotif.setStatus(
        "current"
    )

tnGenericLossOfSignalRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 29)
)
tnGenericLossOfSignalRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLossOfSignalRaisedNotif.setStatus(
        "current"
    )

tnGenericLossOfSignalClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 30)
)
tnGenericLossOfSignalClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLossOfSignalClearedNotif.setStatus(
        "current"
    )

tnGenericTcmLossofTandemConnectionRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 31)
)
tnGenericTcmLossofTandemConnectionRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmLossofTandemConnectionRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmLossofTandemConnectionClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 32)
)
tnGenericTcmLossofTandemConnectionClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmLossofTandemConnectionClearedNotif.setStatus(
        "current"
    )

tnGenericInMaintenanceRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 33)
)
tnGenericInMaintenanceRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericInMaintenanceRaisedNotif.setStatus(
        "current"
    )

tnGenericInMaintenanceClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 34)
)
tnGenericInMaintenanceClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericInMaintenanceClearedNotif.setStatus(
        "current"
    )

tnGenericOpticsModuleMismatchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 35)
)
tnGenericOpticsModuleMismatchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticsModuleMismatchRaisedNotif.setStatus(
        "current"
    )

tnGenericOpticsModuleMismatchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 36)
)
tnGenericOpticsModuleMismatchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticsModuleMismatchClearedNotif.setStatus(
        "current"
    )

tnGenericOpenConnectionIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 37)
)
tnGenericOpenConnectionIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpenConnectionIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericOpenConnectionIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 38)
)
tnGenericOpenConnectionIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpenConnectionIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericTcmOpenConnectionIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 39)
)
tnGenericTcmOpenConnectionIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmOpenConnectionIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmOpenConnectionIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 40)
)
tnGenericTcmOpenConnectionIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmOpenConnectionIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericReplUnitMissMODRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 41)
)
tnGenericReplUnitMissMODRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericReplUnitMissMODRaisedNotif.setStatus(
        "current"
    )

tnGenericReplUnitMissMODClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 42)
)
tnGenericReplUnitMissMODClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericReplUnitMissMODClearedNotif.setStatus(
        "current"
    )

tnGenericServerSignalFailureEgressRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 43)
)
tnGenericServerSignalFailureEgressRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericServerSignalFailureEgressRaisedNotif.setStatus(
        "current"
    )

tnGenericServerSignalFailureEgressClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 44)
)
tnGenericServerSignalFailureEgressClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericServerSignalFailureEgressClearedNotif.setStatus(
        "current"
    )

tnGenericServerSignalFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 45)
)
tnGenericServerSignalFailureRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericServerSignalFailureRaisedNotif.setStatus(
        "current"
    )

tnGenericServerSignalFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 46)
)
tnGenericServerSignalFailureClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericServerSignalFailureClearedNotif.setStatus(
        "current"
    )

tnGenericOduServerSignalFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 47)
)
tnGenericOduServerSignalFailureRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduServerSignalFailureRaisedNotif.setStatus(
        "current"
    )

tnGenericOduServerSignalFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 48)
)
tnGenericOduServerSignalFailureClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduServerSignalFailureClearedNotif.setStatus(
        "current"
    )

tnGenericTcmServerSignalFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 49)
)
tnGenericTcmServerSignalFailureRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmServerSignalFailureRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmServerSignalFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 50)
)
tnGenericTcmServerSignalFailureClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmServerSignalFailureClearedNotif.setStatus(
        "current"
    )

tnGenericCardInitializingRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 51)
)
tnGenericCardInitializingRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardInitializingRaisedNotif.setStatus(
        "current"
    )

tnGenericCardInitializingClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 52)
)
tnGenericCardInitializingClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardInitializingClearedNotif.setStatus(
        "current"
    )

tnGenericTBbeOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 53)
)
tnGenericTBbeOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTBbeOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 54)
)
tnGenericTBbeOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTBbeOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 55)
)
tnGenericTBbeOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTBbeOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 56)
)
tnGenericTBbeOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTBbeOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 57)
)
tnGenericTBbeOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTBbeOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 58)
)
tnGenericTBbeOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTBbeOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 59)
)
tnGenericTBbeOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTBbeOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 60)
)
tnGenericTBbeOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTBbeTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 61)
)
tnGenericTBbeTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTBbeTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 62)
)
tnGenericTBbeTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTBbeTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 63)
)
tnGenericTBbeTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTBbeTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 64)
)
tnGenericTBbeTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBbeTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTEsOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 65)
)
tnGenericTEsOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 66)
)
tnGenericTEsOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTEsOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 67)
)
tnGenericTEsOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 68)
)
tnGenericTEsOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTEsOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 69)
)
tnGenericTEsOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 70)
)
tnGenericTEsOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTEsOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 71)
)
tnGenericTEsOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 72)
)
tnGenericTEsOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTEsTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 73)
)
tnGenericTEsTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 74)
)
tnGenericTEsTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTEsTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 75)
)
tnGenericTEsTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 76)
)
tnGenericTEsTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFecc15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 77)
)
tnGenericTFecc15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFecc15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFecc15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 78)
)
tnGenericTFecc15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFecc15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFecc1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 79)
)
tnGenericTFecc1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFecc1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFecc1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 80)
)
tnGenericTFecc1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFecc1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTrailTraceIdentifierMismatchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 81)
)
tnGenericTrailTraceIdentifierMismatchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTrailTraceIdentifierMismatchRaisedNotif.setStatus(
        "current"
    )

tnGenericTrailTraceIdentifierMismatchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 82)
)
tnGenericTrailTraceIdentifierMismatchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTrailTraceIdentifierMismatchClearedNotif.setStatus(
        "current"
    )

tnGenericOduTrailTraceIdentifierMismatchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 83)
)
tnGenericOduTrailTraceIdentifierMismatchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduTrailTraceIdentifierMismatchRaisedNotif.setStatus(
        "current"
    )

tnGenericOduTrailTraceIdentifierMismatchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 84)
)
tnGenericOduTrailTraceIdentifierMismatchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduTrailTraceIdentifierMismatchClearedNotif.setStatus(
        "current"
    )

tnGenericTcmTrailTraceIdentifierMismatchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 85)
)
tnGenericTcmTrailTraceIdentifierMismatchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmTrailTraceIdentifierMismatchRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmTrailTraceIdentifierMismatchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 86)
)
tnGenericTcmTrailTraceIdentifierMismatchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmTrailTraceIdentifierMismatchClearedNotif.setStatus(
        "current"
    )

tnGenericOpticsModuleUnknownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 87)
)
tnGenericOpticsModuleUnknownRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticsModuleUnknownRaisedNotif.setStatus(
        "current"
    )

tnGenericOpticsModuleUnknownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 88)
)
tnGenericOpticsModuleUnknownClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticsModuleUnknownClearedNotif.setStatus(
        "current"
    )

tnGenericUruORaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 89)
)
tnGenericUruORaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUruORaisedNotif.setStatus(
        "current"
    )

tnGenericUruOClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 90)
)
tnGenericUruOClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUruOClearedNotif.setStatus(
        "current"
    )

tnGenericUruPRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 91)
)
tnGenericUruPRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUruPRaisedNotif.setStatus(
        "current"
    )

tnGenericUruPClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 92)
)
tnGenericUruPClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUruPClearedNotif.setStatus(
        "current"
    )

tnGenericOduUruPRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 93)
)
tnGenericOduUruPRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduUruPRaisedNotif.setStatus(
        "current"
    )

tnGenericOduUruPClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 94)
)
tnGenericOduUruPClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduUruPClearedNotif.setStatus(
        "current"
    )

tnGenericTcmUruPRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 95)
)
tnGenericTcmUruPRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmUruPRaisedNotif.setStatus(
        "current"
    )

tnGenericTcmUruPClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 96)
)
tnGenericTcmUruPClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTcmUruPClearedNotif.setStatus(
        "current"
    )

tnGenericApsLockoutOfProtectionRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 97)
)
tnGenericApsLockoutOfProtectionRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsLockoutOfProtectionRaisedNotif.setStatus(
        "current"
    )

tnGenericApsLockoutOfProtectionClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 98)
)
tnGenericApsLockoutOfProtectionClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsLockoutOfProtectionClearedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingForceSwitchedBackToWorkingRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 99)
)
tnGenericApsWorkingForceSwitchedBackToWorkingRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingForceSwitchedBackToWorkingRaisedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingForceSwitchedBackToWorkingClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 100)
)
tnGenericApsWorkingForceSwitchedBackToWorkingClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingForceSwitchedBackToWorkingClearedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingForceSwitchedToProtectRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 101)
)
tnGenericApsWorkingForceSwitchedToProtectRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingForceSwitchedToProtectRaisedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingForceSwitchedToProtectClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 102)
)
tnGenericApsWorkingForceSwitchedToProtectClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingForceSwitchedToProtectClearedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingManualSwitchedBackToWorkingRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 103)
)
tnGenericApsWorkingManualSwitchedBackToWorkingRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingManualSwitchedBackToWorkingRaisedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingManualSwitchedBackToWorkingClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 104)
)
tnGenericApsWorkingManualSwitchedBackToWorkingClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingManualSwitchedBackToWorkingClearedNotif.setStatus(
        "current"
    )

tnGenericApsSwitchedToWorkRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 105)
)
tnGenericApsSwitchedToWorkRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsSwitchedToWorkRaisedNotif.setStatus(
        "current"
    )

tnGenericApsSwitchedToWorkClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 106)
)
tnGenericApsSwitchedToWorkClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsSwitchedToWorkClearedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingSwitchedToProtectRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 107)
)
tnGenericApsWorkingSwitchedToProtectRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingSwitchedToProtectRaisedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingSwitchedToProtectClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 108)
)
tnGenericApsWorkingSwitchedToProtectClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingSwitchedToProtectClearedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingManualSwitchedToProtectRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 109)
)
tnGenericApsWorkingManualSwitchedToProtectRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingManualSwitchedToProtectRaisedNotif.setStatus(
        "current"
    )

tnGenericApsWorkingManualSwitchedToProtectClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 110)
)
tnGenericApsWorkingManualSwitchedToProtectClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsWorkingManualSwitchedToProtectClearedNotif.setStatus(
        "current"
    )

tnGenericWtrRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 111)
)
tnGenericWtrRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericWtrRaisedNotif.setStatus(
        "current"
    )

tnGenericWtrClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 112)
)
tnGenericWtrClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericWtrClearedNotif.setStatus(
        "current"
    )

tnGenericTSesOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 113)
)
tnGenericTSesOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 114)
)
tnGenericTSesOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTSesOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 115)
)
tnGenericTSesOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 116)
)
tnGenericTSesOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTSesOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 117)
)
tnGenericTSesOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 118)
)
tnGenericTSesOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTSesOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 119)
)
tnGenericTSesOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 120)
)
tnGenericTSesOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTSesTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 121)
)
tnGenericTSesTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 122)
)
tnGenericTSesTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTSesTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 123)
)
tnGenericTSesTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 124)
)
tnGenericTSesTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTUasOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 125)
)
tnGenericTUasOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTUasOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 126)
)
tnGenericTUasOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTUasOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 127)
)
tnGenericTUasOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTUasOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 128)
)
tnGenericTUasOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTUasOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 129)
)
tnGenericTUasOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTUasOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 130)
)
tnGenericTUasOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTUasOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 131)
)
tnGenericTUasOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTUasOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 132)
)
tnGenericTUasOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTUasTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 133)
)
tnGenericTUasTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTUasTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 134)
)
tnGenericTUasTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTUasTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 135)
)
tnGenericTUasTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTUasTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 136)
)
tnGenericTUasTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTUasTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericApsBlockRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 137)
)
tnGenericApsBlockRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsBlockRaisedNotif.setStatus(
        "current"
    )

tnGenericApsBlockClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 138)
)
tnGenericApsBlockClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsBlockClearedNotif.setStatus(
        "current"
    )

tnGenericApsLOSyncRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 139)
)
tnGenericApsLOSyncRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsLOSyncRaisedNotif.setStatus(
        "current"
    )

tnGenericApsLOSyncClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 140)
)
tnGenericApsLOSyncClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsLOSyncClearedNotif.setStatus(
        "current"
    )

tnGenericApsLossOfServiceRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 141)
)
tnGenericApsLossOfServiceRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsLossOfServiceRaisedNotif.setStatus(
        "current"
    )

tnGenericApsLossOfServiceClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 142)
)
tnGenericApsLossOfServiceClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsLossOfServiceClearedNotif.setStatus(
        "current"
    )

tnGenericApsSuspendedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 143)
)
tnGenericApsSuspendedRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsSuspendedRaisedNotif.setStatus(
        "current"
    )

tnGenericApsSuspendedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 144)
)
tnGenericApsSuspendedClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericApsSuspendedClearedNotif.setStatus(
        "current"
    )

tnGenericAuditBlockRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 145)
)
tnGenericAuditBlockRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericAuditBlockRaisedNotif.setStatus(
        "current"
    )

tnGenericAuditBlockClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 146)
)
tnGenericAuditBlockClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericAuditBlockClearedNotif.setStatus(
        "current"
    )

tnGenericBreaker1BatteryFeedDownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 147)
)
tnGenericBreaker1BatteryFeedDownRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericBreaker1BatteryFeedDownRaisedNotif.setStatus(
        "current"
    )

tnGenericBreaker1BatteryFeedDownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 148)
)
tnGenericBreaker1BatteryFeedDownClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericBreaker1BatteryFeedDownClearedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm1RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 149)
)
tnGenericCabinAlarm1RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm1RaisedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm1ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 150)
)
tnGenericCabinAlarm1ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm1ClearedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm2RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 151)
)
tnGenericCabinAlarm2RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm2RaisedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm2ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 152)
)
tnGenericCabinAlarm2ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm2ClearedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm3RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 153)
)
tnGenericCabinAlarm3RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm3RaisedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm3ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 154)
)
tnGenericCabinAlarm3ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm3ClearedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm4RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 155)
)
tnGenericCabinAlarm4RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm4RaisedNotif.setStatus(
        "current"
    )

tnGenericCabinAlarm4ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 156)
)
tnGenericCabinAlarm4ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCabinAlarm4ClearedNotif.setStatus(
        "current"
    )

tnGenericCardBootRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 157)
)
tnGenericCardBootRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardBootRaisedNotif.setStatus(
        "current"
    )

tnGenericCardBootClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 158)
)
tnGenericCardBootClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardBootClearedNotif.setStatus(
        "current"
    )

tnGenericCardMissingRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 159)
)
tnGenericCardMissingRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardMissingRaisedNotif.setStatus(
        "current"
    )

tnGenericCardMissingClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 160)
)
tnGenericCardMissingClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardMissingClearedNotif.setStatus(
        "current"
    )

tnGenericCardUnknownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 161)
)
tnGenericCardUnknownRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardUnknownRaisedNotif.setStatus(
        "current"
    )

tnGenericCardUnknownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 162)
)
tnGenericCardUnknownClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardUnknownClearedNotif.setStatus(
        "current"
    )

tnGenericEqptDgrOchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 163)
)
tnGenericEqptDgrOchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericEqptDgrOchRaisedNotif.setStatus(
        "current"
    )

tnGenericEqptDgrOchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 164)
)
tnGenericEqptDgrOchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericEqptDgrOchClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm1RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 165)
)
tnGenericFrameAlarm1RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm1RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm1ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 166)
)
tnGenericFrameAlarm1ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm1ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm2RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 167)
)
tnGenericFrameAlarm2RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm2RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm2ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 168)
)
tnGenericFrameAlarm2ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm2ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm3RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 169)
)
tnGenericFrameAlarm3RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm3RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm3ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 170)
)
tnGenericFrameAlarm3ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm3ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm4RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 171)
)
tnGenericFrameAlarm4RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm4RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm4ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 172)
)
tnGenericFrameAlarm4ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm4ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm5RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 173)
)
tnGenericFrameAlarm5RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm5RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm5ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 174)
)
tnGenericFrameAlarm5ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm5ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm6RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 175)
)
tnGenericFrameAlarm6RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm6RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm6ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 176)
)
tnGenericFrameAlarm6ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm6ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm7RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 177)
)
tnGenericFrameAlarm7RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm7RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm7ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 178)
)
tnGenericFrameAlarm7ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm7ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm8RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 179)
)
tnGenericFrameAlarm8RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm8RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm8ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 180)
)
tnGenericFrameAlarm8ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm8ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm9RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 181)
)
tnGenericFrameAlarm9RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm9RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm9ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 182)
)
tnGenericFrameAlarm9ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm9ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm10RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 183)
)
tnGenericFrameAlarm10RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm10RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm10ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 184)
)
tnGenericFrameAlarm10ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm10ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm11RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 185)
)
tnGenericFrameAlarm11RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm11RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm11ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 186)
)
tnGenericFrameAlarm11ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm11ClearedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm12RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 187)
)
tnGenericFrameAlarm12RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm12RaisedNotif.setStatus(
        "current"
    )

tnGenericFrameAlarm12ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 188)
)
tnGenericFrameAlarm12ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFrameAlarm12ClearedNotif.setStatus(
        "current"
    )

tnGenericInterShelfLossofCommsRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 189)
)
tnGenericInterShelfLossofCommsRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericInterShelfLossofCommsRaisedNotif.setStatus(
        "current"
    )

tnGenericInterShelfLossofCommsClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 190)
)
tnGenericInterShelfLossofCommsClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericInterShelfLossofCommsClearedNotif.setStatus(
        "current"
    )

tnGenericInventoryErrModRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 191)
)
tnGenericInventoryErrModRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericInventoryErrModRaisedNotif.setStatus(
        "current"
    )

tnGenericInventoryErrModClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 192)
)
tnGenericInventoryErrModClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericInventoryErrModClearedNotif.setStatus(
        "current"
    )

tnGenericLineFacilityLoopbackActiveRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 193)
)
tnGenericLineFacilityLoopbackActiveRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLineFacilityLoopbackActiveRaisedNotif.setStatus(
        "current"
    )

tnGenericLineFacilityLoopbackActiveClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 194)
)
tnGenericLineFacilityLoopbackActiveClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLineFacilityLoopbackActiveClearedNotif.setStatus(
        "current"
    )

tnGenericLossOfFrameRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 195)
)
tnGenericLossOfFrameRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLossOfFrameRaisedNotif.setStatus(
        "current"
    )

tnGenericLossOfFrameClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 196)
)
tnGenericLossOfFrameClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLossOfFrameClearedNotif.setStatus(
        "current"
    )

tnGenericOpticalPowerReceivedOutOfRangeRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 197)
)
tnGenericOpticalPowerReceivedOutOfRangeRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticalPowerReceivedOutOfRangeRaisedNotif.setStatus(
        "current"
    )

tnGenericOpticalPowerReceivedOutOfRangeClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 198)
)
tnGenericOpticalPowerReceivedOutOfRangeClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticalPowerReceivedOutOfRangeClearedNotif.setStatus(
        "current"
    )

tnGenericSfpTempOORRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 199)
)
tnGenericSfpTempOORRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSfpTempOORRaisedNotif.setStatus(
        "current"
    )

tnGenericSfpTempOORClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 200)
)
tnGenericSfpTempOORClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSfpTempOORClearedNotif.setStatus(
        "current"
    )

tnGenericSfpTrmtPwrOORRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 201)
)
tnGenericSfpTrmtPwrOORRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSfpTrmtPwrOORRaisedNotif.setStatus(
        "current"
    )

tnGenericSfpTrmtPwrOORClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 202)
)
tnGenericSfpTrmtPwrOORClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSfpTrmtPwrOORClearedNotif.setStatus(
        "current"
    )

tnGenericSoftwareCompatibilityFailRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 203)
)
tnGenericSoftwareCompatibilityFailRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSoftwareCompatibilityFailRaisedNotif.setStatus(
        "current"
    )

tnGenericSoftwareCompatibilityFailClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 204)
)
tnGenericSoftwareCompatibilityFailClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSoftwareCompatibilityFailClearedNotif.setStatus(
        "current"
    )

tnGenericSoftwareUpgradeFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 205)
)
tnGenericSoftwareUpgradeFailureRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSoftwareUpgradeFailureRaisedNotif.setStatus(
        "current"
    )

tnGenericSoftwareUpgradeFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 206)
)
tnGenericSoftwareUpgradeFailureClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericSoftwareUpgradeFailureClearedNotif.setStatus(
        "current"
    )

tnGenericTCvPcs15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 207)
)
tnGenericTCvPcs15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTCvPcs15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTCvPcs15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 208)
)
tnGenericTCvPcs15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTCvPcs15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTCvPcs1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 209)
)
tnGenericTCvPcs1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTCvPcs1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTCvPcs1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 210)
)
tnGenericTCvPcs1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTCvPcs1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTEsPcs15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 211)
)
tnGenericTEsPcs15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsPcs15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsPcs15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 212)
)
tnGenericTEsPcs15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsPcs15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTEsPcs1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 213)
)
tnGenericTEsPcs1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsPcs1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTEsPcs1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 214)
)
tnGenericTEsPcs1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTEsPcs1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTSefsPcs15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 215)
)
tnGenericTSefsPcs15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSefsPcs15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTSefsPcs15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 216)
)
tnGenericTSefsPcs15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSefsPcs15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTSefsPcs1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 217)
)
tnGenericTSefsPcs1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSefsPcs1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTSefsPcs1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 218)
)
tnGenericTSefsPcs1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSefsPcs1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTSesPcs15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 219)
)
tnGenericTSesPcs15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesPcs15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesPcs15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 220)
)
tnGenericTSesPcs15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesPcs15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTSesPcs1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 221)
)
tnGenericTSesPcs1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesPcs1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTSesPcs1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 222)
)
tnGenericTSesPcs1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTSesPcs1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTxSquelchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 223)
)
tnGenericTxSquelchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTxSquelchRaisedNotif.setStatus(
        "current"
    )

tnGenericTxSquelchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 224)
)
tnGenericTxSquelchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTxSquelchClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm1RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 225)
)
tnGenericUserAlarm1RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm1RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm1ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 226)
)
tnGenericUserAlarm1ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm1ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm2RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 227)
)
tnGenericUserAlarm2RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm2RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm2ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 228)
)
tnGenericUserAlarm2ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm2ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm3RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 229)
)
tnGenericUserAlarm3RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm3RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm3ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 230)
)
tnGenericUserAlarm3ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm3ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm4RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 231)
)
tnGenericUserAlarm4RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm4RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm4ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 232)
)
tnGenericUserAlarm4ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm4ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm5RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 233)
)
tnGenericUserAlarm5RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm5RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm5ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 234)
)
tnGenericUserAlarm5ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm5ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm6RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 235)
)
tnGenericUserAlarm6RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm6RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm6ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 236)
)
tnGenericUserAlarm6ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm6ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm7RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 237)
)
tnGenericUserAlarm7RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm7RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm7ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 238)
)
tnGenericUserAlarm7ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm7ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm8RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 239)
)
tnGenericUserAlarm8RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm8RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm8ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 240)
)
tnGenericUserAlarm8ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm8ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm9RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 241)
)
tnGenericUserAlarm9RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm9RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm9ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 242)
)
tnGenericUserAlarm9ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm9ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm10RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 243)
)
tnGenericUserAlarm10RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm10RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm10ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 244)
)
tnGenericUserAlarm10ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm10ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm11RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 245)
)
tnGenericUserAlarm11RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm11RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm11ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 246)
)
tnGenericUserAlarm11ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm11ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm12RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 247)
)
tnGenericUserAlarm12RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm12RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm12ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 248)
)
tnGenericUserAlarm12ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm12ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm13RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 249)
)
tnGenericUserAlarm13RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm13RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm13ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 250)
)
tnGenericUserAlarm13ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm13ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm14RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 251)
)
tnGenericUserAlarm14RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm14RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm14ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 252)
)
tnGenericUserAlarm14ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm14ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm15RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 253)
)
tnGenericUserAlarm15RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm15RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm15ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 254)
)
tnGenericUserAlarm15ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm15ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm16RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 255)
)
tnGenericUserAlarm16RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm16RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm16ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 256)
)
tnGenericUserAlarm16ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm16ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm17RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 257)
)
tnGenericUserAlarm17RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm17RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm17ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 258)
)
tnGenericUserAlarm17ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm17ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm18RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 259)
)
tnGenericUserAlarm18RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm18RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm18ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 260)
)
tnGenericUserAlarm18ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm18ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm19RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 261)
)
tnGenericUserAlarm19RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm19RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm19ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 262)
)
tnGenericUserAlarm19ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm19ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm20RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 263)
)
tnGenericUserAlarm20RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm20RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm20ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 264)
)
tnGenericUserAlarm20ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm20ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm21RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 265)
)
tnGenericUserAlarm21RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm21RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm21ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 266)
)
tnGenericUserAlarm21ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm21ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm22RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 267)
)
tnGenericUserAlarm22RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm22RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm22ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 268)
)
tnGenericUserAlarm22ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm22ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm23RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 269)
)
tnGenericUserAlarm23RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm23RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm23ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 270)
)
tnGenericUserAlarm23ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm23ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm24RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 271)
)
tnGenericUserAlarm24RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm24RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm24ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 272)
)
tnGenericUserAlarm24ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm24ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm25RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 273)
)
tnGenericUserAlarm25RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm25RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm25ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 274)
)
tnGenericUserAlarm25ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm25ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm26RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 275)
)
tnGenericUserAlarm26RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm26RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm26ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 276)
)
tnGenericUserAlarm26ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm26ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm27RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 277)
)
tnGenericUserAlarm27RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm27RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm27ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 278)
)
tnGenericUserAlarm27ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm27ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm28RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 279)
)
tnGenericUserAlarm28RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm28RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm28ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 280)
)
tnGenericUserAlarm28ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm28ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm29RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 281)
)
tnGenericUserAlarm29RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm29RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm29ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 282)
)
tnGenericUserAlarm29ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm29ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm30RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 283)
)
tnGenericUserAlarm30RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm30RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm30ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 284)
)
tnGenericUserAlarm30ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm30ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm31RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 285)
)
tnGenericUserAlarm31RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm31RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm31ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 286)
)
tnGenericUserAlarm31ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm31ClearedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm32RaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 287)
)
tnGenericUserAlarm32RaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm32RaisedNotif.setStatus(
        "current"
    )

tnGenericUserAlarm32ClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 288)
)
tnGenericUserAlarm32ClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUserAlarm32ClearedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 289)
)
tnGenericTFeBbeOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 290)
)
tnGenericTFeBbeOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 291)
)
tnGenericTFeBbeOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 292)
)
tnGenericTFeBbeOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 293)
)
tnGenericTFeEsOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 294)
)
tnGenericTFeEsOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 295)
)
tnGenericTFeEsOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 296)
)
tnGenericTFeEsOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 297)
)
tnGenericTFeSesOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 298)
)
tnGenericTFeSesOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 299)
)
tnGenericTFeSesOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 300)
)
tnGenericTFeSesOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOdu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 301)
)
tnGenericTFeUasOdu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOdu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOdu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 302)
)
tnGenericTFeUasOdu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOdu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOdu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 303)
)
tnGenericTFeUasOdu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOdu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOdu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 304)
)
tnGenericTFeUasOdu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOdu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 305)
)
tnGenericTFeBbeTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 306)
)
tnGenericTFeBbeTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 307)
)
tnGenericTFeBbeTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 308)
)
tnGenericTFeBbeTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeEsTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 309)
)
tnGenericTFeEsTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeEsTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 310)
)
tnGenericTFeEsTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeEsTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 311)
)
tnGenericTFeEsTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeEsTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 312)
)
tnGenericTFeEsTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeSesTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 313)
)
tnGenericTFeSesTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeSesTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 314)
)
tnGenericTFeSesTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeSesTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 315)
)
tnGenericTFeSesTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeSesTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 316)
)
tnGenericTFeSesTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeUasTcm15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 317)
)
tnGenericTFeUasTcm15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasTcm15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeUasTcm15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 318)
)
tnGenericTFeUasTcm15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasTcm15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeUasTcm1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 319)
)
tnGenericTFeUasTcm1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasTcm1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeUasTcm1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 320)
)
tnGenericTFeUasTcm1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasTcm1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 321)
)
tnGenericTFeBbeOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 322)
)
tnGenericTFeBbeOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 323)
)
tnGenericTFeBbeOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeBbeOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 324)
)
tnGenericTFeBbeOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeBbeOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 325)
)
tnGenericTFeEsOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 326)
)
tnGenericTFeEsOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 327)
)
tnGenericTFeEsOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeEsOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 328)
)
tnGenericTFeEsOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeEsOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 329)
)
tnGenericTFeSesOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 330)
)
tnGenericTFeSesOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 331)
)
tnGenericTFeSesOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeSesOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 332)
)
tnGenericTFeSesOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeSesOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOtu15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 333)
)
tnGenericTFeUasOtu15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOtu15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOtu15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 334)
)
tnGenericTFeUasOtu15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOtu15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOtu1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 335)
)
tnGenericTFeUasOtu1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOtu1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTFeUasOtu1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 336)
)
tnGenericTFeUasOtu1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTFeUasOtu1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInPackets15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 337)
)
tnGenericTPmonPortIfInPackets15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInPackets15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInPackets15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 338)
)
tnGenericTPmonPortIfInPackets15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInPackets15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInPackets1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 339)
)
tnGenericTPmonPortIfInPackets1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInPackets1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInPackets1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 340)
)
tnGenericTPmonPortIfInPackets1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInPackets1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInOctets15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 341)
)
tnGenericTPmonPortIfInOctets15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInOctets15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInOctets15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 342)
)
tnGenericTPmonPortIfInOctets15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInOctets15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInOctets1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 343)
)
tnGenericTPmonPortIfInOctets1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInOctets1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInOctets1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 344)
)
tnGenericTPmonPortIfInOctets1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInOctets1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInDiscards15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 345)
)
tnGenericTPmonPortIfInDiscards15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInDiscards15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInDiscards15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 346)
)
tnGenericTPmonPortIfInDiscards15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInDiscards15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInDiscards1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 347)
)
tnGenericTPmonPortIfInDiscards1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInDiscards1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInDiscards1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 348)
)
tnGenericTPmonPortIfInDiscards1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInDiscards1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInErrors15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 349)
)
tnGenericTPmonPortIfInErrors15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInErrors15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInErrors15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 350)
)
tnGenericTPmonPortIfInErrors15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInErrors15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInErrors1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 351)
)
tnGenericTPmonPortIfInErrors1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInErrors1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfInErrors1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 352)
)
tnGenericTPmonPortIfInErrors1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfInErrors1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutPackets15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 353)
)
tnGenericTPmonPortIfOutPackets15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutPackets15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutPackets15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 354)
)
tnGenericTPmonPortIfOutPackets15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutPackets15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutPackets1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 355)
)
tnGenericTPmonPortIfOutPackets1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutPackets1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutPackets1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 356)
)
tnGenericTPmonPortIfOutPackets1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutPackets1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutOctets15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 357)
)
tnGenericTPmonPortIfOutOctets15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutOctets15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutOctets15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 358)
)
tnGenericTPmonPortIfOutOctets15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutOctets15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutOctets1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 359)
)
tnGenericTPmonPortIfOutOctets1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutOctets1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonPortIfOutOctets1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 360)
)
tnGenericTPmonPortIfOutOctets1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonPortIfOutOctets1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmanFlr1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 361)
)
tnGenericTPmonSlmanFlr1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmanFlr1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmanFlr1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 362)
)
tnGenericTPmonSlmanFlr1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmanFlr1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmafFlr1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 363)
)
tnGenericTPmonSlmafFlr1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmafFlr1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmafFlr1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 364)
)
tnGenericTPmonSlmafFlr1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmafFlr1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmanflr15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 365)
)
tnGenericTPmonSlmanflr15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmanflr15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmanflr15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 366)
)
tnGenericTPmonSlmanflr15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmanflr15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmafflr15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 367)
)
tnGenericTPmonSlmafflr15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmafflr15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmafflr15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 368)
)
tnGenericTPmonSlmafflr15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmafflr15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmnhli15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 369)
)
tnGenericTPmonSlmnhli15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmnhli15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmnhli15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 370)
)
tnGenericTPmonSlmnhli15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmnhli15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmfhli15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 371)
)
tnGenericTPmonSlmfhli15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmfhli15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmfhli15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 372)
)
tnGenericTPmonSlmfhli15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmfhli15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmnhli1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 373)
)
tnGenericTPmonSlmnhli1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmnhli1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmnhli1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 374)
)
tnGenericTPmonSlmnhli1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmnhli1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmfhli1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 375)
)
tnGenericTPmonSlmfhli1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmfhli1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmfhli1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 376)
)
tnGenericTPmonSlmfhli1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmfhli1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmxfflrContRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 377)
)
tnGenericTPmonSlmxfflrContRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmxfflrContRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmxfflrContClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 378)
)
tnGenericTPmonSlmxfflrContClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmxfflrContClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmanflrContRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 379)
)
tnGenericTPmonSlmanflrContRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmanflrContRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmanflrContClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 380)
)
tnGenericTPmonSlmanflrContClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmanflrContClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmafflrContRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 381)
)
tnGenericTPmonSlmafflrContRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmafflrContRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmafflrContClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 382)
)
tnGenericTPmonSlmafflrContClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmafflrContClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmaBfd15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 383)
)
tnGenericTPmonDmaBfd15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmaBfd15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmaBfd15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 384)
)
tnGenericTPmonDmaBfd15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmaBfd15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmaBfd1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 385)
)
tnGenericTPmonDmaBfd1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmaBfd1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmaBfd1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 386)
)
tnGenericTPmonDmaBfd1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmaBfd1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmafFdv15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 387)
)
tnGenericTPmonDmafFdv15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmafFdv15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmafFdv15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 388)
)
tnGenericTPmonDmafFdv15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmafFdv15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmafFdv1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 389)
)
tnGenericTPmonDmafFdv1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmafFdv1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmafFdv1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 390)
)
tnGenericTPmonDmafFdv1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmafFdv1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmanFdv15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 391)
)
tnGenericTPmonDmanFdv15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmanFdv15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmanFdv15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 392)
)
tnGenericTPmonDmanFdv15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmanFdv15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmanFdv1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 393)
)
tnGenericTPmonDmanFdv1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmanFdv1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmanFdv1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 394)
)
tnGenericTPmonDmanFdv1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmanFdv1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxBfd15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 395)
)
tnGenericTPmonDmxBfd15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxBfd15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxBfd15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 396)
)
tnGenericTPmonDmxBfd15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxBfd15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxBfd1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 397)
)
tnGenericTPmonDmxBfd1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxBfd1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxBfd1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 398)
)
tnGenericTPmonDmxBfd1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxBfd1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxfFdv15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 399)
)
tnGenericTPmonDmxfFdv15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxfFdv15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxfFdv15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 400)
)
tnGenericTPmonDmxfFdv15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxfFdv15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxfFdv1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 401)
)
tnGenericTPmonDmxfFdv1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxfFdv1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxfFdv1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 402)
)
tnGenericTPmonDmxfFdv1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxfFdv1DayClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxnFdv15MinRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 403)
)
tnGenericTPmonDmxnFdv15MinRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxnFdv15MinRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxnFdv15MinClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 404)
)
tnGenericTPmonDmxnFdv15MinClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxnFdv15MinClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxnFdv1DayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 405)
)
tnGenericTPmonDmxnFdv1DayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxnFdv1DayRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonDmxnFdv1DayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 406)
)
tnGenericTPmonDmxnFdv1DayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonDmxnFdv1DayClearedNotif.setStatus(
        "current"
    )

tnGenericLagLosRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 407)
)
tnGenericLagLosRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLagLosRaisedNotif.setStatus(
        "current"
    )

tnGenericLagLosClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 408)
)
tnGenericLagLosClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLagLosClearedNotif.setStatus(
        "current"
    )

tnGenericMepLocRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 409)
)
tnGenericMepLocRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMepLocRaisedNotif.setStatus(
        "current"
    )

tnGenericMepLocClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 410)
)
tnGenericMepLocClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMepLocClearedNotif.setStatus(
        "current"
    )

tnGenericUNLRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 411)
)
tnGenericUNLRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNLRaisedNotif.setStatus(
        "current"
    )

tnGenericUNLClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 412)
)
tnGenericUNLClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNLClearedNotif.setStatus(
        "current"
    )

tnGenericMepMmgRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 413)
)
tnGenericMepMmgRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMepMmgRaisedNotif.setStatus(
        "current"
    )

tnGenericMepMmgClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 414)
)
tnGenericMepMmgClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMepMmgClearedNotif.setStatus(
        "current"
    )

tnGenericUNMRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 415)
)
tnGenericUNMRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNMRaisedNotif.setStatus(
        "current"
    )

tnGenericUNMClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 416)
)
tnGenericUNMClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNMClearedNotif.setStatus(
        "current"
    )

tnGenericUNPrRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 417)
)
tnGenericUNPrRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNPrRaisedNotif.setStatus(
        "current"
    )

tnGenericUNPrClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 418)
)
tnGenericUNPrClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNPrClearedNotif.setStatus(
        "current"
    )

tnGenericRDIRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 419)
)
tnGenericRDIRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericRDIRaisedNotif.setStatus(
        "current"
    )

tnGenericRDIClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 420)
)
tnGenericRDIClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericRDIClearedNotif.setStatus(
        "current"
    )

tnGenericUNPRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 421)
)
tnGenericUNPRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNPRaisedNotif.setStatus(
        "current"
    )

tnGenericUNPClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 422)
)
tnGenericUNPClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUNPClearedNotif.setStatus(
        "current"
    )

tnGenericNuatRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 423)
)
tnGenericNuatRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNuatRaisedNotif.setStatus(
        "current"
    )

tnGenericNuatClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 424)
)
tnGenericNuatClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNuatClearedNotif.setStatus(
        "current"
    )

tnGenericFuatRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 425)
)
tnGenericFuatRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFuatRaisedNotif.setStatus(
        "current"
    )

tnGenericFuatClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 426)
)
tnGenericFuatClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericFuatClearedNotif.setStatus(
        "current"
    )

tnGenericAutoLaserOffDueToUpstreamFaultRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 427)
)
tnGenericAutoLaserOffDueToUpstreamFaultRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericAutoLaserOffDueToUpstreamFaultRaisedNotif.setStatus(
        "current"
    )

tnGenericAutoLaserOffDueToUpstreamFaultClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 428)
)
tnGenericAutoLaserOffDueToUpstreamFaultClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericAutoLaserOffDueToUpstreamFaultClearedNotif.setStatus(
        "current"
    )

tnGenericLagProtLosRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 429)
)
tnGenericLagProtLosRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLagProtLosRaisedNotif.setStatus(
        "current"
    )

tnGenericLagProtLosClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 430)
)
tnGenericLagProtLosClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLagProtLosClearedNotif.setStatus(
        "current"
    )

tnGenericMonitorExcRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 431)
)
tnGenericMonitorExcRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMonitorExcRaisedNotif.setStatus(
        "current"
    )

tnGenericMonitorExcClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 432)
)
tnGenericMonitorExcClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMonitorExcClearedNotif.setStatus(
        "current"
    )

tnGenericEquipmentLedOnRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 433)
)
tnGenericEquipmentLedOnRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericEquipmentLedOnRaisedNotif.setStatus(
        "current"
    )

tnGenericEquipmentLedOnClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 434)
)
tnGenericEquipmentLedOnClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericEquipmentLedOnClearedNotif.setStatus(
        "current"
    )

tnGenericUnitInitRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 435)
)
tnGenericUnitInitRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUnitInitRaisedNotif.setStatus(
        "current"
    )

tnGenericUnitInitClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 436)
)
tnGenericUnitInitClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUnitInitClearedNotif.setStatus(
        "current"
    )

tnGenericCardMismatchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 437)
)
tnGenericCardMismatchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardMismatchRaisedNotif.setStatus(
        "current"
    )

tnGenericCardMismatchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 438)
)
tnGenericCardMismatchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCardMismatchClearedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmxnflrContRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 439)
)
tnGenericTPmonSlmxnflrContRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmxnflrContRaisedNotif.setStatus(
        "current"
    )

tnGenericTPmonSlmxnflrContClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 440)
)
tnGenericTPmonSlmxnflrContClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTPmonSlmxnflrContClearedNotif.setStatus(
        "current"
    )

tnGenericOpticalOutputPowerUnachievableRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 441)
)
tnGenericOpticalOutputPowerUnachievableRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticalOutputPowerUnachievableRaisedNotif.setStatus(
        "current"
    )

tnGenericOpticalOutputPowerUnachievableClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 442)
)
tnGenericOpticalOutputPowerUnachievableClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOpticalOutputPowerUnachievableClearedNotif.setStatus(
        "current"
    )

tnGenericDiagnosticTerminalLoopbackActiveRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 443)
)
tnGenericDiagnosticTerminalLoopbackActiveRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericDiagnosticTerminalLoopbackActiveRaisedNotif.setStatus(
        "current"
    )

tnGenericDiagnosticTerminalLoopbackActiveClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 444)
)
tnGenericDiagnosticTerminalLoopbackActiveClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericDiagnosticTerminalLoopbackActiveClearedNotif.setStatus(
        "current"
    )

tnGenericLocalFaultRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 445)
)
tnGenericLocalFaultRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLocalFaultRaisedNotif.setStatus(
        "current"
    )

tnGenericLocalFaultClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 446)
)
tnGenericLocalFaultClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLocalFaultClearedNotif.setStatus(
        "current"
    )

tnGenericRemoteFailureIndicationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 447)
)
tnGenericRemoteFailureIndicationRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericRemoteFailureIndicationRaisedNotif.setStatus(
        "current"
    )

tnGenericRemoteFailureIndicationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 448)
)
tnGenericRemoteFailureIndicationClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericRemoteFailureIndicationClearedNotif.setStatus(
        "current"
    )

tnGenericOduClientSignalFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 477)
)
tnGenericOduClientSignalFailureRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduClientSignalFailureRaisedNotif.setStatus(
        "current"
    )

tnGenericOduClientSignalFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 478)
)
tnGenericOduClientSignalFailureClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericOduClientSignalFailureClearedNotif.setStatus(
        "current"
    )

tnGenericPRBSLSSRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 479)
)
tnGenericPRBSLSSRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericPRBSLSSRaisedNotif.setStatus(
        "current"
    )

tnGenericPRBSLSSClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 480)
)
tnGenericPRBSLSSClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericPRBSLSSClearedNotif.setStatus(
        "current"
    )

tnGenericCsfGfpRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 481)
)
tnGenericCsfGfpRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCsfGfpRaisedNotif.setStatus(
        "current"
    )

tnGenericCsfGfpClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 482)
)
tnGenericCsfGfpClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericCsfGfpClearedNotif.setStatus(
        "current"
    )

tnGenericGfpExmRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 483)
)
tnGenericGfpExmRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericGfpExmRaisedNotif.setStatus(
        "current"
    )

tnGenericGfpExmClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 484)
)
tnGenericGfpExmClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericGfpExmClearedNotif.setStatus(
        "current"
    )

tnGenericGfpLofRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 485)
)
tnGenericGfpLofRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericGfpLofRaisedNotif.setStatus(
        "current"
    )

tnGenericGfpLofClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 486)
)
tnGenericGfpLofClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericGfpLofClearedNotif.setStatus(
        "current"
    )

tnGenericGfpUpmRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 487)
)
tnGenericGfpUpmRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericGfpUpmRaisedNotif.setStatus(
        "current"
    )

tnGenericGfpUpmClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 488)
)
tnGenericGfpUpmClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericGfpUpmClearedNotif.setStatus(
        "current"
    )

tnGenericLOFLOMRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 489)
)
tnGenericLOFLOMRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLOFLOMRaisedNotif.setStatus(
        "current"
    )

tnGenericLOFLOMClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 490)
)
tnGenericLOFLOMClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericLOFLOMClearedNotif.setStatus(
        "current"
    )

tnGenericMsimRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 491)
)
tnGenericMsimRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMsimRaisedNotif.setStatus(
        "current"
    )

tnGenericMsimClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 492)
)
tnGenericMsimClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericMsimClearedNotif.setStatus(
        "current"
    )

tnGenericPayloadTypeMismatchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 493)
)
tnGenericPayloadTypeMismatchRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericPayloadTypeMismatchRaisedNotif.setStatus(
        "current"
    )

tnGenericPayloadTypeMismatchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 494)
)
tnGenericPayloadTypeMismatchClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericPayloadTypeMismatchClearedNotif.setStatus(
        "current"
    )

tnGenericIntrusionRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 495)
)
tnGenericIntrusionRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericIntrusionRaisedNotif.setStatus(
        "current"
    )

tnGenericIntrusionClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 496)
)
tnGenericIntrusionClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericIntrusionClearedNotif.setStatus(
        "current"
    )

tnGenericNtpOutOfSyncRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 497)
)
tnGenericNtpOutOfSyncRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNtpOutOfSyncRaisedNotif.setStatus(
        "current"
    )

tnGenericNtpOutOfSyncClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 498)
)
tnGenericNtpOutOfSyncClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNtpOutOfSyncClearedNotif.setStatus(
        "current"
    )

tnGenericTxAutoLaserShutdownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 499)
)
tnGenericTxAutoLaserShutdownRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTxAutoLaserShutdownRaisedNotif.setStatus(
        "current"
    )

tnGenericTxAutoLaserShutdownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 500)
)
tnGenericTxAutoLaserShutdownClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTxAutoLaserShutdownClearedNotif.setStatus(
        "current"
    )

tnGenericTBerPreFec15minRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 501)
)
tnGenericTBerPreFec15minRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPreFec15minRaisedNotif.setStatus(
        "current"
    )

tnGenericTBerPreFec15minClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 502)
)
tnGenericTBerPreFec15minClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPreFec15minClearedNotif.setStatus(
        "current"
    )

tnGenericTBerPreFec1dayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 503)
)
tnGenericTBerPreFec1dayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPreFec1dayRaisedNotif.setStatus(
        "current"
    )

tnGenericTBerPreFec1dayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 504)
)
tnGenericTBerPreFec1dayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPreFec1dayClearedNotif.setStatus(
        "current"
    )

tnGenericTBerPostFec15minRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 505)
)
tnGenericTBerPostFec15minRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPostFec15minRaisedNotif.setStatus(
        "current"
    )

tnGenericTBerPostFec15minClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 506)
)
tnGenericTBerPostFec15minClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPostFec15minClearedNotif.setStatus(
        "current"
    )

tnGenericTBerPostFec1dayRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 507)
)
tnGenericTBerPostFec1dayRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPostFec1dayRaisedNotif.setStatus(
        "current"
    )

tnGenericTBerPostFec1dayClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 508)
)
tnGenericTBerPostFec1dayClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericTBerPostFec1dayClearedNotif.setStatus(
        "current"
    )

tnGenericUruSRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 509)
)
tnGenericUruSRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUruSRaisedNotif.setStatus(
        "current"
    )

tnGenericUruSClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 510)
)
tnGenericUruSClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericUruSClearedNotif.setStatus(
        "current"
    )

tnGenericNeCertValidityWarnRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 511)
)
tnGenericNeCertValidityWarnRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNeCertValidityWarnRaisedNotif.setStatus(
        "current"
    )

tnGenericNeCertValidityWarnClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 512)
)
tnGenericNeCertValidityWarnClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNeCertValidityWarnClearedNotif.setStatus(
        "current"
    )

tnGenericNeCertValidityExpRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 513)
)
tnGenericNeCertValidityExpRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNeCertValidityExpRaisedNotif.setStatus(
        "current"
    )

tnGenericNeCertValidityExpClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 514)
)
tnGenericNeCertValidityExpClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericNeCertValidityExpClearedNotif.setStatus(
        "current"
    )

tnGenericVoltageLowRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 515)
)
tnGenericVoltageLowRaisedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericVoltageLowRaisedNotif.setStatus(
        "current"
    )

tnGenericVoltageLowClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 0, 516)
)
tnGenericVoltageLowClearedNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapServiceAffecting"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCondition"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapEntityType"))
)
if mibBuilder.loadTexts:
    tnGenericVoltageLowClearedNotif.setStatus(
        "current"
    )

tnGenericPmBinsRolledOverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 1)
)
tnGenericPmBinsRolledOverNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericPmBinsRolledOverNotif.setStatus(
        "current"
    )

tnGenericSecurityFileNameNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 2)
)
tnGenericSecurityFileNameNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityFileNameNotif.setStatus(
        "current"
    )

tnGenericSecurityLoginNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 3)
)
tnGenericSecurityLoginNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityLoginNotif.setStatus(
        "current"
    )

tnGenericSecurityLogoutNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 4)
)
tnGenericSecurityLogoutNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityLogoutNotif.setStatus(
        "current"
    )

tnGenericSecurityAddAccountNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 5)
)
tnGenericSecurityAddAccountNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityAddAccountNotif.setStatus(
        "current"
    )

tnGenericSecurityDeleteAccountNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 6)
)
tnGenericSecurityDeleteAccountNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityDeleteAccountNotif.setStatus(
        "current"
    )

tnGenericSecurityChangeAccountNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 7)
)
tnGenericSecurityChangeAccountNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityChangeAccountNotif.setStatus(
        "current"
    )

tnGenericSubgroupSelectNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 8)
)
tnGenericSubgroupSelectNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSubgroupSelectNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmDmTestCompleteNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 9)
)
tnGenericDot1agCfmDmTestCompleteNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmDmTestCompleteNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmSlmTestCompleteNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 10)
)
tnGenericDot1agCfmSlmTestCompleteNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmSlmTestCompleteNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmLmTestCompleteNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 11)
)
tnGenericDot1agCfmLmTestCompleteNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmLmTestCompleteNotif.setStatus(
        "current"
    )

tnGenericSecurityExceededLoginAttemptsNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 12)
)
tnGenericSecurityExceededLoginAttemptsNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityExceededLoginAttemptsNotif.setStatus(
        "current"
    )

tnGenericSecurityLockAccountNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 13)
)
tnGenericSecurityLockAccountNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityLockAccountNotif.setStatus(
        "current"
    )

tnGenericSecurityUnlockAccountNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 14)
)
tnGenericSecurityUnlockAccountNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityUnlockAccountNotif.setStatus(
        "current"
    )

tnGenericSecurityUnauthAccessAttemptNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 15)
)
tnGenericSecurityUnauthAccessAttemptNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityUnauthAccessAttemptNotif.setStatus(
        "current"
    )

tnGenericSecurityEnableInterfaceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 16)
)
tnGenericSecurityEnableInterfaceNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityEnableInterfaceNotif.setStatus(
        "current"
    )

tnGenericSecurityDisableInterfaceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 17)
)
tnGenericSecurityDisableInterfaceNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericSecurityDisableInterfaceNotif.setStatus(
        "current"
    )

tnGenericDiscoverMeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 0, 18)
)
tnGenericDiscoverMeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericDiscoverMeNotif.setStatus(
        "current"
    )

tnGenericScalarChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5, 0, 1)
)
tnGenericScalarChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericScalarChangeNotif.setStatus(
        "current"
    )

tnGenericIfConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 0, 1)
)
tnGenericIfConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericIfConfigChangeNotif.setStatus(
        "current"
    )

tnGenericIfOperStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 0, 2)
)
tnGenericIfOperStatusChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericIfOperStatusChangeNotif.setStatus(
        "current"
    )

tnGenericOptIfOTUkConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7, 0, 1)
)
tnGenericOptIfOTUkConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericOptIfOTUkConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnAccessPortConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 0, 1)
)
tnGenericTnAccessPortConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnAccessPortConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnIfConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 0, 2)
)
tnGenericTnIfConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnIfConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnLoopbackPortConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 0, 1)
)
tnGenericTnLoopbackPortConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnLoopbackPortConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnDwdmCmnClientPortConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 0, 2)
)
tnGenericTnDwdmCmnClientPortConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnDwdmCmnClientPortConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOtukConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10, 0, 1)
)
tnGenericTnOtukConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOtukConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukNimConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 1)
)
tnGenericTnOthOdukNimConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukNimConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukTtpConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 2)
)
tnGenericTnOthOdukTtpConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukTtpConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukTConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 3)
)
tnGenericTnOthOdukTConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukTConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukTCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 4)
)
tnGenericTnOthOdukTCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukTCreationNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukTDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 5)
)
tnGenericTnOthOdukTDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukTDeletionNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukApsGroupConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 6)
)
tnGenericTnOthOdukApsGroupConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukApsGroupConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukXcConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 7)
)
tnGenericTnOthOdukXcConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukXcConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukApsGroupConvertNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 8)
)
tnGenericTnOthOdukApsGroupConvertNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsAction"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromedIfIndex"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromedIfIndexLo"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromingIfIndex"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapOthOdukApsFromingIfIndexLo"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukApsGroupConvertNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukXcCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 9)
)
tnGenericTnOthOdukXcCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukXcCreationNotif.setStatus(
        "current"
    )

tnGenericTnOthOdukXcDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 0, 10)
)
tnGenericTnOthOdukXcDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthOdukXcDeletionNotif.setStatus(
        "current"
    )

tnGenericTnNetIfConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 0, 1)
)
tnGenericTnNetIfConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnNetIfConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnNetIfFacilityConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 0, 2)
)
tnGenericTnNetIfFacilityConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnNetIfFacilityConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnNetIfFacilityCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 0, 3)
)
tnGenericTnNetIfFacilityCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnNetIfFacilityCreationNotif.setStatus(
        "current"
    )

tnGenericTnNetIfFacilityDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 0, 4)
)
tnGenericTnNetIfFacilityDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnNetIfFacilityDeletionNotif.setStatus(
        "current"
    )

tnGenericTnControlNetworkLinkConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 0, 5)
)
tnGenericTnControlNetworkLinkConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnControlNetworkLinkConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnControlNetworkLinkStateChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 0, 6)
)
tnGenericTnControlNetworkLinkStateChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnGenericTnControlNetworkLinkStateChangeNotif.setStatus(
        "current"
    )

tnGenericTnStatsTCAProfileConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 0, 1)
)
tnGenericTnStatsTCAProfileConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnStatsTCAProfileConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnStatsTCAConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 0, 2)
)
tnGenericTnStatsTCAConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnStatsTCAConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOtuStatsPortConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 0, 3)
)
tnGenericTnOtuStatsPortConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOtuStatsPortConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOdukStatsTcmConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 0, 4)
)
tnGenericTnOdukStatsTcmConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOdukStatsTcmConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOdukStatsRxConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 0, 5)
)
tnGenericTnOdukStatsRxConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOdukStatsRxConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnLagPortConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 0, 1)
)
tnGenericTnLagPortConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnLagPortConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnLagCommandConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 0, 2)
)
tnGenericTnLagCommandConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnLagCommandConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnPmonPolicyConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 0, 1)
)
tnGenericTnPmonPolicyConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnPmonPolicyConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnPmonTcaConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 0, 2)
)
tnGenericTnPmonTcaConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnPmonTcaConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnPortEtherConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16, 0, 1)
)
tnGenericTnPortEtherConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnPortEtherConfigChangeNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMdConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 1)
)
tnGenericDot1agCfmMdConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMdConfigChangeNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMdCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 2)
)
tnGenericDot1agCfmMdCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMdCreationNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMdDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 3)
)
tnGenericDot1agCfmMdDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMdDeletionNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaNetConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 4)
)
tnGenericDot1agCfmMaNetConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaNetConfigChangeNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaNetCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 5)
)
tnGenericDot1agCfmMaNetCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaNetCreationNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaNetDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 6)
)
tnGenericDot1agCfmMaNetDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaNetDeletionNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaCompConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 7)
)
tnGenericDot1agCfmMaCompConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaCompConfigChangeNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaCompCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 8)
)
tnGenericDot1agCfmMaCompCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaCompCreationNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaCompDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 9)
)
tnGenericDot1agCfmMaCompDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaCompDeletionNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaMepListCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 10)
)
tnGenericDot1agCfmMaMepListCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaMepListCreationNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMaMepListDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 11)
)
tnGenericDot1agCfmMaMepListDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMaMepListDeletionNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMepConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 12)
)
tnGenericDot1agCfmMepConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMepConfigChangeNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMepCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 13)
)
tnGenericDot1agCfmMepCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMepCreationNotif.setStatus(
        "current"
    )

tnGenericDot1agCfmMepDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 0, 14)
)
tnGenericDot1agCfmMepDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmMepDeletionNotif.setStatus(
        "current"
    )

tnGenericTnDot1agCfmMepConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 0, 1)
)
tnGenericTnDot1agCfmMepConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnDot1agCfmMepConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnDot1agCfmMepSlmTWTestConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 0, 2)
)
tnGenericTnDot1agCfmMepSlmTWTestConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnDot1agCfmMepSlmTWTestConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnDot1agCfmMepOndemandLmTestConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 0, 3)
)
tnGenericTnDot1agCfmMepOndemandLmTestConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnDot1agCfmMepOndemandLmTestConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTnOamPingCtlCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 0, 1)
)
tnGenericTnOamPingCtlCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOamPingCtlCreationNotif.setStatus(
        "current"
    )

tnGenericTnOamPingCtlDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 0, 2)
)
tnGenericTnOamPingCtlDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOamPingCtlDeletionNotif.setStatus(
        "current"
    )

tnGenericTnOamSaaCtlConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 0, 3)
)
tnGenericTnOamSaaCtlConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTnOamSaaCtlConfigChangeNotif.setStatus(
        "current"
    )

tnGenericRadiusServerCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 0, 1)
)
tnGenericRadiusServerCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericRadiusServerCreationNotif.setStatus(
        "current"
    )

tnGenericRadiusServerDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 0, 2)
)
tnGenericRadiusServerDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericRadiusServerDeletionNotif.setStatus(
        "current"
    )

tnGenericRadiusServerConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 0, 3)
)
tnGenericRadiusServerConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericRadiusServerConfigChangeNotif.setStatus(
        "current"
    )

tnGenericSyslogServerCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 0, 1)
)
tnGenericSyslogServerCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericSyslogServerCreationNotif.setStatus(
        "current"
    )

tnGenericSyslogServerDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 0, 2)
)
tnGenericSyslogServerDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericSyslogServerDeletionNotif.setStatus(
        "current"
    )

tnGenericSyslogServerConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 0, 3)
)
tnGenericSyslogServerConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericSyslogServerConfigChangeNotif.setStatus(
        "current"
    )

tnGenericTransferPMDiscoveryCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 0, 1)
)
tnGenericTransferPMDiscoveryCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTransferPMDiscoveryCreationNotif.setStatus(
        "current"
    )

tnGenericTransferPMDiscoveryDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 0, 2)
)
tnGenericTransferPMDiscoveryDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTransferPMDiscoveryDeletionNotif.setStatus(
        "current"
    )

tnGenericTransferPMDiscoveryConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 0, 3)
)
tnGenericTransferPMDiscoveryConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnGenericTransferPMDiscoveryConfigChangeNotif.setStatus(
        "current"
    )


# Notifications groups

tnGenericConfigurationChangeNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2, 2, 2)
)
tnGenericConfigurationChangeNotifsGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericConfigurationChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericConfigurationChangeNotifsGroup.setStatus(
        "current"
    )

tnGenericStateChangeNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2, 2, 3)
)
tnGenericStateChangeNotifsGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericStateChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericStateChangeNotifsGroup.setStatus(
        "current"
    )

tnGenericTreeUpdateNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2, 2, 4)
)
tnGenericTreeUpdateNotifsGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTreeUpdateNotif")
)
if mibBuilder.loadTexts:
    tnGenericTreeUpdateNotifsGroup.setStatus(
        "current"
    )

tnGenericAlarmNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 2, 2, 1)
)
tnGenericAlarmNotifsGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericBackwardDefectIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericBackwardDefectIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduBackwardDefectIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduBackwardDefectIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmBackwardDefectIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmBackwardDefectIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCommDownRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCommDownClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSignalDegradeRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSignalDegradeClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduSignalDegradeRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduSignalDegradeClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmSignalDegradeRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmSignalDegradeClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericBoardEqptRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericBoardEqptClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericEqptPortRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericEqptPortClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericIntTempHighRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericIntTempHighClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLockedIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLockedIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmLockedIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmLockedIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDwLossOfFrameRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDwLossOfFrameClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDwLossOfMultiFrameRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDwLossOfMultiFrameClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLossOfSignalRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLossOfSignalClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmLossofTandemConnectionRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmLossofTandemConnectionClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInMaintenanceRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInMaintenanceClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticsModuleMismatchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticsModuleMismatchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpenConnectionIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpenConnectionIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmOpenConnectionIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmOpenConnectionIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericReplUnitMissMODRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericReplUnitMissMODClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericServerSignalFailureEgressRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericServerSignalFailureEgressClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericServerSignalFailureRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericServerSignalFailureClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduServerSignalFailureRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduServerSignalFailureClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmServerSignalFailureRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmServerSignalFailureClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardInitializingRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardInitializingClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBbeTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFecc15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFecc15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFecc1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFecc1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrailTraceIdentifierMismatchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrailTraceIdentifierMismatchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduTrailTraceIdentifierMismatchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduTrailTraceIdentifierMismatchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmTrailTraceIdentifierMismatchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmTrailTraceIdentifierMismatchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticsModuleUnknownRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticsModuleUnknownClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUruORaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUruOClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUruPRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUruPClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduUruPRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduUruPClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmUruPRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTcmUruPClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsLockoutOfProtectionRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsLockoutOfProtectionClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingForceSwitchedBackToWorkingRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingForceSwitchedBackToWorkingClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingForceSwitchedToProtectRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingForceSwitchedToProtectClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingManualSwitchedBackToWorkingRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingManualSwitchedBackToWorkingClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsSwitchedToWorkRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsSwitchedToWorkClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingSwitchedToProtectRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingSwitchedToProtectClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingManualSwitchedToProtectRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsWorkingManualSwitchedToProtectClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericWtrRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericWtrClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTUasTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsBlockRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsBlockClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsLOSyncRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsLOSyncClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsLossOfServiceRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsLossOfServiceClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsSuspendedRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericApsSuspendedClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericAuditBlockRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericAuditBlockClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericBreaker1BatteryFeedDownRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericBreaker1BatteryFeedDownClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm1RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm1ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm2RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm2ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm3RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm3ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm4RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCabinAlarm4ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardBootRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardBootClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardMissingRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardMissingClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardUnknownRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardUnknownClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericEqptDgrOchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericEqptDgrOchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm1RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm1ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm2RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm2ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm3RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm3ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm4RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm4ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm5RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm5ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm6RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm6ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm7RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm7ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm8RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm8ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm9RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm9ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm10RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm10ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm11RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm11ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm12RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFrameAlarm12ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInterShelfLossofCommsRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInterShelfLossofCommsClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInventoryErrModRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInventoryErrModClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLineFacilityLoopbackActiveRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLineFacilityLoopbackActiveClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLossOfFrameRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLossOfFrameClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticalPowerReceivedOutOfRangeRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticalPowerReceivedOutOfRangeClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSfpTempOORRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSfpTempOORClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSfpTrmtPwrOORRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSfpTrmtPwrOORClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSoftwareCompatibilityFailRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSoftwareCompatibilityFailClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSoftwareUpgradeFailureRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSoftwareUpgradeFailureClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTCvPcs15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTCvPcs15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTCvPcs1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTCvPcs1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsPcs15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsPcs15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsPcs1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTEsPcs1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSefsPcs15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSefsPcs15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSefsPcs1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSefsPcs1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesPcs15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesPcs15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesPcs1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTSesPcs1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTxSquelchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTxSquelchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm1RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm1ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm2RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm2ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm3RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm3ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm4RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm4ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm5RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm5ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm6RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm6ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm7RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm7ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm8RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm8ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm9RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm9ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm10RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm10ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm11RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm11ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm12RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm12ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm13RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm13ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm14RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm14ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm15RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm15ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm16RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm16ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm17RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm17ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm18RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm18ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm19RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm19ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm20RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm20ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm21RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm21ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm22RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm22ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm23RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm23ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm24RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm24ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm25RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm25ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm26RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm26ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm27RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm27ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm28RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm28ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm29RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm29ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm30RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm30ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm31RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm31ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm32RaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUserAlarm32ClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOdu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOdu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOdu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOdu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasTcm15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasTcm15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasTcm1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasTcm1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeBbeOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeEsOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeSesOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOtu15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOtu15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOtu1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTFeUasOtu1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInPackets15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInPackets15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInPackets1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInPackets1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInOctets15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInOctets15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInOctets1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInOctets1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInDiscards15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInDiscards15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInDiscards1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInDiscards1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInErrors15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInErrors15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInErrors1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfInErrors1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutPackets15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutPackets15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutPackets1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutPackets1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutOctets15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutOctets15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutOctets1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonPortIfOutOctets1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmanFlr1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmanFlr1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmafFlr1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmafFlr1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmanflr15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmanflr15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmafflr15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmafflr15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmnhli15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmnhli15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmfhli15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmfhli15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmnhli1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmnhli1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmfhli1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmfhli1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmxfflrContRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmxfflrContClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmanflrContRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmanflrContClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmafflrContRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmafflrContClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmaBfd15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmaBfd15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmaBfd1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmaBfd1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmafFdv15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmafFdv15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmafFdv1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmafFdv1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmanFdv15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmanFdv15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmanFdv1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmanFdv1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxBfd15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxBfd15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxBfd1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxBfd1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxfFdv15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxfFdv15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxfFdv1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxfFdv1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxnFdv15MinRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxnFdv15MinClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxnFdv1DayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonDmxnFdv1DayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLagLosRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLagLosClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMepLocRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMepLocClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNLRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNLClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMepMmgRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMepMmgClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNMRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNMClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNPrRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNPrClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRDIRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRDIClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNPRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUNPClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNuatRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNuatClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFuatRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericFuatClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericAutoLaserOffDueToUpstreamFaultRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericAutoLaserOffDueToUpstreamFaultClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLagProtLosRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLagProtLosClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMonitorExcRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMonitorExcClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericEquipmentLedOnRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericEquipmentLedOnClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUnitInitRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUnitInitClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardMismatchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCardMismatchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmxnflrContRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTPmonSlmxnflrContClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticalOutputPowerUnachievableRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOpticalOutputPowerUnachievableClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDiagnosticTerminalLoopbackActiveRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDiagnosticTerminalLoopbackActiveClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLocalFaultRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLocalFaultClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRemoteFailureIndicationRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRemoteFailureIndicationClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduClientSignalFailureRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOduClientSignalFailureClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericPRBSLSSRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericPRBSLSSClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCsfGfpRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericCsfGfpClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericGfpExmRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericGfpExmClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericGfpLofRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericGfpLofClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericGfpUpmRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericGfpUpmClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLOFLOMRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericLOFLOMClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMsimRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericMsimClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericPayloadTypeMismatchRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericPayloadTypeMismatchClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericIntrusionRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericIntrusionClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNtpOutOfSyncRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNtpOutOfSyncClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTxAutoLaserShutdownRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTxAutoLaserShutdownClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPreFec15minRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPreFec15minClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPreFec1dayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPreFec1dayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPostFec15minRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPostFec15minClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPostFec1dayRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTBerPostFec1dayClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUruSRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericUruSClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNeCertValidityWarnRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNeCertValidityWarnClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNeCertValidityExpRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericNeCertValidityExpClearedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericVoltageLowRaisedNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericVoltageLowClearedNotif"))
)
if mibBuilder.loadTexts:
    tnGenericAlarmNotifsGroup.setStatus(
        "current"
    )

tnGenericEventNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 2, 2, 1)
)
tnGenericEventNotifsGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericPmBinsRolledOverNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityFileNameNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityLoginNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityLogoutNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityAddAccountNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityDeleteAccountNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityChangeAccountNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSubgroupSelectNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmDmTestCompleteNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmSlmTestCompleteNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmLmTestCompleteNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityExceededLoginAttemptsNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityLockAccountNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityUnlockAccountNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityUnauthAccessAttemptNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityEnableInterfaceNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSecurityDisableInterfaceNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDiscoverMeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericEventNotifsGroup.setStatus(
        "current"
    )

tnGenericScalarConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5, 2, 2, 1)
)
tnGenericScalarConfigChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericScalarChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericScalarConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericInterfaceConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 2, 2, 1)
)
tnGenericInterfaceConfigChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericIfConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericInterfaceConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericInterfaceStateChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 2, 2, 2)
)
tnGenericInterfaceStateChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericIfOperStatusChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericInterfaceStateChangeNotifGroup.setStatus(
        "current"
    )

tnGenericOptIfConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7, 2, 2, 1)
)
tnGenericOptIfConfigChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOptIfOTUkConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericOptIfConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnAccessPortConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 2, 2, 1)
)
tnGenericTnAccessPortConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnAccessPortConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnIfConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnAccessPortConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnOpticalPortConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 2, 2, 1)
)
tnGenericTnOpticalPortConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnLoopbackPortConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnDwdmCmnClientPortConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnOpticalPortConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnOtuOduConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10, 2, 2, 1)
)
tnGenericTnOtuOduConfigChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOtukConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericTnOtuOduConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnOthConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 2, 2, 1)
)
tnGenericTnOthConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukNimConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukTtpConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukTConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukApsGroupConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukXcConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukApsGroupConvertNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnOthCreDelNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 2, 2, 2)
)
tnGenericTnOthCreDelNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukTCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukTDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukXcCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthOdukXcDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthCreDelNotifGroup.setStatus(
        "current"
    )

tnGenericTnL1ServiceConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 2, 2, 1)
)
tnGenericTnL1ServiceConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnNetIfConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnNetIfFacilityConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnControlNetworkLinkConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnL1ServiceConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnL1ServiceCreDelNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 2, 2, 2)
)
tnGenericTnL1ServiceCreDelNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnNetIfFacilityCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnNetIfFacilityDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnL1ServiceCreDelNotifGroup.setStatus(
        "current"
    )

tnGenericTnL1ServiceStateChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 2, 2, 3)
)
tnGenericTnL1ServiceStateChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnControlNetworkLinkStateChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericTnL1ServiceStateChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnStatisticsConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 2, 2, 1)
)
tnGenericTnStatisticsConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnStatsTCAProfileConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnStatsTCAConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOtuStatsPortConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOdukStatsTcmConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOdukStatsRxConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnStatisticsConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnLagConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 2, 2, 1)
)
tnGenericTnLagConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnLagPortConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnLagCommandConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnLagConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnPmonConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 2, 2, 1)
)
tnGenericTnPmonConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnPmonPolicyConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnPmonTcaConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnPmonConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnPortConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16, 2, 2, 1)
)
tnGenericTnPortConfigChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnPortEtherConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericTnPortConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericDot1agCfmConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 2, 2, 1)
)
tnGenericDot1agCfmConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMdConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaNetConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaCompConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMepConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericDot1agCfmCreDelNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 2, 2, 2)
)
tnGenericDot1agCfmCreDelNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMdCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMdDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaNetCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaNetDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaCompCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaCompDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaMepListCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMaMepListDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMepCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmMepDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmCreDelNotifGroup.setStatus(
        "current"
    )

tnGenericTnDot1agCfmConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 2, 2, 1)
)
tnGenericTnDot1agCfmConfigChangeNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnDot1agCfmMepConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnDot1agCfmMepSlmTWTestConfigChangeNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnDot1agCfmMepOndemandLmTestConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnDot1agCfmConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnOamTestConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 2, 2, 1)
)
tnGenericTnOamTestConfigChangeNotifGroup.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOamSaaCtlConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnGenericTnOamTestConfigChangeNotifGroup.setStatus(
        "current"
    )

tnGenericTnOamTestCreDelNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 2, 2, 2)
)
tnGenericTnOamTestCreDelNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOamPingCtlCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOamPingCtlDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTnOamTestCreDelNotifGroup.setStatus(
        "current"
    )

tnGenericRadiusNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 2, 2, 1)
)
tnGenericRadiusNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRadiusServerCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRadiusServerDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRadiusServerConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericRadiusNotifGroup.setStatus(
        "current"
    )

tnGenericSyslogNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 2, 2, 1)
)
tnGenericSyslogNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSyslogServerCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSyslogServerDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSyslogServerConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericSyslogNotifGroup.setStatus(
        "current"
    )

tnGenericTransferPMDiscoveryNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 2, 2, 1)
)
tnGenericTransferPMDiscoveryNotifGroup.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTransferPMDiscoveryCreationNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTransferPMDiscoveryDeletionNotif"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTransferPMDiscoveryConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnGenericTransferPMDiscoveryNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tnGenericTrapBufferCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 1, 2, 1, 1)
)
tnGenericTrapBufferCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapBufferGroup")
)
if mibBuilder.loadTexts:
    tnGenericTrapBufferCompliance.setStatus(
        "current"
    )

tnGenericTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 2, 2, 1, 1)
)
tnGenericTrapCompliance.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericConfigurationChangeNotifsGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericStateChangeNotifsGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTreeUpdateNotifsGroup"))
)
if mibBuilder.loadTexts:
    tnGenericTrapCompliance.setStatus(
        "current"
    )

tnGenericAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 3, 2, 1, 1)
)
tnGenericAlarmCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericAlarmNotifsGroup")
)
if mibBuilder.loadTexts:
    tnGenericAlarmCompliance.setStatus(
        "current"
    )

tnGenericEventCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 4, 2, 1, 1)
)
tnGenericEventCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericEventNotifsGroup")
)
if mibBuilder.loadTexts:
    tnGenericEventCompliance.setStatus(
        "current"
    )

tnGenericScalarCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 5, 2, 1, 1)
)
tnGenericScalarCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericScalarConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericScalarCompliance.setStatus(
        "current"
    )

tnGenericInterfaceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 6, 2, 1, 1)
)
tnGenericInterfaceCompliance.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInterfaceConfigChangeNotifGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericInterfaceStateChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    tnGenericInterfaceCompliance.setStatus(
        "current"
    )

tnGenericOptIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 7, 2, 1, 1)
)
tnGenericOptIfCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericOptIfConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericOptIfCompliance.setStatus(
        "current"
    )

tnGenericTnAccessPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 8, 2, 1, 1)
)
tnGenericTnAccessPortCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnAccessPortConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnAccessPortCompliance.setStatus(
        "current"
    )

tnGenericTnOpticalPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 9, 2, 1, 1)
)
tnGenericTnOpticalPortCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOpticalPortConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnOpticalPortCompliance.setStatus(
        "current"
    )

tnGenericTnOtuOduCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 10, 2, 1, 1)
)
tnGenericTnOtuOduCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOtuOduConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnOtuOduCompliance.setStatus(
        "current"
    )

tnGenericTnOthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 11, 2, 1, 1)
)
tnGenericTnOthCompliance.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthConfigChangeNotifGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOthCreDelNotifGroup"))
)
if mibBuilder.loadTexts:
    tnGenericTnOthCompliance.setStatus(
        "current"
    )

tnGenericTnL1ServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 12, 2, 1, 1)
)
tnGenericTnL1ServiceCompliance.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnL1ServiceConfigChangeNotifGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnL1ServiceCreDelNotifGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnL1ServiceStateChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    tnGenericTnL1ServiceCompliance.setStatus(
        "current"
    )

tnGenericTnStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 13, 2, 1, 1)
)
tnGenericTnStatisticsCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnStatisticsConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnStatisticsCompliance.setStatus(
        "current"
    )

tnGenericTnLagCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 14, 2, 1, 1)
)
tnGenericTnLagCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnLagConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnLagCompliance.setStatus(
        "current"
    )

tnGenericTnPmonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 15, 2, 1, 1)
)
tnGenericTnPmonCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnPmonConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnPmonCompliance.setStatus(
        "current"
    )

tnGenericTnPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 16, 2, 1, 1)
)
tnGenericTnPortCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnPortConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnPortCompliance.setStatus(
        "current"
    )

tnGenericDot1agCfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 17, 2, 1, 1)
)
tnGenericDot1agCfmCompliance.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmConfigChangeNotifGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericDot1agCfmCreDelNotifGroup"))
)
if mibBuilder.loadTexts:
    tnGenericDot1agCfmCompliance.setStatus(
        "current"
    )

tnGenericTnDot1agCfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 18, 2, 1, 1)
)
tnGenericTnDot1agCfmCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnDot1agCfmConfigChangeNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTnDot1agCfmCompliance.setStatus(
        "current"
    )

tnGenericTnOamTestCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 19, 2, 1, 1)
)
tnGenericTnOamTestCompliance.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOamTestConfigChangeNotifGroup"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTnOamTestCreDelNotifGroup"))
)
if mibBuilder.loadTexts:
    tnGenericTnOamTestCompliance.setStatus(
        "current"
    )

tnGenericRadiusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 20, 2, 1, 1)
)
tnGenericRadiusCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericRadiusNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericRadiusCompliance.setStatus(
        "current"
    )

tnGenericSyslogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 21, 2, 1, 1)
)
tnGenericSyslogCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericSyslogNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericSyslogCompliance.setStatus(
        "current"
    )

tnGenericTransferPMDiscoveryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12, 22, 2, 1, 1)
)
tnGenericTransferPMDiscoveryCompliance.setObjects(
    ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTransferPMDiscoveryNotifGroup")
)
if mibBuilder.loadTexts:
    tnGenericTransferPMDiscoveryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GENERIC-NOTIFICATION-MIB",
    **{"TropicGenericTrapObjectValueType": TropicGenericTrapObjectValueType,
       "tnGenericNotificationMibModule": tnGenericNotificationMibModule,
       "tnGenericTrapBuffer": tnGenericTrapBuffer,
       "tnGenericTrapBufferObjects": tnGenericTrapBufferObjects,
       "tnGenericTrapBufferTable": tnGenericTrapBufferTable,
       "tnGenericTrapBufferEntry": tnGenericTrapBufferEntry,
       "tnGenericTrapNumber": tnGenericTrapNumber,
       "tnGenericTrapType": tnGenericTrapType,
       "tnGenericTrapObject": tnGenericTrapObject,
       "tnGenericTrapObjectInstance": tnGenericTrapObjectInstance,
       "tnGenericTrapTime": tnGenericTrapTime,
       "tnGenericTrapCategory": tnGenericTrapCategory,
       "tnGenericTrapDescr": tnGenericTrapDescr,
       "tnGenericTrapData": tnGenericTrapData,
       "tnGenericTrapServiceAffecting": tnGenericTrapServiceAffecting,
       "tnGenericTrapCondition": tnGenericTrapCondition,
       "tnGenericTrapObjectValueType": tnGenericTrapObjectValueType,
       "tnGenericTrapObjectCounter32Val": tnGenericTrapObjectCounter32Val,
       "tnGenericTrapObjectUnsigned32Val": tnGenericTrapObjectUnsigned32Val,
       "tnGenericTrapObjectTimeTicksVal": tnGenericTrapObjectTimeTicksVal,
       "tnGenericTrapObjectInteger32Val": tnGenericTrapObjectInteger32Val,
       "tnGenericTrapObjectOctetStringVal": tnGenericTrapObjectOctetStringVal,
       "tnGenericTrapObjectIpAddressVal": tnGenericTrapObjectIpAddressVal,
       "tnGenericTrapObjectOidVal": tnGenericTrapObjectOidVal,
       "tnGenericTrapObjectCounter64Val": tnGenericTrapObjectCounter64Val,
       "tnGenericTrapDateAndTime": tnGenericTrapDateAndTime,
       "tnGenericTrapConfigurationChangeCounter": tnGenericTrapConfigurationChangeCounter,
       "tnGenericTrapEntityType": tnGenericTrapEntityType,
       "tnGenericLastIssuedTrapNumber": tnGenericLastIssuedTrapNumber,
       "tnGenericTrapNumberResetToBeHandled": tnGenericTrapNumberResetToBeHandled,
       "tnGenericTrapBufferConformance": tnGenericTrapBufferConformance,
       "tnGenericTrapBufferCompliances": tnGenericTrapBufferCompliances,
       "tnGenericTrapBufferCompliance": tnGenericTrapBufferCompliance,
       "tnGenericTrapBufferGroups": tnGenericTrapBufferGroups,
       "tnGenericTrapBufferGroup": tnGenericTrapBufferGroup,
       "tnGenericTrap": tnGenericTrap,
       "tnGenericTrapNotifs": tnGenericTrapNotifs,
       "tnGenericConfigurationChangeNotif": tnGenericConfigurationChangeNotif,
       "tnGenericStateChangeNotif": tnGenericStateChangeNotif,
       "tnGenericTreeUpdateNotif": tnGenericTreeUpdateNotif,
       "tnGenericTrapObjects": tnGenericTrapObjects,
       "tnGenericTrapSeqNumber": tnGenericTrapSeqNumber,
       "tnGenericTrapOthOdukApsAction": tnGenericTrapOthOdukApsAction,
       "tnGenericTrapOthOdukApsFromedIfIndex": tnGenericTrapOthOdukApsFromedIfIndex,
       "tnGenericTrapOthOdukApsFromedIfIndexLo": tnGenericTrapOthOdukApsFromedIfIndexLo,
       "tnGenericTrapOthOdukApsFromingIfIndex": tnGenericTrapOthOdukApsFromingIfIndex,
       "tnGenericTrapOthOdukApsFromingIfIndexLo": tnGenericTrapOthOdukApsFromingIfIndexLo,
       "tnGenericTrapConformance": tnGenericTrapConformance,
       "tnGenericTrapCompliances": tnGenericTrapCompliances,
       "tnGenericTrapCompliance": tnGenericTrapCompliance,
       "tnGenericTrapGroups": tnGenericTrapGroups,
       "tnGenericTrapGroup": tnGenericTrapGroup,
       "tnGenericConfigurationChangeNotifsGroup": tnGenericConfigurationChangeNotifsGroup,
       "tnGenericStateChangeNotifsGroup": tnGenericStateChangeNotifsGroup,
       "tnGenericTreeUpdateNotifsGroup": tnGenericTreeUpdateNotifsGroup,
       "tnGenericAlarm": tnGenericAlarm,
       "tnGenericAlarmNotifs": tnGenericAlarmNotifs,
       "tnGenericBackwardDefectIndicationRaisedNotif": tnGenericBackwardDefectIndicationRaisedNotif,
       "tnGenericBackwardDefectIndicationClearedNotif": tnGenericBackwardDefectIndicationClearedNotif,
       "tnGenericOduBackwardDefectIndicationRaisedNotif": tnGenericOduBackwardDefectIndicationRaisedNotif,
       "tnGenericOduBackwardDefectIndicationClearedNotif": tnGenericOduBackwardDefectIndicationClearedNotif,
       "tnGenericTcmBackwardDefectIndicationRaisedNotif": tnGenericTcmBackwardDefectIndicationRaisedNotif,
       "tnGenericTcmBackwardDefectIndicationClearedNotif": tnGenericTcmBackwardDefectIndicationClearedNotif,
       "tnGenericCommDownRaisedNotif": tnGenericCommDownRaisedNotif,
       "tnGenericCommDownClearedNotif": tnGenericCommDownClearedNotif,
       "tnGenericSignalDegradeRaisedNotif": tnGenericSignalDegradeRaisedNotif,
       "tnGenericSignalDegradeClearedNotif": tnGenericSignalDegradeClearedNotif,
       "tnGenericOduSignalDegradeRaisedNotif": tnGenericOduSignalDegradeRaisedNotif,
       "tnGenericOduSignalDegradeClearedNotif": tnGenericOduSignalDegradeClearedNotif,
       "tnGenericTcmSignalDegradeRaisedNotif": tnGenericTcmSignalDegradeRaisedNotif,
       "tnGenericTcmSignalDegradeClearedNotif": tnGenericTcmSignalDegradeClearedNotif,
       "tnGenericBoardEqptRaisedNotif": tnGenericBoardEqptRaisedNotif,
       "tnGenericBoardEqptClearedNotif": tnGenericBoardEqptClearedNotif,
       "tnGenericEqptPortRaisedNotif": tnGenericEqptPortRaisedNotif,
       "tnGenericEqptPortClearedNotif": tnGenericEqptPortClearedNotif,
       "tnGenericIntTempHighRaisedNotif": tnGenericIntTempHighRaisedNotif,
       "tnGenericIntTempHighClearedNotif": tnGenericIntTempHighClearedNotif,
       "tnGenericLockedIndicationRaisedNotif": tnGenericLockedIndicationRaisedNotif,
       "tnGenericLockedIndicationClearedNotif": tnGenericLockedIndicationClearedNotif,
       "tnGenericTcmLockedIndicationRaisedNotif": tnGenericTcmLockedIndicationRaisedNotif,
       "tnGenericTcmLockedIndicationClearedNotif": tnGenericTcmLockedIndicationClearedNotif,
       "tnGenericDwLossOfFrameRaisedNotif": tnGenericDwLossOfFrameRaisedNotif,
       "tnGenericDwLossOfFrameClearedNotif": tnGenericDwLossOfFrameClearedNotif,
       "tnGenericDwLossOfMultiFrameRaisedNotif": tnGenericDwLossOfMultiFrameRaisedNotif,
       "tnGenericDwLossOfMultiFrameClearedNotif": tnGenericDwLossOfMultiFrameClearedNotif,
       "tnGenericLossOfSignalRaisedNotif": tnGenericLossOfSignalRaisedNotif,
       "tnGenericLossOfSignalClearedNotif": tnGenericLossOfSignalClearedNotif,
       "tnGenericTcmLossofTandemConnectionRaisedNotif": tnGenericTcmLossofTandemConnectionRaisedNotif,
       "tnGenericTcmLossofTandemConnectionClearedNotif": tnGenericTcmLossofTandemConnectionClearedNotif,
       "tnGenericInMaintenanceRaisedNotif": tnGenericInMaintenanceRaisedNotif,
       "tnGenericInMaintenanceClearedNotif": tnGenericInMaintenanceClearedNotif,
       "tnGenericOpticsModuleMismatchRaisedNotif": tnGenericOpticsModuleMismatchRaisedNotif,
       "tnGenericOpticsModuleMismatchClearedNotif": tnGenericOpticsModuleMismatchClearedNotif,
       "tnGenericOpenConnectionIndicationRaisedNotif": tnGenericOpenConnectionIndicationRaisedNotif,
       "tnGenericOpenConnectionIndicationClearedNotif": tnGenericOpenConnectionIndicationClearedNotif,
       "tnGenericTcmOpenConnectionIndicationRaisedNotif": tnGenericTcmOpenConnectionIndicationRaisedNotif,
       "tnGenericTcmOpenConnectionIndicationClearedNotif": tnGenericTcmOpenConnectionIndicationClearedNotif,
       "tnGenericReplUnitMissMODRaisedNotif": tnGenericReplUnitMissMODRaisedNotif,
       "tnGenericReplUnitMissMODClearedNotif": tnGenericReplUnitMissMODClearedNotif,
       "tnGenericServerSignalFailureEgressRaisedNotif": tnGenericServerSignalFailureEgressRaisedNotif,
       "tnGenericServerSignalFailureEgressClearedNotif": tnGenericServerSignalFailureEgressClearedNotif,
       "tnGenericServerSignalFailureRaisedNotif": tnGenericServerSignalFailureRaisedNotif,
       "tnGenericServerSignalFailureClearedNotif": tnGenericServerSignalFailureClearedNotif,
       "tnGenericOduServerSignalFailureRaisedNotif": tnGenericOduServerSignalFailureRaisedNotif,
       "tnGenericOduServerSignalFailureClearedNotif": tnGenericOduServerSignalFailureClearedNotif,
       "tnGenericTcmServerSignalFailureRaisedNotif": tnGenericTcmServerSignalFailureRaisedNotif,
       "tnGenericTcmServerSignalFailureClearedNotif": tnGenericTcmServerSignalFailureClearedNotif,
       "tnGenericCardInitializingRaisedNotif": tnGenericCardInitializingRaisedNotif,
       "tnGenericCardInitializingClearedNotif": tnGenericCardInitializingClearedNotif,
       "tnGenericTBbeOdu15MinRaisedNotif": tnGenericTBbeOdu15MinRaisedNotif,
       "tnGenericTBbeOdu15MinClearedNotif": tnGenericTBbeOdu15MinClearedNotif,
       "tnGenericTBbeOdu1DayRaisedNotif": tnGenericTBbeOdu1DayRaisedNotif,
       "tnGenericTBbeOdu1DayClearedNotif": tnGenericTBbeOdu1DayClearedNotif,
       "tnGenericTBbeOtu15MinRaisedNotif": tnGenericTBbeOtu15MinRaisedNotif,
       "tnGenericTBbeOtu15MinClearedNotif": tnGenericTBbeOtu15MinClearedNotif,
       "tnGenericTBbeOtu1DayRaisedNotif": tnGenericTBbeOtu1DayRaisedNotif,
       "tnGenericTBbeOtu1DayClearedNotif": tnGenericTBbeOtu1DayClearedNotif,
       "tnGenericTBbeTcm15MinRaisedNotif": tnGenericTBbeTcm15MinRaisedNotif,
       "tnGenericTBbeTcm15MinClearedNotif": tnGenericTBbeTcm15MinClearedNotif,
       "tnGenericTBbeTcm1DayRaisedNotif": tnGenericTBbeTcm1DayRaisedNotif,
       "tnGenericTBbeTcm1DayClearedNotif": tnGenericTBbeTcm1DayClearedNotif,
       "tnGenericTEsOdu15MinRaisedNotif": tnGenericTEsOdu15MinRaisedNotif,
       "tnGenericTEsOdu15MinClearedNotif": tnGenericTEsOdu15MinClearedNotif,
       "tnGenericTEsOdu1DayRaisedNotif": tnGenericTEsOdu1DayRaisedNotif,
       "tnGenericTEsOdu1DayClearedNotif": tnGenericTEsOdu1DayClearedNotif,
       "tnGenericTEsOtu15MinRaisedNotif": tnGenericTEsOtu15MinRaisedNotif,
       "tnGenericTEsOtu15MinClearedNotif": tnGenericTEsOtu15MinClearedNotif,
       "tnGenericTEsOtu1DayRaisedNotif": tnGenericTEsOtu1DayRaisedNotif,
       "tnGenericTEsOtu1DayClearedNotif": tnGenericTEsOtu1DayClearedNotif,
       "tnGenericTEsTcm15MinRaisedNotif": tnGenericTEsTcm15MinRaisedNotif,
       "tnGenericTEsTcm15MinClearedNotif": tnGenericTEsTcm15MinClearedNotif,
       "tnGenericTEsTcm1DayRaisedNotif": tnGenericTEsTcm1DayRaisedNotif,
       "tnGenericTEsTcm1DayClearedNotif": tnGenericTEsTcm1DayClearedNotif,
       "tnGenericTFecc15MinRaisedNotif": tnGenericTFecc15MinRaisedNotif,
       "tnGenericTFecc15MinClearedNotif": tnGenericTFecc15MinClearedNotif,
       "tnGenericTFecc1DayRaisedNotif": tnGenericTFecc1DayRaisedNotif,
       "tnGenericTFecc1DayClearedNotif": tnGenericTFecc1DayClearedNotif,
       "tnGenericTrailTraceIdentifierMismatchRaisedNotif": tnGenericTrailTraceIdentifierMismatchRaisedNotif,
       "tnGenericTrailTraceIdentifierMismatchClearedNotif": tnGenericTrailTraceIdentifierMismatchClearedNotif,
       "tnGenericOduTrailTraceIdentifierMismatchRaisedNotif": tnGenericOduTrailTraceIdentifierMismatchRaisedNotif,
       "tnGenericOduTrailTraceIdentifierMismatchClearedNotif": tnGenericOduTrailTraceIdentifierMismatchClearedNotif,
       "tnGenericTcmTrailTraceIdentifierMismatchRaisedNotif": tnGenericTcmTrailTraceIdentifierMismatchRaisedNotif,
       "tnGenericTcmTrailTraceIdentifierMismatchClearedNotif": tnGenericTcmTrailTraceIdentifierMismatchClearedNotif,
       "tnGenericOpticsModuleUnknownRaisedNotif": tnGenericOpticsModuleUnknownRaisedNotif,
       "tnGenericOpticsModuleUnknownClearedNotif": tnGenericOpticsModuleUnknownClearedNotif,
       "tnGenericUruORaisedNotif": tnGenericUruORaisedNotif,
       "tnGenericUruOClearedNotif": tnGenericUruOClearedNotif,
       "tnGenericUruPRaisedNotif": tnGenericUruPRaisedNotif,
       "tnGenericUruPClearedNotif": tnGenericUruPClearedNotif,
       "tnGenericOduUruPRaisedNotif": tnGenericOduUruPRaisedNotif,
       "tnGenericOduUruPClearedNotif": tnGenericOduUruPClearedNotif,
       "tnGenericTcmUruPRaisedNotif": tnGenericTcmUruPRaisedNotif,
       "tnGenericTcmUruPClearedNotif": tnGenericTcmUruPClearedNotif,
       "tnGenericApsLockoutOfProtectionRaisedNotif": tnGenericApsLockoutOfProtectionRaisedNotif,
       "tnGenericApsLockoutOfProtectionClearedNotif": tnGenericApsLockoutOfProtectionClearedNotif,
       "tnGenericApsWorkingForceSwitchedBackToWorkingRaisedNotif": tnGenericApsWorkingForceSwitchedBackToWorkingRaisedNotif,
       "tnGenericApsWorkingForceSwitchedBackToWorkingClearedNotif": tnGenericApsWorkingForceSwitchedBackToWorkingClearedNotif,
       "tnGenericApsWorkingForceSwitchedToProtectRaisedNotif": tnGenericApsWorkingForceSwitchedToProtectRaisedNotif,
       "tnGenericApsWorkingForceSwitchedToProtectClearedNotif": tnGenericApsWorkingForceSwitchedToProtectClearedNotif,
       "tnGenericApsWorkingManualSwitchedBackToWorkingRaisedNotif": tnGenericApsWorkingManualSwitchedBackToWorkingRaisedNotif,
       "tnGenericApsWorkingManualSwitchedBackToWorkingClearedNotif": tnGenericApsWorkingManualSwitchedBackToWorkingClearedNotif,
       "tnGenericApsSwitchedToWorkRaisedNotif": tnGenericApsSwitchedToWorkRaisedNotif,
       "tnGenericApsSwitchedToWorkClearedNotif": tnGenericApsSwitchedToWorkClearedNotif,
       "tnGenericApsWorkingSwitchedToProtectRaisedNotif": tnGenericApsWorkingSwitchedToProtectRaisedNotif,
       "tnGenericApsWorkingSwitchedToProtectClearedNotif": tnGenericApsWorkingSwitchedToProtectClearedNotif,
       "tnGenericApsWorkingManualSwitchedToProtectRaisedNotif": tnGenericApsWorkingManualSwitchedToProtectRaisedNotif,
       "tnGenericApsWorkingManualSwitchedToProtectClearedNotif": tnGenericApsWorkingManualSwitchedToProtectClearedNotif,
       "tnGenericWtrRaisedNotif": tnGenericWtrRaisedNotif,
       "tnGenericWtrClearedNotif": tnGenericWtrClearedNotif,
       "tnGenericTSesOdu15MinRaisedNotif": tnGenericTSesOdu15MinRaisedNotif,
       "tnGenericTSesOdu15MinClearedNotif": tnGenericTSesOdu15MinClearedNotif,
       "tnGenericTSesOdu1DayRaisedNotif": tnGenericTSesOdu1DayRaisedNotif,
       "tnGenericTSesOdu1DayClearedNotif": tnGenericTSesOdu1DayClearedNotif,
       "tnGenericTSesOtu15MinRaisedNotif": tnGenericTSesOtu15MinRaisedNotif,
       "tnGenericTSesOtu15MinClearedNotif": tnGenericTSesOtu15MinClearedNotif,
       "tnGenericTSesOtu1DayRaisedNotif": tnGenericTSesOtu1DayRaisedNotif,
       "tnGenericTSesOtu1DayClearedNotif": tnGenericTSesOtu1DayClearedNotif,
       "tnGenericTSesTcm15MinRaisedNotif": tnGenericTSesTcm15MinRaisedNotif,
       "tnGenericTSesTcm15MinClearedNotif": tnGenericTSesTcm15MinClearedNotif,
       "tnGenericTSesTcm1DayRaisedNotif": tnGenericTSesTcm1DayRaisedNotif,
       "tnGenericTSesTcm1DayClearedNotif": tnGenericTSesTcm1DayClearedNotif,
       "tnGenericTUasOdu15MinRaisedNotif": tnGenericTUasOdu15MinRaisedNotif,
       "tnGenericTUasOdu15MinClearedNotif": tnGenericTUasOdu15MinClearedNotif,
       "tnGenericTUasOdu1DayRaisedNotif": tnGenericTUasOdu1DayRaisedNotif,
       "tnGenericTUasOdu1DayClearedNotif": tnGenericTUasOdu1DayClearedNotif,
       "tnGenericTUasOtu15MinRaisedNotif": tnGenericTUasOtu15MinRaisedNotif,
       "tnGenericTUasOtu15MinClearedNotif": tnGenericTUasOtu15MinClearedNotif,
       "tnGenericTUasOtu1DayRaisedNotif": tnGenericTUasOtu1DayRaisedNotif,
       "tnGenericTUasOtu1DayClearedNotif": tnGenericTUasOtu1DayClearedNotif,
       "tnGenericTUasTcm15MinRaisedNotif": tnGenericTUasTcm15MinRaisedNotif,
       "tnGenericTUasTcm15MinClearedNotif": tnGenericTUasTcm15MinClearedNotif,
       "tnGenericTUasTcm1DayRaisedNotif": tnGenericTUasTcm1DayRaisedNotif,
       "tnGenericTUasTcm1DayClearedNotif": tnGenericTUasTcm1DayClearedNotif,
       "tnGenericApsBlockRaisedNotif": tnGenericApsBlockRaisedNotif,
       "tnGenericApsBlockClearedNotif": tnGenericApsBlockClearedNotif,
       "tnGenericApsLOSyncRaisedNotif": tnGenericApsLOSyncRaisedNotif,
       "tnGenericApsLOSyncClearedNotif": tnGenericApsLOSyncClearedNotif,
       "tnGenericApsLossOfServiceRaisedNotif": tnGenericApsLossOfServiceRaisedNotif,
       "tnGenericApsLossOfServiceClearedNotif": tnGenericApsLossOfServiceClearedNotif,
       "tnGenericApsSuspendedRaisedNotif": tnGenericApsSuspendedRaisedNotif,
       "tnGenericApsSuspendedClearedNotif": tnGenericApsSuspendedClearedNotif,
       "tnGenericAuditBlockRaisedNotif": tnGenericAuditBlockRaisedNotif,
       "tnGenericAuditBlockClearedNotif": tnGenericAuditBlockClearedNotif,
       "tnGenericBreaker1BatteryFeedDownRaisedNotif": tnGenericBreaker1BatteryFeedDownRaisedNotif,
       "tnGenericBreaker1BatteryFeedDownClearedNotif": tnGenericBreaker1BatteryFeedDownClearedNotif,
       "tnGenericCabinAlarm1RaisedNotif": tnGenericCabinAlarm1RaisedNotif,
       "tnGenericCabinAlarm1ClearedNotif": tnGenericCabinAlarm1ClearedNotif,
       "tnGenericCabinAlarm2RaisedNotif": tnGenericCabinAlarm2RaisedNotif,
       "tnGenericCabinAlarm2ClearedNotif": tnGenericCabinAlarm2ClearedNotif,
       "tnGenericCabinAlarm3RaisedNotif": tnGenericCabinAlarm3RaisedNotif,
       "tnGenericCabinAlarm3ClearedNotif": tnGenericCabinAlarm3ClearedNotif,
       "tnGenericCabinAlarm4RaisedNotif": tnGenericCabinAlarm4RaisedNotif,
       "tnGenericCabinAlarm4ClearedNotif": tnGenericCabinAlarm4ClearedNotif,
       "tnGenericCardBootRaisedNotif": tnGenericCardBootRaisedNotif,
       "tnGenericCardBootClearedNotif": tnGenericCardBootClearedNotif,
       "tnGenericCardMissingRaisedNotif": tnGenericCardMissingRaisedNotif,
       "tnGenericCardMissingClearedNotif": tnGenericCardMissingClearedNotif,
       "tnGenericCardUnknownRaisedNotif": tnGenericCardUnknownRaisedNotif,
       "tnGenericCardUnknownClearedNotif": tnGenericCardUnknownClearedNotif,
       "tnGenericEqptDgrOchRaisedNotif": tnGenericEqptDgrOchRaisedNotif,
       "tnGenericEqptDgrOchClearedNotif": tnGenericEqptDgrOchClearedNotif,
       "tnGenericFrameAlarm1RaisedNotif": tnGenericFrameAlarm1RaisedNotif,
       "tnGenericFrameAlarm1ClearedNotif": tnGenericFrameAlarm1ClearedNotif,
       "tnGenericFrameAlarm2RaisedNotif": tnGenericFrameAlarm2RaisedNotif,
       "tnGenericFrameAlarm2ClearedNotif": tnGenericFrameAlarm2ClearedNotif,
       "tnGenericFrameAlarm3RaisedNotif": tnGenericFrameAlarm3RaisedNotif,
       "tnGenericFrameAlarm3ClearedNotif": tnGenericFrameAlarm3ClearedNotif,
       "tnGenericFrameAlarm4RaisedNotif": tnGenericFrameAlarm4RaisedNotif,
       "tnGenericFrameAlarm4ClearedNotif": tnGenericFrameAlarm4ClearedNotif,
       "tnGenericFrameAlarm5RaisedNotif": tnGenericFrameAlarm5RaisedNotif,
       "tnGenericFrameAlarm5ClearedNotif": tnGenericFrameAlarm5ClearedNotif,
       "tnGenericFrameAlarm6RaisedNotif": tnGenericFrameAlarm6RaisedNotif,
       "tnGenericFrameAlarm6ClearedNotif": tnGenericFrameAlarm6ClearedNotif,
       "tnGenericFrameAlarm7RaisedNotif": tnGenericFrameAlarm7RaisedNotif,
       "tnGenericFrameAlarm7ClearedNotif": tnGenericFrameAlarm7ClearedNotif,
       "tnGenericFrameAlarm8RaisedNotif": tnGenericFrameAlarm8RaisedNotif,
       "tnGenericFrameAlarm8ClearedNotif": tnGenericFrameAlarm8ClearedNotif,
       "tnGenericFrameAlarm9RaisedNotif": tnGenericFrameAlarm9RaisedNotif,
       "tnGenericFrameAlarm9ClearedNotif": tnGenericFrameAlarm9ClearedNotif,
       "tnGenericFrameAlarm10RaisedNotif": tnGenericFrameAlarm10RaisedNotif,
       "tnGenericFrameAlarm10ClearedNotif": tnGenericFrameAlarm10ClearedNotif,
       "tnGenericFrameAlarm11RaisedNotif": tnGenericFrameAlarm11RaisedNotif,
       "tnGenericFrameAlarm11ClearedNotif": tnGenericFrameAlarm11ClearedNotif,
       "tnGenericFrameAlarm12RaisedNotif": tnGenericFrameAlarm12RaisedNotif,
       "tnGenericFrameAlarm12ClearedNotif": tnGenericFrameAlarm12ClearedNotif,
       "tnGenericInterShelfLossofCommsRaisedNotif": tnGenericInterShelfLossofCommsRaisedNotif,
       "tnGenericInterShelfLossofCommsClearedNotif": tnGenericInterShelfLossofCommsClearedNotif,
       "tnGenericInventoryErrModRaisedNotif": tnGenericInventoryErrModRaisedNotif,
       "tnGenericInventoryErrModClearedNotif": tnGenericInventoryErrModClearedNotif,
       "tnGenericLineFacilityLoopbackActiveRaisedNotif": tnGenericLineFacilityLoopbackActiveRaisedNotif,
       "tnGenericLineFacilityLoopbackActiveClearedNotif": tnGenericLineFacilityLoopbackActiveClearedNotif,
       "tnGenericLossOfFrameRaisedNotif": tnGenericLossOfFrameRaisedNotif,
       "tnGenericLossOfFrameClearedNotif": tnGenericLossOfFrameClearedNotif,
       "tnGenericOpticalPowerReceivedOutOfRangeRaisedNotif": tnGenericOpticalPowerReceivedOutOfRangeRaisedNotif,
       "tnGenericOpticalPowerReceivedOutOfRangeClearedNotif": tnGenericOpticalPowerReceivedOutOfRangeClearedNotif,
       "tnGenericSfpTempOORRaisedNotif": tnGenericSfpTempOORRaisedNotif,
       "tnGenericSfpTempOORClearedNotif": tnGenericSfpTempOORClearedNotif,
       "tnGenericSfpTrmtPwrOORRaisedNotif": tnGenericSfpTrmtPwrOORRaisedNotif,
       "tnGenericSfpTrmtPwrOORClearedNotif": tnGenericSfpTrmtPwrOORClearedNotif,
       "tnGenericSoftwareCompatibilityFailRaisedNotif": tnGenericSoftwareCompatibilityFailRaisedNotif,
       "tnGenericSoftwareCompatibilityFailClearedNotif": tnGenericSoftwareCompatibilityFailClearedNotif,
       "tnGenericSoftwareUpgradeFailureRaisedNotif": tnGenericSoftwareUpgradeFailureRaisedNotif,
       "tnGenericSoftwareUpgradeFailureClearedNotif": tnGenericSoftwareUpgradeFailureClearedNotif,
       "tnGenericTCvPcs15MinRaisedNotif": tnGenericTCvPcs15MinRaisedNotif,
       "tnGenericTCvPcs15MinClearedNotif": tnGenericTCvPcs15MinClearedNotif,
       "tnGenericTCvPcs1DayRaisedNotif": tnGenericTCvPcs1DayRaisedNotif,
       "tnGenericTCvPcs1DayClearedNotif": tnGenericTCvPcs1DayClearedNotif,
       "tnGenericTEsPcs15MinRaisedNotif": tnGenericTEsPcs15MinRaisedNotif,
       "tnGenericTEsPcs15MinClearedNotif": tnGenericTEsPcs15MinClearedNotif,
       "tnGenericTEsPcs1DayRaisedNotif": tnGenericTEsPcs1DayRaisedNotif,
       "tnGenericTEsPcs1DayClearedNotif": tnGenericTEsPcs1DayClearedNotif,
       "tnGenericTSefsPcs15MinRaisedNotif": tnGenericTSefsPcs15MinRaisedNotif,
       "tnGenericTSefsPcs15MinClearedNotif": tnGenericTSefsPcs15MinClearedNotif,
       "tnGenericTSefsPcs1DayRaisedNotif": tnGenericTSefsPcs1DayRaisedNotif,
       "tnGenericTSefsPcs1DayClearedNotif": tnGenericTSefsPcs1DayClearedNotif,
       "tnGenericTSesPcs15MinRaisedNotif": tnGenericTSesPcs15MinRaisedNotif,
       "tnGenericTSesPcs15MinClearedNotif": tnGenericTSesPcs15MinClearedNotif,
       "tnGenericTSesPcs1DayRaisedNotif": tnGenericTSesPcs1DayRaisedNotif,
       "tnGenericTSesPcs1DayClearedNotif": tnGenericTSesPcs1DayClearedNotif,
       "tnGenericTxSquelchRaisedNotif": tnGenericTxSquelchRaisedNotif,
       "tnGenericTxSquelchClearedNotif": tnGenericTxSquelchClearedNotif,
       "tnGenericUserAlarm1RaisedNotif": tnGenericUserAlarm1RaisedNotif,
       "tnGenericUserAlarm1ClearedNotif": tnGenericUserAlarm1ClearedNotif,
       "tnGenericUserAlarm2RaisedNotif": tnGenericUserAlarm2RaisedNotif,
       "tnGenericUserAlarm2ClearedNotif": tnGenericUserAlarm2ClearedNotif,
       "tnGenericUserAlarm3RaisedNotif": tnGenericUserAlarm3RaisedNotif,
       "tnGenericUserAlarm3ClearedNotif": tnGenericUserAlarm3ClearedNotif,
       "tnGenericUserAlarm4RaisedNotif": tnGenericUserAlarm4RaisedNotif,
       "tnGenericUserAlarm4ClearedNotif": tnGenericUserAlarm4ClearedNotif,
       "tnGenericUserAlarm5RaisedNotif": tnGenericUserAlarm5RaisedNotif,
       "tnGenericUserAlarm5ClearedNotif": tnGenericUserAlarm5ClearedNotif,
       "tnGenericUserAlarm6RaisedNotif": tnGenericUserAlarm6RaisedNotif,
       "tnGenericUserAlarm6ClearedNotif": tnGenericUserAlarm6ClearedNotif,
       "tnGenericUserAlarm7RaisedNotif": tnGenericUserAlarm7RaisedNotif,
       "tnGenericUserAlarm7ClearedNotif": tnGenericUserAlarm7ClearedNotif,
       "tnGenericUserAlarm8RaisedNotif": tnGenericUserAlarm8RaisedNotif,
       "tnGenericUserAlarm8ClearedNotif": tnGenericUserAlarm8ClearedNotif,
       "tnGenericUserAlarm9RaisedNotif": tnGenericUserAlarm9RaisedNotif,
       "tnGenericUserAlarm9ClearedNotif": tnGenericUserAlarm9ClearedNotif,
       "tnGenericUserAlarm10RaisedNotif": tnGenericUserAlarm10RaisedNotif,
       "tnGenericUserAlarm10ClearedNotif": tnGenericUserAlarm10ClearedNotif,
       "tnGenericUserAlarm11RaisedNotif": tnGenericUserAlarm11RaisedNotif,
       "tnGenericUserAlarm11ClearedNotif": tnGenericUserAlarm11ClearedNotif,
       "tnGenericUserAlarm12RaisedNotif": tnGenericUserAlarm12RaisedNotif,
       "tnGenericUserAlarm12ClearedNotif": tnGenericUserAlarm12ClearedNotif,
       "tnGenericUserAlarm13RaisedNotif": tnGenericUserAlarm13RaisedNotif,
       "tnGenericUserAlarm13ClearedNotif": tnGenericUserAlarm13ClearedNotif,
       "tnGenericUserAlarm14RaisedNotif": tnGenericUserAlarm14RaisedNotif,
       "tnGenericUserAlarm14ClearedNotif": tnGenericUserAlarm14ClearedNotif,
       "tnGenericUserAlarm15RaisedNotif": tnGenericUserAlarm15RaisedNotif,
       "tnGenericUserAlarm15ClearedNotif": tnGenericUserAlarm15ClearedNotif,
       "tnGenericUserAlarm16RaisedNotif": tnGenericUserAlarm16RaisedNotif,
       "tnGenericUserAlarm16ClearedNotif": tnGenericUserAlarm16ClearedNotif,
       "tnGenericUserAlarm17RaisedNotif": tnGenericUserAlarm17RaisedNotif,
       "tnGenericUserAlarm17ClearedNotif": tnGenericUserAlarm17ClearedNotif,
       "tnGenericUserAlarm18RaisedNotif": tnGenericUserAlarm18RaisedNotif,
       "tnGenericUserAlarm18ClearedNotif": tnGenericUserAlarm18ClearedNotif,
       "tnGenericUserAlarm19RaisedNotif": tnGenericUserAlarm19RaisedNotif,
       "tnGenericUserAlarm19ClearedNotif": tnGenericUserAlarm19ClearedNotif,
       "tnGenericUserAlarm20RaisedNotif": tnGenericUserAlarm20RaisedNotif,
       "tnGenericUserAlarm20ClearedNotif": tnGenericUserAlarm20ClearedNotif,
       "tnGenericUserAlarm21RaisedNotif": tnGenericUserAlarm21RaisedNotif,
       "tnGenericUserAlarm21ClearedNotif": tnGenericUserAlarm21ClearedNotif,
       "tnGenericUserAlarm22RaisedNotif": tnGenericUserAlarm22RaisedNotif,
       "tnGenericUserAlarm22ClearedNotif": tnGenericUserAlarm22ClearedNotif,
       "tnGenericUserAlarm23RaisedNotif": tnGenericUserAlarm23RaisedNotif,
       "tnGenericUserAlarm23ClearedNotif": tnGenericUserAlarm23ClearedNotif,
       "tnGenericUserAlarm24RaisedNotif": tnGenericUserAlarm24RaisedNotif,
       "tnGenericUserAlarm24ClearedNotif": tnGenericUserAlarm24ClearedNotif,
       "tnGenericUserAlarm25RaisedNotif": tnGenericUserAlarm25RaisedNotif,
       "tnGenericUserAlarm25ClearedNotif": tnGenericUserAlarm25ClearedNotif,
       "tnGenericUserAlarm26RaisedNotif": tnGenericUserAlarm26RaisedNotif,
       "tnGenericUserAlarm26ClearedNotif": tnGenericUserAlarm26ClearedNotif,
       "tnGenericUserAlarm27RaisedNotif": tnGenericUserAlarm27RaisedNotif,
       "tnGenericUserAlarm27ClearedNotif": tnGenericUserAlarm27ClearedNotif,
       "tnGenericUserAlarm28RaisedNotif": tnGenericUserAlarm28RaisedNotif,
       "tnGenericUserAlarm28ClearedNotif": tnGenericUserAlarm28ClearedNotif,
       "tnGenericUserAlarm29RaisedNotif": tnGenericUserAlarm29RaisedNotif,
       "tnGenericUserAlarm29ClearedNotif": tnGenericUserAlarm29ClearedNotif,
       "tnGenericUserAlarm30RaisedNotif": tnGenericUserAlarm30RaisedNotif,
       "tnGenericUserAlarm30ClearedNotif": tnGenericUserAlarm30ClearedNotif,
       "tnGenericUserAlarm31RaisedNotif": tnGenericUserAlarm31RaisedNotif,
       "tnGenericUserAlarm31ClearedNotif": tnGenericUserAlarm31ClearedNotif,
       "tnGenericUserAlarm32RaisedNotif": tnGenericUserAlarm32RaisedNotif,
       "tnGenericUserAlarm32ClearedNotif": tnGenericUserAlarm32ClearedNotif,
       "tnGenericTFeBbeOdu15MinRaisedNotif": tnGenericTFeBbeOdu15MinRaisedNotif,
       "tnGenericTFeBbeOdu15MinClearedNotif": tnGenericTFeBbeOdu15MinClearedNotif,
       "tnGenericTFeBbeOdu1DayRaisedNotif": tnGenericTFeBbeOdu1DayRaisedNotif,
       "tnGenericTFeBbeOdu1DayClearedNotif": tnGenericTFeBbeOdu1DayClearedNotif,
       "tnGenericTFeEsOdu15MinRaisedNotif": tnGenericTFeEsOdu15MinRaisedNotif,
       "tnGenericTFeEsOdu15MinClearedNotif": tnGenericTFeEsOdu15MinClearedNotif,
       "tnGenericTFeEsOdu1DayRaisedNotif": tnGenericTFeEsOdu1DayRaisedNotif,
       "tnGenericTFeEsOdu1DayClearedNotif": tnGenericTFeEsOdu1DayClearedNotif,
       "tnGenericTFeSesOdu15MinRaisedNotif": tnGenericTFeSesOdu15MinRaisedNotif,
       "tnGenericTFeSesOdu15MinClearedNotif": tnGenericTFeSesOdu15MinClearedNotif,
       "tnGenericTFeSesOdu1DayRaisedNotif": tnGenericTFeSesOdu1DayRaisedNotif,
       "tnGenericTFeSesOdu1DayClearedNotif": tnGenericTFeSesOdu1DayClearedNotif,
       "tnGenericTFeUasOdu15MinRaisedNotif": tnGenericTFeUasOdu15MinRaisedNotif,
       "tnGenericTFeUasOdu15MinClearedNotif": tnGenericTFeUasOdu15MinClearedNotif,
       "tnGenericTFeUasOdu1DayRaisedNotif": tnGenericTFeUasOdu1DayRaisedNotif,
       "tnGenericTFeUasOdu1DayClearedNotif": tnGenericTFeUasOdu1DayClearedNotif,
       "tnGenericTFeBbeTcm15MinRaisedNotif": tnGenericTFeBbeTcm15MinRaisedNotif,
       "tnGenericTFeBbeTcm15MinClearedNotif": tnGenericTFeBbeTcm15MinClearedNotif,
       "tnGenericTFeBbeTcm1DayRaisedNotif": tnGenericTFeBbeTcm1DayRaisedNotif,
       "tnGenericTFeBbeTcm1DayClearedNotif": tnGenericTFeBbeTcm1DayClearedNotif,
       "tnGenericTFeEsTcm15MinRaisedNotif": tnGenericTFeEsTcm15MinRaisedNotif,
       "tnGenericTFeEsTcm15MinClearedNotif": tnGenericTFeEsTcm15MinClearedNotif,
       "tnGenericTFeEsTcm1DayRaisedNotif": tnGenericTFeEsTcm1DayRaisedNotif,
       "tnGenericTFeEsTcm1DayClearedNotif": tnGenericTFeEsTcm1DayClearedNotif,
       "tnGenericTFeSesTcm15MinRaisedNotif": tnGenericTFeSesTcm15MinRaisedNotif,
       "tnGenericTFeSesTcm15MinClearedNotif": tnGenericTFeSesTcm15MinClearedNotif,
       "tnGenericTFeSesTcm1DayRaisedNotif": tnGenericTFeSesTcm1DayRaisedNotif,
       "tnGenericTFeSesTcm1DayClearedNotif": tnGenericTFeSesTcm1DayClearedNotif,
       "tnGenericTFeUasTcm15MinRaisedNotif": tnGenericTFeUasTcm15MinRaisedNotif,
       "tnGenericTFeUasTcm15MinClearedNotif": tnGenericTFeUasTcm15MinClearedNotif,
       "tnGenericTFeUasTcm1DayRaisedNotif": tnGenericTFeUasTcm1DayRaisedNotif,
       "tnGenericTFeUasTcm1DayClearedNotif": tnGenericTFeUasTcm1DayClearedNotif,
       "tnGenericTFeBbeOtu15MinRaisedNotif": tnGenericTFeBbeOtu15MinRaisedNotif,
       "tnGenericTFeBbeOtu15MinClearedNotif": tnGenericTFeBbeOtu15MinClearedNotif,
       "tnGenericTFeBbeOtu1DayRaisedNotif": tnGenericTFeBbeOtu1DayRaisedNotif,
       "tnGenericTFeBbeOtu1DayClearedNotif": tnGenericTFeBbeOtu1DayClearedNotif,
       "tnGenericTFeEsOtu15MinRaisedNotif": tnGenericTFeEsOtu15MinRaisedNotif,
       "tnGenericTFeEsOtu15MinClearedNotif": tnGenericTFeEsOtu15MinClearedNotif,
       "tnGenericTFeEsOtu1DayRaisedNotif": tnGenericTFeEsOtu1DayRaisedNotif,
       "tnGenericTFeEsOtu1DayClearedNotif": tnGenericTFeEsOtu1DayClearedNotif,
       "tnGenericTFeSesOtu15MinRaisedNotif": tnGenericTFeSesOtu15MinRaisedNotif,
       "tnGenericTFeSesOtu15MinClearedNotif": tnGenericTFeSesOtu15MinClearedNotif,
       "tnGenericTFeSesOtu1DayRaisedNotif": tnGenericTFeSesOtu1DayRaisedNotif,
       "tnGenericTFeSesOtu1DayClearedNotif": tnGenericTFeSesOtu1DayClearedNotif,
       "tnGenericTFeUasOtu15MinRaisedNotif": tnGenericTFeUasOtu15MinRaisedNotif,
       "tnGenericTFeUasOtu15MinClearedNotif": tnGenericTFeUasOtu15MinClearedNotif,
       "tnGenericTFeUasOtu1DayRaisedNotif": tnGenericTFeUasOtu1DayRaisedNotif,
       "tnGenericTFeUasOtu1DayClearedNotif": tnGenericTFeUasOtu1DayClearedNotif,
       "tnGenericTPmonPortIfInPackets15MinRaisedNotif": tnGenericTPmonPortIfInPackets15MinRaisedNotif,
       "tnGenericTPmonPortIfInPackets15MinClearedNotif": tnGenericTPmonPortIfInPackets15MinClearedNotif,
       "tnGenericTPmonPortIfInPackets1DayRaisedNotif": tnGenericTPmonPortIfInPackets1DayRaisedNotif,
       "tnGenericTPmonPortIfInPackets1DayClearedNotif": tnGenericTPmonPortIfInPackets1DayClearedNotif,
       "tnGenericTPmonPortIfInOctets15MinRaisedNotif": tnGenericTPmonPortIfInOctets15MinRaisedNotif,
       "tnGenericTPmonPortIfInOctets15MinClearedNotif": tnGenericTPmonPortIfInOctets15MinClearedNotif,
       "tnGenericTPmonPortIfInOctets1DayRaisedNotif": tnGenericTPmonPortIfInOctets1DayRaisedNotif,
       "tnGenericTPmonPortIfInOctets1DayClearedNotif": tnGenericTPmonPortIfInOctets1DayClearedNotif,
       "tnGenericTPmonPortIfInDiscards15MinRaisedNotif": tnGenericTPmonPortIfInDiscards15MinRaisedNotif,
       "tnGenericTPmonPortIfInDiscards15MinClearedNotif": tnGenericTPmonPortIfInDiscards15MinClearedNotif,
       "tnGenericTPmonPortIfInDiscards1DayRaisedNotif": tnGenericTPmonPortIfInDiscards1DayRaisedNotif,
       "tnGenericTPmonPortIfInDiscards1DayClearedNotif": tnGenericTPmonPortIfInDiscards1DayClearedNotif,
       "tnGenericTPmonPortIfInErrors15MinRaisedNotif": tnGenericTPmonPortIfInErrors15MinRaisedNotif,
       "tnGenericTPmonPortIfInErrors15MinClearedNotif": tnGenericTPmonPortIfInErrors15MinClearedNotif,
       "tnGenericTPmonPortIfInErrors1DayRaisedNotif": tnGenericTPmonPortIfInErrors1DayRaisedNotif,
       "tnGenericTPmonPortIfInErrors1DayClearedNotif": tnGenericTPmonPortIfInErrors1DayClearedNotif,
       "tnGenericTPmonPortIfOutPackets15MinRaisedNotif": tnGenericTPmonPortIfOutPackets15MinRaisedNotif,
       "tnGenericTPmonPortIfOutPackets15MinClearedNotif": tnGenericTPmonPortIfOutPackets15MinClearedNotif,
       "tnGenericTPmonPortIfOutPackets1DayRaisedNotif": tnGenericTPmonPortIfOutPackets1DayRaisedNotif,
       "tnGenericTPmonPortIfOutPackets1DayClearedNotif": tnGenericTPmonPortIfOutPackets1DayClearedNotif,
       "tnGenericTPmonPortIfOutOctets15MinRaisedNotif": tnGenericTPmonPortIfOutOctets15MinRaisedNotif,
       "tnGenericTPmonPortIfOutOctets15MinClearedNotif": tnGenericTPmonPortIfOutOctets15MinClearedNotif,
       "tnGenericTPmonPortIfOutOctets1DayRaisedNotif": tnGenericTPmonPortIfOutOctets1DayRaisedNotif,
       "tnGenericTPmonPortIfOutOctets1DayClearedNotif": tnGenericTPmonPortIfOutOctets1DayClearedNotif,
       "tnGenericTPmonSlmanFlr1DayRaisedNotif": tnGenericTPmonSlmanFlr1DayRaisedNotif,
       "tnGenericTPmonSlmanFlr1DayClearedNotif": tnGenericTPmonSlmanFlr1DayClearedNotif,
       "tnGenericTPmonSlmafFlr1DayRaisedNotif": tnGenericTPmonSlmafFlr1DayRaisedNotif,
       "tnGenericTPmonSlmafFlr1DayClearedNotif": tnGenericTPmonSlmafFlr1DayClearedNotif,
       "tnGenericTPmonSlmanflr15MinRaisedNotif": tnGenericTPmonSlmanflr15MinRaisedNotif,
       "tnGenericTPmonSlmanflr15MinClearedNotif": tnGenericTPmonSlmanflr15MinClearedNotif,
       "tnGenericTPmonSlmafflr15MinRaisedNotif": tnGenericTPmonSlmafflr15MinRaisedNotif,
       "tnGenericTPmonSlmafflr15MinClearedNotif": tnGenericTPmonSlmafflr15MinClearedNotif,
       "tnGenericTPmonSlmnhli15MinRaisedNotif": tnGenericTPmonSlmnhli15MinRaisedNotif,
       "tnGenericTPmonSlmnhli15MinClearedNotif": tnGenericTPmonSlmnhli15MinClearedNotif,
       "tnGenericTPmonSlmfhli15MinRaisedNotif": tnGenericTPmonSlmfhli15MinRaisedNotif,
       "tnGenericTPmonSlmfhli15MinClearedNotif": tnGenericTPmonSlmfhli15MinClearedNotif,
       "tnGenericTPmonSlmnhli1DayRaisedNotif": tnGenericTPmonSlmnhli1DayRaisedNotif,
       "tnGenericTPmonSlmnhli1DayClearedNotif": tnGenericTPmonSlmnhli1DayClearedNotif,
       "tnGenericTPmonSlmfhli1DayRaisedNotif": tnGenericTPmonSlmfhli1DayRaisedNotif,
       "tnGenericTPmonSlmfhli1DayClearedNotif": tnGenericTPmonSlmfhli1DayClearedNotif,
       "tnGenericTPmonSlmxfflrContRaisedNotif": tnGenericTPmonSlmxfflrContRaisedNotif,
       "tnGenericTPmonSlmxfflrContClearedNotif": tnGenericTPmonSlmxfflrContClearedNotif,
       "tnGenericTPmonSlmanflrContRaisedNotif": tnGenericTPmonSlmanflrContRaisedNotif,
       "tnGenericTPmonSlmanflrContClearedNotif": tnGenericTPmonSlmanflrContClearedNotif,
       "tnGenericTPmonSlmafflrContRaisedNotif": tnGenericTPmonSlmafflrContRaisedNotif,
       "tnGenericTPmonSlmafflrContClearedNotif": tnGenericTPmonSlmafflrContClearedNotif,
       "tnGenericTPmonDmaBfd15MinRaisedNotif": tnGenericTPmonDmaBfd15MinRaisedNotif,
       "tnGenericTPmonDmaBfd15MinClearedNotif": tnGenericTPmonDmaBfd15MinClearedNotif,
       "tnGenericTPmonDmaBfd1DayRaisedNotif": tnGenericTPmonDmaBfd1DayRaisedNotif,
       "tnGenericTPmonDmaBfd1DayClearedNotif": tnGenericTPmonDmaBfd1DayClearedNotif,
       "tnGenericTPmonDmafFdv15MinRaisedNotif": tnGenericTPmonDmafFdv15MinRaisedNotif,
       "tnGenericTPmonDmafFdv15MinClearedNotif": tnGenericTPmonDmafFdv15MinClearedNotif,
       "tnGenericTPmonDmafFdv1DayRaisedNotif": tnGenericTPmonDmafFdv1DayRaisedNotif,
       "tnGenericTPmonDmafFdv1DayClearedNotif": tnGenericTPmonDmafFdv1DayClearedNotif,
       "tnGenericTPmonDmanFdv15MinRaisedNotif": tnGenericTPmonDmanFdv15MinRaisedNotif,
       "tnGenericTPmonDmanFdv15MinClearedNotif": tnGenericTPmonDmanFdv15MinClearedNotif,
       "tnGenericTPmonDmanFdv1DayRaisedNotif": tnGenericTPmonDmanFdv1DayRaisedNotif,
       "tnGenericTPmonDmanFdv1DayClearedNotif": tnGenericTPmonDmanFdv1DayClearedNotif,
       "tnGenericTPmonDmxBfd15MinRaisedNotif": tnGenericTPmonDmxBfd15MinRaisedNotif,
       "tnGenericTPmonDmxBfd15MinClearedNotif": tnGenericTPmonDmxBfd15MinClearedNotif,
       "tnGenericTPmonDmxBfd1DayRaisedNotif": tnGenericTPmonDmxBfd1DayRaisedNotif,
       "tnGenericTPmonDmxBfd1DayClearedNotif": tnGenericTPmonDmxBfd1DayClearedNotif,
       "tnGenericTPmonDmxfFdv15MinRaisedNotif": tnGenericTPmonDmxfFdv15MinRaisedNotif,
       "tnGenericTPmonDmxfFdv15MinClearedNotif": tnGenericTPmonDmxfFdv15MinClearedNotif,
       "tnGenericTPmonDmxfFdv1DayRaisedNotif": tnGenericTPmonDmxfFdv1DayRaisedNotif,
       "tnGenericTPmonDmxfFdv1DayClearedNotif": tnGenericTPmonDmxfFdv1DayClearedNotif,
       "tnGenericTPmonDmxnFdv15MinRaisedNotif": tnGenericTPmonDmxnFdv15MinRaisedNotif,
       "tnGenericTPmonDmxnFdv15MinClearedNotif": tnGenericTPmonDmxnFdv15MinClearedNotif,
       "tnGenericTPmonDmxnFdv1DayRaisedNotif": tnGenericTPmonDmxnFdv1DayRaisedNotif,
       "tnGenericTPmonDmxnFdv1DayClearedNotif": tnGenericTPmonDmxnFdv1DayClearedNotif,
       "tnGenericLagLosRaisedNotif": tnGenericLagLosRaisedNotif,
       "tnGenericLagLosClearedNotif": tnGenericLagLosClearedNotif,
       "tnGenericMepLocRaisedNotif": tnGenericMepLocRaisedNotif,
       "tnGenericMepLocClearedNotif": tnGenericMepLocClearedNotif,
       "tnGenericUNLRaisedNotif": tnGenericUNLRaisedNotif,
       "tnGenericUNLClearedNotif": tnGenericUNLClearedNotif,
       "tnGenericMepMmgRaisedNotif": tnGenericMepMmgRaisedNotif,
       "tnGenericMepMmgClearedNotif": tnGenericMepMmgClearedNotif,
       "tnGenericUNMRaisedNotif": tnGenericUNMRaisedNotif,
       "tnGenericUNMClearedNotif": tnGenericUNMClearedNotif,
       "tnGenericUNPrRaisedNotif": tnGenericUNPrRaisedNotif,
       "tnGenericUNPrClearedNotif": tnGenericUNPrClearedNotif,
       "tnGenericRDIRaisedNotif": tnGenericRDIRaisedNotif,
       "tnGenericRDIClearedNotif": tnGenericRDIClearedNotif,
       "tnGenericUNPRaisedNotif": tnGenericUNPRaisedNotif,
       "tnGenericUNPClearedNotif": tnGenericUNPClearedNotif,
       "tnGenericNuatRaisedNotif": tnGenericNuatRaisedNotif,
       "tnGenericNuatClearedNotif": tnGenericNuatClearedNotif,
       "tnGenericFuatRaisedNotif": tnGenericFuatRaisedNotif,
       "tnGenericFuatClearedNotif": tnGenericFuatClearedNotif,
       "tnGenericAutoLaserOffDueToUpstreamFaultRaisedNotif": tnGenericAutoLaserOffDueToUpstreamFaultRaisedNotif,
       "tnGenericAutoLaserOffDueToUpstreamFaultClearedNotif": tnGenericAutoLaserOffDueToUpstreamFaultClearedNotif,
       "tnGenericLagProtLosRaisedNotif": tnGenericLagProtLosRaisedNotif,
       "tnGenericLagProtLosClearedNotif": tnGenericLagProtLosClearedNotif,
       "tnGenericMonitorExcRaisedNotif": tnGenericMonitorExcRaisedNotif,
       "tnGenericMonitorExcClearedNotif": tnGenericMonitorExcClearedNotif,
       "tnGenericEquipmentLedOnRaisedNotif": tnGenericEquipmentLedOnRaisedNotif,
       "tnGenericEquipmentLedOnClearedNotif": tnGenericEquipmentLedOnClearedNotif,
       "tnGenericUnitInitRaisedNotif": tnGenericUnitInitRaisedNotif,
       "tnGenericUnitInitClearedNotif": tnGenericUnitInitClearedNotif,
       "tnGenericCardMismatchRaisedNotif": tnGenericCardMismatchRaisedNotif,
       "tnGenericCardMismatchClearedNotif": tnGenericCardMismatchClearedNotif,
       "tnGenericTPmonSlmxnflrContRaisedNotif": tnGenericTPmonSlmxnflrContRaisedNotif,
       "tnGenericTPmonSlmxnflrContClearedNotif": tnGenericTPmonSlmxnflrContClearedNotif,
       "tnGenericOpticalOutputPowerUnachievableRaisedNotif": tnGenericOpticalOutputPowerUnachievableRaisedNotif,
       "tnGenericOpticalOutputPowerUnachievableClearedNotif": tnGenericOpticalOutputPowerUnachievableClearedNotif,
       "tnGenericDiagnosticTerminalLoopbackActiveRaisedNotif": tnGenericDiagnosticTerminalLoopbackActiveRaisedNotif,
       "tnGenericDiagnosticTerminalLoopbackActiveClearedNotif": tnGenericDiagnosticTerminalLoopbackActiveClearedNotif,
       "tnGenericLocalFaultRaisedNotif": tnGenericLocalFaultRaisedNotif,
       "tnGenericLocalFaultClearedNotif": tnGenericLocalFaultClearedNotif,
       "tnGenericRemoteFailureIndicationRaisedNotif": tnGenericRemoteFailureIndicationRaisedNotif,
       "tnGenericRemoteFailureIndicationClearedNotif": tnGenericRemoteFailureIndicationClearedNotif,
       "tnGenericOduClientSignalFailureRaisedNotif": tnGenericOduClientSignalFailureRaisedNotif,
       "tnGenericOduClientSignalFailureClearedNotif": tnGenericOduClientSignalFailureClearedNotif,
       "tnGenericPRBSLSSRaisedNotif": tnGenericPRBSLSSRaisedNotif,
       "tnGenericPRBSLSSClearedNotif": tnGenericPRBSLSSClearedNotif,
       "tnGenericCsfGfpRaisedNotif": tnGenericCsfGfpRaisedNotif,
       "tnGenericCsfGfpClearedNotif": tnGenericCsfGfpClearedNotif,
       "tnGenericGfpExmRaisedNotif": tnGenericGfpExmRaisedNotif,
       "tnGenericGfpExmClearedNotif": tnGenericGfpExmClearedNotif,
       "tnGenericGfpLofRaisedNotif": tnGenericGfpLofRaisedNotif,
       "tnGenericGfpLofClearedNotif": tnGenericGfpLofClearedNotif,
       "tnGenericGfpUpmRaisedNotif": tnGenericGfpUpmRaisedNotif,
       "tnGenericGfpUpmClearedNotif": tnGenericGfpUpmClearedNotif,
       "tnGenericLOFLOMRaisedNotif": tnGenericLOFLOMRaisedNotif,
       "tnGenericLOFLOMClearedNotif": tnGenericLOFLOMClearedNotif,
       "tnGenericMsimRaisedNotif": tnGenericMsimRaisedNotif,
       "tnGenericMsimClearedNotif": tnGenericMsimClearedNotif,
       "tnGenericPayloadTypeMismatchRaisedNotif": tnGenericPayloadTypeMismatchRaisedNotif,
       "tnGenericPayloadTypeMismatchClearedNotif": tnGenericPayloadTypeMismatchClearedNotif,
       "tnGenericIntrusionRaisedNotif": tnGenericIntrusionRaisedNotif,
       "tnGenericIntrusionClearedNotif": tnGenericIntrusionClearedNotif,
       "tnGenericNtpOutOfSyncRaisedNotif": tnGenericNtpOutOfSyncRaisedNotif,
       "tnGenericNtpOutOfSyncClearedNotif": tnGenericNtpOutOfSyncClearedNotif,
       "tnGenericTxAutoLaserShutdownRaisedNotif": tnGenericTxAutoLaserShutdownRaisedNotif,
       "tnGenericTxAutoLaserShutdownClearedNotif": tnGenericTxAutoLaserShutdownClearedNotif,
       "tnGenericTBerPreFec15minRaisedNotif": tnGenericTBerPreFec15minRaisedNotif,
       "tnGenericTBerPreFec15minClearedNotif": tnGenericTBerPreFec15minClearedNotif,
       "tnGenericTBerPreFec1dayRaisedNotif": tnGenericTBerPreFec1dayRaisedNotif,
       "tnGenericTBerPreFec1dayClearedNotif": tnGenericTBerPreFec1dayClearedNotif,
       "tnGenericTBerPostFec15minRaisedNotif": tnGenericTBerPostFec15minRaisedNotif,
       "tnGenericTBerPostFec15minClearedNotif": tnGenericTBerPostFec15minClearedNotif,
       "tnGenericTBerPostFec1dayRaisedNotif": tnGenericTBerPostFec1dayRaisedNotif,
       "tnGenericTBerPostFec1dayClearedNotif": tnGenericTBerPostFec1dayClearedNotif,
       "tnGenericUruSRaisedNotif": tnGenericUruSRaisedNotif,
       "tnGenericUruSClearedNotif": tnGenericUruSClearedNotif,
       "tnGenericNeCertValidityWarnRaisedNotif": tnGenericNeCertValidityWarnRaisedNotif,
       "tnGenericNeCertValidityWarnClearedNotif": tnGenericNeCertValidityWarnClearedNotif,
       "tnGenericNeCertValidityExpRaisedNotif": tnGenericNeCertValidityExpRaisedNotif,
       "tnGenericNeCertValidityExpClearedNotif": tnGenericNeCertValidityExpClearedNotif,
       "tnGenericVoltageLowRaisedNotif": tnGenericVoltageLowRaisedNotif,
       "tnGenericVoltageLowClearedNotif": tnGenericVoltageLowClearedNotif,
       "tnGenericAlarmConformance": tnGenericAlarmConformance,
       "tnGenericAlarmCompliances": tnGenericAlarmCompliances,
       "tnGenericAlarmCompliance": tnGenericAlarmCompliance,
       "tnGenericAlarmGroups": tnGenericAlarmGroups,
       "tnGenericAlarmNotifsGroup": tnGenericAlarmNotifsGroup,
       "tnGenericEvent": tnGenericEvent,
       "tnGenericEventNotifs": tnGenericEventNotifs,
       "tnGenericPmBinsRolledOverNotif": tnGenericPmBinsRolledOverNotif,
       "tnGenericSecurityFileNameNotif": tnGenericSecurityFileNameNotif,
       "tnGenericSecurityLoginNotif": tnGenericSecurityLoginNotif,
       "tnGenericSecurityLogoutNotif": tnGenericSecurityLogoutNotif,
       "tnGenericSecurityAddAccountNotif": tnGenericSecurityAddAccountNotif,
       "tnGenericSecurityDeleteAccountNotif": tnGenericSecurityDeleteAccountNotif,
       "tnGenericSecurityChangeAccountNotif": tnGenericSecurityChangeAccountNotif,
       "tnGenericSubgroupSelectNotif": tnGenericSubgroupSelectNotif,
       "tnGenericDot1agCfmDmTestCompleteNotif": tnGenericDot1agCfmDmTestCompleteNotif,
       "tnGenericDot1agCfmSlmTestCompleteNotif": tnGenericDot1agCfmSlmTestCompleteNotif,
       "tnGenericDot1agCfmLmTestCompleteNotif": tnGenericDot1agCfmLmTestCompleteNotif,
       "tnGenericSecurityExceededLoginAttemptsNotif": tnGenericSecurityExceededLoginAttemptsNotif,
       "tnGenericSecurityLockAccountNotif": tnGenericSecurityLockAccountNotif,
       "tnGenericSecurityUnlockAccountNotif": tnGenericSecurityUnlockAccountNotif,
       "tnGenericSecurityUnauthAccessAttemptNotif": tnGenericSecurityUnauthAccessAttemptNotif,
       "tnGenericSecurityEnableInterfaceNotif": tnGenericSecurityEnableInterfaceNotif,
       "tnGenericSecurityDisableInterfaceNotif": tnGenericSecurityDisableInterfaceNotif,
       "tnGenericDiscoverMeNotif": tnGenericDiscoverMeNotif,
       "tnGenericEventConformance": tnGenericEventConformance,
       "tnGenericEventCompliances": tnGenericEventCompliances,
       "tnGenericEventCompliance": tnGenericEventCompliance,
       "tnGenericEventGroups": tnGenericEventGroups,
       "tnGenericEventNotifsGroup": tnGenericEventNotifsGroup,
       "tnGenericScalar": tnGenericScalar,
       "tnGenericScalarNotifs": tnGenericScalarNotifs,
       "tnGenericScalarChangeNotif": tnGenericScalarChangeNotif,
       "tnGenericScalarConformance": tnGenericScalarConformance,
       "tnGenericScalarCompliances": tnGenericScalarCompliances,
       "tnGenericScalarCompliance": tnGenericScalarCompliance,
       "tnGenericScalarGroups": tnGenericScalarGroups,
       "tnGenericScalarConfigChangeNotifGroup": tnGenericScalarConfigChangeNotifGroup,
       "tnGenericInterface": tnGenericInterface,
       "tnGenericInterfaceNotifs": tnGenericInterfaceNotifs,
       "tnGenericIfConfigChangeNotif": tnGenericIfConfigChangeNotif,
       "tnGenericIfOperStatusChangeNotif": tnGenericIfOperStatusChangeNotif,
       "tnGenericInterfaceConformance": tnGenericInterfaceConformance,
       "tnGenericInterfaceCompliances": tnGenericInterfaceCompliances,
       "tnGenericInterfaceCompliance": tnGenericInterfaceCompliance,
       "tnGenericInterfaceGroups": tnGenericInterfaceGroups,
       "tnGenericInterfaceConfigChangeNotifGroup": tnGenericInterfaceConfigChangeNotifGroup,
       "tnGenericInterfaceStateChangeNotifGroup": tnGenericInterfaceStateChangeNotifGroup,
       "tnGenericOptIf": tnGenericOptIf,
       "tnGenericOptIfNotifs": tnGenericOptIfNotifs,
       "tnGenericOptIfOTUkConfigChangeNotif": tnGenericOptIfOTUkConfigChangeNotif,
       "tnGenericOptIfConformance": tnGenericOptIfConformance,
       "tnGenericOptIfCompliances": tnGenericOptIfCompliances,
       "tnGenericOptIfCompliance": tnGenericOptIfCompliance,
       "tnGenericOptIfGroups": tnGenericOptIfGroups,
       "tnGenericOptIfConfigChangeNotifGroup": tnGenericOptIfConfigChangeNotifGroup,
       "tnGenericTnAccessPort": tnGenericTnAccessPort,
       "tnGenericTnAccessPortNotifs": tnGenericTnAccessPortNotifs,
       "tnGenericTnAccessPortConfigChangeNotif": tnGenericTnAccessPortConfigChangeNotif,
       "tnGenericTnIfConfigChangeNotif": tnGenericTnIfConfigChangeNotif,
       "tnGenericTnAccessPortConformance": tnGenericTnAccessPortConformance,
       "tnGenericTnAccessPortCompliances": tnGenericTnAccessPortCompliances,
       "tnGenericTnAccessPortCompliance": tnGenericTnAccessPortCompliance,
       "tnGenericTnAccessPortGroups": tnGenericTnAccessPortGroups,
       "tnGenericTnAccessPortConfigChangeNotifGroup": tnGenericTnAccessPortConfigChangeNotifGroup,
       "tnGenericTnOpticalPort": tnGenericTnOpticalPort,
       "tnGenericTnOpticalPortNotifs": tnGenericTnOpticalPortNotifs,
       "tnGenericTnLoopbackPortConfigChangeNotif": tnGenericTnLoopbackPortConfigChangeNotif,
       "tnGenericTnDwdmCmnClientPortConfigChangeNotif": tnGenericTnDwdmCmnClientPortConfigChangeNotif,
       "tnGenericTnOpticalPortConformance": tnGenericTnOpticalPortConformance,
       "tnGenericTnOpticalPortCompliances": tnGenericTnOpticalPortCompliances,
       "tnGenericTnOpticalPortCompliance": tnGenericTnOpticalPortCompliance,
       "tnGenericTnOpticalPortGroups": tnGenericTnOpticalPortGroups,
       "tnGenericTnOpticalPortConfigChangeNotifGroup": tnGenericTnOpticalPortConfigChangeNotifGroup,
       "tnGenericTnOtuOdu": tnGenericTnOtuOdu,
       "tnGenericTnOtuOduNotifs": tnGenericTnOtuOduNotifs,
       "tnGenericTnOtukConfigChangeNotif": tnGenericTnOtukConfigChangeNotif,
       "tnGenericTnOtuOduConformance": tnGenericTnOtuOduConformance,
       "tnGenericTnOtuOduCompliances": tnGenericTnOtuOduCompliances,
       "tnGenericTnOtuOduCompliance": tnGenericTnOtuOduCompliance,
       "tnGenericTnOtuOduGroups": tnGenericTnOtuOduGroups,
       "tnGenericTnOtuOduConfigChangeNotifGroup": tnGenericTnOtuOduConfigChangeNotifGroup,
       "tnGenericTnOth": tnGenericTnOth,
       "tnGenericTnOthNotifs": tnGenericTnOthNotifs,
       "tnGenericTnOthOdukNimConfigChangeNotif": tnGenericTnOthOdukNimConfigChangeNotif,
       "tnGenericTnOthOdukTtpConfigChangeNotif": tnGenericTnOthOdukTtpConfigChangeNotif,
       "tnGenericTnOthOdukTConfigChangeNotif": tnGenericTnOthOdukTConfigChangeNotif,
       "tnGenericTnOthOdukTCreationNotif": tnGenericTnOthOdukTCreationNotif,
       "tnGenericTnOthOdukTDeletionNotif": tnGenericTnOthOdukTDeletionNotif,
       "tnGenericTnOthOdukApsGroupConfigChangeNotif": tnGenericTnOthOdukApsGroupConfigChangeNotif,
       "tnGenericTnOthOdukXcConfigChangeNotif": tnGenericTnOthOdukXcConfigChangeNotif,
       "tnGenericTnOthOdukApsGroupConvertNotif": tnGenericTnOthOdukApsGroupConvertNotif,
       "tnGenericTnOthOdukXcCreationNotif": tnGenericTnOthOdukXcCreationNotif,
       "tnGenericTnOthOdukXcDeletionNotif": tnGenericTnOthOdukXcDeletionNotif,
       "tnGenericTnOthConformance": tnGenericTnOthConformance,
       "tnGenericTnOthCompliances": tnGenericTnOthCompliances,
       "tnGenericTnOthCompliance": tnGenericTnOthCompliance,
       "tnGenericTnOthGroups": tnGenericTnOthGroups,
       "tnGenericTnOthConfigChangeNotifGroup": tnGenericTnOthConfigChangeNotifGroup,
       "tnGenericTnOthCreDelNotifGroup": tnGenericTnOthCreDelNotifGroup,
       "tnGenericTnL1Service": tnGenericTnL1Service,
       "tnGenericTnL1ServiceNotifs": tnGenericTnL1ServiceNotifs,
       "tnGenericTnNetIfConfigChangeNotif": tnGenericTnNetIfConfigChangeNotif,
       "tnGenericTnNetIfFacilityConfigChangeNotif": tnGenericTnNetIfFacilityConfigChangeNotif,
       "tnGenericTnNetIfFacilityCreationNotif": tnGenericTnNetIfFacilityCreationNotif,
       "tnGenericTnNetIfFacilityDeletionNotif": tnGenericTnNetIfFacilityDeletionNotif,
       "tnGenericTnControlNetworkLinkConfigChangeNotif": tnGenericTnControlNetworkLinkConfigChangeNotif,
       "tnGenericTnControlNetworkLinkStateChangeNotif": tnGenericTnControlNetworkLinkStateChangeNotif,
       "tnGenericTnL1ServiceConformance": tnGenericTnL1ServiceConformance,
       "tnGenericTnL1ServiceCompliances": tnGenericTnL1ServiceCompliances,
       "tnGenericTnL1ServiceCompliance": tnGenericTnL1ServiceCompliance,
       "tnGenericTnL1ServiceGroups": tnGenericTnL1ServiceGroups,
       "tnGenericTnL1ServiceConfigChangeNotifGroup": tnGenericTnL1ServiceConfigChangeNotifGroup,
       "tnGenericTnL1ServiceCreDelNotifGroup": tnGenericTnL1ServiceCreDelNotifGroup,
       "tnGenericTnL1ServiceStateChangeNotifGroup": tnGenericTnL1ServiceStateChangeNotifGroup,
       "tnGenericTnStatistics": tnGenericTnStatistics,
       "tnGenericTnStatisticsNotifs": tnGenericTnStatisticsNotifs,
       "tnGenericTnStatsTCAProfileConfigChangeNotif": tnGenericTnStatsTCAProfileConfigChangeNotif,
       "tnGenericTnStatsTCAConfigChangeNotif": tnGenericTnStatsTCAConfigChangeNotif,
       "tnGenericTnOtuStatsPortConfigChangeNotif": tnGenericTnOtuStatsPortConfigChangeNotif,
       "tnGenericTnOdukStatsTcmConfigChangeNotif": tnGenericTnOdukStatsTcmConfigChangeNotif,
       "tnGenericTnOdukStatsRxConfigChangeNotif": tnGenericTnOdukStatsRxConfigChangeNotif,
       "tnGenericTnStatisticsConformance": tnGenericTnStatisticsConformance,
       "tnGenericTnStatisticsCompliances": tnGenericTnStatisticsCompliances,
       "tnGenericTnStatisticsCompliance": tnGenericTnStatisticsCompliance,
       "tnGenericTnStatisticsGroups": tnGenericTnStatisticsGroups,
       "tnGenericTnStatisticsConfigChangeNotifGroup": tnGenericTnStatisticsConfigChangeNotifGroup,
       "tnGenericTnLag": tnGenericTnLag,
       "tnGenericTnLagNotifs": tnGenericTnLagNotifs,
       "tnGenericTnLagPortConfigChangeNotif": tnGenericTnLagPortConfigChangeNotif,
       "tnGenericTnLagCommandConfigChangeNotif": tnGenericTnLagCommandConfigChangeNotif,
       "tnGenericTnLagConformance": tnGenericTnLagConformance,
       "tnGenericTnLagCompliances": tnGenericTnLagCompliances,
       "tnGenericTnLagCompliance": tnGenericTnLagCompliance,
       "tnGenericTnLagGroups": tnGenericTnLagGroups,
       "tnGenericTnLagConfigChangeNotifGroup": tnGenericTnLagConfigChangeNotifGroup,
       "tnGenericTnPmon": tnGenericTnPmon,
       "tnGenericTnPmonNotifs": tnGenericTnPmonNotifs,
       "tnGenericTnPmonPolicyConfigChangeNotif": tnGenericTnPmonPolicyConfigChangeNotif,
       "tnGenericTnPmonTcaConfigChangeNotif": tnGenericTnPmonTcaConfigChangeNotif,
       "tnGenericTnPmonConformance": tnGenericTnPmonConformance,
       "tnGenericTnPmonCompliances": tnGenericTnPmonCompliances,
       "tnGenericTnPmonCompliance": tnGenericTnPmonCompliance,
       "tnGenericTnPmonGroups": tnGenericTnPmonGroups,
       "tnGenericTnPmonConfigChangeNotifGroup": tnGenericTnPmonConfigChangeNotifGroup,
       "tnGenericTnPort": tnGenericTnPort,
       "tnGenericTnPortNotifs": tnGenericTnPortNotifs,
       "tnGenericTnPortEtherConfigChangeNotif": tnGenericTnPortEtherConfigChangeNotif,
       "tnGenericTnPortConformance": tnGenericTnPortConformance,
       "tnGenericTnPortCompliances": tnGenericTnPortCompliances,
       "tnGenericTnPortCompliance": tnGenericTnPortCompliance,
       "tnGenericTnPortGroups": tnGenericTnPortGroups,
       "tnGenericTnPortConfigChangeNotifGroup": tnGenericTnPortConfigChangeNotifGroup,
       "tnGenericDot1agCfm": tnGenericDot1agCfm,
       "tnGenericDot1agCfmNotifs": tnGenericDot1agCfmNotifs,
       "tnGenericDot1agCfmMdConfigChangeNotif": tnGenericDot1agCfmMdConfigChangeNotif,
       "tnGenericDot1agCfmMdCreationNotif": tnGenericDot1agCfmMdCreationNotif,
       "tnGenericDot1agCfmMdDeletionNotif": tnGenericDot1agCfmMdDeletionNotif,
       "tnGenericDot1agCfmMaNetConfigChangeNotif": tnGenericDot1agCfmMaNetConfigChangeNotif,
       "tnGenericDot1agCfmMaNetCreationNotif": tnGenericDot1agCfmMaNetCreationNotif,
       "tnGenericDot1agCfmMaNetDeletionNotif": tnGenericDot1agCfmMaNetDeletionNotif,
       "tnGenericDot1agCfmMaCompConfigChangeNotif": tnGenericDot1agCfmMaCompConfigChangeNotif,
       "tnGenericDot1agCfmMaCompCreationNotif": tnGenericDot1agCfmMaCompCreationNotif,
       "tnGenericDot1agCfmMaCompDeletionNotif": tnGenericDot1agCfmMaCompDeletionNotif,
       "tnGenericDot1agCfmMaMepListCreationNotif": tnGenericDot1agCfmMaMepListCreationNotif,
       "tnGenericDot1agCfmMaMepListDeletionNotif": tnGenericDot1agCfmMaMepListDeletionNotif,
       "tnGenericDot1agCfmMepConfigChangeNotif": tnGenericDot1agCfmMepConfigChangeNotif,
       "tnGenericDot1agCfmMepCreationNotif": tnGenericDot1agCfmMepCreationNotif,
       "tnGenericDot1agCfmMepDeletionNotif": tnGenericDot1agCfmMepDeletionNotif,
       "tnGenericDot1agCfmConformance": tnGenericDot1agCfmConformance,
       "tnGenericDot1agCfmCompliances": tnGenericDot1agCfmCompliances,
       "tnGenericDot1agCfmCompliance": tnGenericDot1agCfmCompliance,
       "tnGenericDot1agCfmGroups": tnGenericDot1agCfmGroups,
       "tnGenericDot1agCfmConfigChangeNotifGroup": tnGenericDot1agCfmConfigChangeNotifGroup,
       "tnGenericDot1agCfmCreDelNotifGroup": tnGenericDot1agCfmCreDelNotifGroup,
       "tnGenericTnDot1agCfm": tnGenericTnDot1agCfm,
       "tnGenericTnDot1agCfmNotifs": tnGenericTnDot1agCfmNotifs,
       "tnGenericTnDot1agCfmMepConfigChangeNotif": tnGenericTnDot1agCfmMepConfigChangeNotif,
       "tnGenericTnDot1agCfmMepSlmTWTestConfigChangeNotif": tnGenericTnDot1agCfmMepSlmTWTestConfigChangeNotif,
       "tnGenericTnDot1agCfmMepOndemandLmTestConfigChangeNotif": tnGenericTnDot1agCfmMepOndemandLmTestConfigChangeNotif,
       "tnGenericTnDot1agCfmConformance": tnGenericTnDot1agCfmConformance,
       "tnGenericTnDot1agCfmCompliances": tnGenericTnDot1agCfmCompliances,
       "tnGenericTnDot1agCfmCompliance": tnGenericTnDot1agCfmCompliance,
       "tnGenericTnDot1agCfmGroups": tnGenericTnDot1agCfmGroups,
       "tnGenericTnDot1agCfmConfigChangeNotifGroup": tnGenericTnDot1agCfmConfigChangeNotifGroup,
       "tnGenericTnOamTest": tnGenericTnOamTest,
       "tnGenericTnOamTestNotifs": tnGenericTnOamTestNotifs,
       "tnGenericTnOamPingCtlCreationNotif": tnGenericTnOamPingCtlCreationNotif,
       "tnGenericTnOamPingCtlDeletionNotif": tnGenericTnOamPingCtlDeletionNotif,
       "tnGenericTnOamSaaCtlConfigChangeNotif": tnGenericTnOamSaaCtlConfigChangeNotif,
       "tnGenericTnOamTestConformance": tnGenericTnOamTestConformance,
       "tnGenericTnOamTestCompliances": tnGenericTnOamTestCompliances,
       "tnGenericTnOamTestCompliance": tnGenericTnOamTestCompliance,
       "tnGenericTnOamTestGroups": tnGenericTnOamTestGroups,
       "tnGenericTnOamTestConfigChangeNotifGroup": tnGenericTnOamTestConfigChangeNotifGroup,
       "tnGenericTnOamTestCreDelNotifGroup": tnGenericTnOamTestCreDelNotifGroup,
       "tnGenericRadius": tnGenericRadius,
       "tnGenericRadiusNotifs": tnGenericRadiusNotifs,
       "tnGenericRadiusServerCreationNotif": tnGenericRadiusServerCreationNotif,
       "tnGenericRadiusServerDeletionNotif": tnGenericRadiusServerDeletionNotif,
       "tnGenericRadiusServerConfigChangeNotif": tnGenericRadiusServerConfigChangeNotif,
       "tnGenericRadiusConformance": tnGenericRadiusConformance,
       "tnGenericRadiusCompliances": tnGenericRadiusCompliances,
       "tnGenericRadiusCompliance": tnGenericRadiusCompliance,
       "tnGenericRadiusGroups": tnGenericRadiusGroups,
       "tnGenericRadiusNotifGroup": tnGenericRadiusNotifGroup,
       "tnGenericSyslog": tnGenericSyslog,
       "tnGenericSyslogNotifs": tnGenericSyslogNotifs,
       "tnGenericSyslogServerCreationNotif": tnGenericSyslogServerCreationNotif,
       "tnGenericSyslogServerDeletionNotif": tnGenericSyslogServerDeletionNotif,
       "tnGenericSyslogServerConfigChangeNotif": tnGenericSyslogServerConfigChangeNotif,
       "tnGenericSyslogConformance": tnGenericSyslogConformance,
       "tnGenericSyslogCompliances": tnGenericSyslogCompliances,
       "tnGenericSyslogCompliance": tnGenericSyslogCompliance,
       "tnGenericSyslogGroups": tnGenericSyslogGroups,
       "tnGenericSyslogNotifGroup": tnGenericSyslogNotifGroup,
       "tnGenericTransferPMDiscovery": tnGenericTransferPMDiscovery,
       "tnGenericTransferPMDiscoveryNotifs": tnGenericTransferPMDiscoveryNotifs,
       "tnGenericTransferPMDiscoveryCreationNotif": tnGenericTransferPMDiscoveryCreationNotif,
       "tnGenericTransferPMDiscoveryDeletionNotif": tnGenericTransferPMDiscoveryDeletionNotif,
       "tnGenericTransferPMDiscoveryConfigChangeNotif": tnGenericTransferPMDiscoveryConfigChangeNotif,
       "tnGenericTransferPMDiscoveryConformance": tnGenericTransferPMDiscoveryConformance,
       "tnGenericTransferPMDiscoveryCompliances": tnGenericTransferPMDiscoveryCompliances,
       "tnGenericTransferPMDiscoveryCompliance": tnGenericTransferPMDiscoveryCompliance,
       "tnGenericTransferPMDiscoveryGroups": tnGenericTransferPMDiscoveryGroups,
       "tnGenericTransferPMDiscoveryNotifGroup": tnGenericTransferPMDiscoveryNotifGroup}
)
