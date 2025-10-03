# SNMP MIB module (MITEL-APPLIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mitel\MITEL-APPLIST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:44 2025
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

(mitelIdentification,) = mibBuilder.importSymbols(
    "MITEL-MIB",
    "mitelIdentification")

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

mitelIdApplications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7)
)
if mibBuilder.loadTexts:
    mitelIdApplications.setRevisions(
        ("2014-02-11 12:00",
         "2008-11-25 00:00",
         "2008-10-02 00:00",
         "2008-08-13 00:00",
         "2007-06-07 00:00",
         "2007-04-09 00:00",
         "2007-02-12 00:00",
         "2006-08-10 00:00",
         "2005-02-23 21:34")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MitelIdAppMasTeleworker_ObjectIdentity = ObjectIdentity
mitelIdAppMasTeleworker = _MitelIdAppMasTeleworker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mitelIdAppMasTeleworker.setStatus("current")
_MitelIdAppMasOfficeServerSuite_ObjectIdentity = ObjectIdentity
mitelIdAppMasOfficeServerSuite = _MitelIdAppMasOfficeServerSuite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 2)
)
if mibBuilder.loadTexts:
    mitelIdAppMasOfficeServerSuite.setStatus("current")
_MitelIdAppMasManagedVpn_ObjectIdentity = ObjectIdentity
mitelIdAppMasManagedVpn = _MitelIdAppMasManagedVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 3)
)
if mibBuilder.loadTexts:
    mitelIdAppMasManagedVpn.setStatus("current")
_MitelIdAppMasMobileExtention_ObjectIdentity = ObjectIdentity
mitelIdAppMasMobileExtention = _MitelIdAppMasMobileExtention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 4)
)
if mibBuilder.loadTexts:
    mitelIdAppMasMobileExtention.setStatus("current")
_MitelIdAppCallServer_ObjectIdentity = ObjectIdentity
mitelIdAppCallServer = _MitelIdAppCallServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 5)
)
if mibBuilder.loadTexts:
    mitelIdAppCallServer.setStatus("current")
_MitelIdAppQuickConference_ObjectIdentity = ObjectIdentity
mitelIdAppQuickConference = _MitelIdAppQuickConference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 6)
)
if mibBuilder.loadTexts:
    mitelIdAppQuickConference.setStatus("current")
_MitelIdAppSecureCallRecConn_ObjectIdentity = ObjectIdentity
mitelIdAppSecureCallRecConn = _MitelIdAppSecureCallRecConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 7)
)
if mibBuilder.loadTexts:
    mitelIdAppSecureCallRecConn.setStatus("current")
_MitelIdAppSuiteAppService_ObjectIdentity = ObjectIdentity
mitelIdAppSuiteAppService = _MitelIdAppSuiteAppService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 8)
)
if mibBuilder.loadTexts:
    mitelIdAppSuiteAppService.setStatus("current")
_MitelIdAppAudioWebConferencing_ObjectIdentity = ObjectIdentity
mitelIdAppAudioWebConferencing = _MitelIdAppAudioWebConferencing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 9)
)
if mibBuilder.loadTexts:
    mitelIdAppAudioWebConferencing.setStatus("current")
_MitelIdAppCustomerServiceManager_ObjectIdentity = ObjectIdentity
mitelIdAppCustomerServiceManager = _MitelIdAppCustomerServiceManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 10)
)
if mibBuilder.loadTexts:
    mitelIdAppCustomerServiceManager.setStatus("current")
_MitelIdAppNupointUnifiedMessenger_ObjectIdentity = ObjectIdentity
mitelIdAppNupointUnifiedMessenger = _MitelIdAppNupointUnifiedMessenger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 11)
)
if mibBuilder.loadTexts:
    mitelIdAppNupointUnifiedMessenger.setStatus("current")
_MitelIdAppUnifiedCommunicationsServer_ObjectIdentity = ObjectIdentity
mitelIdAppUnifiedCommunicationsServer = _MitelIdAppUnifiedCommunicationsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 12)
)
if mibBuilder.loadTexts:
    mitelIdAppUnifiedCommunicationsServer.setStatus("current")
_MitelIdAppUnifiedIPClient_ObjectIdentity = ObjectIdentity
mitelIdAppUnifiedIPClient = _MitelIdAppUnifiedIPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 13)
)
if mibBuilder.loadTexts:
    mitelIdAppUnifiedIPClient.setStatus("current")
_MitelIdAppMediaServiceManager_ObjectIdentity = ObjectIdentity
mitelIdAppMediaServiceManager = _MitelIdAppMediaServiceManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 14)
)
if mibBuilder.loadTexts:
    mitelIdAppMediaServiceManager.setStatus("current")
_MitelIdAppMitelCommunicationDirectorManager_ObjectIdentity = ObjectIdentity
mitelIdAppMitelCommunicationDirectorManager = _MitelIdAppMitelCommunicationDirectorManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 7, 15)
)
if mibBuilder.loadTexts:
    mitelIdAppMitelCommunicationDirectorManager.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-APPLIST-MIB",
    **{"mitelIdApplications": mitelIdApplications,
       "mitelIdAppMasTeleworker": mitelIdAppMasTeleworker,
       "mitelIdAppMasOfficeServerSuite": mitelIdAppMasOfficeServerSuite,
       "mitelIdAppMasManagedVpn": mitelIdAppMasManagedVpn,
       "mitelIdAppMasMobileExtention": mitelIdAppMasMobileExtention,
       "mitelIdAppCallServer": mitelIdAppCallServer,
       "mitelIdAppQuickConference": mitelIdAppQuickConference,
       "mitelIdAppSecureCallRecConn": mitelIdAppSecureCallRecConn,
       "mitelIdAppSuiteAppService": mitelIdAppSuiteAppService,
       "mitelIdAppAudioWebConferencing": mitelIdAppAudioWebConferencing,
       "mitelIdAppCustomerServiceManager": mitelIdAppCustomerServiceManager,
       "mitelIdAppNupointUnifiedMessenger": mitelIdAppNupointUnifiedMessenger,
       "mitelIdAppUnifiedCommunicationsServer": mitelIdAppUnifiedCommunicationsServer,
       "mitelIdAppUnifiedIPClient": mitelIdAppUnifiedIPClient,
       "mitelIdAppMediaServiceManager": mitelIdAppMediaServiceManager,
       "mitelIdAppMitelCommunicationDirectorManager": mitelIdAppMitelCommunicationDirectorManager}
)
