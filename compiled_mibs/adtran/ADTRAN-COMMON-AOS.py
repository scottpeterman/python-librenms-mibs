# SNMP MIB module (ADTRAN-COMMON-AOS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adtran\ADTRAN-COMMON-AOS
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:32 2025
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

(adGenAOS,
 adGenAOSCommon) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOS",
    "adGenAOSCommon")

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenAOSCommonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1)
)
if mibBuilder.loadTexts:
    adGenAOSCommonMib.setRevisions(
        ("2015-01-05 00:00",
         "2014-11-05 22:05",
         "2014-09-10 00:00",
         "2013-08-23 00:00",
         "2007-08-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSUnit_ObjectIdentity = ObjectIdentity
adGenAOSUnit = _AdGenAOSUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1)
)
_AdGenAOSSnmp_ObjectIdentity = ObjectIdentity
adGenAOSSnmp = _AdGenAOSSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2)
)
_AdAOSDownload_ObjectIdentity = ObjectIdentity
adAOSDownload = _AdAOSDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3)
)
_AdGenAOSCpuUtil_ObjectIdentity = ObjectIdentity
adGenAOSCpuUtil = _AdGenAOSCpuUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4)
)
_AdGenAOSMux_ObjectIdentity = ObjectIdentity
adGenAOSMux = _AdGenAOSMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5)
)
_AdGenAOSFileSystem_ObjectIdentity = ObjectIdentity
adGenAOSFileSystem = _AdGenAOSFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6)
)
_AdGenAosIfPerfHistory_ObjectIdentity = ObjectIdentity
adGenAosIfPerfHistory = _AdGenAosIfPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7)
)
_AdGenAOSFan_ObjectIdentity = ObjectIdentity
adGenAOSFan = _AdGenAOSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8)
)
_AdGenAOSNetSync_ObjectIdentity = ObjectIdentity
adGenAOSNetSync = _AdGenAOSNetSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9)
)
_AdGenAOSOverTempProtection_ObjectIdentity = ObjectIdentity
adGenAOSOverTempProtection = _AdGenAOSOverTempProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10)
)
_AdGenAOSDyingGasp_ObjectIdentity = ObjectIdentity
adGenAOSDyingGasp = _AdGenAOSDyingGasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-COMMON-AOS",
    **{"adGenAOSCommonMib": adGenAOSCommonMib,
       "adGenAOSUnit": adGenAOSUnit,
       "adGenAOSSnmp": adGenAOSSnmp,
       "adAOSDownload": adAOSDownload,
       "adGenAOSCpuUtil": adGenAOSCpuUtil,
       "adGenAOSMux": adGenAOSMux,
       "adGenAOSFileSystem": adGenAOSFileSystem,
       "adGenAosIfPerfHistory": adGenAosIfPerfHistory,
       "adGenAOSFan": adGenAOSFan,
       "adGenAOSNetSync": adGenAOSNetSync,
       "adGenAOSOverTempProtection": adGenAOSOverTempProtection,
       "adGenAOSDyingGasp": adGenAOSDyingGasp}
)
