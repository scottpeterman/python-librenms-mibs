# SNMP MIB module (FOUNDRY-SN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\brocade\FOUNDRY-SN-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:27 2025
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

(snAgGblTrapMessage,
 snAgentBrdIndex,
 snChasFanDescription,
 snChasFanIndex,
 snChasPwrSupplyDescription,
 snChasPwrSupplyIndex) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "snAgGblTrapMessage",
    "snAgentBrdIndex",
    "snChasFanDescription",
    "snChasFanIndex",
    "snChasPwrSupplyDescription",
    "snChasPwrSupplyIndex")

(foundry,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "foundry")

(snL4LinkVirtualInterface,
 snL4MaxSessionLimit,
 snL4TcpSynLimit,
 snL4TrapLinkName,
 snL4TrapRealServerCurConnections,
 snL4TrapRealServerIP,
 snL4TrapRealServerName,
 snL4TrapRealServerPort) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB",
    "snL4LinkVirtualInterface",
    "snL4MaxSessionLimit",
    "snL4TcpSynLimit",
    "snL4TrapLinkName",
    "snL4TrapRealServerCurConnections",
    "snL4TrapRealServerIP",
    "snL4TrapRealServerName",
    "snL4TrapRealServerPort")

(wgPnPIfIndex,
 wgPnPMacAddress,
 wgPnPStatus) = mibBuilder.importSymbols(
    "FOUNDRY-SN-WIRELESS-GROUP-MIB",
    "wgPnPIfIndex",
    "wgPnPMacAddress",
    "wgPnPStatus")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

snTrapL4MaxSessionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 19)
)
snTrapL4MaxSessionLimitReached.setObjects(
    ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4MaxSessionLimit")
)
if mibBuilder.loadTexts:
    snTrapL4MaxSessionLimitReached.setStatus(
        ""
    )

snTrapL4TcpSynLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 20)
)
snTrapL4TcpSynLimitReached.setObjects(
    ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit")
)
if mibBuilder.loadTexts:
    snTrapL4TcpSynLimitReached.setStatus(
        ""
    )

snTrapL4RealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 21)
)
snTrapL4RealServerUp.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerUp.setStatus(
        ""
    )

snTrapL4RealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 22)
)
snTrapL4RealServerDown.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerDown.setStatus(
        ""
    )

snTrapL4RealServerPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 23)
)
snTrapL4RealServerPortUp.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortUp.setStatus(
        ""
    )

snTrapL4RealServerPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 24)
)
snTrapL4RealServerPortDown.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortDown.setStatus(
        ""
    )

snTrapL4RealServerMaxConnectionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 25)
)
snTrapL4RealServerMaxConnectionLimitReached.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerCurConnections"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerMaxConnectionLimitReached.setStatus(
        ""
    )

snTrapL4BecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 26)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeStandby.setStatus(
        ""
    )

snTrapL4BecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 27)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeActive.setStatus(
        ""
    )

snTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 28)
)
snTrapModuleInserted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleInserted.setStatus(
        ""
    )

snTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 29)
)
snTrapModuleRemoved.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleRemoved.setStatus(
        ""
    )

snTrapChasPwrSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 30)
)
snTrapChasPwrSupplyFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyFailed.setStatus(
        ""
    )

snTrapChasFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 31)
)
snTrapChasFanFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasFanFailed.setStatus(
        ""
    )

snTrapLockedAddressViolation2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 32)
)
snTrapLockedAddressViolation2.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLockedAddressViolation2.setStatus(
        ""
    )

snTrapFsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 33)
)
snTrapFsrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFsrpIfStateChange.setStatus(
        ""
    )

snTrapVrrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 34)
)
snTrapVrrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpIfStateChange.setStatus(
        ""
    )

snTrapMgmtModuleRedunStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 35)
)
snTrapMgmtModuleRedunStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMgmtModuleRedunStateChange.setStatus(
        ""
    )

snTrapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 36)
)
snTrapTemperatureWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTemperatureWarning.setStatus(
        ""
    )

snTrapAccessListDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 37)
)
snTrapAccessListDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAccessListDeny.setStatus(
        ""
    )

snTrapMacFilterDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 38)
)
snTrapMacFilterDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterDeny.setStatus(
        ""
    )

snTrapL4GslbRemoteUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 39)
)
snTrapL4GslbRemoteUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteUp.setStatus(
        ""
    )

snTrapL4GslbRemoteDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 40)
)
snTrapL4GslbRemoteDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteDown.setStatus(
        ""
    )

snTrapL4GslbRemoteControllerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 41)
)
snTrapL4GslbRemoteControllerUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerUp.setStatus(
        ""
    )

snTrapL4GslbRemoteControllerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 42)
)
snTrapL4GslbRemoteControllerDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerDown.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 43)
)
snTrapL4GslbHealthCheckIpUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpUp.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 44)
)
snTrapL4GslbHealthCheckIpDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpDown.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 45)
)
snTrapL4GslbHealthCheckIpPortUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortUp.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 46)
)
snTrapL4GslbHealthCheckIpPortDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortDown.setStatus(
        ""
    )

snTrapL4FirewallBecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 47)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeStandby.setStatus(
        ""
    )

snTrapL4FirewallBecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 48)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeActive.setStatus(
        ""
    )

snTrapL4FirewallPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 49)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathUp.setStatus(
        ""
    )

snTrapL4FirewallPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 50)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathDown.setStatus(
        ""
    )

snTrapIcmpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 51)
)
snTrapIcmpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpLocalExceedBurst.setStatus(
        ""
    )

snTrapIcmpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 52)
)
snTrapIcmpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpTransitExceedBurst.setStatus(
        ""
    )

snTrapTcpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 53)
)
snTrapTcpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpLocalExceedBurst.setStatus(
        ""
    )

snTrapTcpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 54)
)
snTrapTcpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpTransitExceedBurst.setStatus(
        ""
    )

snTrapL4ContentVerification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 55)
)
if mibBuilder.loadTexts:
    snTrapL4ContentVerification.setStatus(
        ""
    )

snTrapDuplicateIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 56)
)
if mibBuilder.loadTexts:
    snTrapDuplicateIp.setStatus(
        ""
    )

snTrapMplsProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 57)
)
if mibBuilder.loadTexts:
    snTrapMplsProblem.setStatus(
        ""
    )

snTrapMplsException = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 58)
)
if mibBuilder.loadTexts:
    snTrapMplsException.setStatus(
        ""
    )

snTrapMplsAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 59)
)
if mibBuilder.loadTexts:
    snTrapMplsAudit.setStatus(
        ""
    )

snTrapMplsDeveloper = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 60)
)
if mibBuilder.loadTexts:
    snTrapMplsDeveloper.setStatus(
        ""
    )

snTrapNoBmFreeQueue = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 61)
)
snTrapNoBmFreeQueue.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapNoBmFreeQueue.setStatus(
        ""
    )

snTrapSmcDmaDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 62)
)
snTrapSmcDmaDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcDmaDrop.setStatus(
        ""
    )

snTrapSmcBpDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 63)
)
snTrapSmcBpDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcBpDrop.setStatus(
        ""
    )

snTrapBmWriteSeqDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 64)
)
snTrapBmWriteSeqDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBmWriteSeqDrop.setStatus(
        ""
    )

snTrapBgpPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 65)
)
snTrapBgpPeerUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerUp.setStatus(
        ""
    )

snTrapBgpPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 66)
)
snTrapBgpPeerDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerDown.setStatus(
        ""
    )

snTrapL4RealServerResponseTimeLowerLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 67)
)
snTrapL4RealServerResponseTimeLowerLimit.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeLowerLimit.setStatus(
        ""
    )

snTrapL4RealServerResponseTimeUpperLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 68)
)
snTrapL4RealServerResponseTimeUpperLimit.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeUpperLimit.setStatus(
        ""
    )

snTrapL4TcpAttackRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 69)
)
snTrapL4TcpAttackRateExceedMax.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedMax.setStatus(
        ""
    )

snTrapL4TcpAttackRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 70)
)
snTrapL4TcpAttackRateExceedThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedThreshold.setStatus(
        ""
    )

snTrapL4ConnectionRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 71)
)
snTrapL4ConnectionRateExceedMax.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedMax.setStatus(
        ""
    )

snTrapL4ConnectionRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 72)
)
snTrapL4ConnectionRateExceedThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedThreshold.setStatus(
        ""
    )

snTrapRunningConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 73)
)
snTrapRunningConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapRunningConfigChanged.setStatus(
        ""
    )

snTrapStartupConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 74)
)
snTrapStartupConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStartupConfigChanged.setStatus(
        ""
    )

snTrapUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 75)
)
snTrapUserLogin.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogin.setStatus(
        ""
    )

snTrapUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 76)
)
snTrapUserLogout.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogout.setStatus(
        ""
    )

snTrapPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 77)
)
snTrapPortSecurityViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityViolation.setStatus(
        ""
    )

snTrapPortSecurityShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 78)
)
snTrapPortSecurityShutdown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityShutdown.setStatus(
        ""
    )

snTrapMrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 79)
)
snTrapMrpStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpStateChange.setStatus(
        ""
    )

snTrapMrpCamError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 80)
)
snTrapMrpCamError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpCamError.setStatus(
        ""
    )

snTrapChasPwrSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 81)
)
snTrapChasPwrSupplyOK.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyOK.setStatus(
        ""
    )

snTrapVrrpeIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 82)
)
snTrapVrrpeIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpeIfStateChange.setStatus(
        ""
    )

snTrapVsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 83)
)
snTrapVsrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVsrpIfStateChange.setStatus(
        ""
    )

snTrapSrcIpAddressViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 84)
)
snTrapSrcIpAddressViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSrcIpAddressViolation.setStatus(
        ""
    )

snTrapMacAuthEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 85)
)
snTrapMacAuthEnable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthEnable.setStatus(
        ""
    )

snTrapMacAuthDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 86)
)
snTrapMacAuthDisable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthDisable.setStatus(
        ""
    )

snTrapMacAuthMACAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 87)
)
snTrapMacAuthMACAccepted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthMACAccepted.setStatus(
        ""
    )

snTrapMacAuthMACRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 88)
)
snTrapMacAuthMACRejected.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthMACRejected.setStatus(
        ""
    )

snTrapMacAuthPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 89)
)
snTrapMacAuthPortDisabled.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthPortDisabled.setStatus(
        ""
    )

snTrapClientLoginReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 110)
)
snTrapClientLoginReject.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapClientLoginReject.setStatus(
        ""
    )

snTrapLocalUserConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 111)
)
snTrapLocalUserConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLocalUserConfigChange.setStatus(
        ""
    )

snTrapVlanConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 112)
)
snTrapVlanConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVlanConfigChange.setStatus(
        ""
    )

snTrapAclConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 113)
)
snTrapAclConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAclConfigChange.setStatus(
        ""
    )

snTrapMacFilterConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 114)
)
snTrapMacFilterConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterConfigChange.setStatus(
        ""
    )

snTrapSNMPConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 115)
)
snTrapSNMPConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSNMPConfigChange.setStatus(
        ""
    )

snTrapSyslogConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 116)
)
snTrapSyslogConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSyslogConfigChange.setStatus(
        ""
    )

snTrapPasswordConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 117)
)
snTrapPasswordConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPasswordConfigChange.setStatus(
        ""
    )

snTrapServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 118)
)
snTrapServerStatusChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapServerStatusChange.setStatus(
        ""
    )

snTrapL4RealServerPortMaxConnectionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 119)
)
snTrapL4RealServerPortMaxConnectionLimitReached.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortMaxConnectionLimitReached.setStatus(
        ""
    )

snTrapL4LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 120)
)
snTrapL4LinkDown.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapLinkName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4LinkVirtualInterface"))
)
if mibBuilder.loadTexts:
    snTrapL4LinkDown.setStatus(
        ""
    )

snTrapL4LinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 121)
)
snTrapL4LinkUp.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapLinkName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4LinkVirtualInterface"))
)
if mibBuilder.loadTexts:
    snTrapL4LinkUp.setStatus(
        ""
    )

snTrapPortPriorityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 122)
)
snTrapPortPriorityChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortPriorityChange.setStatus(
        ""
    )

snTrapAutoPortDisableTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 123)
)
snTrapAutoPortDisableTrigger.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAutoPortDisableTrigger.setStatus(
        ""
    )

snTrapAutoPortDisableRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 124)
)
snTrapAutoPortDisableRelease.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAutoPortDisableRelease.setStatus(
        ""
    )

snTrapPnPStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 125)
)
snTrapPnPStatusChange.setObjects(
      *(("FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgPnPStatus"),
        ("FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgPnPStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapPnPStatusChange.setStatus(
        ""
    )

snTrapWirelessIsrpPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 126)
)
snTrapWirelessIsrpPeerStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessIsrpPeerStateChange.setStatus(
        ""
    )

snTrapWirelessStationStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 127)
)
snTrapWirelessStationStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessStationStateChange.setStatus(
        ""
    )

snTrapWirelessStationRoamingEventTriggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 128)
)
snTrapWirelessStationRoamingEventTriggered.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessStationRoamingEventTriggered.setStatus(
        ""
    )

snTrapWirelessSappStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 129)
)
snTrapWirelessSappStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessSappStateChange.setStatus(
        ""
    )

snTrapExternalPowerConnectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 130)
)
snTrapExternalPowerConnectionStatus.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapExternalPowerConnectionStatus.setStatus(
        ""
    )

snTrapDot1xSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 131)
)
snTrapDot1xSecurityViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xSecurityViolation.setStatus(
        ""
    )

snTrapDot1xPortLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 132)
)
snTrapDot1xPortLinkChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xPortLinkChange.setStatus(
        ""
    )

snTrapDot1xPortControlChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 133)
)
snTrapDot1xPortControlChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xPortControlChange.setStatus(
        ""
    )

snTrapDot1xVlanIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 134)
)
snTrapDot1xVlanIdChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xVlanIdChange.setStatus(
        ""
    )

snTrapDot1xFilterSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 135)
)
snTrapDot1xFilterSetupFailure.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xFilterSetupFailure.setStatus(
        ""
    )

snTrapDot1xError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 136)
)
snTrapDot1xError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xError.setStatus(
        ""
    )

snTrapPortConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 137)
)
snTrapPortConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortConfigChange.setStatus(
        ""
    )

snTrapMacAuthVlanIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 138)
)
snTrapMacAuthVlanIdChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthVlanIdChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-TRAP-MIB",
    **{"snTrapL4MaxSessionLimitReached": snTrapL4MaxSessionLimitReached,
       "snTrapL4TcpSynLimitReached": snTrapL4TcpSynLimitReached,
       "snTrapL4RealServerUp": snTrapL4RealServerUp,
       "snTrapL4RealServerDown": snTrapL4RealServerDown,
       "snTrapL4RealServerPortUp": snTrapL4RealServerPortUp,
       "snTrapL4RealServerPortDown": snTrapL4RealServerPortDown,
       "snTrapL4RealServerMaxConnectionLimitReached": snTrapL4RealServerMaxConnectionLimitReached,
       "snTrapL4BecomeStandby": snTrapL4BecomeStandby,
       "snTrapL4BecomeActive": snTrapL4BecomeActive,
       "snTrapModuleInserted": snTrapModuleInserted,
       "snTrapModuleRemoved": snTrapModuleRemoved,
       "snTrapChasPwrSupplyFailed": snTrapChasPwrSupplyFailed,
       "snTrapChasFanFailed": snTrapChasFanFailed,
       "snTrapLockedAddressViolation2": snTrapLockedAddressViolation2,
       "snTrapFsrpIfStateChange": snTrapFsrpIfStateChange,
       "snTrapVrrpIfStateChange": snTrapVrrpIfStateChange,
       "snTrapMgmtModuleRedunStateChange": snTrapMgmtModuleRedunStateChange,
       "snTrapTemperatureWarning": snTrapTemperatureWarning,
       "snTrapAccessListDeny": snTrapAccessListDeny,
       "snTrapMacFilterDeny": snTrapMacFilterDeny,
       "snTrapL4GslbRemoteUp": snTrapL4GslbRemoteUp,
       "snTrapL4GslbRemoteDown": snTrapL4GslbRemoteDown,
       "snTrapL4GslbRemoteControllerUp": snTrapL4GslbRemoteControllerUp,
       "snTrapL4GslbRemoteControllerDown": snTrapL4GslbRemoteControllerDown,
       "snTrapL4GslbHealthCheckIpUp": snTrapL4GslbHealthCheckIpUp,
       "snTrapL4GslbHealthCheckIpDown": snTrapL4GslbHealthCheckIpDown,
       "snTrapL4GslbHealthCheckIpPortUp": snTrapL4GslbHealthCheckIpPortUp,
       "snTrapL4GslbHealthCheckIpPortDown": snTrapL4GslbHealthCheckIpPortDown,
       "snTrapL4FirewallBecomeStandby": snTrapL4FirewallBecomeStandby,
       "snTrapL4FirewallBecomeActive": snTrapL4FirewallBecomeActive,
       "snTrapL4FirewallPathUp": snTrapL4FirewallPathUp,
       "snTrapL4FirewallPathDown": snTrapL4FirewallPathDown,
       "snTrapIcmpLocalExceedBurst": snTrapIcmpLocalExceedBurst,
       "snTrapIcmpTransitExceedBurst": snTrapIcmpTransitExceedBurst,
       "snTrapTcpLocalExceedBurst": snTrapTcpLocalExceedBurst,
       "snTrapTcpTransitExceedBurst": snTrapTcpTransitExceedBurst,
       "snTrapL4ContentVerification": snTrapL4ContentVerification,
       "snTrapDuplicateIp": snTrapDuplicateIp,
       "snTrapMplsProblem": snTrapMplsProblem,
       "snTrapMplsException": snTrapMplsException,
       "snTrapMplsAudit": snTrapMplsAudit,
       "snTrapMplsDeveloper": snTrapMplsDeveloper,
       "snTrapNoBmFreeQueue": snTrapNoBmFreeQueue,
       "snTrapSmcDmaDrop": snTrapSmcDmaDrop,
       "snTrapSmcBpDrop": snTrapSmcBpDrop,
       "snTrapBmWriteSeqDrop": snTrapBmWriteSeqDrop,
       "snTrapBgpPeerUp": snTrapBgpPeerUp,
       "snTrapBgpPeerDown": snTrapBgpPeerDown,
       "snTrapL4RealServerResponseTimeLowerLimit": snTrapL4RealServerResponseTimeLowerLimit,
       "snTrapL4RealServerResponseTimeUpperLimit": snTrapL4RealServerResponseTimeUpperLimit,
       "snTrapL4TcpAttackRateExceedMax": snTrapL4TcpAttackRateExceedMax,
       "snTrapL4TcpAttackRateExceedThreshold": snTrapL4TcpAttackRateExceedThreshold,
       "snTrapL4ConnectionRateExceedMax": snTrapL4ConnectionRateExceedMax,
       "snTrapL4ConnectionRateExceedThreshold": snTrapL4ConnectionRateExceedThreshold,
       "snTrapRunningConfigChanged": snTrapRunningConfigChanged,
       "snTrapStartupConfigChanged": snTrapStartupConfigChanged,
       "snTrapUserLogin": snTrapUserLogin,
       "snTrapUserLogout": snTrapUserLogout,
       "snTrapPortSecurityViolation": snTrapPortSecurityViolation,
       "snTrapPortSecurityShutdown": snTrapPortSecurityShutdown,
       "snTrapMrpStateChange": snTrapMrpStateChange,
       "snTrapMrpCamError": snTrapMrpCamError,
       "snTrapChasPwrSupplyOK": snTrapChasPwrSupplyOK,
       "snTrapVrrpeIfStateChange": snTrapVrrpeIfStateChange,
       "snTrapVsrpIfStateChange": snTrapVsrpIfStateChange,
       "snTrapSrcIpAddressViolation": snTrapSrcIpAddressViolation,
       "snTrapMacAuthEnable": snTrapMacAuthEnable,
       "snTrapMacAuthDisable": snTrapMacAuthDisable,
       "snTrapMacAuthMACAccepted": snTrapMacAuthMACAccepted,
       "snTrapMacAuthMACRejected": snTrapMacAuthMACRejected,
       "snTrapMacAuthPortDisabled": snTrapMacAuthPortDisabled,
       "snTrapClientLoginReject": snTrapClientLoginReject,
       "snTrapLocalUserConfigChange": snTrapLocalUserConfigChange,
       "snTrapVlanConfigChange": snTrapVlanConfigChange,
       "snTrapAclConfigChange": snTrapAclConfigChange,
       "snTrapMacFilterConfigChange": snTrapMacFilterConfigChange,
       "snTrapSNMPConfigChange": snTrapSNMPConfigChange,
       "snTrapSyslogConfigChange": snTrapSyslogConfigChange,
       "snTrapPasswordConfigChange": snTrapPasswordConfigChange,
       "snTrapServerStatusChange": snTrapServerStatusChange,
       "snTrapL4RealServerPortMaxConnectionLimitReached": snTrapL4RealServerPortMaxConnectionLimitReached,
       "snTrapL4LinkDown": snTrapL4LinkDown,
       "snTrapL4LinkUp": snTrapL4LinkUp,
       "snTrapPortPriorityChange": snTrapPortPriorityChange,
       "snTrapAutoPortDisableTrigger": snTrapAutoPortDisableTrigger,
       "snTrapAutoPortDisableRelease": snTrapAutoPortDisableRelease,
       "snTrapPnPStatusChange": snTrapPnPStatusChange,
       "snTrapWirelessIsrpPeerStateChange": snTrapWirelessIsrpPeerStateChange,
       "snTrapWirelessStationStateChange": snTrapWirelessStationStateChange,
       "snTrapWirelessStationRoamingEventTriggered": snTrapWirelessStationRoamingEventTriggered,
       "snTrapWirelessSappStateChange": snTrapWirelessSappStateChange,
       "snTrapExternalPowerConnectionStatus": snTrapExternalPowerConnectionStatus,
       "snTrapDot1xSecurityViolation": snTrapDot1xSecurityViolation,
       "snTrapDot1xPortLinkChange": snTrapDot1xPortLinkChange,
       "snTrapDot1xPortControlChange": snTrapDot1xPortControlChange,
       "snTrapDot1xVlanIdChange": snTrapDot1xVlanIdChange,
       "snTrapDot1xFilterSetupFailure": snTrapDot1xFilterSetupFailure,
       "snTrapDot1xError": snTrapDot1xError,
       "snTrapPortConfigChange": snTrapPortConfigChange,
       "snTrapMacAuthVlanIdChange": snTrapMacAuthVlanIdChange}
)
