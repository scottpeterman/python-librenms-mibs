# SNMP MIB module (TAIT-TNADMIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tait\TAIT-TNADMIN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:40 2025
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

(tnAdminMIB,
 tnAdminMibModule) = mibBuilder.importSymbols(
    "TAIT-TNADMIN-MODULE-MIB",
    "tnAdminMIB",
    "tnAdminMibModule")

(PercentHundredths,
 TaitServiceState) = mibBuilder.importSymbols(
    "TAIT-TNADMIN-TC",
    "PercentHundredths",
    "TaitServiceState")


# MODULE-IDENTITY

tnAdminMibObjNotif = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    tnAdminMibObjNotif.setRevisions(
        ("2020-02-10 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnAdminConfs_ObjectIdentity = ObjectIdentity
tnAdminConfs = _TnAdminConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 1)
)
_TnAdminGroups_ObjectIdentity = ObjectIdentity
tnAdminGroups = _TnAdminGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 1, 1)
)
_TnAdminCompl_ObjectIdentity = ObjectIdentity
tnAdminCompl = _TnAdminCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 1, 2)
)
_TnAdminObjs_ObjectIdentity = ObjectIdentity
tnAdminObjs = _TnAdminObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2)
)
_TnAdminTaitServiceObjs_ObjectIdentity = ObjectIdentity
tnAdminTaitServiceObjs = _TnAdminTaitServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1)
)
_TnAdminTaitServiceTable_Object = MibTable
tnAdminTaitServiceTable = _TnAdminTaitServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnAdminTaitServiceTable.setStatus("current")
_TnAdminTaitServiceEntry_Object = MibTableRow
tnAdminTaitServiceEntry = _TnAdminTaitServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1)
)
tnAdminTaitServiceEntry.setIndexNames(
    (0, "TAIT-TNADMIN-MIB", "tnAdminTaitServicePort"),
)
if mibBuilder.loadTexts:
    tnAdminTaitServiceEntry.setStatus("current")


class _TnAdminTaitServicePort_Type(Integer32):
    """Custom type tnAdminTaitServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnAdminTaitServicePort_Type.__name__ = "Integer32"
_TnAdminTaitServicePort_Object = MibTableColumn
tnAdminTaitServicePort = _TnAdminTaitServicePort_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 1),
    _TnAdminTaitServicePort_Type()
)
tnAdminTaitServicePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAdminTaitServicePort.setStatus("current")
_TnAdminTaitServiceName_Type = DisplayString
_TnAdminTaitServiceName_Object = MibTableColumn
tnAdminTaitServiceName = _TnAdminTaitServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 2),
    _TnAdminTaitServiceName_Type()
)
tnAdminTaitServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceName.setStatus("current")
_TnAdminTaitServiceVersion_Type = DisplayString
_TnAdminTaitServiceVersion_Object = MibTableColumn
tnAdminTaitServiceVersion = _TnAdminTaitServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 3),
    _TnAdminTaitServiceVersion_Type()
)
tnAdminTaitServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceVersion.setStatus("current")


class _TnAdminTaitServiceSize_Type(Integer32):
    """Custom type tnAdminTaitServiceSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnAdminTaitServiceSize_Type.__name__ = "Integer32"
_TnAdminTaitServiceSize_Object = MibTableColumn
tnAdminTaitServiceSize = _TnAdminTaitServiceSize_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 4),
    _TnAdminTaitServiceSize_Type()
)
tnAdminTaitServiceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceSize.setStatus("current")
_TnAdminTaitServiceRam_Type = PercentHundredths
_TnAdminTaitServiceRam_Object = MibTableColumn
tnAdminTaitServiceRam = _TnAdminTaitServiceRam_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 5),
    _TnAdminTaitServiceRam_Type()
)
tnAdminTaitServiceRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceRam.setStatus("current")
_TnAdminTaitServiceCpu_Type = PercentHundredths
_TnAdminTaitServiceCpu_Object = MibTableColumn
tnAdminTaitServiceCpu = _TnAdminTaitServiceCpu_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 6),
    _TnAdminTaitServiceCpu_Type()
)
tnAdminTaitServiceCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceCpu.setStatus("current")


class _TnAdminTaitServiceUptime_Type(Integer32):
    """Custom type tnAdminTaitServiceUptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnAdminTaitServiceUptime_Type.__name__ = "Integer32"
_TnAdminTaitServiceUptime_Object = MibTableColumn
tnAdminTaitServiceUptime = _TnAdminTaitServiceUptime_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 7),
    _TnAdminTaitServiceUptime_Type()
)
tnAdminTaitServiceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceUptime.setStatus("current")
_TnAdminTaitServiceState_Type = TaitServiceState
_TnAdminTaitServiceState_Object = MibTableColumn
tnAdminTaitServiceState = _TnAdminTaitServiceState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 8),
    _TnAdminTaitServiceState_Type()
)
tnAdminTaitServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceState.setStatus("current")


class _TnAdminTaitServiceProcessId_Type(Integer32):
    """Custom type tnAdminTaitServiceProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194304),
    )


_TnAdminTaitServiceProcessId_Type.__name__ = "Integer32"
_TnAdminTaitServiceProcessId_Object = MibTableColumn
tnAdminTaitServiceProcessId = _TnAdminTaitServiceProcessId_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 2, 1, 1, 1, 9),
    _TnAdminTaitServiceProcessId_Type()
)
tnAdminTaitServiceProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAdminTaitServiceProcessId.setStatus("current")
_TnAdminEvents_ObjectIdentity = ObjectIdentity
tnAdminEvents = _TnAdminEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 3)
)

# Managed Objects groups

tnAdminTaitServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 1, 1, 2)
)
tnAdminTaitServiceGroup.setObjects(
      *(("TAIT-TNADMIN-MIB", "tnAdminTaitServiceName"),
        ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceVersion"),
        ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceSize"),
        ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceRam"),
        ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceCpu"),
        ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceUptime"),
        ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceState"),
        ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceProcessId"))
)
if mibBuilder.loadTexts:
    tnAdminTaitServiceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tn9300ComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3570, 3, 15, 1, 2, 1)
)
tn9300ComplianceV1.setObjects(
    ("TAIT-TNADMIN-MIB", "tnAdminTaitServiceGroup")
)
if mibBuilder.loadTexts:
    tn9300ComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAIT-TNADMIN-MIB",
    **{"tnAdminMibObjNotif": tnAdminMibObjNotif,
       "tnAdminConfs": tnAdminConfs,
       "tnAdminGroups": tnAdminGroups,
       "tnAdminTaitServiceGroup": tnAdminTaitServiceGroup,
       "tnAdminCompl": tnAdminCompl,
       "tn9300ComplianceV1": tn9300ComplianceV1,
       "tnAdminObjs": tnAdminObjs,
       "tnAdminTaitServiceObjs": tnAdminTaitServiceObjs,
       "tnAdminTaitServiceTable": tnAdminTaitServiceTable,
       "tnAdminTaitServiceEntry": tnAdminTaitServiceEntry,
       "tnAdminTaitServicePort": tnAdminTaitServicePort,
       "tnAdminTaitServiceName": tnAdminTaitServiceName,
       "tnAdminTaitServiceVersion": tnAdminTaitServiceVersion,
       "tnAdminTaitServiceSize": tnAdminTaitServiceSize,
       "tnAdminTaitServiceRam": tnAdminTaitServiceRam,
       "tnAdminTaitServiceCpu": tnAdminTaitServiceCpu,
       "tnAdminTaitServiceUptime": tnAdminTaitServiceUptime,
       "tnAdminTaitServiceState": tnAdminTaitServiceState,
       "tnAdminTaitServiceProcessId": tnAdminTaitServiceProcessId,
       "tnAdminEvents": tnAdminEvents}
)
