# SNMP MIB module (DASAN-DSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-DSL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:03 2025
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

(dasanMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dasanDslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanDslMIBObjects_ObjectIdentity = ObjectIdentity
dasanDslMIBObjects = _DasanDslMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1)
)
_DsDslSystem_ObjectIdentity = ObjectIdentity
dsDslSystem = _DsDslSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 1)
)
_DsDslModules_ObjectIdentity = ObjectIdentity
dsDslModules = _DsDslModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2)
)
_ModuleNumber_Type = Integer32
_ModuleNumber_Object = MibScalar
moduleNumber = _ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 1),
    _ModuleNumber_Type()
)
moduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumber.setStatus("obsolete")
_ModuleTableLastChange_Type = TimeTicks
_ModuleTableLastChange_Object = MibScalar
moduleTableLastChange = _ModuleTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 2),
    _ModuleTableLastChange_Type()
)
moduleTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTableLastChange.setStatus("obsolete")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1)
)
moduleEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")
_ModuleIndex_Type = Integer32
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("obsolete")
_ModuleDescr_Type = DisplayString
_ModuleDescr_Object = MibTableColumn
moduleDescr = _ModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 2),
    _ModuleDescr_Type()
)
moduleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescr.setStatus("obsolete")
_ModuleType_Type = DisplayString
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 3),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("obsolete")
_ModulePhysAddress_Type = PhysAddress
_ModulePhysAddress_Object = MibTableColumn
modulePhysAddress = _ModulePhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 4),
    _ModulePhysAddress_Type()
)
modulePhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePhysAddress.setStatus("obsolete")


class _ModuleOperStatus_Type(Integer32):
    """Custom type moduleOperStatus based on Integer32"""
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


_ModuleOperStatus_Type.__name__ = "Integer32"
_ModuleOperStatus_Object = MibTableColumn
moduleOperStatus = _ModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 5),
    _ModuleOperStatus_Type()
)
moduleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleOperStatus.setStatus("obsolete")
_ModuleUpTime_Type = DisplayString
_ModuleUpTime_Object = MibTableColumn
moduleUpTime = _ModuleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 6),
    _ModuleUpTime_Type()
)
moduleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleUpTime.setStatus("obsolete")
_ModuleAvailableMemory_Type = Integer32
_ModuleAvailableMemory_Object = MibTableColumn
moduleAvailableMemory = _ModuleAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 7),
    _ModuleAvailableMemory_Type()
)
moduleAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAvailableMemory.setStatus("obsolete")
_ModulePortNumber_Type = Integer32
_ModulePortNumber_Object = MibTableColumn
modulePortNumber = _ModulePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 8),
    _ModulePortNumber_Type()
)
modulePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePortNumber.setStatus("obsolete")
_ModulePortIndexBase_Type = Integer32
_ModulePortIndexBase_Object = MibTableColumn
modulePortIndexBase = _ModulePortIndexBase_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 9),
    _ModulePortIndexBase_Type()
)
modulePortIndexBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePortIndexBase.setStatus("obsolete")
_ModuleSpecific_Type = ObjectIdentifier
_ModuleSpecific_Object = MibTableColumn
moduleSpecific = _ModuleSpecific_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 2, 3, 1, 10),
    _ModuleSpecific_Type()
)
moduleSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSpecific.setStatus("obsolete")
_DsDslPorts_ObjectIdentity = ObjectIdentity
dsDslPorts = _DsDslPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3)
)
_DsDslPortNumber_Type = Integer32
_DsDslPortNumber_Object = MibScalar
dsDslPortNumber = _DsDslPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 1),
    _DsDslPortNumber_Type()
)
dsDslPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDslPortNumber.setStatus("obsolete")
_DsDslPortTable_Object = MibTable
dsDslPortTable = _DsDslPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dsDslPortTable.setStatus("current")
_DsDslPortEntry_Object = MibTableRow
dsDslPortEntry = _DsDslPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1)
)
dsDslPortEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dsDslPortEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("obsolete")
_PortDescr_Type = DisplayString
_PortDescr_Object = MibTableColumn
portDescr = _PortDescr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 2),
    _PortDescr_Type()
)
portDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDescr.setStatus("obsolete")
_PortType_Type = DisplayString
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("obsolete")
_PortIfIndex_Type = Integer32
_PortIfIndex_Object = MibTableColumn
portIfIndex = _PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 4),
    _PortIfIndex_Type()
)
portIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfIndex.setStatus("obsolete")


class _PortAdminStatus_Type(Integer32):
    """Custom type portAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              26)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 26))
    )


_PortAdminStatus_Type.__name__ = "Integer32"
_PortAdminStatus_Object = MibTableColumn
portAdminStatus = _PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 5),
    _PortAdminStatus_Type()
)
portAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAdminStatus.setStatus("obsolete")


class _PortOperStatus_Type(Integer32):
    """Custom type portOperStatus based on Integer32"""
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


_PortOperStatus_Type.__name__ = "Integer32"
_PortOperStatus_Object = MibTableColumn
portOperStatus = _PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 6),
    _PortOperStatus_Type()
)
portOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperStatus.setStatus("obsolete")


class _PortModemStatus_Type(Integer32):
    """Custom type portModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("trying", 2),
          ("established", 3))
    )


_PortModemStatus_Type.__name__ = "Integer32"
_PortModemStatus_Object = MibTableColumn
portModemStatus = _PortModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 7),
    _PortModemStatus_Type()
)
portModemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portModemStatus.setStatus("obsolete")
_PortLineQuality_Type = DisplayString
_PortLineQuality_Object = MibTableColumn
portLineQuality = _PortLineQuality_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 8),
    _PortLineQuality_Type()
)
portLineQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineQuality.setStatus("obsolete")
_PortUpStreamSpeed_Type = Integer32
_PortUpStreamSpeed_Object = MibTableColumn
portUpStreamSpeed = _PortUpStreamSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 9),
    _PortUpStreamSpeed_Type()
)
portUpStreamSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUpStreamSpeed.setStatus("obsolete")
_PortDownStreamSpeed_Type = Integer32
_PortDownStreamSpeed_Object = MibTableColumn
portDownStreamSpeed = _PortDownStreamSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 10),
    _PortDownStreamSpeed_Type()
)
portDownStreamSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDownStreamSpeed.setStatus("obsolete")
_PortLastModemStatusChange_Type = DisplayString
_PortLastModemStatusChange_Object = MibTableColumn
portLastModemStatusChange = _PortLastModemStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 11),
    _PortLastModemStatusChange_Type()
)
portLastModemStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastModemStatusChange.setStatus("obsolete")
_PortSpecific_Type = ObjectIdentifier
_PortSpecific_Object = MibTableColumn
portSpecific = _PortSpecific_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 3, 2, 1, 12),
    _PortSpecific_Type()
)
portSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpecific.setStatus("obsolete")
_DsDslLearnedMacs_ObjectIdentity = ObjectIdentity
dsDslLearnedMacs = _DsDslLearnedMacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 4)
)
_MacNumber_Type = Integer32
_MacNumber_Object = MibScalar
macNumber = _MacNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 4, 1),
    _MacNumber_Type()
)
macNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macNumber.setStatus("obsolete")
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    macTable.setStatus("current")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 4, 2, 1)
)
macEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "macIndex"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("deprecated")
_MacIndex_Type = Integer32
_MacIndex_Object = MibTableColumn
macIndex = _MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 4, 2, 1, 1),
    _MacIndex_Type()
)
macIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macIndex.setStatus("obsolete")
_MacAddress_Type = PhysAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 4, 2, 1, 2),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("obsolete")
_AgingTime_Type = Integer32
_AgingTime_Object = MibTableColumn
agingTime = _AgingTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 1, 4, 2, 1, 3),
    _AgingTime_Type()
)
agingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agingTime.setStatus("obsolete")
_DasanDslMIBObjects2_ObjectIdentity = ObjectIdentity
dasanDslMIBObjects2 = _DasanDslMIBObjects2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2)
)
_DsVdslNotifications_ObjectIdentity = ObjectIdentity
dsVdslNotifications = _DsVdslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 0)
)
_DsVdslSystemBaseInfo_ObjectIdentity = ObjectIdentity
dsVdslSystemBaseInfo = _DsVdslSystemBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1)
)
_DsVdslSystemFWVersion_Type = OctetString
_DsVdslSystemFWVersion_Object = MibScalar
dsVdslSystemFWVersion = _DsVdslSystemFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 1),
    _DsVdslSystemFWVersion_Type()
)
dsVdslSystemFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslSystemFWVersion.setStatus("current")


class _DsVdslSystemLowPowerMode_Type(Integer32):
    """Custom type dsVdslSystemLowPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DsVdslSystemLowPowerMode_Type.__name__ = "Integer32"
_DsVdslSystemLowPowerMode_Object = MibScalar
dsVdslSystemLowPowerMode = _DsVdslSystemLowPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 2),
    _DsVdslSystemLowPowerMode_Type()
)
dsVdslSystemLowPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslSystemLowPowerMode.setStatus("current")
_DsVdslSystemBmeReset_Type = Integer32
_DsVdslSystemBmeReset_Object = MibScalar
dsVdslSystemBmeReset = _DsVdslSystemBmeReset_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 3),
    _DsVdslSystemBmeReset_Type()
)
dsVdslSystemBmeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslSystemBmeReset.setStatus("current")
_DsVdslSystemUpboConfTable_Object = MibTable
dsVdslSystemUpboConfTable = _DsVdslSystemUpboConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 50)
)
if mibBuilder.loadTexts:
    dsVdslSystemUpboConfTable.setStatus("current")
_DsVdslSystemUpboConfEntry_Object = MibTableRow
dsVdslSystemUpboConfEntry = _DsVdslSystemUpboConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 50, 1)
)
dsVdslSystemUpboConfEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsVdslSystemUpboConfLength"),
)
if mibBuilder.loadTexts:
    dsVdslSystemUpboConfEntry.setStatus("current")
_DsVdslSystemUpboConfLength_Type = Integer32
_DsVdslSystemUpboConfLength_Object = MibTableColumn
dsVdslSystemUpboConfLength = _DsVdslSystemUpboConfLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 50, 1, 1),
    _DsVdslSystemUpboConfLength_Type()
)
dsVdslSystemUpboConfLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslSystemUpboConfLength.setStatus("current")
_DsVdslSystemUpboConfArrayK1_Type = OctetString
_DsVdslSystemUpboConfArrayK1_Object = MibTableColumn
dsVdslSystemUpboConfArrayK1 = _DsVdslSystemUpboConfArrayK1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 50, 1, 2),
    _DsVdslSystemUpboConfArrayK1_Type()
)
dsVdslSystemUpboConfArrayK1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslSystemUpboConfArrayK1.setStatus("current")
_DsVdslSystemUpboConfArrayK2_Type = OctetString
_DsVdslSystemUpboConfArrayK2_Object = MibTableColumn
dsVdslSystemUpboConfArrayK2 = _DsVdslSystemUpboConfArrayK2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 1, 50, 1, 3),
    _DsVdslSystemUpboConfArrayK2_Type()
)
dsVdslSystemUpboConfArrayK2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslSystemUpboConfArrayK2.setStatus("current")
_DsVdslStatus_ObjectIdentity = ObjectIdentity
dsVdslStatus = _DsVdslStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2)
)
_DsVdslStatusBitAlloc_ObjectIdentity = ObjectIdentity
dsVdslStatusBitAlloc = _DsVdslStatusBitAlloc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1)
)
_DsVdslStatusBAIfindex_Type = Integer32
_DsVdslStatusBAIfindex_Object = MibScalar
dsVdslStatusBAIfindex = _DsVdslStatusBAIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 1),
    _DsVdslStatusBAIfindex_Type()
)
dsVdslStatusBAIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslStatusBAIfindex.setStatus("current")


class _DsVdslStatusBAPhySide_Type(Integer32):
    """Custom type dsVdslStatusBAPhySide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_DsVdslStatusBAPhySide_Type.__name__ = "Integer32"
_DsVdslStatusBAPhySide_Object = MibScalar
dsVdslStatusBAPhySide = _DsVdslStatusBAPhySide_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 2),
    _DsVdslStatusBAPhySide_Type()
)
dsVdslStatusBAPhySide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslStatusBAPhySide.setStatus("current")
_DsVdslStatusBASectionSize_Type = Integer32
_DsVdslStatusBASectionSize_Object = MibScalar
dsVdslStatusBASectionSize = _DsVdslStatusBASectionSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 3),
    _DsVdslStatusBASectionSize_Type()
)
dsVdslStatusBASectionSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslStatusBASectionSize.setStatus("current")


class _DsVdslStatusBAAction_Type(Integer32):
    """Custom type dsVdslStatusBAAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("get", 1)
    )


_DsVdslStatusBAAction_Type.__name__ = "Integer32"
_DsVdslStatusBAAction_Object = MibScalar
dsVdslStatusBAAction = _DsVdslStatusBAAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 4),
    _DsVdslStatusBAAction_Type()
)
dsVdslStatusBAAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslStatusBAAction.setStatus("current")


class _DsVdslStatusBAStatus_Type(Integer32):
    """Custom type dsVdslStatusBAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("busy", 2),
          ("passed", 3),
          ("failed", 4))
    )


_DsVdslStatusBAStatus_Type.__name__ = "Integer32"
_DsVdslStatusBAStatus_Object = MibScalar
dsVdslStatusBAStatus = _DsVdslStatusBAStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 5),
    _DsVdslStatusBAStatus_Type()
)
dsVdslStatusBAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslStatusBAStatus.setStatus("current")
_DsVdslStatusBALastTime_Type = OctetString
_DsVdslStatusBALastTime_Object = MibScalar
dsVdslStatusBALastTime = _DsVdslStatusBALastTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 6),
    _DsVdslStatusBALastTime_Type()
)
dsVdslStatusBALastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslStatusBALastTime.setStatus("current")
_DsVdslStatusBATable_Object = MibTable
dsVdslStatusBATable = _DsVdslStatusBATable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dsVdslStatusBATable.setStatus("current")
_DsVdslStatusBAEntry_Object = MibTableRow
dsVdslStatusBAEntry = _DsVdslStatusBAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 7, 1)
)
dsVdslStatusBAEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsVdslStatusBASectionIndex"),
)
if mibBuilder.loadTexts:
    dsVdslStatusBAEntry.setStatus("current")
_DsVdslStatusBASectionIndex_Type = Integer32
_DsVdslStatusBASectionIndex_Object = MibTableColumn
dsVdslStatusBASectionIndex = _DsVdslStatusBASectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 7, 1, 1),
    _DsVdslStatusBASectionIndex_Type()
)
dsVdslStatusBASectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsVdslStatusBASectionIndex.setStatus("current")
_DsVdslStatusBABitLoading_Type = Integer32
_DsVdslStatusBABitLoading_Object = MibTableColumn
dsVdslStatusBABitLoading = _DsVdslStatusBABitLoading_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 2, 1, 7, 1, 2),
    _DsVdslStatusBABitLoading_Type()
)
dsVdslStatusBABitLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslStatusBABitLoading.setStatus("current")
_DsVdslLine_ObjectIdentity = ObjectIdentity
dsVdslLine = _DsVdslLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3)
)
_DsVdslLinePsdShaping_ObjectIdentity = ObjectIdentity
dsVdslLinePsdShaping = _DsVdslLinePsdShaping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1)
)
_DsVdslLinePsdShapingTable_Object = MibTable
dsVdslLinePsdShapingTable = _DsVdslLinePsdShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingTable.setStatus("current")
_DsVdslLinePsdShapingEntry_Object = MibTableRow
dsVdslLinePsdShapingEntry = _DsVdslLinePsdShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1)
)
dsVdslLinePsdShapingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingEntry.setStatus("current")


class _DsVdslLinePsdShapingUsFlag_Type(Integer32):
    """Custom type dsVdslLinePsdShapingUsFlag based on Integer32"""
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
        *(("disable", 0),
          ("enableAuto", 1),
          ("enableManual", 2),
          ("enableStandard", 3))
    )


_DsVdslLinePsdShapingUsFlag_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingUsFlag_Object = MibTableColumn
dsVdslLinePsdShapingUsFlag = _DsVdslLinePsdShapingUsFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 1),
    _DsVdslLinePsdShapingUsFlag_Type()
)
dsVdslLinePsdShapingUsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsFlag.setStatus("current")


class _DsVdslLinePsdShapingUsEwlName_Type(Integer32):
    """Custom type dsVdslLinePsdShapingUsEwlName based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("us0", 0),
          ("us50", 1),
          ("us100", 2),
          ("us150", 3),
          ("us200", 4),
          ("us250", 5),
          ("us300", 6),
          ("us350", 7),
          ("us400", 8),
          ("us450", 9),
          ("us500", 10),
          ("us550", 11),
          ("us600", 12),
          ("us650", 13),
          ("us700", 14),
          ("us750", 15),
          ("us800", 16),
          ("us850", 17),
          ("us900", 18),
          ("us950", 19),
          ("usFull", 20))
    )


_DsVdslLinePsdShapingUsEwlName_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingUsEwlName_Object = MibTableColumn
dsVdslLinePsdShapingUsEwlName = _DsVdslLinePsdShapingUsEwlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 2),
    _DsVdslLinePsdShapingUsEwlName_Type()
)
dsVdslLinePsdShapingUsEwlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsEwlName.setStatus("current")
_DsVdslLinePsdShapingUsEwlLength_Type = Integer32
_DsVdslLinePsdShapingUsEwlLength_Object = MibTableColumn
dsVdslLinePsdShapingUsEwlLength = _DsVdslLinePsdShapingUsEwlLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 3),
    _DsVdslLinePsdShapingUsEwlLength_Type()
)
dsVdslLinePsdShapingUsEwlLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsEwlLength.setStatus("current")
_DsVdslLinePsdShapingUsRetryCount_Type = Integer32
_DsVdslLinePsdShapingUsRetryCount_Object = MibTableColumn
dsVdslLinePsdShapingUsRetryCount = _DsVdslLinePsdShapingUsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 4),
    _DsVdslLinePsdShapingUsRetryCount_Type()
)
dsVdslLinePsdShapingUsRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsRetryCount.setStatus("current")


class _DsVdslLinePsdShapingUsAutoStatus_Type(Integer32):
    """Custom type dsVdslLinePsdShapingUsAutoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("userClear", 1),
          ("linkOn", 2),
          ("training", 3),
          ("adminDown", 4))
    )


_DsVdslLinePsdShapingUsAutoStatus_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingUsAutoStatus_Object = MibTableColumn
dsVdslLinePsdShapingUsAutoStatus = _DsVdslLinePsdShapingUsAutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 5),
    _DsVdslLinePsdShapingUsAutoStatus_Type()
)
dsVdslLinePsdShapingUsAutoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsAutoStatus.setStatus("current")


class _DsVdslLinePsdShapingUsAutoDr_Type(Integer32):
    """Custom type dsVdslLinePsdShapingUsAutoDr based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("us0", 0),
          ("us50", 1),
          ("us100", 2),
          ("us150", 3),
          ("us200", 4),
          ("us250", 5),
          ("us300", 6),
          ("us350", 7),
          ("us400", 8),
          ("us450", 9),
          ("us500", 10),
          ("us550", 11),
          ("us600", 12),
          ("us650", 13),
          ("us700", 14),
          ("us750", 15),
          ("us800", 16),
          ("us850", 17),
          ("us900", 18),
          ("us950", 19),
          ("usFull", 20))
    )


_DsVdslLinePsdShapingUsAutoDr_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingUsAutoDr_Object = MibTableColumn
dsVdslLinePsdShapingUsAutoDr = _DsVdslLinePsdShapingUsAutoDr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 6),
    _DsVdslLinePsdShapingUsAutoDr_Type()
)
dsVdslLinePsdShapingUsAutoDr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsAutoDr.setStatus("current")
_DsVdslLinePsdShapingUsCurrentTryCount_Type = Integer32
_DsVdslLinePsdShapingUsCurrentTryCount_Object = MibTableColumn
dsVdslLinePsdShapingUsCurrentTryCount = _DsVdslLinePsdShapingUsCurrentTryCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 7),
    _DsVdslLinePsdShapingUsCurrentTryCount_Type()
)
dsVdslLinePsdShapingUsCurrentTryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsCurrentTryCount.setStatus("current")
_DsVdslLinePsdShapingUsEwlOnAutoDr_Type = Integer32
_DsVdslLinePsdShapingUsEwlOnAutoDr_Object = MibTableColumn
dsVdslLinePsdShapingUsEwlOnAutoDr = _DsVdslLinePsdShapingUsEwlOnAutoDr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 8),
    _DsVdslLinePsdShapingUsEwlOnAutoDr_Type()
)
dsVdslLinePsdShapingUsEwlOnAutoDr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsEwlOnAutoDr.setStatus("current")


class _DsVdslLinePsdShapingUsClearAutoDr_Type(Integer32):
    """Custom type dsVdslLinePsdShapingUsClearAutoDr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_DsVdslLinePsdShapingUsClearAutoDr_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingUsClearAutoDr_Object = MibTableColumn
dsVdslLinePsdShapingUsClearAutoDr = _DsVdslLinePsdShapingUsClearAutoDr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 11),
    _DsVdslLinePsdShapingUsClearAutoDr_Type()
)
dsVdslLinePsdShapingUsClearAutoDr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsClearAutoDr.setStatus("current")


class _DsVdslLinePsdShapingUsMethodType_Type(Integer32):
    """Custom type dsVdslLinePsdShapingUsMethodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("methodNormal", 0),
          ("method50mTo950m", 1),
          ("method50mToFull", 2))
    )


_DsVdslLinePsdShapingUsMethodType_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingUsMethodType_Object = MibTableColumn
dsVdslLinePsdShapingUsMethodType = _DsVdslLinePsdShapingUsMethodType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 13),
    _DsVdslLinePsdShapingUsMethodType_Type()
)
dsVdslLinePsdShapingUsMethodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsMethodType.setStatus("current")
_DsVdslLinePsdShapingUsStepCount_Type = Integer32
_DsVdslLinePsdShapingUsStepCount_Object = MibTableColumn
dsVdslLinePsdShapingUsStepCount = _DsVdslLinePsdShapingUsStepCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 14),
    _DsVdslLinePsdShapingUsStepCount_Type()
)
dsVdslLinePsdShapingUsStepCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingUsStepCount.setStatus("current")


class _DsVdslLinePsdShapingDsFlag_Type(Integer32):
    """Custom type dsVdslLinePsdShapingDsFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DsVdslLinePsdShapingDsFlag_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingDsFlag_Object = MibTableColumn
dsVdslLinePsdShapingDsFlag = _DsVdslLinePsdShapingDsFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 21),
    _DsVdslLinePsdShapingDsFlag_Type()
)
dsVdslLinePsdShapingDsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingDsFlag.setStatus("current")


class _DsVdslLinePsdShapingDsEwlName_Type(Integer32):
    """Custom type dsVdslLinePsdShapingDsEwlName based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ds0", 0),
          ("ds250", 1),
          ("ds500", 2),
          ("ds750", 3),
          ("ds1000", 4),
          ("ds1250", 5),
          ("ds1500", 6),
          ("ds1750", 7),
          ("ds2000", 8),
          ("ds2250", 9),
          ("ds2500", 10),
          ("ds2750", 11),
          ("ds3000", 12),
          ("ds3250", 13),
          ("ds3500", 14),
          ("ds3750", 15),
          ("ds4000", 16),
          ("ds4250", 17),
          ("ds4500", 18),
          ("ds4750", 19))
    )


_DsVdslLinePsdShapingDsEwlName_Type.__name__ = "Integer32"
_DsVdslLinePsdShapingDsEwlName_Object = MibTableColumn
dsVdslLinePsdShapingDsEwlName = _DsVdslLinePsdShapingDsEwlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 22),
    _DsVdslLinePsdShapingDsEwlName_Type()
)
dsVdslLinePsdShapingDsEwlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingDsEwlName.setStatus("current")
_DsVdslLinePsdShapingDsEwlLength_Type = Integer32
_DsVdslLinePsdShapingDsEwlLength_Object = MibTableColumn
dsVdslLinePsdShapingDsEwlLength = _DsVdslLinePsdShapingDsEwlLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 23),
    _DsVdslLinePsdShapingDsEwlLength_Type()
)
dsVdslLinePsdShapingDsEwlLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingDsEwlLength.setStatus("current")
_DsVdslLinePsdShapingDsFreqMin_Type = Integer32
_DsVdslLinePsdShapingDsFreqMin_Object = MibTableColumn
dsVdslLinePsdShapingDsFreqMin = _DsVdslLinePsdShapingDsFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 24),
    _DsVdslLinePsdShapingDsFreqMin_Type()
)
dsVdslLinePsdShapingDsFreqMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingDsFreqMin.setStatus("current")
_DsVdslLinePsdShapingDsFreqMax_Type = Integer32
_DsVdslLinePsdShapingDsFreqMax_Object = MibTableColumn
dsVdslLinePsdShapingDsFreqMax = _DsVdslLinePsdShapingDsFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 1, 1, 1, 25),
    _DsVdslLinePsdShapingDsFreqMax_Type()
)
dsVdslLinePsdShapingDsFreqMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLinePsdShapingDsFreqMax.setStatus("current")
_DsVdslLineConfig_ObjectIdentity = ObjectIdentity
dsVdslLineConfig = _DsVdslLineConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2)
)
_DsVdslLineConfigTable_Object = MibTable
dsVdslLineConfigTable = _DsVdslLineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dsVdslLineConfigTable.setStatus("current")
_DsVdslLineConfigEntry_Object = MibTableRow
dsVdslLineConfigEntry = _DsVdslLineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1)
)
dsVdslLineConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsVdslLineConfigEntry.setStatus("current")


class _DsVdslLineConfMicroCut_Type(Integer32):
    """Custom type dsVdslLineConfMicroCut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsVdslLineConfMicroCut_Type.__name__ = "Integer32"
_DsVdslLineConfMicroCut_Object = MibTableColumn
dsVdslLineConfMicroCut = _DsVdslLineConfMicroCut_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 1),
    _DsVdslLineConfMicroCut_Type()
)
dsVdslLineConfMicroCut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfMicroCut.setStatus("current")


class _DsVdslLineConfigMicroCutThreshold_Type(Integer32):
    """Custom type dsVdslLineConfigMicroCutThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DsVdslLineConfigMicroCutThreshold_Type.__name__ = "Integer32"
_DsVdslLineConfigMicroCutThreshold_Object = MibTableColumn
dsVdslLineConfigMicroCutThreshold = _DsVdslLineConfigMicroCutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 2),
    _DsVdslLineConfigMicroCutThreshold_Type()
)
dsVdslLineConfigMicroCutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigMicroCutThreshold.setStatus("current")
_DsVdslLineConfigMicroCutStatTotal_Type = Integer32
_DsVdslLineConfigMicroCutStatTotal_Object = MibTableColumn
dsVdslLineConfigMicroCutStatTotal = _DsVdslLineConfigMicroCutStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 3),
    _DsVdslLineConfigMicroCutStatTotal_Type()
)
dsVdslLineConfigMicroCutStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigMicroCutStatTotal.setStatus("current")
_DsVdslLineConfigMicroCutStatCurrent_Type = Integer32
_DsVdslLineConfigMicroCutStatCurrent_Object = MibTableColumn
dsVdslLineConfigMicroCutStatCurrent = _DsVdslLineConfigMicroCutStatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 4),
    _DsVdslLineConfigMicroCutStatCurrent_Type()
)
dsVdslLineConfigMicroCutStatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigMicroCutStatCurrent.setStatus("current")
_DsVdslLineConfigMicroCutStatLinkdown_Type = Integer32
_DsVdslLineConfigMicroCutStatLinkdown_Object = MibTableColumn
dsVdslLineConfigMicroCutStatLinkdown = _DsVdslLineConfigMicroCutStatLinkdown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 5),
    _DsVdslLineConfigMicroCutStatLinkdown_Type()
)
dsVdslLineConfigMicroCutStatLinkdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigMicroCutStatLinkdown.setStatus("current")


class _DsVdslLineConfigMicroCutStatCleared_Type(Integer32):
    """Custom type dsVdslLineConfigMicroCutStatCleared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 1),
          ("clearTotal", 2),
          ("clearCurrent", 3),
          ("clearLinkdown", 4))
    )


_DsVdslLineConfigMicroCutStatCleared_Type.__name__ = "Integer32"
_DsVdslLineConfigMicroCutStatCleared_Object = MibTableColumn
dsVdslLineConfigMicroCutStatCleared = _DsVdslLineConfigMicroCutStatCleared_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 6),
    _DsVdslLineConfigMicroCutStatCleared_Type()
)
dsVdslLineConfigMicroCutStatCleared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigMicroCutStatCleared.setStatus("current")


class _DsVdslLineConfigTrustSnr_Type(Integer32):
    """Custom type dsVdslLineConfigTrustSnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_DsVdslLineConfigTrustSnr_Type.__name__ = "Integer32"
_DsVdslLineConfigTrustSnr_Object = MibTableColumn
dsVdslLineConfigTrustSnr = _DsVdslLineConfigTrustSnr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 7),
    _DsVdslLineConfigTrustSnr_Type()
)
dsVdslLineConfigTrustSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnr.setStatus("current")


class _DsVdslLineConfigTrustSnrThreshUpMargin_Type(Integer32):
    """Custom type dsVdslLineConfigTrustSnrThreshUpMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_DsVdslLineConfigTrustSnrThreshUpMargin_Type.__name__ = "Integer32"
_DsVdslLineConfigTrustSnrThreshUpMargin_Object = MibTableColumn
dsVdslLineConfigTrustSnrThreshUpMargin = _DsVdslLineConfigTrustSnrThreshUpMargin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 8),
    _DsVdslLineConfigTrustSnrThreshUpMargin_Type()
)
dsVdslLineConfigTrustSnrThreshUpMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrThreshUpMargin.setStatus("current")


class _DsVdslLineConfigTrustSnrThreshUpTime_Type(Integer32):
    """Custom type dsVdslLineConfigTrustSnrThreshUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DsVdslLineConfigTrustSnrThreshUpTime_Type.__name__ = "Integer32"
_DsVdslLineConfigTrustSnrThreshUpTime_Object = MibTableColumn
dsVdslLineConfigTrustSnrThreshUpTime = _DsVdslLineConfigTrustSnrThreshUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 9),
    _DsVdslLineConfigTrustSnrThreshUpTime_Type()
)
dsVdslLineConfigTrustSnrThreshUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrThreshUpTime.setStatus("current")


class _DsVdslLineConfigTrustSnrThreshDownMargin_Type(Integer32):
    """Custom type dsVdslLineConfigTrustSnrThreshDownMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_DsVdslLineConfigTrustSnrThreshDownMargin_Type.__name__ = "Integer32"
_DsVdslLineConfigTrustSnrThreshDownMargin_Object = MibTableColumn
dsVdslLineConfigTrustSnrThreshDownMargin = _DsVdslLineConfigTrustSnrThreshDownMargin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 10),
    _DsVdslLineConfigTrustSnrThreshDownMargin_Type()
)
dsVdslLineConfigTrustSnrThreshDownMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrThreshDownMargin.setStatus("current")


class _DsVdslLineConfigTrustSnrThreshDownTime_Type(Integer32):
    """Custom type dsVdslLineConfigTrustSnrThreshDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DsVdslLineConfigTrustSnrThreshDownTime_Type.__name__ = "Integer32"
_DsVdslLineConfigTrustSnrThreshDownTime_Object = MibTableColumn
dsVdslLineConfigTrustSnrThreshDownTime = _DsVdslLineConfigTrustSnrThreshDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 11),
    _DsVdslLineConfigTrustSnrThreshDownTime_Type()
)
dsVdslLineConfigTrustSnrThreshDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrThreshDownTime.setStatus("current")
_DsVdslLineConfigTrustSnrStatUpRunning_Type = Integer32
_DsVdslLineConfigTrustSnrStatUpRunning_Object = MibTableColumn
dsVdslLineConfigTrustSnrStatUpRunning = _DsVdslLineConfigTrustSnrStatUpRunning_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 12),
    _DsVdslLineConfigTrustSnrStatUpRunning_Type()
)
dsVdslLineConfigTrustSnrStatUpRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrStatUpRunning.setStatus("current")
_DsVdslLineConfigTrustSnrStatUpTime_Type = Integer32
_DsVdslLineConfigTrustSnrStatUpTime_Object = MibTableColumn
dsVdslLineConfigTrustSnrStatUpTime = _DsVdslLineConfigTrustSnrStatUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 13),
    _DsVdslLineConfigTrustSnrStatUpTime_Type()
)
dsVdslLineConfigTrustSnrStatUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrStatUpTime.setStatus("current")
_DsVdslLineConfigTrustSnrStatDownRunning_Type = Integer32
_DsVdslLineConfigTrustSnrStatDownRunning_Object = MibTableColumn
dsVdslLineConfigTrustSnrStatDownRunning = _DsVdslLineConfigTrustSnrStatDownRunning_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 14),
    _DsVdslLineConfigTrustSnrStatDownRunning_Type()
)
dsVdslLineConfigTrustSnrStatDownRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrStatDownRunning.setStatus("current")
_DsVdslLineConfigTrustSnrStatDownTime_Type = Integer32
_DsVdslLineConfigTrustSnrStatDownTime_Object = MibTableColumn
dsVdslLineConfigTrustSnrStatDownTime = _DsVdslLineConfigTrustSnrStatDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 15),
    _DsVdslLineConfigTrustSnrStatDownTime_Type()
)
dsVdslLineConfigTrustSnrStatDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrStatDownTime.setStatus("current")
_DsVdslLineConfigTrustSnrStatLinkdown_Type = Integer32
_DsVdslLineConfigTrustSnrStatLinkdown_Object = MibTableColumn
dsVdslLineConfigTrustSnrStatLinkdown = _DsVdslLineConfigTrustSnrStatLinkdown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 16),
    _DsVdslLineConfigTrustSnrStatLinkdown_Type()
)
dsVdslLineConfigTrustSnrStatLinkdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrStatLinkdown.setStatus("current")


class _DsVdslLineConfigTrustSnrStatCleared_Type(Integer32):
    """Custom type dsVdslLineConfigTrustSnrStatCleared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 1),
          ("clearUpRunning", 2),
          ("clearUpTime", 3),
          ("clearDownRunning", 4),
          ("clearDownTime", 5),
          ("clearLinkdown", 6))
    )


_DsVdslLineConfigTrustSnrStatCleared_Type.__name__ = "Integer32"
_DsVdslLineConfigTrustSnrStatCleared_Object = MibTableColumn
dsVdslLineConfigTrustSnrStatCleared = _DsVdslLineConfigTrustSnrStatCleared_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 2, 1, 1, 17),
    _DsVdslLineConfigTrustSnrStatCleared_Type()
)
dsVdslLineConfigTrustSnrStatCleared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineConfigTrustSnrStatCleared.setStatus("current")
_DsVdslLineStatus_ObjectIdentity = ObjectIdentity
dsVdslLineStatus = _DsVdslLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 11)
)
_DsVdslLineStatusTable_Object = MibTable
dsVdslLineStatusTable = _DsVdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 11, 1)
)
if mibBuilder.loadTexts:
    dsVdslLineStatusTable.setStatus("current")
_DsVdslLineStatusEntry_Object = MibTableRow
dsVdslLineStatusEntry = _DsVdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 11, 1, 1)
)
dsVdslLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsVdslLineStatusEntry.setStatus("current")


class _DsVdslLineStatusCpeLinkdownReason_Type(Integer32):
    """Custom type dsVdslLineStatusCpeLinkdownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", -1),
          ("lossOfPower", 0),
          ("portStop", 1),
          ("lossOfSignalPM", 2),
          ("lossOfSignalNonPM", 3),
          ("lossOfFramePM", 4),
          ("lossOfFrameNonPM", 5),
          ("excessiveSevereError", 6),
          ("iniCRC", 7),
          ("cRC", 8),
          ("feLPR", 9),
          ("feLOS", 10),
          ("feLOF", 11),
          ("feESE", 12),
          ("feIniCRC", 13),
          ("feCRC", 14),
          ("unknownFailure", 15))
    )


_DsVdslLineStatusCpeLinkdownReason_Type.__name__ = "Integer32"
_DsVdslLineStatusCpeLinkdownReason_Object = MibTableColumn
dsVdslLineStatusCpeLinkdownReason = _DsVdslLineStatusCpeLinkdownReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 3, 11, 1, 1, 1),
    _DsVdslLineStatusCpeLinkdownReason_Type()
)
dsVdslLineStatusCpeLinkdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineStatusCpeLinkdownReason.setStatus("current")
_DsVdslPM_ObjectIdentity = ObjectIdentity
dsVdslPM = _DsVdslPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5)
)
_DsVdslPMMediaAdaptor_ObjectIdentity = ObjectIdentity
dsVdslPMMediaAdaptor = _DsVdslPMMediaAdaptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1)
)
_DsVdslPMMATable_Object = MibTable
dsVdslPMMATable = _DsVdslPMMATable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dsVdslPMMATable.setStatus("current")
_DsVdslPMMAEntry_Object = MibTableRow
dsVdslPMMAEntry = _DsVdslPMMAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1)
)
dsVdslPMMAEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsVdslPMMAEntry.setStatus("current")
_DsVdslPMMARxFrameCount_Type = Counter64
_DsVdslPMMARxFrameCount_Object = MibTableColumn
dsVdslPMMARxFrameCount = _DsVdslPMMARxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1, 1),
    _DsVdslPMMARxFrameCount_Type()
)
dsVdslPMMARxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMMARxFrameCount.setStatus("current")
_DsVdslPMMARxCRCErr_Type = Counter64
_DsVdslPMMARxCRCErr_Object = MibTableColumn
dsVdslPMMARxCRCErr = _DsVdslPMMARxCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1, 2),
    _DsVdslPMMARxCRCErr_Type()
)
dsVdslPMMARxCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMMARxCRCErr.setStatus("current")
_DsVdslPMMARxDrop_Type = Counter64
_DsVdslPMMARxDrop_Object = MibTableColumn
dsVdslPMMARxDrop = _DsVdslPMMARxDrop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1, 3),
    _DsVdslPMMARxDrop_Type()
)
dsVdslPMMARxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMMARxDrop.setStatus("current")
_DsVdslPMMATxFrameCount_Type = Counter64
_DsVdslPMMATxFrameCount_Object = MibTableColumn
dsVdslPMMATxFrameCount = _DsVdslPMMATxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1, 4),
    _DsVdslPMMATxFrameCount_Type()
)
dsVdslPMMATxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMMATxFrameCount.setStatus("current")
_DsVdslPMMATxDrop_Type = Counter64
_DsVdslPMMATxDrop_Object = MibTableColumn
dsVdslPMMATxDrop = _DsVdslPMMATxDrop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1, 5),
    _DsVdslPMMATxDrop_Type()
)
dsVdslPMMATxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMMATxDrop.setStatus("current")
_DsVdslPMMAEnetCrcErrCnt_Type = Counter64
_DsVdslPMMAEnetCrcErrCnt_Object = MibTableColumn
dsVdslPMMAEnetCrcErrCnt = _DsVdslPMMAEnetCrcErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1, 6),
    _DsVdslPMMAEnetCrcErrCnt_Type()
)
dsVdslPMMAEnetCrcErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMMAEnetCrcErrCnt.setStatus("current")
_DsVdslPMMACleared_Type = TimeTicks
_DsVdslPMMACleared_Object = MibTableColumn
dsVdslPMMACleared = _DsVdslPMMACleared_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 1, 1, 1, 7),
    _DsVdslPMMACleared_Type()
)
dsVdslPMMACleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMMACleared.setStatus("current")
_DsVdslPMStatCount_ObjectIdentity = ObjectIdentity
dsVdslPMStatCount = _DsVdslPMStatCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2)
)
_DsVdslPMCoStatTable_Object = MibTable
dsVdslPMCoStatTable = _DsVdslPMCoStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    dsVdslPMCoStatTable.setStatus("current")
_DsVdslPMCoStatEntry_Object = MibTableRow
dsVdslPMCoStatEntry = _DsVdslPMCoStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1)
)
dsVdslPMCoStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsVdslPMCoStatEntry.setStatus("current")
_DsVdslPMLos_Type = Unsigned32
_DsVdslPMLos_Object = MibTableColumn
dsVdslPMLos = _DsVdslPMLos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 1),
    _DsVdslPMLos_Type()
)
dsVdslPMLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMLos.setStatus("current")
_DsVdslPMLof_Type = Unsigned32
_DsVdslPMLof_Object = MibTableColumn
dsVdslPMLof = _DsVdslPMLof_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 2),
    _DsVdslPMLof_Type()
)
dsVdslPMLof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMLof.setStatus("current")
_DsVdslPMLol_Type = Unsigned32
_DsVdslPMLol_Object = MibTableColumn
dsVdslPMLol = _DsVdslPMLol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 3),
    _DsVdslPMLol_Type()
)
dsVdslPMLol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMLol.setStatus("current")
_DsVdslPMCorrBlk_Type = Unsigned32
_DsVdslPMCorrBlk_Object = MibTableColumn
dsVdslPMCorrBlk = _DsVdslPMCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 4),
    _DsVdslPMCorrBlk_Type()
)
dsVdslPMCorrBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMCorrBlk.setStatus("current")
_DsVdslPMUnCorrBlk_Type = Unsigned32
_DsVdslPMUnCorrBlk_Object = MibTableColumn
dsVdslPMUnCorrBlk = _DsVdslPMUnCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 5),
    _DsVdslPMUnCorrBlk_Type()
)
dsVdslPMUnCorrBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMUnCorrBlk.setStatus("current")
_DsVdslPMCRC_Type = Unsigned32
_DsVdslPMCRC_Object = MibTableColumn
dsVdslPMCRC = _DsVdslPMCRC_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 6),
    _DsVdslPMCRC_Type()
)
dsVdslPMCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMCRC.setStatus("current")
_DsVdslPMServiceError_Type = Unsigned32
_DsVdslPMServiceError_Object = MibTableColumn
dsVdslPMServiceError = _DsVdslPMServiceError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 7),
    _DsVdslPMServiceError_Type()
)
dsVdslPMServiceError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMServiceError.setStatus("current")
_DsVdslPMLoss_Type = Unsigned32
_DsVdslPMLoss_Object = MibTableColumn
dsVdslPMLoss = _DsVdslPMLoss_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 18),
    _DsVdslPMLoss_Type()
)
dsVdslPMLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMLoss.setStatus("current")
_DsVdslPMLofs_Type = Unsigned32
_DsVdslPMLofs_Object = MibTableColumn
dsVdslPMLofs = _DsVdslPMLofs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 19),
    _DsVdslPMLofs_Type()
)
dsVdslPMLofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMLofs.setStatus("current")
_DsVdslPMLols_Type = Unsigned32
_DsVdslPMLols_Object = MibTableColumn
dsVdslPMLols = _DsVdslPMLols_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 20),
    _DsVdslPMLols_Type()
)
dsVdslPMLols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMLols.setStatus("current")
_DsVdslPMESs_Type = Unsigned32
_DsVdslPMESs_Object = MibTableColumn
dsVdslPMESs = _DsVdslPMESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 21),
    _DsVdslPMESs_Type()
)
dsVdslPMESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMESs.setStatus("current")
_DsVdslPMSESs_Type = Unsigned32
_DsVdslPMSESs_Object = MibTableColumn
dsVdslPMSESs = _DsVdslPMSESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 22),
    _DsVdslPMSESs_Type()
)
dsVdslPMSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMSESs.setStatus("current")
_DsVdslPMUASs_Type = Unsigned32
_DsVdslPMUASs_Object = MibTableColumn
dsVdslPMUASs = _DsVdslPMUASs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 23),
    _DsVdslPMUASs_Type()
)
dsVdslPMUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMUASs.setStatus("current")
_DsVdslPMCRCs_Type = Unsigned32
_DsVdslPMCRCs_Object = MibTableColumn
dsVdslPMCRCs = _DsVdslPMCRCs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 24),
    _DsVdslPMCRCs_Type()
)
dsVdslPMCRCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMCRCs.setStatus("current")
_DsVdslPM15minElapsedTime_Type = Gauge32
_DsVdslPM15minElapsedTime_Object = MibTableColumn
dsVdslPM15minElapsedTime = _DsVdslPM15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 28),
    _DsVdslPM15minElapsedTime_Type()
)
dsVdslPM15minElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPM15minElapsedTime.setStatus("current")
_DsVdslPM1dayElapsedTime_Type = Gauge32
_DsVdslPM1dayElapsedTime_Object = MibTableColumn
dsVdslPM1dayElapsedTime = _DsVdslPM1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 29),
    _DsVdslPM1dayElapsedTime_Type()
)
dsVdslPM1dayElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPM1dayElapsedTime.setStatus("current")


class _DsVdslPMClear_Type(Integer32):
    """Custom type dsVdslPMClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_DsVdslPMClear_Type.__name__ = "Integer32"
_DsVdslPMClear_Object = MibTableColumn
dsVdslPMClear = _DsVdslPMClear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 1, 1, 30),
    _DsVdslPMClear_Type()
)
dsVdslPMClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMClear.setStatus("current")
_DsVdslPMCoStat15minTable_Object = MibTable
dsVdslPMCoStat15minTable = _DsVdslPMCoStat15minTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    dsVdslPMCoStat15minTable.setStatus("current")
_DsVdslPMCoStat15minEntry_Object = MibTableRow
dsVdslPMCoStat15minEntry = _DsVdslPMCoStat15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1)
)
dsVdslPMCoStat15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DASAN-DSL-MIB", "dsVdslPM15minInterval"),
)
if mibBuilder.loadTexts:
    dsVdslPMCoStat15minEntry.setStatus("current")


class _DsVdslPM15minInterval_Type(Integer32):
    """Custom type dsVdslPM15minInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DsVdslPM15minInterval_Type.__name__ = "Integer32"
_DsVdslPM15minInterval_Object = MibTableColumn
dsVdslPM15minInterval = _DsVdslPM15minInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 1),
    _DsVdslPM15minInterval_Type()
)
dsVdslPM15minInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsVdslPM15minInterval.setStatus("current")
_DsVdslPM15minLos_Type = Unsigned32
_DsVdslPM15minLos_Object = MibTableColumn
dsVdslPM15minLos = _DsVdslPM15minLos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 2),
    _DsVdslPM15minLos_Type()
)
dsVdslPM15minLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minLos.setStatus("current")
_DsVdslPM15minLof_Type = Unsigned32
_DsVdslPM15minLof_Object = MibTableColumn
dsVdslPM15minLof = _DsVdslPM15minLof_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 3),
    _DsVdslPM15minLof_Type()
)
dsVdslPM15minLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minLof.setStatus("current")
_DsVdslPM15minLol_Type = Unsigned32
_DsVdslPM15minLol_Object = MibTableColumn
dsVdslPM15minLol = _DsVdslPM15minLol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 4),
    _DsVdslPM15minLol_Type()
)
dsVdslPM15minLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minLol.setStatus("current")
_DsVdslPM15minCorrBlk_Type = Unsigned32
_DsVdslPM15minCorrBlk_Object = MibTableColumn
dsVdslPM15minCorrBlk = _DsVdslPM15minCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 5),
    _DsVdslPM15minCorrBlk_Type()
)
dsVdslPM15minCorrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minCorrBlk.setStatus("current")
_DsVdslPM15minUnCorrBlk_Type = Unsigned32
_DsVdslPM15minUnCorrBlk_Object = MibTableColumn
dsVdslPM15minUnCorrBlk = _DsVdslPM15minUnCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 6),
    _DsVdslPM15minUnCorrBlk_Type()
)
dsVdslPM15minUnCorrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minUnCorrBlk.setStatus("current")
_DsVdslPM15minCRC_Type = Unsigned32
_DsVdslPM15minCRC_Object = MibTableColumn
dsVdslPM15minCRC = _DsVdslPM15minCRC_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 7),
    _DsVdslPM15minCRC_Type()
)
dsVdslPM15minCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minCRC.setStatus("current")
_DsVdslPM15minServiceError_Type = Unsigned32
_DsVdslPM15minServiceError_Object = MibTableColumn
dsVdslPM15minServiceError = _DsVdslPM15minServiceError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 8),
    _DsVdslPM15minServiceError_Type()
)
dsVdslPM15minServiceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minServiceError.setStatus("current")
_DsVdslPM15minLoss_Type = Unsigned32
_DsVdslPM15minLoss_Object = MibTableColumn
dsVdslPM15minLoss = _DsVdslPM15minLoss_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 19),
    _DsVdslPM15minLoss_Type()
)
dsVdslPM15minLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minLoss.setStatus("current")
_DsVdslPM15minLofs_Type = Unsigned32
_DsVdslPM15minLofs_Object = MibTableColumn
dsVdslPM15minLofs = _DsVdslPM15minLofs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 20),
    _DsVdslPM15minLofs_Type()
)
dsVdslPM15minLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minLofs.setStatus("current")
_DsVdslPM15minLols_Type = Unsigned32
_DsVdslPM15minLols_Object = MibTableColumn
dsVdslPM15minLols = _DsVdslPM15minLols_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 21),
    _DsVdslPM15minLols_Type()
)
dsVdslPM15minLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minLols.setStatus("current")
_DsVdslPM15minESs_Type = Unsigned32
_DsVdslPM15minESs_Object = MibTableColumn
dsVdslPM15minESs = _DsVdslPM15minESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 22),
    _DsVdslPM15minESs_Type()
)
dsVdslPM15minESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minESs.setStatus("current")
_DsVdslPM15minSESs_Type = Unsigned32
_DsVdslPM15minSESs_Object = MibTableColumn
dsVdslPM15minSESs = _DsVdslPM15minSESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 23),
    _DsVdslPM15minSESs_Type()
)
dsVdslPM15minSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minSESs.setStatus("current")
_DsVdslPM15minUASs_Type = Unsigned32
_DsVdslPM15minUASs_Object = MibTableColumn
dsVdslPM15minUASs = _DsVdslPM15minUASs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 24),
    _DsVdslPM15minUASs_Type()
)
dsVdslPM15minUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minUASs.setStatus("current")
_DsVdslPM15minCRCs_Type = Unsigned32
_DsVdslPM15minCRCs_Object = MibTableColumn
dsVdslPM15minCRCs = _DsVdslPM15minCRCs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 2, 1, 25),
    _DsVdslPM15minCRCs_Type()
)
dsVdslPM15minCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM15minCRCs.setStatus("current")
_DsVdslPMCoStat1dayTable_Object = MibTable
dsVdslPMCoStat1dayTable = _DsVdslPMCoStat1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3)
)
if mibBuilder.loadTexts:
    dsVdslPMCoStat1dayTable.setStatus("current")
_DsVdslPMCoStat1dayEntry_Object = MibTableRow
dsVdslPMCoStat1dayEntry = _DsVdslPMCoStat1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1)
)
dsVdslPMCoStat1dayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DASAN-DSL-MIB", "dsVdslPM1dayInterval"),
)
if mibBuilder.loadTexts:
    dsVdslPMCoStat1dayEntry.setStatus("current")


class _DsVdslPM1dayInterval_Type(Integer32):
    """Custom type dsVdslPM1dayInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DsVdslPM1dayInterval_Type.__name__ = "Integer32"
_DsVdslPM1dayInterval_Object = MibTableColumn
dsVdslPM1dayInterval = _DsVdslPM1dayInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 1),
    _DsVdslPM1dayInterval_Type()
)
dsVdslPM1dayInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsVdslPM1dayInterval.setStatus("current")
_DsVdslPM1dayLos_Type = Unsigned32
_DsVdslPM1dayLos_Object = MibTableColumn
dsVdslPM1dayLos = _DsVdslPM1dayLos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 2),
    _DsVdslPM1dayLos_Type()
)
dsVdslPM1dayLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayLos.setStatus("current")
_DsVdslPM1dayLof_Type = Unsigned32
_DsVdslPM1dayLof_Object = MibTableColumn
dsVdslPM1dayLof = _DsVdslPM1dayLof_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 3),
    _DsVdslPM1dayLof_Type()
)
dsVdslPM1dayLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayLof.setStatus("current")
_DsVdslPM1dayLol_Type = Unsigned32
_DsVdslPM1dayLol_Object = MibTableColumn
dsVdslPM1dayLol = _DsVdslPM1dayLol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 4),
    _DsVdslPM1dayLol_Type()
)
dsVdslPM1dayLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayLol.setStatus("current")
_DsVdslPM1dayCorrBlk_Type = Unsigned32
_DsVdslPM1dayCorrBlk_Object = MibTableColumn
dsVdslPM1dayCorrBlk = _DsVdslPM1dayCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 5),
    _DsVdslPM1dayCorrBlk_Type()
)
dsVdslPM1dayCorrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayCorrBlk.setStatus("current")
_DsVdslPM1dayUnCorrBlk_Type = Unsigned32
_DsVdslPM1dayUnCorrBlk_Object = MibTableColumn
dsVdslPM1dayUnCorrBlk = _DsVdslPM1dayUnCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 6),
    _DsVdslPM1dayUnCorrBlk_Type()
)
dsVdslPM1dayUnCorrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayUnCorrBlk.setStatus("current")
_DsVdslPM1dayCRC_Type = Unsigned32
_DsVdslPM1dayCRC_Object = MibTableColumn
dsVdslPM1dayCRC = _DsVdslPM1dayCRC_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 7),
    _DsVdslPM1dayCRC_Type()
)
dsVdslPM1dayCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayCRC.setStatus("current")
_DsVdslPMdayServiceError_Type = Unsigned32
_DsVdslPMdayServiceError_Object = MibTableColumn
dsVdslPMdayServiceError = _DsVdslPMdayServiceError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 8),
    _DsVdslPMdayServiceError_Type()
)
dsVdslPMdayServiceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMdayServiceError.setStatus("current")
_DsVdslPM1dayLoss_Type = Unsigned32
_DsVdslPM1dayLoss_Object = MibTableColumn
dsVdslPM1dayLoss = _DsVdslPM1dayLoss_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 19),
    _DsVdslPM1dayLoss_Type()
)
dsVdslPM1dayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayLoss.setStatus("current")
_DsVdslPM1dayLofs_Type = Unsigned32
_DsVdslPM1dayLofs_Object = MibTableColumn
dsVdslPM1dayLofs = _DsVdslPM1dayLofs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 20),
    _DsVdslPM1dayLofs_Type()
)
dsVdslPM1dayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayLofs.setStatus("current")
_DsVdslPM1dayLols_Type = Unsigned32
_DsVdslPM1dayLols_Object = MibTableColumn
dsVdslPM1dayLols = _DsVdslPM1dayLols_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 21),
    _DsVdslPM1dayLols_Type()
)
dsVdslPM1dayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayLols.setStatus("current")
_DsVdslPM1dayESs_Type = Unsigned32
_DsVdslPM1dayESs_Object = MibTableColumn
dsVdslPM1dayESs = _DsVdslPM1dayESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 22),
    _DsVdslPM1dayESs_Type()
)
dsVdslPM1dayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayESs.setStatus("current")
_DsVdslPM1daySESs_Type = Unsigned32
_DsVdslPM1daySESs_Object = MibTableColumn
dsVdslPM1daySESs = _DsVdslPM1daySESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 23),
    _DsVdslPM1daySESs_Type()
)
dsVdslPM1daySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1daySESs.setStatus("current")
_DsVdslPM1dayUASs_Type = Unsigned32
_DsVdslPM1dayUASs_Object = MibTableColumn
dsVdslPM1dayUASs = _DsVdslPM1dayUASs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 24),
    _DsVdslPM1dayUASs_Type()
)
dsVdslPM1dayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayUASs.setStatus("current")
_DsVdslPM1dayCRCs_Type = Unsigned32
_DsVdslPM1dayCRCs_Object = MibTableColumn
dsVdslPM1dayCRCs = _DsVdslPM1dayCRCs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 3, 1, 25),
    _DsVdslPM1dayCRCs_Type()
)
dsVdslPM1dayCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPM1dayCRCs.setStatus("current")
_DsVdslPMCpeStatTable_Object = MibTable
dsVdslPMCpeStatTable = _DsVdslPMCpeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4)
)
if mibBuilder.loadTexts:
    dsVdslPMCpeStatTable.setStatus("current")
_DsVdslPMCpeStatEntry_Object = MibTableRow
dsVdslPMCpeStatEntry = _DsVdslPMCpeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4, 1)
)
dsVdslPMCpeStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsVdslPMCpeStatEntry.setStatus("current")
_DsVdslPMCpeLos_Type = Unsigned32
_DsVdslPMCpeLos_Object = MibTableColumn
dsVdslPMCpeLos = _DsVdslPMCpeLos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4, 1, 1),
    _DsVdslPMCpeLos_Type()
)
dsVdslPMCpeLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMCpeLos.setStatus("current")
_DsVdslPMCpeLof_Type = Unsigned32
_DsVdslPMCpeLof_Object = MibTableColumn
dsVdslPMCpeLof = _DsVdslPMCpeLof_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4, 1, 2),
    _DsVdslPMCpeLof_Type()
)
dsVdslPMCpeLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMCpeLof.setStatus("current")
_DsVdslPMCpeCorrBlk_Type = Unsigned32
_DsVdslPMCpeCorrBlk_Object = MibTableColumn
dsVdslPMCpeCorrBlk = _DsVdslPMCpeCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4, 1, 3),
    _DsVdslPMCpeCorrBlk_Type()
)
dsVdslPMCpeCorrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMCpeCorrBlk.setStatus("current")
_DsVdslPMCpeUnCorrBlk_Type = Unsigned32
_DsVdslPMCpeUnCorrBlk_Object = MibTableColumn
dsVdslPMCpeUnCorrBlk = _DsVdslPMCpeUnCorrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4, 1, 4),
    _DsVdslPMCpeUnCorrBlk_Type()
)
dsVdslPMCpeUnCorrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMCpeUnCorrBlk.setStatus("current")
_DsVdslPMCpeCRC_Type = Unsigned32
_DsVdslPMCpeCRC_Object = MibTableColumn
dsVdslPMCpeCRC = _DsVdslPMCpeCRC_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4, 1, 5),
    _DsVdslPMCpeCRC_Type()
)
dsVdslPMCpeCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslPMCpeCRC.setStatus("current")


class _DsVdslPMCpeClear_Type(Integer32):
    """Custom type dsVdslPMCpeClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_DsVdslPMCpeClear_Type.__name__ = "Integer32"
_DsVdslPMCpeClear_Object = MibTableColumn
dsVdslPMCpeClear = _DsVdslPMCpeClear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 5, 2, 4, 1, 6),
    _DsVdslPMCpeClear_Type()
)
dsVdslPMCpeClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslPMCpeClear.setStatus("current")
_DsVdslProfile_ObjectIdentity = ObjectIdentity
dsVdslProfile = _DsVdslProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6)
)
_DsVdslLineCfgProfile_ObjectIdentity = ObjectIdentity
dsVdslLineCfgProfile = _DsVdslLineCfgProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1)
)
_DsVdslLineCfgProfileTable_Object = MibTable
dsVdslLineCfgProfileTable = _DsVdslLineCfgProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    dsVdslLineCfgProfileTable.setStatus("current")
_DsVdslLineCfgProfileEntry_Object = MibTableRow
dsVdslLineCfgProfileEntry = _DsVdslLineCfgProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1)
)
dsVdslLineCfgProfileEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsVdslLineCfgProfileName"),
)
if mibBuilder.loadTexts:
    dsVdslLineCfgProfileEntry.setStatus("current")
_DsVdslLineCfgProfileName_Type = DisplayString
_DsVdslLineCfgProfileName_Object = MibTableColumn
dsVdslLineCfgProfileName = _DsVdslLineCfgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 1),
    _DsVdslLineCfgProfileName_Type()
)
dsVdslLineCfgProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsVdslLineCfgProfileName.setStatus("current")


class _DsVdslLineCfgDownMaxSnrMgn_Type(Unsigned32):
    """Custom type dsVdslLineCfgDownMaxSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DsVdslLineCfgDownMaxSnrMgn_Type.__name__ = "Unsigned32"
_DsVdslLineCfgDownMaxSnrMgn_Object = MibTableColumn
dsVdslLineCfgDownMaxSnrMgn = _DsVdslLineCfgDownMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 4),
    _DsVdslLineCfgDownMaxSnrMgn_Type()
)
dsVdslLineCfgDownMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMaxSnrMgn.setUnits("0.25dBm")


class _DsVdslLineCfgDownMinSnrMgn_Type(Unsigned32):
    """Custom type dsVdslLineCfgDownMinSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DsVdslLineCfgDownMinSnrMgn_Type.__name__ = "Unsigned32"
_DsVdslLineCfgDownMinSnrMgn_Object = MibTableColumn
dsVdslLineCfgDownMinSnrMgn = _DsVdslLineCfgDownMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 5),
    _DsVdslLineCfgDownMinSnrMgn_Type()
)
dsVdslLineCfgDownMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMinSnrMgn.setUnits("0.25dBm")


class _DsVdslLineCfgDownTargetSnrMgn_Type(Unsigned32):
    """Custom type dsVdslLineCfgDownTargetSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DsVdslLineCfgDownTargetSnrMgn_Type.__name__ = "Unsigned32"
_DsVdslLineCfgDownTargetSnrMgn_Object = MibTableColumn
dsVdslLineCfgDownTargetSnrMgn = _DsVdslLineCfgDownTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 6),
    _DsVdslLineCfgDownTargetSnrMgn_Type()
)
dsVdslLineCfgDownTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownTargetSnrMgn.setUnits("0.25dBm")


class _DsVdslLineCfgUpMaxSnrMgn_Type(Unsigned32):
    """Custom type dsVdslLineCfgUpMaxSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DsVdslLineCfgUpMaxSnrMgn_Type.__name__ = "Unsigned32"
_DsVdslLineCfgUpMaxSnrMgn_Object = MibTableColumn
dsVdslLineCfgUpMaxSnrMgn = _DsVdslLineCfgUpMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 7),
    _DsVdslLineCfgUpMaxSnrMgn_Type()
)
dsVdslLineCfgUpMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMaxSnrMgn.setUnits("0.25dBm")


class _DsVdslLineCfgUpMinSnrMgn_Type(Unsigned32):
    """Custom type dsVdslLineCfgUpMinSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DsVdslLineCfgUpMinSnrMgn_Type.__name__ = "Unsigned32"
_DsVdslLineCfgUpMinSnrMgn_Object = MibTableColumn
dsVdslLineCfgUpMinSnrMgn = _DsVdslLineCfgUpMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 8),
    _DsVdslLineCfgUpMinSnrMgn_Type()
)
dsVdslLineCfgUpMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMinSnrMgn.setUnits("0.25dBm")


class _DsVdslLineCfgUpTargetSnrMgn_Type(Unsigned32):
    """Custom type dsVdslLineCfgUpTargetSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DsVdslLineCfgUpTargetSnrMgn_Type.__name__ = "Unsigned32"
_DsVdslLineCfgUpTargetSnrMgn_Object = MibTableColumn
dsVdslLineCfgUpTargetSnrMgn = _DsVdslLineCfgUpTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 9),
    _DsVdslLineCfgUpTargetSnrMgn_Type()
)
dsVdslLineCfgUpTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpTargetSnrMgn.setUnits("0.25dBm")


class _DsVdslLineCfgDownMaxDataRate_Type(Unsigned32):
    """Custom type dsVdslLineCfgDownMaxDataRate based on Unsigned32"""
    defaultValue = 0


_DsVdslLineCfgDownMaxDataRate_Type.__name__ = "Unsigned32"
_DsVdslLineCfgDownMaxDataRate_Object = MibTableColumn
dsVdslLineCfgDownMaxDataRate = _DsVdslLineCfgDownMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 10),
    _DsVdslLineCfgDownMaxDataRate_Type()
)
dsVdslLineCfgDownMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMaxDataRate.setUnits("kbps")


class _DsVdslLineCfgDownMinDataRate_Type(Unsigned32):
    """Custom type dsVdslLineCfgDownMinDataRate based on Unsigned32"""
    defaultValue = 0


_DsVdslLineCfgDownMinDataRate_Type.__name__ = "Unsigned32"
_DsVdslLineCfgDownMinDataRate_Object = MibTableColumn
dsVdslLineCfgDownMinDataRate = _DsVdslLineCfgDownMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 11),
    _DsVdslLineCfgDownMinDataRate_Type()
)
dsVdslLineCfgDownMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMinDataRate.setUnits("kbps")


class _DsVdslLineCfgUpMaxDataRate_Type(Unsigned32):
    """Custom type dsVdslLineCfgUpMaxDataRate based on Unsigned32"""
    defaultValue = 0


_DsVdslLineCfgUpMaxDataRate_Type.__name__ = "Unsigned32"
_DsVdslLineCfgUpMaxDataRate_Object = MibTableColumn
dsVdslLineCfgUpMaxDataRate = _DsVdslLineCfgUpMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 12),
    _DsVdslLineCfgUpMaxDataRate_Type()
)
dsVdslLineCfgUpMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMaxDataRate.setUnits("kbps")


class _DsVdslLineCfgUpMinDataRate_Type(Unsigned32):
    """Custom type dsVdslLineCfgUpMinDataRate based on Unsigned32"""
    defaultValue = 0


_DsVdslLineCfgUpMinDataRate_Type.__name__ = "Unsigned32"
_DsVdslLineCfgUpMinDataRate_Object = MibTableColumn
dsVdslLineCfgUpMinDataRate = _DsVdslLineCfgUpMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 13),
    _DsVdslLineCfgUpMinDataRate_Type()
)
dsVdslLineCfgUpMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMinDataRate.setUnits("kbps")


class _DsVdslLineCfgDownMaxInterDelay_Type(Integer32):
    """Custom type dsVdslLineCfgDownMaxInterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DsVdslLineCfgDownMaxInterDelay_Type.__name__ = "Integer32"
_DsVdslLineCfgDownMaxInterDelay_Object = MibTableColumn
dsVdslLineCfgDownMaxInterDelay = _DsVdslLineCfgDownMaxInterDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 16),
    _DsVdslLineCfgDownMaxInterDelay_Type()
)
dsVdslLineCfgDownMaxInterDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMaxInterDelay.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownMaxInterDelay.setUnits("milliseconds")


class _DsVdslLineCfgUpMaxInterDelay_Type(Integer32):
    """Custom type dsVdslLineCfgUpMaxInterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DsVdslLineCfgUpMaxInterDelay_Type.__name__ = "Integer32"
_DsVdslLineCfgUpMaxInterDelay_Object = MibTableColumn
dsVdslLineCfgUpMaxInterDelay = _DsVdslLineCfgUpMaxInterDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 17),
    _DsVdslLineCfgUpMaxInterDelay_Type()
)
dsVdslLineCfgUpMaxInterDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMaxInterDelay.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpMaxInterDelay.setUnits("milliseconds")
_DsVdslLineCfgHamband_Type = Counter64
_DsVdslLineCfgHamband_Object = MibTableColumn
dsVdslLineCfgHamband = _DsVdslLineCfgHamband_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 20),
    _DsVdslLineCfgHamband_Type()
)
dsVdslLineCfgHamband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgHamband.setStatus("current")


class _DsVdslLineCfgDownINP_Type(Integer32):
    """Custom type dsVdslLineCfgDownINP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsVdslLineCfgDownINP_Type.__name__ = "Integer32"
_DsVdslLineCfgDownINP_Object = MibTableColumn
dsVdslLineCfgDownINP = _DsVdslLineCfgDownINP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 21),
    _DsVdslLineCfgDownINP_Type()
)
dsVdslLineCfgDownINP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownINP.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgDownINP.setUnits("unit of 125usec")


class _DsVdslLineCfgUpINP_Type(Integer32):
    """Custom type dsVdslLineCfgUpINP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsVdslLineCfgUpINP_Type.__name__ = "Integer32"
_DsVdslLineCfgUpINP_Object = MibTableColumn
dsVdslLineCfgUpINP = _DsVdslLineCfgUpINP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 22),
    _DsVdslLineCfgUpINP_Type()
)
dsVdslLineCfgUpINP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpINP.setStatus("current")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpINP.setUnits("unit of 125usec")


class _DsVdslLineCfgPBOLength_Type(Integer32):
    """Custom type dsVdslLineCfgPBOLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("pbo100m", 1),
          ("pbo200m", 2),
          ("pbo300m", 3),
          ("pbo400m", 4),
          ("pbo500m", 5),
          ("pbo600m", 6),
          ("pbo700m", 7),
          ("pbo800m", 8),
          ("pbo900m", 9),
          ("pbo1000m", 10))
    )


_DsVdslLineCfgPBOLength_Type.__name__ = "Integer32"
_DsVdslLineCfgPBOLength_Object = MibTableColumn
dsVdslLineCfgPBOLength = _DsVdslLineCfgPBOLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 23),
    _DsVdslLineCfgPBOLength_Type()
)
dsVdslLineCfgPBOLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineCfgPBOLength.setStatus("current")


class _DsVdslLineCfgPSDMaskLevel_Type(Integer32):
    """Custom type dsVdslLineCfgPSDMaskLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", -1),
          ("old-gains", 0),
          ("aNSI-M1", 1),
          ("aNSI-M2", 2),
          ("eTSI-M1", 3),
          ("eTSI-M2", 4),
          ("aNNEX-F-8-5", 5),
          ("aNSI-M1-EX", 6),
          ("aNSI-M2-EX", 7),
          ("eTSI-M1-EX", 8),
          ("eTSI-M2-EX", 9),
          ("aNNEX-F-11-5", 10),
          ("pSD-K", 11))
    )


_DsVdslLineCfgPSDMaskLevel_Type.__name__ = "Integer32"
_DsVdslLineCfgPSDMaskLevel_Object = MibTableColumn
dsVdslLineCfgPSDMaskLevel = _DsVdslLineCfgPSDMaskLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 24),
    _DsVdslLineCfgPSDMaskLevel_Type()
)
dsVdslLineCfgPSDMaskLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsVdslLineCfgPSDMaskLevel.setStatus("current")


class _DsVdslLineCfgTCMAdmin_Type(Integer32):
    """Custom type dsVdslLineCfgTCMAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_DsVdslLineCfgTCMAdmin_Type.__name__ = "Integer32"
_DsVdslLineCfgTCMAdmin_Object = MibTableColumn
dsVdslLineCfgTCMAdmin = _DsVdslLineCfgTCMAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 25),
    _DsVdslLineCfgTCMAdmin_Type()
)
dsVdslLineCfgTCMAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgTCMAdmin.setStatus("current")


class _DsVdslLineCfgUpboEnable_Type(Integer32):
    """Custom type dsVdslLineCfgUpboEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsVdslLineCfgUpboEnable_Type.__name__ = "Integer32"
_DsVdslLineCfgUpboEnable_Object = MibTableColumn
dsVdslLineCfgUpboEnable = _DsVdslLineCfgUpboEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 26),
    _DsVdslLineCfgUpboEnable_Type()
)
dsVdslLineCfgUpboEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgUpboEnable.setStatus("current")


class _DsVdslLineCfgChannel_Type(Integer32):
    """Custom type dsVdslLineCfgChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast", 0),
          ("slow", 1))
    )


_DsVdslLineCfgChannel_Type.__name__ = "Integer32"
_DsVdslLineCfgChannel_Object = MibTableColumn
dsVdslLineCfgChannel = _DsVdslLineCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 27),
    _DsVdslLineCfgChannel_Type()
)
dsVdslLineCfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgChannel.setStatus("current")


class _DsVdslLineCfgStandard_Type(Integer32):
    """Custom type dsVdslLineCfgStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vdsl", 1),
          ("vdsl2", 2))
    )


_DsVdslLineCfgStandard_Type.__name__ = "Integer32"
_DsVdslLineCfgStandard_Object = MibTableColumn
dsVdslLineCfgStandard = _DsVdslLineCfgStandard_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 28),
    _DsVdslLineCfgStandard_Type()
)
dsVdslLineCfgStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgStandard.setStatus("current")


class _DsVdslLineCfgLineProfile_Type(Integer32):
    """Custom type dsVdslLineCfgLineProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("sym25", 1),
          ("asym50-3b", 2),
          ("asym50-4b", 3),
          ("asym70", 4),
          ("asym100", 5),
          ("sym100", 6),
          ("sym50", 7),
          ("v8a-998", 8),
          ("v8b-998", 9),
          ("v8c-998", 10),
          ("v8d-998", 11),
          ("v12a-998", 12),
          ("v12b-998", 13),
          ("v17a-998", 14),
          ("v30a-998", 15),
          ("v12a-997", 16),
          ("v12b-997", 17),
          ("v17a-998-8k", 18))
    )


_DsVdslLineCfgLineProfile_Type.__name__ = "Integer32"
_DsVdslLineCfgLineProfile_Object = MibTableColumn
dsVdslLineCfgLineProfile = _DsVdslLineCfgLineProfile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 29),
    _DsVdslLineCfgLineProfile_Type()
)
dsVdslLineCfgLineProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgLineProfile.setStatus("current")


class _DsVdslLineCfgToneDisableMode_Type(Integer32):
    """Custom type dsVdslLineCfgToneDisableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("isdn", 2),
          ("adsl", 3),
          ("adsl2", 4),
          ("t-lan", 5),
          ("adsl-s", 6))
    )


_DsVdslLineCfgToneDisableMode_Type.__name__ = "Integer32"
_DsVdslLineCfgToneDisableMode_Object = MibTableColumn
dsVdslLineCfgToneDisableMode = _DsVdslLineCfgToneDisableMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 30),
    _DsVdslLineCfgToneDisableMode_Type()
)
dsVdslLineCfgToneDisableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgToneDisableMode.setStatus("current")


class _DsVdslLineCfgOptionband_Type(Integer32):
    """Custom type dsVdslLineCfgOptionband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", -1),
          ("annex-B-6-64", 1),
          ("annex-A-6-32", 2),
          ("annex-B-32-64", 3),
          ("exclude", 4),
          ("annex-M", 5))
    )


_DsVdslLineCfgOptionband_Type.__name__ = "Integer32"
_DsVdslLineCfgOptionband_Object = MibTableColumn
dsVdslLineCfgOptionband = _DsVdslLineCfgOptionband_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 31),
    _DsVdslLineCfgOptionband_Type()
)
dsVdslLineCfgOptionband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgOptionband.setStatus("current")


class _DsVdslLineCfgProfileAction_Type(Integer32):
    """Custom type dsVdslLineCfgProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("set", 1)
    )


_DsVdslLineCfgProfileAction_Type.__name__ = "Integer32"
_DsVdslLineCfgProfileAction_Object = MibTableColumn
dsVdslLineCfgProfileAction = _DsVdslLineCfgProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 33),
    _DsVdslLineCfgProfileAction_Type()
)
dsVdslLineCfgProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsVdslLineCfgProfileAction.setStatus("current")
_DsVdslLineCfgProfRowStatus_Type = RowStatus
_DsVdslLineCfgProfRowStatus_Object = MibTableColumn
dsVdslLineCfgProfRowStatus = _DsVdslLineCfgProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 6, 1, 1, 1, 100),
    _DsVdslLineCfgProfRowStatus_Type()
)
dsVdslLineCfgProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsVdslLineCfgProfRowStatus.setStatus("current")
_DsVdslCpeNosAutoUp_ObjectIdentity = ObjectIdentity
dsVdslCpeNosAutoUp = _DsVdslCpeNosAutoUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9)
)
_DsCpeNosAutoUpInfo_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpInfo = _DsCpeNosAutoUpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1)
)
_DsCpeNosAutoUpBase_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpBase = _DsCpeNosAutoUpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 1)
)


class _DsCpeNosAutoUpConfStatus_Type(Integer32):
    """Custom type dsCpeNosAutoUpConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsCpeNosAutoUpConfStatus_Type.__name__ = "Integer32"
_DsCpeNosAutoUpConfStatus_Object = MibScalar
dsCpeNosAutoUpConfStatus = _DsCpeNosAutoUpConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 1, 1),
    _DsCpeNosAutoUpConfStatus_Type()
)
dsCpeNosAutoUpConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpConfStatus.setStatus("current")
_DsCpeNosAutoUpControl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpControl = _DsCpeNosAutoUpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 2)
)


class _DsCpeNosAutoUpControlRequest_Type(Integer32):
    """Custom type dsCpeNosAutoUpControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setConfStatus", 1)
    )


_DsCpeNosAutoUpControlRequest_Type.__name__ = "Integer32"
_DsCpeNosAutoUpControlRequest_Object = MibScalar
dsCpeNosAutoUpControlRequest = _DsCpeNosAutoUpControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 2, 1),
    _DsCpeNosAutoUpControlRequest_Type()
)
dsCpeNosAutoUpControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpControlRequest.setStatus("current")
_DsCpeNosAutoUpControlStatus_Type = SleControlStatusType
_DsCpeNosAutoUpControlStatus_Object = MibScalar
dsCpeNosAutoUpControlStatus = _DsCpeNosAutoUpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 2, 2),
    _DsCpeNosAutoUpControlStatus_Type()
)
dsCpeNosAutoUpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpControlStatus.setStatus("current")
_DsCpeNosAutoUpControlTimer_Type = Gauge32
_DsCpeNosAutoUpControlTimer_Object = MibScalar
dsCpeNosAutoUpControlTimer = _DsCpeNosAutoUpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 2, 3),
    _DsCpeNosAutoUpControlTimer_Type()
)
dsCpeNosAutoUpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpControlTimer.setStatus("current")
_DsCpeNosAutoUpControlTimeStamp_Type = TimeTicks
_DsCpeNosAutoUpControlTimeStamp_Object = MibScalar
dsCpeNosAutoUpControlTimeStamp = _DsCpeNosAutoUpControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 2, 4),
    _DsCpeNosAutoUpControlTimeStamp_Type()
)
dsCpeNosAutoUpControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpControlTimeStamp.setStatus("current")
_DsCpeNosAutoUpControlReqResult_Type = SleControlRequestResultType
_DsCpeNosAutoUpControlReqResult_Object = MibScalar
dsCpeNosAutoUpControlReqResult = _DsCpeNosAutoUpControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 2, 5),
    _DsCpeNosAutoUpControlReqResult_Type()
)
dsCpeNosAutoUpControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpControlReqResult.setStatus("current")


class _DsCpeNosAutoUpControlConfStatus_Type(Integer32):
    """Custom type dsCpeNosAutoUpControlConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsCpeNosAutoUpControlConfStatus_Type.__name__ = "Integer32"
_DsCpeNosAutoUpControlConfStatus_Object = MibScalar
dsCpeNosAutoUpControlConfStatus = _DsCpeNosAutoUpControlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 1, 2, 6),
    _DsCpeNosAutoUpControlConfStatus_Type()
)
dsCpeNosAutoUpControlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpControlConfStatus.setStatus("current")
_DsCpeNosAutoUpCtrl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpCtrl = _DsCpeNosAutoUpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2)
)
_DsCpeNosAutoUpCtrlTable_Object = MibTable
dsCpeNosAutoUpCtrlTable = _DsCpeNosAutoUpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlTable.setStatus("current")
_DsCpeNosAutoUpCtrlEntry_Object = MibTableRow
dsCpeNosAutoUpCtrlEntry = _DsCpeNosAutoUpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 1, 1)
)
dsCpeNosAutoUpCtrlEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlName"),
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlEntry.setStatus("current")
_DsCpeNosAutoUpCtrlName_Type = OctetString
_DsCpeNosAutoUpCtrlName_Object = MibTableColumn
dsCpeNosAutoUpCtrlName = _DsCpeNosAutoUpCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 1, 1, 1),
    _DsCpeNosAutoUpCtrlName_Type()
)
dsCpeNosAutoUpCtrlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlName.setStatus("current")
_DsCpeNosAutoUpCtrlHW_Type = OctetString
_DsCpeNosAutoUpCtrlHW_Object = MibTableColumn
dsCpeNosAutoUpCtrlHW = _DsCpeNosAutoUpCtrlHW_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 1, 1, 2),
    _DsCpeNosAutoUpCtrlHW_Type()
)
dsCpeNosAutoUpCtrlHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlHW.setStatus("current")
_DsCpeNosAutoUpCtrlOldFW_Type = OctetString
_DsCpeNosAutoUpCtrlOldFW_Object = MibTableColumn
dsCpeNosAutoUpCtrlOldFW = _DsCpeNosAutoUpCtrlOldFW_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 1, 1, 3),
    _DsCpeNosAutoUpCtrlOldFW_Type()
)
dsCpeNosAutoUpCtrlOldFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlOldFW.setStatus("current")
_DsCpeNosAutoUpCtrlNewFW_Type = OctetString
_DsCpeNosAutoUpCtrlNewFW_Object = MibTableColumn
dsCpeNosAutoUpCtrlNewFW = _DsCpeNosAutoUpCtrlNewFW_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 1, 1, 4),
    _DsCpeNosAutoUpCtrlNewFW_Type()
)
dsCpeNosAutoUpCtrlNewFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlNewFW.setStatus("current")
_DsCpeNosAutoUpCtrlFWSize_Type = Unsigned32
_DsCpeNosAutoUpCtrlFWSize_Object = MibTableColumn
dsCpeNosAutoUpCtrlFWSize = _DsCpeNosAutoUpCtrlFWSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 1, 1, 5),
    _DsCpeNosAutoUpCtrlFWSize_Type()
)
dsCpeNosAutoUpCtrlFWSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlFWSize.setStatus("current")
_DsCpeNosAutoUpCtrlControl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpCtrlControl = _DsCpeNosAutoUpCtrlControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2)
)


class _DsCpeNosAutoUpCtrlControlRequest_Type(Integer32):
    """Custom type dsCpeNosAutoUpCtrlControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createControlList", 1),
          ("deleteControlList", 2))
    )


_DsCpeNosAutoUpCtrlControlRequest_Type.__name__ = "Integer32"
_DsCpeNosAutoUpCtrlControlRequest_Object = MibScalar
dsCpeNosAutoUpCtrlControlRequest = _DsCpeNosAutoUpCtrlControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 1),
    _DsCpeNosAutoUpCtrlControlRequest_Type()
)
dsCpeNosAutoUpCtrlControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlRequest.setStatus("current")
_DsCpeNosAutoUpCtrlControlStatus_Type = SleControlStatusType
_DsCpeNosAutoUpCtrlControlStatus_Object = MibScalar
dsCpeNosAutoUpCtrlControlStatus = _DsCpeNosAutoUpCtrlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 2),
    _DsCpeNosAutoUpCtrlControlStatus_Type()
)
dsCpeNosAutoUpCtrlControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlStatus.setStatus("current")
_DsCpeNosAutoUpCtrlControlTimer_Type = Gauge32
_DsCpeNosAutoUpCtrlControlTimer_Object = MibScalar
dsCpeNosAutoUpCtrlControlTimer = _DsCpeNosAutoUpCtrlControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 3),
    _DsCpeNosAutoUpCtrlControlTimer_Type()
)
dsCpeNosAutoUpCtrlControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlTimer.setStatus("current")
_DsCpeNosAutoUpCtrlControlTimeStamp_Type = TimeTicks
_DsCpeNosAutoUpCtrlControlTimeStamp_Object = MibScalar
dsCpeNosAutoUpCtrlControlTimeStamp = _DsCpeNosAutoUpCtrlControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 4),
    _DsCpeNosAutoUpCtrlControlTimeStamp_Type()
)
dsCpeNosAutoUpCtrlControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlTimeStamp.setStatus("current")
_DsCpeNosAutoUpCtrlControlReqResult_Type = SleControlRequestResultType
_DsCpeNosAutoUpCtrlControlReqResult_Object = MibScalar
dsCpeNosAutoUpCtrlControlReqResult = _DsCpeNosAutoUpCtrlControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 5),
    _DsCpeNosAutoUpCtrlControlReqResult_Type()
)
dsCpeNosAutoUpCtrlControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlReqResult.setStatus("current")
_DsCpeNosAutoUpCtrlControlName_Type = OctetString
_DsCpeNosAutoUpCtrlControlName_Object = MibScalar
dsCpeNosAutoUpCtrlControlName = _DsCpeNosAutoUpCtrlControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 6),
    _DsCpeNosAutoUpCtrlControlName_Type()
)
dsCpeNosAutoUpCtrlControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlName.setStatus("current")
_DsCpeNosAutoUpCtrlControlHW_Type = OctetString
_DsCpeNosAutoUpCtrlControlHW_Object = MibScalar
dsCpeNosAutoUpCtrlControlHW = _DsCpeNosAutoUpCtrlControlHW_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 7),
    _DsCpeNosAutoUpCtrlControlHW_Type()
)
dsCpeNosAutoUpCtrlControlHW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlHW.setStatus("current")
_DsCpeNosAutoUpCtrlControlOldFW_Type = OctetString
_DsCpeNosAutoUpCtrlControlOldFW_Object = MibScalar
dsCpeNosAutoUpCtrlControlOldFW = _DsCpeNosAutoUpCtrlControlOldFW_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 8),
    _DsCpeNosAutoUpCtrlControlOldFW_Type()
)
dsCpeNosAutoUpCtrlControlOldFW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlOldFW.setStatus("current")
_DsCpeNosAutoUpCtrlControlNewFW_Type = OctetString
_DsCpeNosAutoUpCtrlControlNewFW_Object = MibScalar
dsCpeNosAutoUpCtrlControlNewFW = _DsCpeNosAutoUpCtrlControlNewFW_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 9),
    _DsCpeNosAutoUpCtrlControlNewFW_Type()
)
dsCpeNosAutoUpCtrlControlNewFW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlNewFW.setStatus("current")
_DsCpeNosAutoUpCtrlControlFWSize_Type = Unsigned32
_DsCpeNosAutoUpCtrlControlFWSize_Object = MibScalar
dsCpeNosAutoUpCtrlControlFWSize = _DsCpeNosAutoUpCtrlControlFWSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 2, 2, 10),
    _DsCpeNosAutoUpCtrlControlFWSize_Type()
)
dsCpeNosAutoUpCtrlControlFWSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpCtrlControlFWSize.setStatus("current")
_DsCpeNosAutoUpSched_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpSched = _DsCpeNosAutoUpSched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3)
)
_DsCpeNosAutoUpSchedTable_Object = MibTable
dsCpeNosAutoUpSchedTable = _DsCpeNosAutoUpSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1)
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedTable.setStatus("current")
_DsCpeNosAutoUpSchedEntry_Object = MibTableRow
dsCpeNosAutoUpSchedEntry = _DsCpeNosAutoUpSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1)
)
dsCpeNosAutoUpSchedEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsCpeNosAutoUpSchedName"),
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedEntry.setStatus("current")
_DsCpeNosAutoUpSchedName_Type = OctetString
_DsCpeNosAutoUpSchedName_Object = MibTableColumn
dsCpeNosAutoUpSchedName = _DsCpeNosAutoUpSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 1),
    _DsCpeNosAutoUpSchedName_Type()
)
dsCpeNosAutoUpSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedName.setStatus("current")


class _DsCpeNosAutoUpSchedType_Type(Integer32):
    """Custom type dsCpeNosAutoUpSchedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("afterNsec", 1),
          ("period", 2),
          ("daily", 3),
          ("at", 4))
    )


_DsCpeNosAutoUpSchedType_Type.__name__ = "Integer32"
_DsCpeNosAutoUpSchedType_Object = MibTableColumn
dsCpeNosAutoUpSchedType = _DsCpeNosAutoUpSchedType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 2),
    _DsCpeNosAutoUpSchedType_Type()
)
dsCpeNosAutoUpSchedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedType.setStatus("current")
_DsCpeNosAutoUpSchedSec_Type = Integer32
_DsCpeNosAutoUpSchedSec_Object = MibTableColumn
dsCpeNosAutoUpSchedSec = _DsCpeNosAutoUpSchedSec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 3),
    _DsCpeNosAutoUpSchedSec_Type()
)
dsCpeNosAutoUpSchedSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedSec.setStatus("current")
_DsCpeNosAutoUpSchedInterval_Type = Integer32
_DsCpeNosAutoUpSchedInterval_Object = MibTableColumn
dsCpeNosAutoUpSchedInterval = _DsCpeNosAutoUpSchedInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 4),
    _DsCpeNosAutoUpSchedInterval_Type()
)
dsCpeNosAutoUpSchedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedInterval.setStatus("current")
_DsCpeNosAutoUpSchedYear_Type = Integer32
_DsCpeNosAutoUpSchedYear_Object = MibTableColumn
dsCpeNosAutoUpSchedYear = _DsCpeNosAutoUpSchedYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 5),
    _DsCpeNosAutoUpSchedYear_Type()
)
dsCpeNosAutoUpSchedYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedYear.setStatus("current")
_DsCpeNosAutoUpSchedMonth_Type = Integer32
_DsCpeNosAutoUpSchedMonth_Object = MibTableColumn
dsCpeNosAutoUpSchedMonth = _DsCpeNosAutoUpSchedMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 6),
    _DsCpeNosAutoUpSchedMonth_Type()
)
dsCpeNosAutoUpSchedMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedMonth.setStatus("current")
_DsCpeNosAutoUpSchedDay_Type = Integer32
_DsCpeNosAutoUpSchedDay_Object = MibTableColumn
dsCpeNosAutoUpSchedDay = _DsCpeNosAutoUpSchedDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 7),
    _DsCpeNosAutoUpSchedDay_Type()
)
dsCpeNosAutoUpSchedDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedDay.setStatus("current")
_DsCpeNosAutoUpSchedHour_Type = Integer32
_DsCpeNosAutoUpSchedHour_Object = MibTableColumn
dsCpeNosAutoUpSchedHour = _DsCpeNosAutoUpSchedHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 8),
    _DsCpeNosAutoUpSchedHour_Type()
)
dsCpeNosAutoUpSchedHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedHour.setStatus("current")
_DsCpeNosAutoUpSchedMinute_Type = Integer32
_DsCpeNosAutoUpSchedMinute_Object = MibTableColumn
dsCpeNosAutoUpSchedMinute = _DsCpeNosAutoUpSchedMinute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 9),
    _DsCpeNosAutoUpSchedMinute_Type()
)
dsCpeNosAutoUpSchedMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedMinute.setStatus("current")
_DsCpeNosAutoUpSchedPortMap_Type = OctetString
_DsCpeNosAutoUpSchedPortMap_Object = MibTableColumn
dsCpeNosAutoUpSchedPortMap = _DsCpeNosAutoUpSchedPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 10),
    _DsCpeNosAutoUpSchedPortMap_Type()
)
dsCpeNosAutoUpSchedPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedPortMap.setStatus("current")
_DsCpeNosAutoUpSchedCtrlMap_Type = OctetString
_DsCpeNosAutoUpSchedCtrlMap_Object = MibTableColumn
dsCpeNosAutoUpSchedCtrlMap = _DsCpeNosAutoUpSchedCtrlMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 1, 1, 11),
    _DsCpeNosAutoUpSchedCtrlMap_Type()
)
dsCpeNosAutoUpSchedCtrlMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCtrlMap.setStatus("current")
_DsCpeNosAutoUpSchedControl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpSchedControl = _DsCpeNosAutoUpSchedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2)
)


class _DsCpeNosAutoUpSchedControlRequest_Type(Integer32):
    """Custom type dsCpeNosAutoUpSchedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createScheduleList", 1),
          ("deleteScheduleList", 2))
    )


_DsCpeNosAutoUpSchedControlRequest_Type.__name__ = "Integer32"
_DsCpeNosAutoUpSchedControlRequest_Object = MibScalar
dsCpeNosAutoUpSchedControlRequest = _DsCpeNosAutoUpSchedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 1),
    _DsCpeNosAutoUpSchedControlRequest_Type()
)
dsCpeNosAutoUpSchedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlRequest.setStatus("current")
_DsCpeNosAutoUpSchedControlStatus_Type = SleControlStatusType
_DsCpeNosAutoUpSchedControlStatus_Object = MibScalar
dsCpeNosAutoUpSchedControlStatus = _DsCpeNosAutoUpSchedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 2),
    _DsCpeNosAutoUpSchedControlStatus_Type()
)
dsCpeNosAutoUpSchedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlStatus.setStatus("current")
_DsCpeNosAutoUpSchedControlTimer_Type = Gauge32
_DsCpeNosAutoUpSchedControlTimer_Object = MibScalar
dsCpeNosAutoUpSchedControlTimer = _DsCpeNosAutoUpSchedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 3),
    _DsCpeNosAutoUpSchedControlTimer_Type()
)
dsCpeNosAutoUpSchedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlTimer.setStatus("current")
_DsCpeNosAutoUpSchedControlTimeStamp_Type = TimeTicks
_DsCpeNosAutoUpSchedControlTimeStamp_Object = MibScalar
dsCpeNosAutoUpSchedControlTimeStamp = _DsCpeNosAutoUpSchedControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 4),
    _DsCpeNosAutoUpSchedControlTimeStamp_Type()
)
dsCpeNosAutoUpSchedControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlTimeStamp.setStatus("current")
_DsCpeNosAutoUpSchedControlReqResult_Type = SleControlRequestResultType
_DsCpeNosAutoUpSchedControlReqResult_Object = MibScalar
dsCpeNosAutoUpSchedControlReqResult = _DsCpeNosAutoUpSchedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 5),
    _DsCpeNosAutoUpSchedControlReqResult_Type()
)
dsCpeNosAutoUpSchedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlReqResult.setStatus("current")
_DsCpeNosAutoUpSchedControlName_Type = OctetString
_DsCpeNosAutoUpSchedControlName_Object = MibScalar
dsCpeNosAutoUpSchedControlName = _DsCpeNosAutoUpSchedControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 6),
    _DsCpeNosAutoUpSchedControlName_Type()
)
dsCpeNosAutoUpSchedControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlName.setStatus("current")


class _DsCpeNosAutoUpSchedControlType_Type(Integer32):
    """Custom type dsCpeNosAutoUpSchedControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("afterNsec", 1),
          ("period", 2),
          ("daily", 3),
          ("at", 4))
    )


_DsCpeNosAutoUpSchedControlType_Type.__name__ = "Integer32"
_DsCpeNosAutoUpSchedControlType_Object = MibScalar
dsCpeNosAutoUpSchedControlType = _DsCpeNosAutoUpSchedControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 7),
    _DsCpeNosAutoUpSchedControlType_Type()
)
dsCpeNosAutoUpSchedControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlType.setStatus("current")
_DsCpeNosAutoUpSchedControlSec_Type = Integer32
_DsCpeNosAutoUpSchedControlSec_Object = MibScalar
dsCpeNosAutoUpSchedControlSec = _DsCpeNosAutoUpSchedControlSec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 8),
    _DsCpeNosAutoUpSchedControlSec_Type()
)
dsCpeNosAutoUpSchedControlSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlSec.setStatus("current")
_DsCpeNosAutoUpSchedControlInterval_Type = Integer32
_DsCpeNosAutoUpSchedControlInterval_Object = MibScalar
dsCpeNosAutoUpSchedControlInterval = _DsCpeNosAutoUpSchedControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 9),
    _DsCpeNosAutoUpSchedControlInterval_Type()
)
dsCpeNosAutoUpSchedControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlInterval.setStatus("current")
_DsCpeNosAutoUpSchedControlYear_Type = Integer32
_DsCpeNosAutoUpSchedControlYear_Object = MibScalar
dsCpeNosAutoUpSchedControlYear = _DsCpeNosAutoUpSchedControlYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 10),
    _DsCpeNosAutoUpSchedControlYear_Type()
)
dsCpeNosAutoUpSchedControlYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlYear.setStatus("current")
_DsCpeNosAutoUpSchedControlMonth_Type = Integer32
_DsCpeNosAutoUpSchedControlMonth_Object = MibScalar
dsCpeNosAutoUpSchedControlMonth = _DsCpeNosAutoUpSchedControlMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 11),
    _DsCpeNosAutoUpSchedControlMonth_Type()
)
dsCpeNosAutoUpSchedControlMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlMonth.setStatus("current")
_DsCpeNosAutoupSchedControlDay_Type = Integer32
_DsCpeNosAutoupSchedControlDay_Object = MibScalar
dsCpeNosAutoupSchedControlDay = _DsCpeNosAutoupSchedControlDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 12),
    _DsCpeNosAutoupSchedControlDay_Type()
)
dsCpeNosAutoupSchedControlDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoupSchedControlDay.setStatus("current")
_DsCpeNosAutoUpSchedControlHour_Type = Integer32
_DsCpeNosAutoUpSchedControlHour_Object = MibScalar
dsCpeNosAutoUpSchedControlHour = _DsCpeNosAutoUpSchedControlHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 13),
    _DsCpeNosAutoUpSchedControlHour_Type()
)
dsCpeNosAutoUpSchedControlHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlHour.setStatus("current")
_DsCpeNosAutoUpSchedControlMinute_Type = Integer32
_DsCpeNosAutoUpSchedControlMinute_Object = MibScalar
dsCpeNosAutoUpSchedControlMinute = _DsCpeNosAutoUpSchedControlMinute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 14),
    _DsCpeNosAutoUpSchedControlMinute_Type()
)
dsCpeNosAutoUpSchedControlMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlMinute.setStatus("current")
_DsCpeNosAutoUpSchedControlPortMap_Type = OctetString
_DsCpeNosAutoUpSchedControlPortMap_Object = MibScalar
dsCpeNosAutoUpSchedControlPortMap = _DsCpeNosAutoUpSchedControlPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 15),
    _DsCpeNosAutoUpSchedControlPortMap_Type()
)
dsCpeNosAutoUpSchedControlPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlPortMap.setStatus("current")
_DsCpeNosAutoUpSchedControlCtrlMap_Type = OctetString
_DsCpeNosAutoUpSchedControlCtrlMap_Object = MibScalar
dsCpeNosAutoUpSchedControlCtrlMap = _DsCpeNosAutoUpSchedControlCtrlMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 3, 2, 16),
    _DsCpeNosAutoUpSchedControlCtrlMap_Type()
)
dsCpeNosAutoUpSchedControlCtrlMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedControlCtrlMap.setStatus("current")
_DsCpeNosAutoUpPort_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpPort = _DsCpeNosAutoUpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4)
)
_DsCpeNosAutoUpPortTable_Object = MibTable
dsCpeNosAutoUpPortTable = _DsCpeNosAutoUpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortTable.setStatus("current")
_DsCpeNosAutoUpPortEntry_Object = MibTableRow
dsCpeNosAutoUpPortEntry = _DsCpeNosAutoUpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1)
)
dsCpeNosAutoUpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortEntry.setStatus("current")
_DsCpeNosAutoUpPortPortNum_Type = Integer32
_DsCpeNosAutoUpPortPortNum_Object = MibTableColumn
dsCpeNosAutoUpPortPortNum = _DsCpeNosAutoUpPortPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1, 1),
    _DsCpeNosAutoUpPortPortNum_Type()
)
dsCpeNosAutoUpPortPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortPortNum.setStatus("current")
_DsCpeNosAutoUpPortRetry_Type = Integer32
_DsCpeNosAutoUpPortRetry_Object = MibTableColumn
dsCpeNosAutoUpPortRetry = _DsCpeNosAutoUpPortRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1, 2),
    _DsCpeNosAutoUpPortRetry_Type()
)
dsCpeNosAutoUpPortRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortRetry.setStatus("current")
_DsCpeNosAutoUpPortTimeout_Type = Integer32
_DsCpeNosAutoUpPortTimeout_Object = MibTableColumn
dsCpeNosAutoUpPortTimeout = _DsCpeNosAutoUpPortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1, 3),
    _DsCpeNosAutoUpPortTimeout_Type()
)
dsCpeNosAutoUpPortTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortTimeout.setStatus("current")
_DsCpeNosAutoUpPortSchedMap_Type = OctetString
_DsCpeNosAutoUpPortSchedMap_Object = MibTableColumn
dsCpeNosAutoUpPortSchedMap = _DsCpeNosAutoUpPortSchedMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1, 4),
    _DsCpeNosAutoUpPortSchedMap_Type()
)
dsCpeNosAutoUpPortSchedMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortSchedMap.setStatus("current")
_DsCpeNosAutoUpPortCurrState_Type = Integer32
_DsCpeNosAutoUpPortCurrState_Object = MibTableColumn
dsCpeNosAutoUpPortCurrState = _DsCpeNosAutoUpPortCurrState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1, 5),
    _DsCpeNosAutoUpPortCurrState_Type()
)
dsCpeNosAutoUpPortCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortCurrState.setStatus("current")
_DsCpeNosAutoUpPortCurrSched_Type = Integer32
_DsCpeNosAutoUpPortCurrSched_Object = MibTableColumn
dsCpeNosAutoUpPortCurrSched = _DsCpeNosAutoUpPortCurrSched_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1, 6),
    _DsCpeNosAutoUpPortCurrSched_Type()
)
dsCpeNosAutoUpPortCurrSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortCurrSched.setStatus("current")
_DsCpeNosAutoUpPortCurrCtrl_Type = Integer32
_DsCpeNosAutoUpPortCurrCtrl_Object = MibTableColumn
dsCpeNosAutoUpPortCurrCtrl = _DsCpeNosAutoUpPortCurrCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 1, 1, 7),
    _DsCpeNosAutoUpPortCurrCtrl_Type()
)
dsCpeNosAutoUpPortCurrCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortCurrCtrl.setStatus("current")
_DsCpeNosAutoUpPortControl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpPortControl = _DsCpeNosAutoUpPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2)
)


class _DsCpeNosAutoUpPortControlRequest_Type(Integer32):
    """Custom type dsCpeNosAutoUpPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setSchedule", 1)
    )


_DsCpeNosAutoUpPortControlRequest_Type.__name__ = "Integer32"
_DsCpeNosAutoUpPortControlRequest_Object = MibScalar
dsCpeNosAutoUpPortControlRequest = _DsCpeNosAutoUpPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 1),
    _DsCpeNosAutoUpPortControlRequest_Type()
)
dsCpeNosAutoUpPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlRequest.setStatus("current")
_DsCpeNosAutoUpPortControlStatus_Type = SleControlStatusType
_DsCpeNosAutoUpPortControlStatus_Object = MibScalar
dsCpeNosAutoUpPortControlStatus = _DsCpeNosAutoUpPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 2),
    _DsCpeNosAutoUpPortControlStatus_Type()
)
dsCpeNosAutoUpPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlStatus.setStatus("current")
_DsCpeNosAutoUpPortControlTimer_Type = Gauge32
_DsCpeNosAutoUpPortControlTimer_Object = MibScalar
dsCpeNosAutoUpPortControlTimer = _DsCpeNosAutoUpPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 3),
    _DsCpeNosAutoUpPortControlTimer_Type()
)
dsCpeNosAutoUpPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlTimer.setStatus("current")
_DsCpeNosAutoUpPortControlTimeStamp_Type = TimeTicks
_DsCpeNosAutoUpPortControlTimeStamp_Object = MibScalar
dsCpeNosAutoUpPortControlTimeStamp = _DsCpeNosAutoUpPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 4),
    _DsCpeNosAutoUpPortControlTimeStamp_Type()
)
dsCpeNosAutoUpPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlTimeStamp.setStatus("current")
_DsCpeNosAutoUpPortControlReqResult_Type = SleControlRequestResultType
_DsCpeNosAutoUpPortControlReqResult_Object = MibScalar
dsCpeNosAutoUpPortControlReqResult = _DsCpeNosAutoUpPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 5),
    _DsCpeNosAutoUpPortControlReqResult_Type()
)
dsCpeNosAutoUpPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlReqResult.setStatus("current")
_DsCpeNosAutoUpPortControlPortNum_Type = Integer32
_DsCpeNosAutoUpPortControlPortNum_Object = MibScalar
dsCpeNosAutoUpPortControlPortNum = _DsCpeNosAutoUpPortControlPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 6),
    _DsCpeNosAutoUpPortControlPortNum_Type()
)
dsCpeNosAutoUpPortControlPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlPortNum.setStatus("current")
_DsCpeNosAutoUpPortControlRetry_Type = Integer32
_DsCpeNosAutoUpPortControlRetry_Object = MibScalar
dsCpeNosAutoUpPortControlRetry = _DsCpeNosAutoUpPortControlRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 7),
    _DsCpeNosAutoUpPortControlRetry_Type()
)
dsCpeNosAutoUpPortControlRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlRetry.setStatus("current")
_DsCpeNosAutoUpPortControlTimeout_Type = Integer32
_DsCpeNosAutoUpPortControlTimeout_Object = MibScalar
dsCpeNosAutoUpPortControlTimeout = _DsCpeNosAutoUpPortControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 4, 2, 8),
    _DsCpeNosAutoUpPortControlTimeout_Type()
)
dsCpeNosAutoUpPortControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpPortControlTimeout.setStatus("current")
_DsCpeNosAutoUpNos_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpNos = _DsCpeNosAutoUpNos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5)
)
_DsCpeNosAutoUpNosTable_Object = MibTable
dsCpeNosAutoUpNosTable = _DsCpeNosAutoUpNosTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosTable.setStatus("current")
_DsCpeNosAutoUpNosEntry_Object = MibTableRow
dsCpeNosAutoUpNosEntry = _DsCpeNosAutoUpNosEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 1, 1)
)
dsCpeNosAutoUpNosEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsCpeNosAutoUpNosName"),
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosEntry.setStatus("current")
_DsCpeNosAutoUpNosName_Type = OctetString
_DsCpeNosAutoUpNosName_Object = MibTableColumn
dsCpeNosAutoUpNosName = _DsCpeNosAutoUpNosName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 1, 1, 1),
    _DsCpeNosAutoUpNosName_Type()
)
dsCpeNosAutoUpNosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosName.setStatus("current")
_DsCpeNosAutoUpNosSize_Type = Integer32
_DsCpeNosAutoUpNosSize_Object = MibTableColumn
dsCpeNosAutoUpNosSize = _DsCpeNosAutoUpNosSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 1, 1, 2),
    _DsCpeNosAutoUpNosSize_Type()
)
dsCpeNosAutoUpNosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosSize.setStatus("current")
_DsCpeNosAutoUpNosControl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpNosControl = _DsCpeNosAutoUpNosControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2)
)


class _DsCpeNosAutoUpNosControlRequest_Type(Integer32):
    """Custom type dsCpeNosAutoUpNosControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftpGet", 1),
          ("tftpGet", 2),
          ("delete", 3))
    )


_DsCpeNosAutoUpNosControlRequest_Type.__name__ = "Integer32"
_DsCpeNosAutoUpNosControlRequest_Object = MibScalar
dsCpeNosAutoUpNosControlRequest = _DsCpeNosAutoUpNosControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 1),
    _DsCpeNosAutoUpNosControlRequest_Type()
)
dsCpeNosAutoUpNosControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlRequest.setStatus("current")
_DsCpeNosAutoUpNosControlStatus_Type = SleControlStatusType
_DsCpeNosAutoUpNosControlStatus_Object = MibScalar
dsCpeNosAutoUpNosControlStatus = _DsCpeNosAutoUpNosControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 2),
    _DsCpeNosAutoUpNosControlStatus_Type()
)
dsCpeNosAutoUpNosControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlStatus.setStatus("current")
_DsCpeNosAutoUpNosControlTimer_Type = Gauge32
_DsCpeNosAutoUpNosControlTimer_Object = MibScalar
dsCpeNosAutoUpNosControlTimer = _DsCpeNosAutoUpNosControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 3),
    _DsCpeNosAutoUpNosControlTimer_Type()
)
dsCpeNosAutoUpNosControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlTimer.setStatus("current")
_DsCpeNosAutoUpNosControlTimeStamp_Type = TimeTicks
_DsCpeNosAutoUpNosControlTimeStamp_Object = MibScalar
dsCpeNosAutoUpNosControlTimeStamp = _DsCpeNosAutoUpNosControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 4),
    _DsCpeNosAutoUpNosControlTimeStamp_Type()
)
dsCpeNosAutoUpNosControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlTimeStamp.setStatus("current")
_DsCpeNosAutoUpNosControlReqResult_Type = SleControlRequestResultType
_DsCpeNosAutoUpNosControlReqResult_Object = MibScalar
dsCpeNosAutoUpNosControlReqResult = _DsCpeNosAutoUpNosControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 5),
    _DsCpeNosAutoUpNosControlReqResult_Type()
)
dsCpeNosAutoUpNosControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlReqResult.setStatus("current")
_DsCpeNosAutoUpNosControlServerIP_Type = IpAddress
_DsCpeNosAutoUpNosControlServerIP_Object = MibScalar
dsCpeNosAutoUpNosControlServerIP = _DsCpeNosAutoUpNosControlServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 6),
    _DsCpeNosAutoUpNosControlServerIP_Type()
)
dsCpeNosAutoUpNosControlServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlServerIP.setStatus("current")
_DsCpeNosAutoUpNosControlUserID_Type = OctetString
_DsCpeNosAutoUpNosControlUserID_Object = MibScalar
dsCpeNosAutoUpNosControlUserID = _DsCpeNosAutoUpNosControlUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 7),
    _DsCpeNosAutoUpNosControlUserID_Type()
)
dsCpeNosAutoUpNosControlUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlUserID.setStatus("current")
_DsCpeNosAutoUpNosControlPasswd_Type = OctetString
_DsCpeNosAutoUpNosControlPasswd_Object = MibScalar
dsCpeNosAutoUpNosControlPasswd = _DsCpeNosAutoUpNosControlPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 8),
    _DsCpeNosAutoUpNosControlPasswd_Type()
)
dsCpeNosAutoUpNosControlPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlPasswd.setStatus("current")
_DsCpeNosAutoUpNosControlSrcName_Type = OctetString
_DsCpeNosAutoUpNosControlSrcName_Object = MibScalar
dsCpeNosAutoUpNosControlSrcName = _DsCpeNosAutoUpNosControlSrcName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 9),
    _DsCpeNosAutoUpNosControlSrcName_Type()
)
dsCpeNosAutoUpNosControlSrcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlSrcName.setStatus("current")
_DsCpeNosAutoUpNosControlDestName_Type = OctetString
_DsCpeNosAutoUpNosControlDestName_Object = MibScalar
dsCpeNosAutoUpNosControlDestName = _DsCpeNosAutoUpNosControlDestName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 5, 2, 10),
    _DsCpeNosAutoUpNosControlDestName_Type()
)
dsCpeNosAutoUpNosControlDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpNosControlDestName.setStatus("current")
_DsCpeNosAutoUpResultLog_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpResultLog = _DsCpeNosAutoUpResultLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6)
)
_DsCpeNosAutoUpRLogTable_Object = MibTable
dsCpeNosAutoUpRLogTable = _DsCpeNosAutoUpRLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 1)
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogTable.setStatus("current")
_DsCpeNosAutoUpRLogEntry_Object = MibTableRow
dsCpeNosAutoUpRLogEntry = _DsCpeNosAutoUpRLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 1, 1)
)
dsCpeNosAutoUpRLogEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsCpeNosAutoUpRLogName"),
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogEntry.setStatus("current")
_DsCpeNosAutoUpRLogName_Type = OctetString
_DsCpeNosAutoUpRLogName_Object = MibTableColumn
dsCpeNosAutoUpRLogName = _DsCpeNosAutoUpRLogName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 1, 1, 1),
    _DsCpeNosAutoUpRLogName_Type()
)
dsCpeNosAutoUpRLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogName.setStatus("current")
_DsCpeNosAutoUpRLogValue_Type = OctetString
_DsCpeNosAutoUpRLogValue_Object = MibTableColumn
dsCpeNosAutoUpRLogValue = _DsCpeNosAutoUpRLogValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 1, 1, 2),
    _DsCpeNosAutoUpRLogValue_Type()
)
dsCpeNosAutoUpRLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogValue.setStatus("current")
_DsCpeNosAutoUpRLogControl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpRLogControl = _DsCpeNosAutoUpRLogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2)
)


class _DsCpeNosAutoUpRLogControlRequest_Type(Integer32):
    """Custom type dsCpeNosAutoUpRLogControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp-put", 1),
          ("tftp-put", 2),
          ("delete", 3))
    )


_DsCpeNosAutoUpRLogControlRequest_Type.__name__ = "Integer32"
_DsCpeNosAutoUpRLogControlRequest_Object = MibScalar
dsCpeNosAutoUpRLogControlRequest = _DsCpeNosAutoUpRLogControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 1),
    _DsCpeNosAutoUpRLogControlRequest_Type()
)
dsCpeNosAutoUpRLogControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlRequest.setStatus("current")
_DsCpeNosAutoUpRLogControlStatus_Type = SleControlStatusType
_DsCpeNosAutoUpRLogControlStatus_Object = MibScalar
dsCpeNosAutoUpRLogControlStatus = _DsCpeNosAutoUpRLogControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 2),
    _DsCpeNosAutoUpRLogControlStatus_Type()
)
dsCpeNosAutoUpRLogControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlStatus.setStatus("current")
_DsCpeNosAutoUpRLogControlTimer_Type = Gauge32
_DsCpeNosAutoUpRLogControlTimer_Object = MibScalar
dsCpeNosAutoUpRLogControlTimer = _DsCpeNosAutoUpRLogControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 3),
    _DsCpeNosAutoUpRLogControlTimer_Type()
)
dsCpeNosAutoUpRLogControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlTimer.setStatus("current")
_DsCpeNosAutoUpRLogControlTimeStamp_Type = TimeTicks
_DsCpeNosAutoUpRLogControlTimeStamp_Object = MibScalar
dsCpeNosAutoUpRLogControlTimeStamp = _DsCpeNosAutoUpRLogControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 4),
    _DsCpeNosAutoUpRLogControlTimeStamp_Type()
)
dsCpeNosAutoUpRLogControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlTimeStamp.setStatus("current")
_DsCpeNosAutoUpRLogControlReqResult_Type = SleControlRequestResultType
_DsCpeNosAutoUpRLogControlReqResult_Object = MibScalar
dsCpeNosAutoUpRLogControlReqResult = _DsCpeNosAutoUpRLogControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 5),
    _DsCpeNosAutoUpRLogControlReqResult_Type()
)
dsCpeNosAutoUpRLogControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlReqResult.setStatus("current")
_DsCpeNosAutoUpRLogControlServerIP_Type = IpAddress
_DsCpeNosAutoUpRLogControlServerIP_Object = MibScalar
dsCpeNosAutoUpRLogControlServerIP = _DsCpeNosAutoUpRLogControlServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 6),
    _DsCpeNosAutoUpRLogControlServerIP_Type()
)
dsCpeNosAutoUpRLogControlServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlServerIP.setStatus("current")
_DsCpeNosAutoUpRLogControlUserID_Type = OctetString
_DsCpeNosAutoUpRLogControlUserID_Object = MibScalar
dsCpeNosAutoUpRLogControlUserID = _DsCpeNosAutoUpRLogControlUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 7),
    _DsCpeNosAutoUpRLogControlUserID_Type()
)
dsCpeNosAutoUpRLogControlUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlUserID.setStatus("current")
_DsCpeNosAutoUpRLogControlPasswd_Type = OctetString
_DsCpeNosAutoUpRLogControlPasswd_Object = MibScalar
dsCpeNosAutoUpRLogControlPasswd = _DsCpeNosAutoUpRLogControlPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 8),
    _DsCpeNosAutoUpRLogControlPasswd_Type()
)
dsCpeNosAutoUpRLogControlPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlPasswd.setStatus("current")
_DsCpeNosAutoUpRLogControlSrcName_Type = OctetString
_DsCpeNosAutoUpRLogControlSrcName_Object = MibScalar
dsCpeNosAutoUpRLogControlSrcName = _DsCpeNosAutoUpRLogControlSrcName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 9),
    _DsCpeNosAutoUpRLogControlSrcName_Type()
)
dsCpeNosAutoUpRLogControlSrcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlSrcName.setStatus("current")
_DsCpeNosAutoUpRLogControlDestName_Type = OctetString
_DsCpeNosAutoUpRLogControlDestName_Object = MibScalar
dsCpeNosAutoUpRLogControlDestName = _DsCpeNosAutoUpRLogControlDestName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 6, 2, 10),
    _DsCpeNosAutoUpRLogControlDestName_Type()
)
dsCpeNosAutoUpRLogControlDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpRLogControlDestName.setStatus("current")
_DsCpeNosAutoUpSchedCount_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpSchedCount = _DsCpeNosAutoUpSchedCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7)
)
_DsCpeNosAutoUpSchedCountTable_Object = MibTable
dsCpeNosAutoUpSchedCountTable = _DsCpeNosAutoUpSchedCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 1)
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountTable.setStatus("current")
_DsCpeNosAutoUpSchedCountEntry_Object = MibTableRow
dsCpeNosAutoUpSchedCountEntry = _DsCpeNosAutoUpSchedCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 1, 1)
)
dsCpeNosAutoUpSchedCountEntry.setIndexNames(
    (0, "DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountPort"),
    (0, "DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountSched"),
)
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountEntry.setStatus("current")
_DsCpeNosAutoUpSchedCountPort_Type = Integer32
_DsCpeNosAutoUpSchedCountPort_Object = MibTableColumn
dsCpeNosAutoUpSchedCountPort = _DsCpeNosAutoUpSchedCountPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 1, 1, 1),
    _DsCpeNosAutoUpSchedCountPort_Type()
)
dsCpeNosAutoUpSchedCountPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountPort.setStatus("current")
_DsCpeNosAutoUpSchedCountSched_Type = Integer32
_DsCpeNosAutoUpSchedCountSched_Object = MibTableColumn
dsCpeNosAutoUpSchedCountSched = _DsCpeNosAutoUpSchedCountSched_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 1, 1, 2),
    _DsCpeNosAutoUpSchedCountSched_Type()
)
dsCpeNosAutoUpSchedCountSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountSched.setStatus("current")
_DsCpeNosAutoUpSchedCountFail_Type = Integer32
_DsCpeNosAutoUpSchedCountFail_Object = MibTableColumn
dsCpeNosAutoUpSchedCountFail = _DsCpeNosAutoUpSchedCountFail_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 1, 1, 3),
    _DsCpeNosAutoUpSchedCountFail_Type()
)
dsCpeNosAutoUpSchedCountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountFail.setStatus("current")
_DsCpeNosAutoUpSchedCountTotal_Type = Integer32
_DsCpeNosAutoUpSchedCountTotal_Object = MibTableColumn
dsCpeNosAutoUpSchedCountTotal = _DsCpeNosAutoUpSchedCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 1, 1, 4),
    _DsCpeNosAutoUpSchedCountTotal_Type()
)
dsCpeNosAutoUpSchedCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountTotal.setStatus("current")
_DsCpeNosAutoUpSchedCountControl_ObjectIdentity = ObjectIdentity
dsCpeNosAutoUpSchedCountControl = _DsCpeNosAutoUpSchedCountControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 2)
)


class _DsCpeNosAutoUpSchedCountControlRequest_Type(Integer32):
    """Custom type dsCpeNosAutoUpSchedCountControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStat", 1)
    )


_DsCpeNosAutoUpSchedCountControlRequest_Type.__name__ = "Integer32"
_DsCpeNosAutoUpSchedCountControlRequest_Object = MibScalar
dsCpeNosAutoUpSchedCountControlRequest = _DsCpeNosAutoUpSchedCountControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 2, 1),
    _DsCpeNosAutoUpSchedCountControlRequest_Type()
)
dsCpeNosAutoUpSchedCountControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountControlRequest.setStatus("current")
_DsCpeNosAutoUpSchedCountControlStatus_Type = Integer32
_DsCpeNosAutoUpSchedCountControlStatus_Object = MibScalar
dsCpeNosAutoUpSchedCountControlStatus = _DsCpeNosAutoUpSchedCountControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 2, 2),
    _DsCpeNosAutoUpSchedCountControlStatus_Type()
)
dsCpeNosAutoUpSchedCountControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountControlStatus.setStatus("current")
_DsCpeNosAutoUpSchedCountControlTimer_Type = Gauge32
_DsCpeNosAutoUpSchedCountControlTimer_Object = MibScalar
dsCpeNosAutoUpSchedCountControlTimer = _DsCpeNosAutoUpSchedCountControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 2, 3),
    _DsCpeNosAutoUpSchedCountControlTimer_Type()
)
dsCpeNosAutoUpSchedCountControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountControlTimer.setStatus("current")
_DsCpeNosAutoUpSchedCountControlTimeStamp_Type = TimeTicks
_DsCpeNosAutoUpSchedCountControlTimeStamp_Object = MibScalar
dsCpeNosAutoUpSchedCountControlTimeStamp = _DsCpeNosAutoUpSchedCountControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 2, 4),
    _DsCpeNosAutoUpSchedCountControlTimeStamp_Type()
)
dsCpeNosAutoUpSchedCountControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountControlTimeStamp.setStatus("current")
_DsCpeNosAutoUpSchedCountControlReqResult_Type = Integer32
_DsCpeNosAutoUpSchedCountControlReqResult_Object = MibScalar
dsCpeNosAutoUpSchedCountControlReqResult = _DsCpeNosAutoUpSchedCountControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 2, 5),
    _DsCpeNosAutoUpSchedCountControlReqResult_Type()
)
dsCpeNosAutoUpSchedCountControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountControlReqResult.setStatus("current")
_DsCpeNosAutoUpSchedCountControlPort_Type = Integer32
_DsCpeNosAutoUpSchedCountControlPort_Object = MibScalar
dsCpeNosAutoUpSchedCountControlPort = _DsCpeNosAutoUpSchedCountControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 9, 7, 2, 6),
    _DsCpeNosAutoUpSchedCountControlPort_Type()
)
dsCpeNosAutoUpSchedCountControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCpeNosAutoUpSchedCountControlPort.setStatus("current")

# Managed Objects groups

dsVdslObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 9, 3, 2, 20)
)
dsVdslObjectGroup.setObjects(
      *(("DASAN-DSL-MIB", "dsVdslSystemFWVersion"),
        ("DASAN-DSL-MIB", "dsVdslStatusBAIfindex"),
        ("DASAN-DSL-MIB", "dsVdslStatusBAPhySide"),
        ("DASAN-DSL-MIB", "dsVdslStatusBASectionSize"),
        ("DASAN-DSL-MIB", "dsVdslStatusBAAction"),
        ("DASAN-DSL-MIB", "dsVdslStatusBAStatus"),
        ("DASAN-DSL-MIB", "dsVdslStatusBALastTime"),
        ("DASAN-DSL-MIB", "dsVdslStatusBABitLoading"),
        ("DASAN-DSL-MIB", "dsVdslPMMARxFrameCount"),
        ("DASAN-DSL-MIB", "dsVdslPMMARxCRCErr"),
        ("DASAN-DSL-MIB", "dsVdslPMMARxDrop"),
        ("DASAN-DSL-MIB", "dsVdslPMMATxFrameCount"),
        ("DASAN-DSL-MIB", "dsVdslPMMATxDrop"),
        ("DASAN-DSL-MIB", "dsVdslPMMAEnetCrcErrCnt"),
        ("DASAN-DSL-MIB", "dsVdslPMMACleared"),
        ("DASAN-DSL-MIB", "dsVdslPMLos"),
        ("DASAN-DSL-MIB", "dsVdslPMLof"),
        ("DASAN-DSL-MIB", "dsVdslPMLol"),
        ("DASAN-DSL-MIB", "dsVdslPMCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPMUnCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPMCRC"),
        ("DASAN-DSL-MIB", "dsVdslPMServiceError"),
        ("DASAN-DSL-MIB", "dsVdslPMLoss"),
        ("DASAN-DSL-MIB", "dsVdslPMLofs"),
        ("DASAN-DSL-MIB", "dsVdslPMLols"),
        ("DASAN-DSL-MIB", "dsVdslPMESs"),
        ("DASAN-DSL-MIB", "dsVdslPMSESs"),
        ("DASAN-DSL-MIB", "dsVdslPMUASs"),
        ("DASAN-DSL-MIB", "dsVdslPMCRCs"),
        ("DASAN-DSL-MIB", "dsVdslPM15minElapsedTime"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayElapsedTime"),
        ("DASAN-DSL-MIB", "dsVdslPMClear"),
        ("DASAN-DSL-MIB", "dsVdslPM15minLos"),
        ("DASAN-DSL-MIB", "dsVdslPM15minLof"),
        ("DASAN-DSL-MIB", "dsVdslPM15minLol"),
        ("DASAN-DSL-MIB", "dsVdslPM15minCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPM15minUnCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPM15minCRC"),
        ("DASAN-DSL-MIB", "dsVdslPM15minServiceError"),
        ("DASAN-DSL-MIB", "dsVdslPM15minLoss"),
        ("DASAN-DSL-MIB", "dsVdslPM15minLofs"),
        ("DASAN-DSL-MIB", "dsVdslPM15minLols"),
        ("DASAN-DSL-MIB", "dsVdslPM15minESs"),
        ("DASAN-DSL-MIB", "dsVdslPM15minSESs"),
        ("DASAN-DSL-MIB", "dsVdslPM15minUASs"),
        ("DASAN-DSL-MIB", "dsVdslPM15minCRCs"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayLos"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayLof"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayLol"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayUnCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayCRC"),
        ("DASAN-DSL-MIB", "dsVdslPMdayServiceError"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayLoss"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayLofs"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayLols"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayESs"),
        ("DASAN-DSL-MIB", "dsVdslPM1daySESs"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayUASs"),
        ("DASAN-DSL-MIB", "dsVdslPM1dayCRCs"),
        ("DASAN-DSL-MIB", "dsVdslPMCpeLos"),
        ("DASAN-DSL-MIB", "dsVdslPMCpeLof"),
        ("DASAN-DSL-MIB", "dsVdslPMCpeCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPMCpeUnCorrBlk"),
        ("DASAN-DSL-MIB", "dsVdslPMCpeCRC"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgDownMaxSnrMgn"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgDownMinSnrMgn"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgDownTargetSnrMgn"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpMaxSnrMgn"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpTargetSnrMgn"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgDownMaxDataRate"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgDownMinDataRate"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpMaxDataRate"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpMinDataRate"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgDownMaxInterDelay"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpMaxInterDelay"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgHamband"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgDownINP"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpINP"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgPBOLength"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgPSDMaskLevel"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgTCMAdmin"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpboEnable"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgChannel"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgStandard"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgLineProfile"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgToneDisableMode"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgOptionband"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgProfRowStatus"),
        ("DASAN-DSL-MIB", "dsVdslPMCpeClear"),
        ("DASAN-DSL-MIB", "dsVdslSystemUpboConfLength"),
        ("DASAN-DSL-MIB", "dsVdslSystemUpboConfArrayK1"),
        ("DASAN-DSL-MIB", "dsVdslSystemUpboConfArrayK2"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsFlag"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsEwlName"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsEwlLength"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsRetryCount"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsAutoStatus"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsAutoDr"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsCurrentTryCount"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsEwlOnAutoDr"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsClearAutoDr"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingDsFlag"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingDsEwlName"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingDsEwlLength"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingDsFreqMin"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingDsFreqMax"),
        ("DASAN-DSL-MIB", "dsVdslLineConfMicroCut"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigMicroCutThreshold"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigMicroCutStatTotal"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigMicroCutStatCurrent"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigMicroCutStatLinkdown"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigMicroCutStatCleared"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnr"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrStatLinkdown"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrStatCleared"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpConfStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpControlRequest"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpControlStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpControlTimer"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpControlTimeStamp"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpControlReqResult"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpControlConfStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlHW"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlOldFW"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlNewFW"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlFWSize"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlRequest"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlTimer"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlTimeStamp"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlReqResult"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlHW"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlOldFW"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlNewFW"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpCtrlControlFWSize"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedType"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedSec"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedInterval"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedYear"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedMonth"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedDay"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedHour"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedMinute"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedPortMap"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCtrlMap"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlRequest"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlTimer"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlTimeStamp"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlReqResult"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlType"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlSec"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlInterval"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlYear"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlMonth"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoupSchedControlDay"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlHour"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlMinute"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlPortMap"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedControlCtrlMap"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortPortNum"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortRetry"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortTimeout"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortSchedMap"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortCurrState"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortCurrSched"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortCurrCtrl"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlRequest"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlTimer"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlTimeStamp"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlReqResult"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlPortNum"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlRetry"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpPortControlTimeout"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosSize"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlRequest"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlTimer"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlTimeStamp"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlReqResult"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlServerIP"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlUserID"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlPasswd"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlSrcName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpNosControlDestName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogValue"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlRequest"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlTimer"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlTimeStamp"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlReqResult"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlServerIP"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlUserID"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlPasswd"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlSrcName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpRLogControlDestName"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountPort"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountSched"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountFail"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountTotal"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountControlRequest"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountControlStatus"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountControlTimer"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountControlTimeStamp"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountControlReqResult"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrThreshCoMargin"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgUpMinSnrMgn"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrThreshCoTime"),
        ("DASAN-DSL-MIB", "dsVdslLineCfgProfileAction"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrThreshCpeMargin"),
        ("DASAN-DSL-MIB", "dsCpeNosAutoUpSchedCountControlPort"),
        ("DASAN-DSL-MIB", "dsVdslSystemLowPowerMode"),
        ("DASAN-DSL-MIB", "dsVdslStatusBASectionIndex"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsMethodType"),
        ("DASAN-DSL-MIB", "dsVdslLinePsdShapingUsStepCount"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrStatDownTime"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrStatDownRunning"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrStatUpRunning"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrStatUpTime"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrThreshUpMargin"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrThreshUpTime"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrThreshDownTime"),
        ("DASAN-DSL-MIB", "dsVdslLineConfigTrustSnrThreshDownMargin"))
)
if mibBuilder.loadTexts:
    dsVdslObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-DSL-MIB",
    **{"dasanDslMIB": dasanDslMIB,
       "dasanDslMIBObjects": dasanDslMIBObjects,
       "dsDslSystem": dsDslSystem,
       "dsDslModules": dsDslModules,
       "moduleNumber": moduleNumber,
       "moduleTableLastChange": moduleTableLastChange,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleDescr": moduleDescr,
       "moduleType": moduleType,
       "modulePhysAddress": modulePhysAddress,
       "moduleOperStatus": moduleOperStatus,
       "moduleUpTime": moduleUpTime,
       "moduleAvailableMemory": moduleAvailableMemory,
       "modulePortNumber": modulePortNumber,
       "modulePortIndexBase": modulePortIndexBase,
       "moduleSpecific": moduleSpecific,
       "dsDslPorts": dsDslPorts,
       "dsDslPortNumber": dsDslPortNumber,
       "dsDslPortTable": dsDslPortTable,
       "dsDslPortEntry": dsDslPortEntry,
       "portIndex": portIndex,
       "portDescr": portDescr,
       "portType": portType,
       "portIfIndex": portIfIndex,
       "portAdminStatus": portAdminStatus,
       "portOperStatus": portOperStatus,
       "portModemStatus": portModemStatus,
       "portLineQuality": portLineQuality,
       "portUpStreamSpeed": portUpStreamSpeed,
       "portDownStreamSpeed": portDownStreamSpeed,
       "portLastModemStatusChange": portLastModemStatusChange,
       "portSpecific": portSpecific,
       "dsDslLearnedMacs": dsDslLearnedMacs,
       "macNumber": macNumber,
       "macTable": macTable,
       "macEntry": macEntry,
       "macIndex": macIndex,
       "macAddress": macAddress,
       "agingTime": agingTime,
       "dasanDslMIBObjects2": dasanDslMIBObjects2,
       "dsVdslNotifications": dsVdslNotifications,
       "dsVdslSystemBaseInfo": dsVdslSystemBaseInfo,
       "dsVdslSystemFWVersion": dsVdslSystemFWVersion,
       "dsVdslSystemLowPowerMode": dsVdslSystemLowPowerMode,
       "dsVdslSystemBmeReset": dsVdslSystemBmeReset,
       "dsVdslSystemUpboConfTable": dsVdslSystemUpboConfTable,
       "dsVdslSystemUpboConfEntry": dsVdslSystemUpboConfEntry,
       "dsVdslSystemUpboConfLength": dsVdslSystemUpboConfLength,
       "dsVdslSystemUpboConfArrayK1": dsVdslSystemUpboConfArrayK1,
       "dsVdslSystemUpboConfArrayK2": dsVdslSystemUpboConfArrayK2,
       "dsVdslStatus": dsVdslStatus,
       "dsVdslStatusBitAlloc": dsVdslStatusBitAlloc,
       "dsVdslStatusBAIfindex": dsVdslStatusBAIfindex,
       "dsVdslStatusBAPhySide": dsVdslStatusBAPhySide,
       "dsVdslStatusBASectionSize": dsVdslStatusBASectionSize,
       "dsVdslStatusBAAction": dsVdslStatusBAAction,
       "dsVdslStatusBAStatus": dsVdslStatusBAStatus,
       "dsVdslStatusBALastTime": dsVdslStatusBALastTime,
       "dsVdslStatusBATable": dsVdslStatusBATable,
       "dsVdslStatusBAEntry": dsVdslStatusBAEntry,
       "dsVdslStatusBASectionIndex": dsVdslStatusBASectionIndex,
       "dsVdslStatusBABitLoading": dsVdslStatusBABitLoading,
       "dsVdslLine": dsVdslLine,
       "dsVdslLinePsdShaping": dsVdslLinePsdShaping,
       "dsVdslLinePsdShapingTable": dsVdslLinePsdShapingTable,
       "dsVdslLinePsdShapingEntry": dsVdslLinePsdShapingEntry,
       "dsVdslLinePsdShapingUsFlag": dsVdslLinePsdShapingUsFlag,
       "dsVdslLinePsdShapingUsEwlName": dsVdslLinePsdShapingUsEwlName,
       "dsVdslLinePsdShapingUsEwlLength": dsVdslLinePsdShapingUsEwlLength,
       "dsVdslLinePsdShapingUsRetryCount": dsVdslLinePsdShapingUsRetryCount,
       "dsVdslLinePsdShapingUsAutoStatus": dsVdslLinePsdShapingUsAutoStatus,
       "dsVdslLinePsdShapingUsAutoDr": dsVdslLinePsdShapingUsAutoDr,
       "dsVdslLinePsdShapingUsCurrentTryCount": dsVdslLinePsdShapingUsCurrentTryCount,
       "dsVdslLinePsdShapingUsEwlOnAutoDr": dsVdslLinePsdShapingUsEwlOnAutoDr,
       "dsVdslLinePsdShapingUsClearAutoDr": dsVdslLinePsdShapingUsClearAutoDr,
       "dsVdslLinePsdShapingUsMethodType": dsVdslLinePsdShapingUsMethodType,
       "dsVdslLinePsdShapingUsStepCount": dsVdslLinePsdShapingUsStepCount,
       "dsVdslLinePsdShapingDsFlag": dsVdslLinePsdShapingDsFlag,
       "dsVdslLinePsdShapingDsEwlName": dsVdslLinePsdShapingDsEwlName,
       "dsVdslLinePsdShapingDsEwlLength": dsVdslLinePsdShapingDsEwlLength,
       "dsVdslLinePsdShapingDsFreqMin": dsVdslLinePsdShapingDsFreqMin,
       "dsVdslLinePsdShapingDsFreqMax": dsVdslLinePsdShapingDsFreqMax,
       "dsVdslLineConfig": dsVdslLineConfig,
       "dsVdslLineConfigTable": dsVdslLineConfigTable,
       "dsVdslLineConfigEntry": dsVdslLineConfigEntry,
       "dsVdslLineConfMicroCut": dsVdslLineConfMicroCut,
       "dsVdslLineConfigMicroCutThreshold": dsVdslLineConfigMicroCutThreshold,
       "dsVdslLineConfigMicroCutStatTotal": dsVdslLineConfigMicroCutStatTotal,
       "dsVdslLineConfigMicroCutStatCurrent": dsVdslLineConfigMicroCutStatCurrent,
       "dsVdslLineConfigMicroCutStatLinkdown": dsVdslLineConfigMicroCutStatLinkdown,
       "dsVdslLineConfigMicroCutStatCleared": dsVdslLineConfigMicroCutStatCleared,
       "dsVdslLineConfigTrustSnr": dsVdslLineConfigTrustSnr,
       "dsVdslLineConfigTrustSnrThreshUpMargin": dsVdslLineConfigTrustSnrThreshUpMargin,
       "dsVdslLineConfigTrustSnrThreshUpTime": dsVdslLineConfigTrustSnrThreshUpTime,
       "dsVdslLineConfigTrustSnrThreshDownMargin": dsVdslLineConfigTrustSnrThreshDownMargin,
       "dsVdslLineConfigTrustSnrThreshDownTime": dsVdslLineConfigTrustSnrThreshDownTime,
       "dsVdslLineConfigTrustSnrStatUpRunning": dsVdslLineConfigTrustSnrStatUpRunning,
       "dsVdslLineConfigTrustSnrStatUpTime": dsVdslLineConfigTrustSnrStatUpTime,
       "dsVdslLineConfigTrustSnrStatDownRunning": dsVdslLineConfigTrustSnrStatDownRunning,
       "dsVdslLineConfigTrustSnrStatDownTime": dsVdslLineConfigTrustSnrStatDownTime,
       "dsVdslLineConfigTrustSnrStatLinkdown": dsVdslLineConfigTrustSnrStatLinkdown,
       "dsVdslLineConfigTrustSnrStatCleared": dsVdslLineConfigTrustSnrStatCleared,
       "dsVdslLineStatus": dsVdslLineStatus,
       "dsVdslLineStatusTable": dsVdslLineStatusTable,
       "dsVdslLineStatusEntry": dsVdslLineStatusEntry,
       "dsVdslLineStatusCpeLinkdownReason": dsVdslLineStatusCpeLinkdownReason,
       "dsVdslPM": dsVdslPM,
       "dsVdslPMMediaAdaptor": dsVdslPMMediaAdaptor,
       "dsVdslPMMATable": dsVdslPMMATable,
       "dsVdslPMMAEntry": dsVdslPMMAEntry,
       "dsVdslPMMARxFrameCount": dsVdslPMMARxFrameCount,
       "dsVdslPMMARxCRCErr": dsVdslPMMARxCRCErr,
       "dsVdslPMMARxDrop": dsVdslPMMARxDrop,
       "dsVdslPMMATxFrameCount": dsVdslPMMATxFrameCount,
       "dsVdslPMMATxDrop": dsVdslPMMATxDrop,
       "dsVdslPMMAEnetCrcErrCnt": dsVdslPMMAEnetCrcErrCnt,
       "dsVdslPMMACleared": dsVdslPMMACleared,
       "dsVdslPMStatCount": dsVdslPMStatCount,
       "dsVdslPMCoStatTable": dsVdslPMCoStatTable,
       "dsVdslPMCoStatEntry": dsVdslPMCoStatEntry,
       "dsVdslPMLos": dsVdslPMLos,
       "dsVdslPMLof": dsVdslPMLof,
       "dsVdslPMLol": dsVdslPMLol,
       "dsVdslPMCorrBlk": dsVdslPMCorrBlk,
       "dsVdslPMUnCorrBlk": dsVdslPMUnCorrBlk,
       "dsVdslPMCRC": dsVdslPMCRC,
       "dsVdslPMServiceError": dsVdslPMServiceError,
       "dsVdslPMLoss": dsVdslPMLoss,
       "dsVdslPMLofs": dsVdslPMLofs,
       "dsVdslPMLols": dsVdslPMLols,
       "dsVdslPMESs": dsVdslPMESs,
       "dsVdslPMSESs": dsVdslPMSESs,
       "dsVdslPMUASs": dsVdslPMUASs,
       "dsVdslPMCRCs": dsVdslPMCRCs,
       "dsVdslPM15minElapsedTime": dsVdslPM15minElapsedTime,
       "dsVdslPM1dayElapsedTime": dsVdslPM1dayElapsedTime,
       "dsVdslPMClear": dsVdslPMClear,
       "dsVdslPMCoStat15minTable": dsVdslPMCoStat15minTable,
       "dsVdslPMCoStat15minEntry": dsVdslPMCoStat15minEntry,
       "dsVdslPM15minInterval": dsVdslPM15minInterval,
       "dsVdslPM15minLos": dsVdslPM15minLos,
       "dsVdslPM15minLof": dsVdslPM15minLof,
       "dsVdslPM15minLol": dsVdslPM15minLol,
       "dsVdslPM15minCorrBlk": dsVdslPM15minCorrBlk,
       "dsVdslPM15minUnCorrBlk": dsVdslPM15minUnCorrBlk,
       "dsVdslPM15minCRC": dsVdslPM15minCRC,
       "dsVdslPM15minServiceError": dsVdslPM15minServiceError,
       "dsVdslPM15minLoss": dsVdslPM15minLoss,
       "dsVdslPM15minLofs": dsVdslPM15minLofs,
       "dsVdslPM15minLols": dsVdslPM15minLols,
       "dsVdslPM15minESs": dsVdslPM15minESs,
       "dsVdslPM15minSESs": dsVdslPM15minSESs,
       "dsVdslPM15minUASs": dsVdslPM15minUASs,
       "dsVdslPM15minCRCs": dsVdslPM15minCRCs,
       "dsVdslPMCoStat1dayTable": dsVdslPMCoStat1dayTable,
       "dsVdslPMCoStat1dayEntry": dsVdslPMCoStat1dayEntry,
       "dsVdslPM1dayInterval": dsVdslPM1dayInterval,
       "dsVdslPM1dayLos": dsVdslPM1dayLos,
       "dsVdslPM1dayLof": dsVdslPM1dayLof,
       "dsVdslPM1dayLol": dsVdslPM1dayLol,
       "dsVdslPM1dayCorrBlk": dsVdslPM1dayCorrBlk,
       "dsVdslPM1dayUnCorrBlk": dsVdslPM1dayUnCorrBlk,
       "dsVdslPM1dayCRC": dsVdslPM1dayCRC,
       "dsVdslPMdayServiceError": dsVdslPMdayServiceError,
       "dsVdslPM1dayLoss": dsVdslPM1dayLoss,
       "dsVdslPM1dayLofs": dsVdslPM1dayLofs,
       "dsVdslPM1dayLols": dsVdslPM1dayLols,
       "dsVdslPM1dayESs": dsVdslPM1dayESs,
       "dsVdslPM1daySESs": dsVdslPM1daySESs,
       "dsVdslPM1dayUASs": dsVdslPM1dayUASs,
       "dsVdslPM1dayCRCs": dsVdslPM1dayCRCs,
       "dsVdslPMCpeStatTable": dsVdslPMCpeStatTable,
       "dsVdslPMCpeStatEntry": dsVdslPMCpeStatEntry,
       "dsVdslPMCpeLos": dsVdslPMCpeLos,
       "dsVdslPMCpeLof": dsVdslPMCpeLof,
       "dsVdslPMCpeCorrBlk": dsVdslPMCpeCorrBlk,
       "dsVdslPMCpeUnCorrBlk": dsVdslPMCpeUnCorrBlk,
       "dsVdslPMCpeCRC": dsVdslPMCpeCRC,
       "dsVdslPMCpeClear": dsVdslPMCpeClear,
       "dsVdslProfile": dsVdslProfile,
       "dsVdslLineCfgProfile": dsVdslLineCfgProfile,
       "dsVdslLineCfgProfileTable": dsVdslLineCfgProfileTable,
       "dsVdslLineCfgProfileEntry": dsVdslLineCfgProfileEntry,
       "dsVdslLineCfgProfileName": dsVdslLineCfgProfileName,
       "dsVdslLineCfgDownMaxSnrMgn": dsVdslLineCfgDownMaxSnrMgn,
       "dsVdslLineCfgDownMinSnrMgn": dsVdslLineCfgDownMinSnrMgn,
       "dsVdslLineCfgDownTargetSnrMgn": dsVdslLineCfgDownTargetSnrMgn,
       "dsVdslLineCfgUpMaxSnrMgn": dsVdslLineCfgUpMaxSnrMgn,
       "dsVdslLineCfgUpMinSnrMgn": dsVdslLineCfgUpMinSnrMgn,
       "dsVdslLineCfgUpTargetSnrMgn": dsVdslLineCfgUpTargetSnrMgn,
       "dsVdslLineCfgDownMaxDataRate": dsVdslLineCfgDownMaxDataRate,
       "dsVdslLineCfgDownMinDataRate": dsVdslLineCfgDownMinDataRate,
       "dsVdslLineCfgUpMaxDataRate": dsVdslLineCfgUpMaxDataRate,
       "dsVdslLineCfgUpMinDataRate": dsVdslLineCfgUpMinDataRate,
       "dsVdslLineCfgDownMaxInterDelay": dsVdslLineCfgDownMaxInterDelay,
       "dsVdslLineCfgUpMaxInterDelay": dsVdslLineCfgUpMaxInterDelay,
       "dsVdslLineCfgHamband": dsVdslLineCfgHamband,
       "dsVdslLineCfgDownINP": dsVdslLineCfgDownINP,
       "dsVdslLineCfgUpINP": dsVdslLineCfgUpINP,
       "dsVdslLineCfgPBOLength": dsVdslLineCfgPBOLength,
       "dsVdslLineCfgPSDMaskLevel": dsVdslLineCfgPSDMaskLevel,
       "dsVdslLineCfgTCMAdmin": dsVdslLineCfgTCMAdmin,
       "dsVdslLineCfgUpboEnable": dsVdslLineCfgUpboEnable,
       "dsVdslLineCfgChannel": dsVdslLineCfgChannel,
       "dsVdslLineCfgStandard": dsVdslLineCfgStandard,
       "dsVdslLineCfgLineProfile": dsVdslLineCfgLineProfile,
       "dsVdslLineCfgToneDisableMode": dsVdslLineCfgToneDisableMode,
       "dsVdslLineCfgOptionband": dsVdslLineCfgOptionband,
       "dsVdslLineCfgProfileAction": dsVdslLineCfgProfileAction,
       "dsVdslLineCfgProfRowStatus": dsVdslLineCfgProfRowStatus,
       "dsVdslCpeNosAutoUp": dsVdslCpeNosAutoUp,
       "dsCpeNosAutoUpInfo": dsCpeNosAutoUpInfo,
       "dsCpeNosAutoUpBase": dsCpeNosAutoUpBase,
       "dsCpeNosAutoUpConfStatus": dsCpeNosAutoUpConfStatus,
       "dsCpeNosAutoUpControl": dsCpeNosAutoUpControl,
       "dsCpeNosAutoUpControlRequest": dsCpeNosAutoUpControlRequest,
       "dsCpeNosAutoUpControlStatus": dsCpeNosAutoUpControlStatus,
       "dsCpeNosAutoUpControlTimer": dsCpeNosAutoUpControlTimer,
       "dsCpeNosAutoUpControlTimeStamp": dsCpeNosAutoUpControlTimeStamp,
       "dsCpeNosAutoUpControlReqResult": dsCpeNosAutoUpControlReqResult,
       "dsCpeNosAutoUpControlConfStatus": dsCpeNosAutoUpControlConfStatus,
       "dsCpeNosAutoUpCtrl": dsCpeNosAutoUpCtrl,
       "dsCpeNosAutoUpCtrlTable": dsCpeNosAutoUpCtrlTable,
       "dsCpeNosAutoUpCtrlEntry": dsCpeNosAutoUpCtrlEntry,
       "dsCpeNosAutoUpCtrlName": dsCpeNosAutoUpCtrlName,
       "dsCpeNosAutoUpCtrlHW": dsCpeNosAutoUpCtrlHW,
       "dsCpeNosAutoUpCtrlOldFW": dsCpeNosAutoUpCtrlOldFW,
       "dsCpeNosAutoUpCtrlNewFW": dsCpeNosAutoUpCtrlNewFW,
       "dsCpeNosAutoUpCtrlFWSize": dsCpeNosAutoUpCtrlFWSize,
       "dsCpeNosAutoUpCtrlControl": dsCpeNosAutoUpCtrlControl,
       "dsCpeNosAutoUpCtrlControlRequest": dsCpeNosAutoUpCtrlControlRequest,
       "dsCpeNosAutoUpCtrlControlStatus": dsCpeNosAutoUpCtrlControlStatus,
       "dsCpeNosAutoUpCtrlControlTimer": dsCpeNosAutoUpCtrlControlTimer,
       "dsCpeNosAutoUpCtrlControlTimeStamp": dsCpeNosAutoUpCtrlControlTimeStamp,
       "dsCpeNosAutoUpCtrlControlReqResult": dsCpeNosAutoUpCtrlControlReqResult,
       "dsCpeNosAutoUpCtrlControlName": dsCpeNosAutoUpCtrlControlName,
       "dsCpeNosAutoUpCtrlControlHW": dsCpeNosAutoUpCtrlControlHW,
       "dsCpeNosAutoUpCtrlControlOldFW": dsCpeNosAutoUpCtrlControlOldFW,
       "dsCpeNosAutoUpCtrlControlNewFW": dsCpeNosAutoUpCtrlControlNewFW,
       "dsCpeNosAutoUpCtrlControlFWSize": dsCpeNosAutoUpCtrlControlFWSize,
       "dsCpeNosAutoUpSched": dsCpeNosAutoUpSched,
       "dsCpeNosAutoUpSchedTable": dsCpeNosAutoUpSchedTable,
       "dsCpeNosAutoUpSchedEntry": dsCpeNosAutoUpSchedEntry,
       "dsCpeNosAutoUpSchedName": dsCpeNosAutoUpSchedName,
       "dsCpeNosAutoUpSchedType": dsCpeNosAutoUpSchedType,
       "dsCpeNosAutoUpSchedSec": dsCpeNosAutoUpSchedSec,
       "dsCpeNosAutoUpSchedInterval": dsCpeNosAutoUpSchedInterval,
       "dsCpeNosAutoUpSchedYear": dsCpeNosAutoUpSchedYear,
       "dsCpeNosAutoUpSchedMonth": dsCpeNosAutoUpSchedMonth,
       "dsCpeNosAutoUpSchedDay": dsCpeNosAutoUpSchedDay,
       "dsCpeNosAutoUpSchedHour": dsCpeNosAutoUpSchedHour,
       "dsCpeNosAutoUpSchedMinute": dsCpeNosAutoUpSchedMinute,
       "dsCpeNosAutoUpSchedPortMap": dsCpeNosAutoUpSchedPortMap,
       "dsCpeNosAutoUpSchedCtrlMap": dsCpeNosAutoUpSchedCtrlMap,
       "dsCpeNosAutoUpSchedControl": dsCpeNosAutoUpSchedControl,
       "dsCpeNosAutoUpSchedControlRequest": dsCpeNosAutoUpSchedControlRequest,
       "dsCpeNosAutoUpSchedControlStatus": dsCpeNosAutoUpSchedControlStatus,
       "dsCpeNosAutoUpSchedControlTimer": dsCpeNosAutoUpSchedControlTimer,
       "dsCpeNosAutoUpSchedControlTimeStamp": dsCpeNosAutoUpSchedControlTimeStamp,
       "dsCpeNosAutoUpSchedControlReqResult": dsCpeNosAutoUpSchedControlReqResult,
       "dsCpeNosAutoUpSchedControlName": dsCpeNosAutoUpSchedControlName,
       "dsCpeNosAutoUpSchedControlType": dsCpeNosAutoUpSchedControlType,
       "dsCpeNosAutoUpSchedControlSec": dsCpeNosAutoUpSchedControlSec,
       "dsCpeNosAutoUpSchedControlInterval": dsCpeNosAutoUpSchedControlInterval,
       "dsCpeNosAutoUpSchedControlYear": dsCpeNosAutoUpSchedControlYear,
       "dsCpeNosAutoUpSchedControlMonth": dsCpeNosAutoUpSchedControlMonth,
       "dsCpeNosAutoupSchedControlDay": dsCpeNosAutoupSchedControlDay,
       "dsCpeNosAutoUpSchedControlHour": dsCpeNosAutoUpSchedControlHour,
       "dsCpeNosAutoUpSchedControlMinute": dsCpeNosAutoUpSchedControlMinute,
       "dsCpeNosAutoUpSchedControlPortMap": dsCpeNosAutoUpSchedControlPortMap,
       "dsCpeNosAutoUpSchedControlCtrlMap": dsCpeNosAutoUpSchedControlCtrlMap,
       "dsCpeNosAutoUpPort": dsCpeNosAutoUpPort,
       "dsCpeNosAutoUpPortTable": dsCpeNosAutoUpPortTable,
       "dsCpeNosAutoUpPortEntry": dsCpeNosAutoUpPortEntry,
       "dsCpeNosAutoUpPortPortNum": dsCpeNosAutoUpPortPortNum,
       "dsCpeNosAutoUpPortRetry": dsCpeNosAutoUpPortRetry,
       "dsCpeNosAutoUpPortTimeout": dsCpeNosAutoUpPortTimeout,
       "dsCpeNosAutoUpPortSchedMap": dsCpeNosAutoUpPortSchedMap,
       "dsCpeNosAutoUpPortCurrState": dsCpeNosAutoUpPortCurrState,
       "dsCpeNosAutoUpPortCurrSched": dsCpeNosAutoUpPortCurrSched,
       "dsCpeNosAutoUpPortCurrCtrl": dsCpeNosAutoUpPortCurrCtrl,
       "dsCpeNosAutoUpPortControl": dsCpeNosAutoUpPortControl,
       "dsCpeNosAutoUpPortControlRequest": dsCpeNosAutoUpPortControlRequest,
       "dsCpeNosAutoUpPortControlStatus": dsCpeNosAutoUpPortControlStatus,
       "dsCpeNosAutoUpPortControlTimer": dsCpeNosAutoUpPortControlTimer,
       "dsCpeNosAutoUpPortControlTimeStamp": dsCpeNosAutoUpPortControlTimeStamp,
       "dsCpeNosAutoUpPortControlReqResult": dsCpeNosAutoUpPortControlReqResult,
       "dsCpeNosAutoUpPortControlPortNum": dsCpeNosAutoUpPortControlPortNum,
       "dsCpeNosAutoUpPortControlRetry": dsCpeNosAutoUpPortControlRetry,
       "dsCpeNosAutoUpPortControlTimeout": dsCpeNosAutoUpPortControlTimeout,
       "dsCpeNosAutoUpNos": dsCpeNosAutoUpNos,
       "dsCpeNosAutoUpNosTable": dsCpeNosAutoUpNosTable,
       "dsCpeNosAutoUpNosEntry": dsCpeNosAutoUpNosEntry,
       "dsCpeNosAutoUpNosName": dsCpeNosAutoUpNosName,
       "dsCpeNosAutoUpNosSize": dsCpeNosAutoUpNosSize,
       "dsCpeNosAutoUpNosControl": dsCpeNosAutoUpNosControl,
       "dsCpeNosAutoUpNosControlRequest": dsCpeNosAutoUpNosControlRequest,
       "dsCpeNosAutoUpNosControlStatus": dsCpeNosAutoUpNosControlStatus,
       "dsCpeNosAutoUpNosControlTimer": dsCpeNosAutoUpNosControlTimer,
       "dsCpeNosAutoUpNosControlTimeStamp": dsCpeNosAutoUpNosControlTimeStamp,
       "dsCpeNosAutoUpNosControlReqResult": dsCpeNosAutoUpNosControlReqResult,
       "dsCpeNosAutoUpNosControlServerIP": dsCpeNosAutoUpNosControlServerIP,
       "dsCpeNosAutoUpNosControlUserID": dsCpeNosAutoUpNosControlUserID,
       "dsCpeNosAutoUpNosControlPasswd": dsCpeNosAutoUpNosControlPasswd,
       "dsCpeNosAutoUpNosControlSrcName": dsCpeNosAutoUpNosControlSrcName,
       "dsCpeNosAutoUpNosControlDestName": dsCpeNosAutoUpNosControlDestName,
       "dsCpeNosAutoUpResultLog": dsCpeNosAutoUpResultLog,
       "dsCpeNosAutoUpRLogTable": dsCpeNosAutoUpRLogTable,
       "dsCpeNosAutoUpRLogEntry": dsCpeNosAutoUpRLogEntry,
       "dsCpeNosAutoUpRLogName": dsCpeNosAutoUpRLogName,
       "dsCpeNosAutoUpRLogValue": dsCpeNosAutoUpRLogValue,
       "dsCpeNosAutoUpRLogControl": dsCpeNosAutoUpRLogControl,
       "dsCpeNosAutoUpRLogControlRequest": dsCpeNosAutoUpRLogControlRequest,
       "dsCpeNosAutoUpRLogControlStatus": dsCpeNosAutoUpRLogControlStatus,
       "dsCpeNosAutoUpRLogControlTimer": dsCpeNosAutoUpRLogControlTimer,
       "dsCpeNosAutoUpRLogControlTimeStamp": dsCpeNosAutoUpRLogControlTimeStamp,
       "dsCpeNosAutoUpRLogControlReqResult": dsCpeNosAutoUpRLogControlReqResult,
       "dsCpeNosAutoUpRLogControlServerIP": dsCpeNosAutoUpRLogControlServerIP,
       "dsCpeNosAutoUpRLogControlUserID": dsCpeNosAutoUpRLogControlUserID,
       "dsCpeNosAutoUpRLogControlPasswd": dsCpeNosAutoUpRLogControlPasswd,
       "dsCpeNosAutoUpRLogControlSrcName": dsCpeNosAutoUpRLogControlSrcName,
       "dsCpeNosAutoUpRLogControlDestName": dsCpeNosAutoUpRLogControlDestName,
       "dsCpeNosAutoUpSchedCount": dsCpeNosAutoUpSchedCount,
       "dsCpeNosAutoUpSchedCountTable": dsCpeNosAutoUpSchedCountTable,
       "dsCpeNosAutoUpSchedCountEntry": dsCpeNosAutoUpSchedCountEntry,
       "dsCpeNosAutoUpSchedCountPort": dsCpeNosAutoUpSchedCountPort,
       "dsCpeNosAutoUpSchedCountSched": dsCpeNosAutoUpSchedCountSched,
       "dsCpeNosAutoUpSchedCountFail": dsCpeNosAutoUpSchedCountFail,
       "dsCpeNosAutoUpSchedCountTotal": dsCpeNosAutoUpSchedCountTotal,
       "dsCpeNosAutoUpSchedCountControl": dsCpeNosAutoUpSchedCountControl,
       "dsCpeNosAutoUpSchedCountControlRequest": dsCpeNosAutoUpSchedCountControlRequest,
       "dsCpeNosAutoUpSchedCountControlStatus": dsCpeNosAutoUpSchedCountControlStatus,
       "dsCpeNosAutoUpSchedCountControlTimer": dsCpeNosAutoUpSchedCountControlTimer,
       "dsCpeNosAutoUpSchedCountControlTimeStamp": dsCpeNosAutoUpSchedCountControlTimeStamp,
       "dsCpeNosAutoUpSchedCountControlReqResult": dsCpeNosAutoUpSchedCountControlReqResult,
       "dsCpeNosAutoUpSchedCountControlPort": dsCpeNosAutoUpSchedCountControlPort,
       "dsVdslObjectGroup": dsVdslObjectGroup}
)
