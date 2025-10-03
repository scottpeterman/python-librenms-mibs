# SNMP MIB module (FORTINET-FORTIAUTHENTICATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIAUTHENTICATOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:48 2025
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

(FnIndex,
 fnGenTrapMsg,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnIndex",
    "fnGenTrapMsg",
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

fnFortiAuthenticatorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113)
)
if mibBuilder.loadTexts:
    fnFortiAuthenticatorMib.setRevisions(
        ("2020-04-16 00:00",
         "2019-01-17 00:00",
         "2015-06-08 00:00",
         "2012-11-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FacHaState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknownOrDetermining", 1),
          ("clusterPrimary", 2),
          ("clusterSecondary", 3),
          ("standalonePrimary", 4),
          ("loadBalancer", 5),
          ("disabled", 255))
    )



# MIB Managed Objects in the order of their OIDs

_FacTraps_ObjectIdentity = ObjectIdentity
facTraps = _FacTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0)
)
_FacSystem_ObjectIdentity = ObjectIdentity
facSystem = _FacSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1)
)
_FacSysModel_Type = DisplayString
_FacSysModel_Object = MibScalar
facSysModel = _FacSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 1),
    _FacSysModel_Type()
)
facSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facSysModel.setStatus("current")
_FacSysSerial_Type = DisplayString
_FacSysSerial_Object = MibScalar
facSysSerial = _FacSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 2),
    _FacSysSerial_Type()
)
facSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facSysSerial.setStatus("current")
_FacSysVersion_Type = DisplayString
_FacSysVersion_Object = MibScalar
facSysVersion = _FacSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 3),
    _FacSysVersion_Type()
)
facSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facSysVersion.setStatus("current")
_FacSysCpuUsage_Type = Gauge32
_FacSysCpuUsage_Object = MibScalar
facSysCpuUsage = _FacSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 4),
    _FacSysCpuUsage_Type()
)
facSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facSysCpuUsage.setStatus("current")
_FacSysMemUsage_Type = Gauge32
_FacSysMemUsage_Object = MibScalar
facSysMemUsage = _FacSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 5),
    _FacSysMemUsage_Type()
)
facSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facSysMemUsage.setStatus("current")
_FacSysLogDiskUsage_Type = Gauge32
_FacSysLogDiskUsage_Object = MibScalar
facSysLogDiskUsage = _FacSysLogDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 6),
    _FacSysLogDiskUsage_Type()
)
facSysLogDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facSysLogDiskUsage.setStatus("current")
_FacHa_ObjectIdentity = ObjectIdentity
facHa = _FacHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 201)
)
_FacHaCurrentStatus_Type = FacHaState
_FacHaCurrentStatus_Object = MibScalar
facHaCurrentStatus = _FacHaCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 201, 1),
    _FacHaCurrentStatus_Type()
)
facHaCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facHaCurrentStatus.setStatus("current")
_FacAuth_ObjectIdentity = ObjectIdentity
facAuth = _FacAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202)
)
_FacAuthUserCount_Type = FnIndex
_FacAuthUserCount_Object = MibScalar
facAuthUserCount = _FacAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 1),
    _FacAuthUserCount_Type()
)
facAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthUserCount.setStatus("current")
_FacAuthGroupCount_Type = FnIndex
_FacAuthGroupCount_Object = MibScalar
facAuthGroupCount = _FacAuthGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 2),
    _FacAuthGroupCount_Type()
)
facAuthGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthGroupCount.setStatus("current")
_FacFortiTokenCount_Type = FnIndex
_FacFortiTokenCount_Object = MibScalar
facFortiTokenCount = _FacFortiTokenCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 3),
    _FacFortiTokenCount_Type()
)
facFortiTokenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facFortiTokenCount.setStatus("current")
_FacAuthUsersRemaining_Type = FnIndex
_FacAuthUsersRemaining_Object = MibScalar
facAuthUsersRemaining = _FacAuthUsersRemaining_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 4),
    _FacAuthUsersRemaining_Type()
)
facAuthUsersRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthUsersRemaining.setStatus("current")
_FacAuthGroupRemaining_Type = FnIndex
_FacAuthGroupRemaining_Object = MibScalar
facAuthGroupRemaining = _FacAuthGroupRemaining_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 5),
    _FacAuthGroupRemaining_Type()
)
facAuthGroupRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthGroupRemaining.setStatus("current")
_FacFortiTokenRemaining_Type = FnIndex
_FacFortiTokenRemaining_Object = MibScalar
facFortiTokenRemaining = _FacFortiTokenRemaining_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 6),
    _FacFortiTokenRemaining_Type()
)
facFortiTokenRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facFortiTokenRemaining.setStatus("current")
_FacRadiusNasCount_Type = FnIndex
_FacRadiusNasCount_Object = MibScalar
facRadiusNasCount = _FacRadiusNasCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 7),
    _FacRadiusNasCount_Type()
)
facRadiusNasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusNasCount.setStatus("current")
_FacRadiusNasRemaining_Type = FnIndex
_FacRadiusNasRemaining_Object = MibScalar
facRadiusNasRemaining = _FacRadiusNasRemaining_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 8),
    _FacRadiusNasRemaining_Type()
)
facRadiusNasRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusNasRemaining.setStatus("current")
_FacUserCertificateCount_Type = FnIndex
_FacUserCertificateCount_Object = MibScalar
facUserCertificateCount = _FacUserCertificateCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 9),
    _FacUserCertificateCount_Type()
)
facUserCertificateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facUserCertificateCount.setStatus("current")
_FacRadiusLoginsTotal_Type = FnIndex
_FacRadiusLoginsTotal_Object = MibScalar
facRadiusLoginsTotal = _FacRadiusLoginsTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 10),
    _FacRadiusLoginsTotal_Type()
)
facRadiusLoginsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusLoginsTotal.setStatus("current")
_FacRadiusLogins5Mins_Type = FnIndex
_FacRadiusLogins5Mins_Object = MibScalar
facRadiusLogins5Mins = _FacRadiusLogins5Mins_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 11),
    _FacRadiusLogins5Mins_Type()
)
facRadiusLogins5Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusLogins5Mins.setStatus("current")
_FacRadiusFailuresTotal_Type = FnIndex
_FacRadiusFailuresTotal_Object = MibScalar
facRadiusFailuresTotal = _FacRadiusFailuresTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 12),
    _FacRadiusFailuresTotal_Type()
)
facRadiusFailuresTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusFailuresTotal.setStatus("current")
_FacRadiusFailures5Mins_Type = FnIndex
_FacRadiusFailures5Mins_Object = MibScalar
facRadiusFailures5Mins = _FacRadiusFailures5Mins_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 13),
    _FacRadiusFailures5Mins_Type()
)
facRadiusFailures5Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusFailures5Mins.setStatus("current")
_FacRadiusAccountingTotal_Type = FnIndex
_FacRadiusAccountingTotal_Object = MibScalar
facRadiusAccountingTotal = _FacRadiusAccountingTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 14),
    _FacRadiusAccountingTotal_Type()
)
facRadiusAccountingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusAccountingTotal.setStatus("current")
_FacRadiusAccounting5Mins_Type = FnIndex
_FacRadiusAccounting5Mins_Object = MibScalar
facRadiusAccounting5Mins = _FacRadiusAccounting5Mins_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 15),
    _FacRadiusAccounting5Mins_Type()
)
facRadiusAccounting5Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusAccounting5Mins.setStatus("current")
_FacLdapLoginsTotal_Type = FnIndex
_FacLdapLoginsTotal_Object = MibScalar
facLdapLoginsTotal = _FacLdapLoginsTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 16),
    _FacLdapLoginsTotal_Type()
)
facLdapLoginsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facLdapLoginsTotal.setStatus("current")
_FacLdapLogins5Mins_Type = FnIndex
_FacLdapLogins5Mins_Object = MibScalar
facLdapLogins5Mins = _FacLdapLogins5Mins_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 17),
    _FacLdapLogins5Mins_Type()
)
facLdapLogins5Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facLdapLogins5Mins.setStatus("current")
_FacLdapFailuresTotal_Type = FnIndex
_FacLdapFailuresTotal_Object = MibScalar
facLdapFailuresTotal = _FacLdapFailuresTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 18),
    _FacLdapFailuresTotal_Type()
)
facLdapFailuresTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facLdapFailuresTotal.setStatus("current")
_FacLdapFailures5Mins_Type = FnIndex
_FacLdapFailures5Mins_Object = MibScalar
facLdapFailures5Mins = _FacLdapFailures5Mins_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 19),
    _FacLdapFailures5Mins_Type()
)
facLdapFailures5Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facLdapFailures5Mins.setStatus("current")
_FacAuthEventsTotal_Type = FnIndex
_FacAuthEventsTotal_Object = MibScalar
facAuthEventsTotal = _FacAuthEventsTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 20),
    _FacAuthEventsTotal_Type()
)
facAuthEventsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthEventsTotal.setStatus("current")
_FacAuthEvents5Mins_Type = FnIndex
_FacAuthEvents5Mins_Object = MibScalar
facAuthEvents5Mins = _FacAuthEvents5Mins_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 21),
    _FacAuthEvents5Mins_Type()
)
facAuthEvents5Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthEvents5Mins.setStatus("current")
_FacAuthFailuresTotal_Type = FnIndex
_FacAuthFailuresTotal_Object = MibScalar
facAuthFailuresTotal = _FacAuthFailuresTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 22),
    _FacAuthFailuresTotal_Type()
)
facAuthFailuresTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthFailuresTotal.setStatus("current")
_FacAuthFailures5Mins_Type = FnIndex
_FacAuthFailures5Mins_Object = MibScalar
facAuthFailures5Mins = _FacAuthFailures5Mins_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 23),
    _FacAuthFailures5Mins_Type()
)
facAuthFailures5Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facAuthFailures5Mins.setStatus("current")
_FacRadiusProxyInTotal_Type = FnIndex
_FacRadiusProxyInTotal_Object = MibScalar
facRadiusProxyInTotal = _FacRadiusProxyInTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 24),
    _FacRadiusProxyInTotal_Type()
)
facRadiusProxyInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusProxyInTotal.setStatus("current")
_FacRadiusProxyOutTotal_Type = FnIndex
_FacRadiusProxyOutTotal_Object = MibScalar
facRadiusProxyOutTotal = _FacRadiusProxyOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 25),
    _FacRadiusProxyOutTotal_Type()
)
facRadiusProxyOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRadiusProxyOutTotal.setStatus("current")
_FacFssoUserCount_Type = FnIndex
_FacFssoUserCount_Object = MibScalar
facFssoUserCount = _FacFssoUserCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 26),
    _FacFssoUserCount_Type()
)
facFssoUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facFssoUserCount.setStatus("current")
_FacFssoUserRemaining_Type = FnIndex
_FacFssoUserRemaining_Object = MibScalar
facFssoUserRemaining = _FacFssoUserRemaining_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 27),
    _FacFssoUserRemaining_Type()
)
facFssoUserRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facFssoUserRemaining.setStatus("current")


class _FacRaidStatus_Type(Integer32):
    """Custom type facRaidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ok", 1),
          ("degraded", 2),
          ("failed", 3),
          ("initializing", 4),
          ("verifying", 5),
          ("rebuilding", 6))
    )


_FacRaidStatus_Type.__name__ = "Integer32"
_FacRaidStatus_Object = MibScalar
facRaidStatus = _FacRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 113, 1, 202, 28),
    _FacRaidStatus_Type()
)
facRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facRaidStatus.setStatus("current")
_FacModel_ObjectIdentity = ObjectIdentity
facModel = _FacModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100)
)
_Facvm_ObjectIdentity = ObjectIdentity
facvm = _Facvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 101)
)
_Facvmhv_ObjectIdentity = ObjectIdentity
facvmhv = _Facvmhv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 102)
)
_Facvmxen_ObjectIdentity = ObjectIdentity
facvmxen = _Facvmxen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 103)
)
_Facvmkvm_ObjectIdentity = ObjectIdentity
facvmkvm = _Facvmkvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 104)
)
_Facdocker_ObjectIdentity = ObjectIdentity
facdocker = _Facdocker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 105)
)
_Fac2hd_ObjectIdentity = ObjectIdentity
fac2hd = _Fac2hd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 204)
)
_Fac2he_ObjectIdentity = ObjectIdentity
fac2he = _Fac2he_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 205)
)
_Fac4hc_ObjectIdentity = ObjectIdentity
fac4hc = _Fac4hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 303)
)
_Fac4he_ObjectIdentity = ObjectIdentity
fac4he = _Fac4he_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 305)
)
_Fac1kc_ObjectIdentity = ObjectIdentity
fac1kc = _Fac1kc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 403)
)
_Fac1kd_ObjectIdentity = ObjectIdentity
fac1kd = _Fac1kd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 404)
)
_Fac2ke_ObjectIdentity = ObjectIdentity
fac2ke = _Fac2ke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 505)
)
_Fac3kd_ObjectIdentity = ObjectIdentity
fac3kd = _Fac3kd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 604)
)
_Fac3ke_ObjectIdentity = ObjectIdentity
fac3ke = _Fac3ke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 605)
)
_Fac3hf_ObjectIdentity = ObjectIdentity
fac3hf = _Fac3hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 706)
)
_Fac8hf_ObjectIdentity = ObjectIdentity
fac8hf = _Fac8hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 100, 806)
)
_FacMIBConformance_ObjectIdentity = ObjectIdentity
facMIBConformance = _FacMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 113, 600)
)

# Managed Objects groups

facSystemConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 113, 600, 1)
)
facSystemConformanceGroup.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysModel"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysVersion"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysCpuUsage"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysMemUsage"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysLogDiskUsage"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthUserCount"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthGroupCount"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facFortiTokenCount"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthUsersRemaining"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthGroupRemaining"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facFortiTokenRemaining"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusNasCount"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusNasRemaining"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facUserCertificateCount"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusLoginsTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusLogins5Mins"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusFailuresTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusFailures5Mins"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusAccountingTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusAccounting5Mins"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facLdapLoginsTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facLdapLogins5Mins"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facLdapFailuresTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facLdapFailures5Mins"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthEventsTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthEvents5Mins"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthFailuresTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthFailures5Mins"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facHaCurrentStatus"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusProxyInTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusProxyOutTotal"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facFssoUserCount"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facFssoUserRemaining"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRaidStatus"))
)
if mibBuilder.loadTexts:
    facSystemConformanceGroup.setStatus("current")


# Notification objects

facTrapAuthUsersThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 100)
)
facTrapAuthUsersThreshold.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthUsersRemaining"))
)
if mibBuilder.loadTexts:
    facTrapAuthUsersThreshold.setStatus(
        "current"
    )

facTrapAuthGroupThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 101)
)
facTrapAuthGroupThreshold.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthGroupRemaining"))
)
if mibBuilder.loadTexts:
    facTrapAuthGroupThreshold.setStatus(
        "current"
    )

facTrapRadiusNasThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 102)
)
facTrapRadiusNasThreshold.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRadiusNasRemaining"))
)
if mibBuilder.loadTexts:
    facTrapRadiusNasThreshold.setStatus(
        "current"
    )

facTrapAuthEventsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 103)
)
facTrapAuthEventsThreshold.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthEvents5Mins"))
)
if mibBuilder.loadTexts:
    facTrapAuthEventsThreshold.setStatus(
        "current"
    )

facTrapAuthFailureThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 104)
)
facTrapAuthFailureThreshold.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facAuthFailures5Mins"))
)
if mibBuilder.loadTexts:
    facTrapAuthFailureThreshold.setStatus(
        "current"
    )

facTrapUserLockout = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 105)
)
facTrapUserLockout.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    facTrapUserLockout.setStatus(
        "current"
    )

facTrapHAStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 106)
)
facTrapHAStatusChange.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facHaCurrentStatus"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    facTrapHAStatusChange.setStatus(
        "current"
    )

facTrapHASyncActivityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 107)
)
facTrapHASyncActivityLow.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    facTrapHASyncActivityLow.setStatus(
        "current"
    )

facTrapRaidStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 113, 0, 108)
)
facTrapRaidStatusChange.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSysSerial"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facRaidStatus"))
)
if mibBuilder.loadTexts:
    facTrapRaidStatusChange.setStatus(
        "current"
    )


# Notifications groups

facTrapsConformanceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 113, 600, 2)
)
facTrapsConformanceGroup.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapAuthUsersThreshold"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapAuthGroupThreshold"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapRadiusNasThreshold"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapAuthEventsThreshold"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapAuthFailureThreshold"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapUserLockout"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapHAStatusChange"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapHASyncActivityLow"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapRaidStatusChange"))
)
if mibBuilder.loadTexts:
    facTrapsConformanceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

facMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 113, 600, 100)
)
facMIBCompliance.setObjects(
      *(("FORTINET-FORTIAUTHENTICATOR-MIB", "facSystemConformanceGroup"),
        ("FORTINET-FORTIAUTHENTICATOR-MIB", "facTrapsConformanceGroup"))
)
if mibBuilder.loadTexts:
    facMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIAUTHENTICATOR-MIB",
    **{"FacHaState": FacHaState,
       "fnFortiAuthenticatorMib": fnFortiAuthenticatorMib,
       "facTraps": facTraps,
       "facTrapAuthUsersThreshold": facTrapAuthUsersThreshold,
       "facTrapAuthGroupThreshold": facTrapAuthGroupThreshold,
       "facTrapRadiusNasThreshold": facTrapRadiusNasThreshold,
       "facTrapAuthEventsThreshold": facTrapAuthEventsThreshold,
       "facTrapAuthFailureThreshold": facTrapAuthFailureThreshold,
       "facTrapUserLockout": facTrapUserLockout,
       "facTrapHAStatusChange": facTrapHAStatusChange,
       "facTrapHASyncActivityLow": facTrapHASyncActivityLow,
       "facTrapRaidStatusChange": facTrapRaidStatusChange,
       "facSystem": facSystem,
       "facSysModel": facSysModel,
       "facSysSerial": facSysSerial,
       "facSysVersion": facSysVersion,
       "facSysCpuUsage": facSysCpuUsage,
       "facSysMemUsage": facSysMemUsage,
       "facSysLogDiskUsage": facSysLogDiskUsage,
       "facHa": facHa,
       "facHaCurrentStatus": facHaCurrentStatus,
       "facAuth": facAuth,
       "facAuthUserCount": facAuthUserCount,
       "facAuthGroupCount": facAuthGroupCount,
       "facFortiTokenCount": facFortiTokenCount,
       "facAuthUsersRemaining": facAuthUsersRemaining,
       "facAuthGroupRemaining": facAuthGroupRemaining,
       "facFortiTokenRemaining": facFortiTokenRemaining,
       "facRadiusNasCount": facRadiusNasCount,
       "facRadiusNasRemaining": facRadiusNasRemaining,
       "facUserCertificateCount": facUserCertificateCount,
       "facRadiusLoginsTotal": facRadiusLoginsTotal,
       "facRadiusLogins5Mins": facRadiusLogins5Mins,
       "facRadiusFailuresTotal": facRadiusFailuresTotal,
       "facRadiusFailures5Mins": facRadiusFailures5Mins,
       "facRadiusAccountingTotal": facRadiusAccountingTotal,
       "facRadiusAccounting5Mins": facRadiusAccounting5Mins,
       "facLdapLoginsTotal": facLdapLoginsTotal,
       "facLdapLogins5Mins": facLdapLogins5Mins,
       "facLdapFailuresTotal": facLdapFailuresTotal,
       "facLdapFailures5Mins": facLdapFailures5Mins,
       "facAuthEventsTotal": facAuthEventsTotal,
       "facAuthEvents5Mins": facAuthEvents5Mins,
       "facAuthFailuresTotal": facAuthFailuresTotal,
       "facAuthFailures5Mins": facAuthFailures5Mins,
       "facRadiusProxyInTotal": facRadiusProxyInTotal,
       "facRadiusProxyOutTotal": facRadiusProxyOutTotal,
       "facFssoUserCount": facFssoUserCount,
       "facFssoUserRemaining": facFssoUserRemaining,
       "facRaidStatus": facRaidStatus,
       "facModel": facModel,
       "facvm": facvm,
       "facvmhv": facvmhv,
       "facvmxen": facvmxen,
       "facvmkvm": facvmkvm,
       "facdocker": facdocker,
       "fac2hd": fac2hd,
       "fac2he": fac2he,
       "fac4hc": fac4hc,
       "fac4he": fac4he,
       "fac1kc": fac1kc,
       "fac1kd": fac1kd,
       "fac2ke": fac2ke,
       "fac3kd": fac3kd,
       "fac3ke": fac3ke,
       "fac3hf": fac3hf,
       "fac8hf": fac8hf,
       "facMIBConformance": facMIBConformance,
       "facSystemConformanceGroup": facSystemConformanceGroup,
       "facTrapsConformanceGroup": facTrapsConformanceGroup,
       "facMIBCompliance": facMIBCompliance}
)
