# SNMP MIB module (FORTINET-FORTIWEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIWEB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:58 2025
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

(fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "fnSysSerial",
    "fortinet")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

fnFortiWebMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107)
)
if mibBuilder.loadTexts:
    fnFortiWebMib.setRevisions(
        ("2018-07-13 00:00",
         "2018-04-04 00:00",
         "2018-03-21 00:00",
         "2017-11-17 00:00",
         "2017-02-13 00:00",
         "2016-12-13 00:00",
         "2016-10-25 00:00",
         "2016-09-13 00:00",
         "2016-07-01 00:00",
         "2015-12-17 00:00",
         "2015-12-16 00:00",
         "2015-12-03 00:00",
         "2015-10-20 00:00",
         "2015-07-13 00:00",
         "2010-03-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FwOpMode(TextualConvention, Integer32):
    status = "current"
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
        *(("inline", 1),
          ("offline", 2),
          ("transparent", 3),
          ("wccp", 4))
    )



class FwHaMode(TextualConvention, Integer32):
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
        *(("standalone", 1),
          ("master", 2),
          ("slave", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FwModel_ObjectIdentity = ObjectIdentity
fwModel = _FwModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1)
)
_Fwb100D_ObjectIdentity = ObjectIdentity
fwb100D = _Fwb100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 1004)
)
_Fwb400B_ObjectIdentity = ObjectIdentity
fwb400B = _Fwb400B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 4002)
)
_Fwb400C_ObjectIdentity = ObjectIdentity
fwb400C = _Fwb400C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 4003)
)
_Fwb400D_ObjectIdentity = ObjectIdentity
fwb400D = _Fwb400D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 4004)
)
_Fwb600D_ObjectIdentity = ObjectIdentity
fwb600D = _Fwb600D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 6004)
)
_Fwb1000B_ObjectIdentity = ObjectIdentity
fwb1000B = _Fwb1000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 10002)
)
_Fwb1000C_ObjectIdentity = ObjectIdentity
fwb1000C = _Fwb1000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 10003)
)
_Fwb1000D_ObjectIdentity = ObjectIdentity
fwb1000D = _Fwb1000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 10004)
)
_Fwb2000E_ObjectIdentity = ObjectIdentity
fwb2000E = _Fwb2000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 10005)
)
_Fwb1000E_ObjectIdentity = ObjectIdentity
fwb1000E = _Fwb1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 10006)
)
_Fwb3000C_ObjectIdentity = ObjectIdentity
fwb3000C = _Fwb3000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 30003)
)
_Fwb3000CFSX_ObjectIdentity = ObjectIdentity
fwb3000CFSX = _Fwb3000CFSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 30004)
)
_Fwb3000D_ObjectIdentity = ObjectIdentity
fwb3000D = _Fwb3000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 30005)
)
_Fwb3000DFSX_ObjectIdentity = ObjectIdentity
fwb3000DFSX = _Fwb3000DFSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 30006)
)
_Fwb3000E_ObjectIdentity = ObjectIdentity
fwb3000E = _Fwb3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 30007)
)
_Fwb3010E_ObjectIdentity = ObjectIdentity
fwb3010E = _Fwb3010E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 30008)
)
_Fwb4000C_ObjectIdentity = ObjectIdentity
fwb4000C = _Fwb4000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 40003)
)
_Fwb4000D_ObjectIdentity = ObjectIdentity
fwb4000D = _Fwb4000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 40004)
)
_Fwb4000E_ObjectIdentity = ObjectIdentity
fwb4000E = _Fwb4000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 40005)
)
_FwbVM_ObjectIdentity = ObjectIdentity
fwbVM = _FwbVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50001)
)
_FwbXENOPEN_ObjectIdentity = ObjectIdentity
fwbXENOPEN = _FwbXENOPEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50002)
)
_FwbXENSERVER_ObjectIdentity = ObjectIdentity
fwbXENSERVER = _FwbXENSERVER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50003)
)
_FwbXENAWS_ObjectIdentity = ObjectIdentity
fwbXENAWS = _FwbXENAWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50004)
)
_FwbHYPERV_ObjectIdentity = ObjectIdentity
fwbHYPERV = _FwbHYPERV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50005)
)
_FwbKVM_ObjectIdentity = ObjectIdentity
fwbKVM = _FwbKVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50006)
)
_FwbAZURE_ObjectIdentity = ObjectIdentity
fwbAZURE = _FwbAZURE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50007)
)
_FwbVMPAYG_ObjectIdentity = ObjectIdentity
fwbVMPAYG = _FwbVMPAYG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50008)
)
_FwbKVMPAYG_ObjectIdentity = ObjectIdentity
fwbKVMPAYG = _FwbKVMPAYG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50009)
)
_FwbGCP_ObjectIdentity = ObjectIdentity
fwbGCP = _FwbGCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50010)
)
_FwbVBOX_ObjectIdentity = ObjectIdentity
fwbVBOX = _FwbVBOX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50011)
)
_FwbDOCKER_ObjectIdentity = ObjectIdentity
fwbDOCKER = _FwbDOCKER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 1, 50012)
)
_FwSystem_ObjectIdentity = ObjectIdentity
fwSystem = _FwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2)
)
_FwSystemInfo_ObjectIdentity = ObjectIdentity
fwSystemInfo = _FwSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1)
)


class _FwSysModel_Type(DisplayString):
    """Custom type fwSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FwSysModel_Type.__name__ = "DisplayString"
_FwSysModel_Object = MibScalar
fwSysModel = _FwSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 1),
    _FwSysModel_Type()
)
fwSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysModel.setStatus("current")


class _FwSysVersion_Type(DisplayString):
    """Custom type fwSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FwSysVersion_Type.__name__ = "DisplayString"
_FwSysVersion_Object = MibScalar
fwSysVersion = _FwSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 2),
    _FwSysVersion_Type()
)
fwSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysVersion.setStatus("current")
_FwSysHaMode_Type = FwHaMode
_FwSysHaMode_Object = MibScalar
fwSysHaMode = _FwSysHaMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 3),
    _FwSysHaMode_Type()
)
fwSysHaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysHaMode.setStatus("current")
_FwSysOpMode_Type = FwOpMode
_FwSysOpMode_Object = MibScalar
fwSysOpMode = _FwSysOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 4),
    _FwSysOpMode_Type()
)
fwSysOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysOpMode.setStatus("current")


class _FwSysCpuUsage_Type(Gauge32):
    """Custom type fwSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FwSysCpuUsage_Type.__name__ = "Gauge32"
_FwSysCpuUsage_Object = MibScalar
fwSysCpuUsage = _FwSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 5),
    _FwSysCpuUsage_Type()
)
fwSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysCpuUsage.setStatus("current")
_FwSysCpuFreq_Type = Gauge32
_FwSysCpuFreq_Object = MibScalar
fwSysCpuFreq = _FwSysCpuFreq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 6),
    _FwSysCpuFreq_Type()
)
fwSysCpuFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysCpuFreq.setStatus("current")


class _FwSysMemUsage_Type(Gauge32):
    """Custom type fwSysMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FwSysMemUsage_Type.__name__ = "Gauge32"
_FwSysMemUsage_Object = MibScalar
fwSysMemUsage = _FwSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 7),
    _FwSysMemUsage_Type()
)
fwSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysMemUsage.setStatus("current")
_FwSysMemCapacity_Type = Gauge32
_FwSysMemCapacity_Object = MibScalar
fwSysMemCapacity = _FwSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 8),
    _FwSysMemCapacity_Type()
)
fwSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysMemCapacity.setStatus("current")
_FwSysDiskUsage_Type = Gauge32
_FwSysDiskUsage_Object = MibScalar
fwSysDiskUsage = _FwSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 9),
    _FwSysDiskUsage_Type()
)
fwSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysDiskUsage.setStatus("current")
_FwSysDiskCapacity_Type = Gauge32
_FwSysDiskCapacity_Object = MibScalar
fwSysDiskCapacity = _FwSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 1, 10),
    _FwSysDiskCapacity_Type()
)
fwSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSysDiskCapacity.setStatus("current")
_FwSystemCPU_ObjectIdentity = ObjectIdentity
fwSystemCPU = _FwSystemCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 2)
)
_CPUNumber_Type = Integer32
_CPUNumber_Object = MibScalar
cPUNumber = _CPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 2, 1),
    _CPUNumber_Type()
)
cPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPUNumber.setStatus("current")
_CPUTable_Object = MibTable
cPUTable = _CPUTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cPUTable.setStatus("current")
_CPUEntry_Object = MibTableRow
cPUEntry = _CPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 2, 2, 1)
)
cPUEntry.setIndexNames(
    (0, "FORTINET-FORTIWEB-MIB", "cPUIndex"),
)
if mibBuilder.loadTexts:
    cPUEntry.setStatus("current")


class _CPUIndex_Type(Integer32):
    """Custom type cPUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CPUIndex_Type.__name__ = "Integer32"
_CPUIndex_Object = MibTableColumn
cPUIndex = _CPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 2, 2, 1, 1),
    _CPUIndex_Type()
)
cPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPUIndex.setStatus("current")
_CPUusage_Type = Integer32
_CPUusage_Object = MibTableColumn
cPUusage = _CPUusage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 2, 2, 2, 1, 2),
    _CPUusage_Type()
)
cPUusage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPUusage.setStatus("current")
_FwProxy_ObjectIdentity = ObjectIdentity
fwProxy = _FwProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 3)
)
_FwProxyNumber_Type = Counter32
_FwProxyNumber_Object = MibScalar
fwProxyNumber = _FwProxyNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 3, 1),
    _FwProxyNumber_Type()
)
fwProxyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwProxyNumber.setStatus("current")
_FwPServerNumber_Type = Counter32
_FwPServerNumber_Object = MibScalar
fwPServerNumber = _FwPServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 3, 2),
    _FwPServerNumber_Type()
)
fwPServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPServerNumber.setStatus("current")
_FwVServerNumber_Type = Counter32
_FwVServerNumber_Object = MibScalar
fwVServerNumber = _FwVServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 3, 3),
    _FwVServerNumber_Type()
)
fwVServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVServerNumber.setStatus("current")
_FwMonitorNumber_Type = Counter32
_FwMonitorNumber_Object = MibScalar
fwMonitorNumber = _FwMonitorNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 3, 4),
    _FwMonitorNumber_Type()
)
fwMonitorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMonitorNumber.setStatus("current")
_FwServiceNumber_Type = Counter32
_FwServiceNumber_Object = MibScalar
fwServiceNumber = _FwServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 3, 5),
    _FwServiceNumber_Type()
)
fwServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwServiceNumber.setStatus("current")
_FwPortSvrNumber_Type = Counter32
_FwPortSvrNumber_Object = MibScalar
fwPortSvrNumber = _FwPortSvrNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 3, 6),
    _FwPortSvrNumber_Type()
)
fwPortSvrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPortSvrNumber.setStatus("current")
_FwWAFProtection_ObjectIdentity = ObjectIdentity
fwWAFProtection = _FwWAFProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 4)
)
_FwWAFInputRuleNumber_Type = Counter32
_FwWAFInputRuleNumber_Object = MibScalar
fwWAFInputRuleNumber = _FwWAFInputRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 4, 1),
    _FwWAFInputRuleNumber_Type()
)
fwWAFInputRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwWAFInputRuleNumber.setStatus("current")
_FwWAFParameterNumber_Type = Counter32
_FwWAFParameterNumber_Object = MibScalar
fwWAFParameterNumber = _FwWAFParameterNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 4, 2),
    _FwWAFParameterNumber_Type()
)
fwWAFParameterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwWAFParameterNumber.setStatus("current")
_FwWAFAccessNumber_Type = Counter32
_FwWAFAccessNumber_Object = MibScalar
fwWAFAccessNumber = _FwWAFAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 4, 3),
    _FwWAFAccessNumber_Type()
)
fwWAFAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwWAFAccessNumber.setStatus("current")
_FwWAFSvrPortNumber_Type = Counter32
_FwWAFSvrPortNumber_Object = MibScalar
fwWAFSvrPortNumber = _FwWAFSvrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 4, 4),
    _FwWAFSvrPortNumber_Type()
)
fwWAFSvrPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwWAFSvrPortNumber.setStatus("current")
_FwWAFStartPageNumber_Type = Counter32
_FwWAFStartPageNumber_Object = MibScalar
fwWAFStartPageNumber = _FwWAFStartPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 4, 5),
    _FwWAFStartPageNumber_Type()
)
fwWAFStartPageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwWAFStartPageNumber.setStatus("current")
_FwWAFProfileNumber_Type = Counter32
_FwWAFProfileNumber_Object = MibScalar
fwWAFProfileNumber = _FwWAFProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 4, 6),
    _FwWAFProfileNumber_Type()
)
fwWAFProfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwWAFProfileNumber.setStatus("current")
_FwTraps_ObjectIdentity = ObjectIdentity
fwTraps = _FwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10)
)
_FwTrapPrefix_ObjectIdentity = ObjectIdentity
fwTrapPrefix = _FwTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0)
)
_FnWafInfo_Object = MibTable
fnWafInfo = _FnWafInfo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1)
)
if mibBuilder.loadTexts:
    fnWafInfo.setStatus("current")
_FnWafInfoDetail_Object = MibTableRow
fnWafInfoDetail = _FnWafInfoDetail_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1)
)
fnWafInfoDetail.setIndexNames(
    (0, "FORTINET-FORTIWEB-MIB", "fnWafIndex"),
)
if mibBuilder.loadTexts:
    fnWafInfoDetail.setStatus("current")


class _FnWafIndex_Type(Integer32):
    """Custom type fnWafIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FnWafIndex_Type.__name__ = "Integer32"
_FnWafIndex_Object = MibTableColumn
fnWafIndex = _FnWafIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 1),
    _FnWafIndex_Type()
)
fnWafIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnWafIndex.setStatus("current")
_FnWafDate_Type = DisplayString
_FnWafDate_Object = MibTableColumn
fnWafDate = _FnWafDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 2),
    _FnWafDate_Type()
)
fnWafDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafDate.setStatus("current")
_FnWafTime_Type = DisplayString
_FnWafTime_Object = MibTableColumn
fnWafTime = _FnWafTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 3),
    _FnWafTime_Type()
)
fnWafTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafTime.setStatus("current")
_FnWafSrcIP_Type = DisplayString
_FnWafSrcIP_Object = MibTableColumn
fnWafSrcIP = _FnWafSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 4),
    _FnWafSrcIP_Type()
)
fnWafSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafSrcIP.setStatus("current")
_FnWafDstIP_Type = DisplayString
_FnWafDstIP_Object = MibTableColumn
fnWafDstIP = _FnWafDstIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 5),
    _FnWafDstIP_Type()
)
fnWafDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafDstIP.setStatus("current")
_FnWafSrcPort_Type = DisplayString
_FnWafSrcPort_Object = MibTableColumn
fnWafSrcPort = _FnWafSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 6),
    _FnWafSrcPort_Type()
)
fnWafSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafSrcPort.setStatus("current")
_FnWafDstPort_Type = DisplayString
_FnWafDstPort_Object = MibTableColumn
fnWafDstPort = _FnWafDstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 7),
    _FnWafDstPort_Type()
)
fnWafDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafDstPort.setStatus("current")
_FnWafHost_Type = DisplayString
_FnWafHost_Object = MibTableColumn
fnWafHost = _FnWafHost_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 8),
    _FnWafHost_Type()
)
fnWafHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafHost.setStatus("current")
_FnWafURL_Type = DisplayString
_FnWafURL_Object = MibTableColumn
fnWafURL = _FnWafURL_Object(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 1, 1, 9),
    _FnWafURL_Type()
)
fnWafURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWafURL.setStatus("current")
_FwMibConformance_ObjectIdentity = ObjectIdentity
fwMibConformance = _FwMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 107, 100)
)

# Managed Objects groups

fwSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 107, 100, 2)
)
fwSystemObjectGroup.setObjects(
      *(("FORTINET-FORTIWEB-MIB", "fwSysModel"),
        ("FORTINET-FORTIWEB-MIB", "fwSysVersion"),
        ("FORTINET-FORTIWEB-MIB", "fwSysHaMode"),
        ("FORTINET-FORTIWEB-MIB", "fwSysOpMode"),
        ("FORTINET-FORTIWEB-MIB", "fwSysCpuUsage"),
        ("FORTINET-FORTIWEB-MIB", "fwSysCpuFreq"),
        ("FORTINET-FORTIWEB-MIB", "fwSysMemUsage"),
        ("FORTINET-FORTIWEB-MIB", "fwSysMemCapacity"),
        ("FORTINET-FORTIWEB-MIB", "fwSysDiskUsage"),
        ("FORTINET-FORTIWEB-MIB", "fwSysDiskCapacity"))
)
if mibBuilder.loadTexts:
    fwSystemObjectGroup.setStatus("current")


# Notification objects

fwTrapHaHBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 1)
)
fwTrapHaHBFail.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapHaHBFail.setStatus(
        "current"
    )

fwTrapModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 2)
)
fwTrapModeChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapModeChange.setStatus(
        "current"
    )

fwTrapPolicyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 3)
)
fwTrapPolicyStart.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapPolicyStart.setStatus(
        "current"
    )

fwTrapPolicyStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 4)
)
fwTrapPolicyStop.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapPolicyStop.setStatus(
        "current"
    )

fwTrapPServerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 5)
)
fwTrapPServerFailed.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapPServerFailed.setStatus(
        "current"
    )

fwTrapXMLIntrusionAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 10)
)
fwTrapXMLIntrusionAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapXMLIntrusionAttack.setStatus(
        "current"
    )

fwTrapXMLSchemaAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 11)
)
fwTrapXMLSchemaAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapXMLSchemaAttack.setStatus(
        "current"
    )

fwTrapXMLFilterAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 12)
)
fwTrapXMLFilterAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapXMLFilterAttack.setStatus(
        "current"
    )

fwTrapXMLSigEncAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 13)
)
fwTrapXMLSigEncAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapXMLSigEncAttack.setStatus(
        "current"
    )

fwTrapXMLWSDLAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 14)
)
fwTrapXMLWSDLAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapXMLWSDLAttack.setStatus(
        "current"
    )

fwTrapXMLSqlAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 15)
)
fwTrapXMLSqlAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapXMLSqlAttack.setStatus(
        "current"
    )

fwTrapWAFAMethodAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 30)
)
fwTrapWAFAMethodAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFAMethodAttack.setStatus(
        "current"
    )

fwTrapWAFXSSAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 31)
)
fwTrapWAFXSSAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFXSSAttack.setStatus(
        "current"
    )

fwTrapWAFSqlAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 32)
)
fwTrapWAFSqlAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFSqlAttack.setStatus(
        "current"
    )

fwTrapWAFExploitAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 33)
)
fwTrapWAFExploitAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFExploitAttack.setStatus(
        "current"
    )

fwTrapWAFDisclosureAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 34)
)
fwTrapWAFDisclosureAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFDisclosureAttack.setStatus(
        "current"
    )

fwTrapWAFAccessAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 35)
)
fwTrapWAFAccessAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFAccessAttack.setStatus(
        "current"
    )

fwTrapWAFSPageAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 36)
)
fwTrapWAFSPageAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapWAFSPageAttack.setStatus(
        "current"
    )

fwTrapWAFPValidAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 37)
)
fwTrapWAFPValidAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fwTrapWAFPValidAttack.setStatus(
        "current"
    )

fwTrapWAFBListAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 38)
)
fwTrapWAFBListAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFBListAttack.setStatus(
        "current"
    )

fwTrapWAFBLoginAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 39)
)
fwTrapWAFBLoginAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFBLoginAttack.setStatus(
        "current"
    )

fwTrapWAFRobotAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 40)
)
fwTrapWAFRobotAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFRobotAttack.setStatus(
        "current"
    )

fwTrapWAFHideFieldAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 41)
)
fwTrapWAFHideFieldAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFHideFieldAttack.setStatus(
        "current"
    )

fwTrapWAFUrlAccessAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 42)
)
fwTrapWAFUrlAccessAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFUrlAccessAttack.setStatus(
        "current"
    )

fwTrapWAFBadRobotAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 43)
)
fwTrapWAFBadRobotAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFBadRobotAttack.setStatus(
        "current"
    )

fwTrapWAFSignatureAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 44)
)
fwTrapWAFSignatureAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFSignatureAttack.setStatus(
        "current"
    )

fwTrapWAFWListAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 107, 10, 0, 45)
)
fwTrapWAFWListAttack.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIWEB-MIB", "fnWafInfoDetail"))
)
if mibBuilder.loadTexts:
    fwTrapWAFWListAttack.setStatus(
        "current"
    )


# Notifications groups

fwTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 107, 100, 1)
)
fwTrapGroup.setObjects(
      *(("FORTINET-FORTIWEB-MIB", "fwTrapHaHBFail"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapModeChange"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapPolicyStart"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapPolicyStop"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapPServerFailed"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapXMLIntrusionAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapXMLSchemaAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapXMLFilterAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapXMLSigEncAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapXMLWSDLAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapXMLSqlAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFAMethodAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFXSSAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFSqlAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFExploitAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFDisclosureAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFAccessAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFSPageAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFPValidAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFBListAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFWListAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFBLoginAttack"),
        ("FORTINET-FORTIWEB-MIB", "fwTrapWAFRobotAttack"))
)
if mibBuilder.loadTexts:
    fwTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fwMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 107, 100, 100)
)
fwMibCompliance.setObjects(
      *(("FORTINET-FORTIWEB-MIB", "fwTrapGroup"),
        ("FORTINET-FORTIWEB-MIB", "fwSystemObjectGroup"))
)
if mibBuilder.loadTexts:
    fwMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIWEB-MIB",
    **{"FwOpMode": FwOpMode,
       "FwHaMode": FwHaMode,
       "fnFortiWebMib": fnFortiWebMib,
       "fwModel": fwModel,
       "fwb100D": fwb100D,
       "fwb400B": fwb400B,
       "fwb400C": fwb400C,
       "fwb400D": fwb400D,
       "fwb600D": fwb600D,
       "fwb1000B": fwb1000B,
       "fwb1000C": fwb1000C,
       "fwb1000D": fwb1000D,
       "fwb2000E": fwb2000E,
       "fwb1000E": fwb1000E,
       "fwb3000C": fwb3000C,
       "fwb3000CFSX": fwb3000CFSX,
       "fwb3000D": fwb3000D,
       "fwb3000DFSX": fwb3000DFSX,
       "fwb3000E": fwb3000E,
       "fwb3010E": fwb3010E,
       "fwb4000C": fwb4000C,
       "fwb4000D": fwb4000D,
       "fwb4000E": fwb4000E,
       "fwbVM": fwbVM,
       "fwbXENOPEN": fwbXENOPEN,
       "fwbXENSERVER": fwbXENSERVER,
       "fwbXENAWS": fwbXENAWS,
       "fwbHYPERV": fwbHYPERV,
       "fwbKVM": fwbKVM,
       "fwbAZURE": fwbAZURE,
       "fwbVMPAYG": fwbVMPAYG,
       "fwbKVMPAYG": fwbKVMPAYG,
       "fwbGCP": fwbGCP,
       "fwbVBOX": fwbVBOX,
       "fwbDOCKER": fwbDOCKER,
       "fwSystem": fwSystem,
       "fwSystemInfo": fwSystemInfo,
       "fwSysModel": fwSysModel,
       "fwSysVersion": fwSysVersion,
       "fwSysHaMode": fwSysHaMode,
       "fwSysOpMode": fwSysOpMode,
       "fwSysCpuUsage": fwSysCpuUsage,
       "fwSysCpuFreq": fwSysCpuFreq,
       "fwSysMemUsage": fwSysMemUsage,
       "fwSysMemCapacity": fwSysMemCapacity,
       "fwSysDiskUsage": fwSysDiskUsage,
       "fwSysDiskCapacity": fwSysDiskCapacity,
       "fwSystemCPU": fwSystemCPU,
       "cPUNumber": cPUNumber,
       "cPUTable": cPUTable,
       "cPUEntry": cPUEntry,
       "cPUIndex": cPUIndex,
       "cPUusage": cPUusage,
       "fwProxy": fwProxy,
       "fwProxyNumber": fwProxyNumber,
       "fwPServerNumber": fwPServerNumber,
       "fwVServerNumber": fwVServerNumber,
       "fwMonitorNumber": fwMonitorNumber,
       "fwServiceNumber": fwServiceNumber,
       "fwPortSvrNumber": fwPortSvrNumber,
       "fwWAFProtection": fwWAFProtection,
       "fwWAFInputRuleNumber": fwWAFInputRuleNumber,
       "fwWAFParameterNumber": fwWAFParameterNumber,
       "fwWAFAccessNumber": fwWAFAccessNumber,
       "fwWAFSvrPortNumber": fwWAFSvrPortNumber,
       "fwWAFStartPageNumber": fwWAFStartPageNumber,
       "fwWAFProfileNumber": fwWAFProfileNumber,
       "fwTraps": fwTraps,
       "fwTrapPrefix": fwTrapPrefix,
       "fwTrapHaHBFail": fwTrapHaHBFail,
       "fwTrapModeChange": fwTrapModeChange,
       "fwTrapPolicyStart": fwTrapPolicyStart,
       "fwTrapPolicyStop": fwTrapPolicyStop,
       "fwTrapPServerFailed": fwTrapPServerFailed,
       "fwTrapXMLIntrusionAttack": fwTrapXMLIntrusionAttack,
       "fwTrapXMLSchemaAttack": fwTrapXMLSchemaAttack,
       "fwTrapXMLFilterAttack": fwTrapXMLFilterAttack,
       "fwTrapXMLSigEncAttack": fwTrapXMLSigEncAttack,
       "fwTrapXMLWSDLAttack": fwTrapXMLWSDLAttack,
       "fwTrapXMLSqlAttack": fwTrapXMLSqlAttack,
       "fwTrapWAFAMethodAttack": fwTrapWAFAMethodAttack,
       "fwTrapWAFXSSAttack": fwTrapWAFXSSAttack,
       "fwTrapWAFSqlAttack": fwTrapWAFSqlAttack,
       "fwTrapWAFExploitAttack": fwTrapWAFExploitAttack,
       "fwTrapWAFDisclosureAttack": fwTrapWAFDisclosureAttack,
       "fwTrapWAFAccessAttack": fwTrapWAFAccessAttack,
       "fwTrapWAFSPageAttack": fwTrapWAFSPageAttack,
       "fwTrapWAFPValidAttack": fwTrapWAFPValidAttack,
       "fwTrapWAFBListAttack": fwTrapWAFBListAttack,
       "fwTrapWAFBLoginAttack": fwTrapWAFBLoginAttack,
       "fwTrapWAFRobotAttack": fwTrapWAFRobotAttack,
       "fwTrapWAFHideFieldAttack": fwTrapWAFHideFieldAttack,
       "fwTrapWAFUrlAccessAttack": fwTrapWAFUrlAccessAttack,
       "fwTrapWAFBadRobotAttack": fwTrapWAFBadRobotAttack,
       "fwTrapWAFSignatureAttack": fwTrapWAFSignatureAttack,
       "fwTrapWAFWListAttack": fwTrapWAFWListAttack,
       "fnWafInfo": fnWafInfo,
       "fnWafInfoDetail": fnWafInfoDetail,
       "fnWafIndex": fnWafIndex,
       "fnWafDate": fnWafDate,
       "fnWafTime": fnWafTime,
       "fnWafSrcIP": fnWafSrcIP,
       "fnWafDstIP": fnWafDstIP,
       "fnWafSrcPort": fnWafSrcPort,
       "fnWafDstPort": fnWafDstPort,
       "fnWafHost": fnWafHost,
       "fnWafURL": fnWafURL,
       "fwMibConformance": fwMibConformance,
       "fwTrapGroup": fwTrapGroup,
       "fwSystemObjectGroup": fwSystemObjectGroup,
       "fwMibCompliance": fwMibCompliance}
)
